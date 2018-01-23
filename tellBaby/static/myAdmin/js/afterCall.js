(function ($) {
    $(function () {

        $(".call").click(function () {
            var id = $(this).attr("data-id")
            var href = "/admin/twentyFour/callhistory/add/?resume=" + id + "&_popup=1"

             window.open(href,"view_window",'width=350, height=667')
        });
    })

})(django.jQuery);