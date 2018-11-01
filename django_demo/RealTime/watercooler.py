
import logging
import signal
import time
# 创建应用程序实例时，将创建一个新字典来存储订阅。
from collections import defaultdict
from urllib.parse import urlparse

# 从标准库导入Tornado HTTP服务器模块
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
# 用于处理命令行参数的Tornado实用程序的新导入import。
from tornado.options import define, parse_command_line, options
from tornado.web import Application
from tornado.websocket import WebSocketHandler, WebSocketClosedError

# 定义命令行上可用的选项。选项可以映射到Python类型。在这种情况下，debug为True或False，端口应为整数。allowed_hosts可以多次传递。
define('debug', default=False, type=bool, help='Run in debug mode')
define('port', default=8080, type=int, help='Server port')
define('allowed_hosts', default="localhost:8080", multiple=True,
       help='Allowed hosts for cross domain connections')


# SprintHandler是websocket连接的处理程序类。
# open，on_message和on_close方法是WebSocketHandler定义的API，编写这些API以添加我们需要的功能。
class SprintHandler(WebSocketHandler):
    """Handles real-time updates to the board."""
    def check_origin(self, origin):
        """
        Application为具有到websocket处理程序的单个路由，并配置为侦听端口8080。
        :param origin:
        :return:
        """
        allowed = super().check_origin(origin)
        parsed = urlparse(origin.lower())
        # allowed_hosts选项域可用于跨域连接。这将允许来自本地服务器或使用命令行上的 - allowed_hosts选项配置的任何服务器的连接。
        # 启用调试后，它将允许来自任何服务器的连接。
        matched = any(parsed.netloc == host for host in options.allowed_hosts)
        # check_origin更新为使用新的allowed_hosts和debug设置。
        return options.debug or allowed or matched

    # 新客户端连接时获取有关相关sprint的更新。
    def open(self, sprint):
        """Subscribe to sprint updates on a new connection."""
        self.sprint = sprint
        self.application.add_subscriber(self.sprint, self)

    # 当处理程序收到消息时，它将调用应用程序来广播消息并将其自身作为发送方传递，以确保它没有立即给出消息。
    def on_message(self, message):
        """Broadcast updates to other interested clients."""
        self.application.broadcast(message, channel=self.sprint, sender=self)

    # 客户端关闭连接，则应从订户列表中删除客户端。
    def on_close(self):
        """Remove subscription."""
        self.application.remove_subscriber(self.sprint, self)


class ScrumApplication(Application):

    def __init__(self, **kwargs):
        """
        重写check_origin以允许跨域请求。目前它将允许来自本地运行的任何服务器的连接。这将适用于开发，我们将在以后进行更多配置。
        :param kwargs:
        """
        routes = [
            (r'/(?P<sprint>[0-9]+)', SprintHandler),
        ]
        super().__init__(routes, **kwargs)
        # 字典会将sprint ID映射到连接列表。 这些路由也是在这里构建的，而不是在创建应用程序时传入。
        self.subscriptions = defaultdict(list)

    # 公开了add_subscriber，remove_subscriber和get_subscribers方法，用于操作和查询可用订户。
    # 而不是公开底层订阅字典。这种抽象将使以后更容易重构。
    def add_subscriber(self, channel, subscriber):
        self.subscriptions[channel].append(subscriber)

    def remove_subscriber(self, channel, subscriber):
        self.subscriptions[channel].remove(subscriber)

    def get_subscribers(self, channel):
        return self.subscriptions[channel]

    # 当服务器从其中一个客户端获取消息时，它需要将该消息广播给所有感兴趣的客户端。
    # 由于应用程序正在跟踪所有订阅，因此它也可以处理此广播
    def broadcast(self, message, channel=None, sender=None):
        if channel is None:
            for c in self.subscriptions.keys():
                # 将消息转发为从客户端发送到其所有对等端的消息。对等方是对同一sprint感兴趣的任何其他客户端。
                # 如果没有，那么消息就会消失在以太网中。
                # channel = None向所有客户端广播消息而不管sprint
                self.broadcast(message, channel=c, sender=sender)
        else:
            peers = self.get_subscribers(channel)
            for peer in peers:
                if peer != sender:
                    try:
                        peer.write_message(message)
                    # 尝试写入已关闭的连接会引发WebSocketClosedError。
                    # 在引发异常的情况下，简单地从订户列表中移除对等体。
                    except WebSocketClosedError:
                        # Remove dead peer
                        self.remove_subscriber(channel, peer)


def shutdown(server):
    """
    关闭HTTP服务器。它首先停止服务器接受新连接; 然后，在短暂超时后，它会完全停止IOLoop。
    :param server:
    """
    ioloop = IOLoop.instance()
    # 此代码设置日志记录以提供对当前服务器状态的深入了解。
    logging.info('Stopping server.')
    server.stop()

    def finalize():
        ioloop.stop()
        # 此代码设置日志记录以提供对当前服务器状态的深入了解。
        logging.info('Stopped.')

    ioloop.add_timeout(time.time() + 1.5, finalize)


if __name__ == "__main__":
    # 需要调用parse_command_line才能填充选项。未在命令行上给出的选项将使用define给出的默认值填充。
    parse_command_line()
    # 创建应用程序实例，debug被传递给应用程序实例，端口号用于启动应用程序。
    application = ScrumApplication(debug=options.debug)
    server = HTTPServer(application)
    # 不是使用application.start，而是使用应用程序构建HTTP服务器实例并启动它。
    server.listen(options.port)
    # 创建的服务器绑定到SIGINT的信号处理程序。捕获信号时，它将调用先前的关闭代码。
    signal.signal(signal.SIGINT, lambda sig, frame: shutdown(server))
    # 此代码设置日志记录以提供对当前服务器状态的深入了解。
    logging.info('Starting server on localhost:{}'.format(options.port))
    IOLoop.instance().start()
