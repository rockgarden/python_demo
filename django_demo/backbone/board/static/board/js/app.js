// 初始化

// 通过自调用函数解析 index.html 中的 JSON (#config) 并返回给全局变量app
var app = (function ($) {
    //解析 index.html 中的 JSON (#config) 并返回给全局变量app
    var config = $('#config'),
        app = JSON.parse(config.text());

    // 确保路由在DOM完全为APP运行准备好后才初始化. 最初app.router()为null，当router.js载入时它会被加入.
    //jQuery的$(document).ready事件确保app.router在router.js加载后初始化.
    $(document).ready(function () {
    	var router = new app.router();
    });
        
    return app;
})(jQuery);