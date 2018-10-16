// 初始化

// 通过自调用函数解析 index.html 中的 JSON (#config) 并返回给全局变量app
var app = (function ($) {
    var config = $('#config'),
        app = JSON.parse(config.text());
    
    $(document).ready(function () {
    	var router = new app.router();
    });
        
    return app;
})(jQuery);