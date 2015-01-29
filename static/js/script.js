(function() {
    $('.linker').click(function(e) {
        e.preventDefault();
        var href = $(this).attr('href').split('/');
        var controller = href.shift();
        var action = href[0] ? href.shift() : "";
        var params = href[0] ? href : "";
        var place = $(this).data('place');
        linker(controller, action, params, place);
    });

    function linker(controller, action, params, place) {
        url = "/ajax/" + controller;
        if (action)
            url += "/" + action;
        if (params) {
            $.each(params, function(i) {
                url += "/" + params[i];
            });
        }
        $.get(url, function(data) {
            $(place).html(data)
        });
    }
})();
