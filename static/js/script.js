(function() {
    $('.linker').click(function() {
        var page = $(this).data('page');
        var place = $(this).data('place');
        linker(page, place);
    });

    function linker(page, place) {
        $.get("/ajax/" + page, function(data) {
            $(place).html(data)
        });
    }
})();
