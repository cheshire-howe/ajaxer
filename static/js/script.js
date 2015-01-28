(function() {
    $('.linker').click(function() {
        var page = $(this).data('page');
        var place = $(this).data('place');
        var method = $(this).data('method') ? $(this).data('method') : ""
        linker(page, place, method);
    });

    function linker(page, place, method) {
        $.get("/ajax/" + page + "/" + method, function(data) {
            $(place).html(data)
        });
    }
})();
