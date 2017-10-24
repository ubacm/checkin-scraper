$(document).ready(function () {
    $(document).on('input', '#filter', function () {
        var filterNames = $(this).val();
        if (filterNames == "") {
            $('tr').show();
            return;
        }
        var matches = filterNames.match(/\@([a-z0-9][a-z0-9._-]*)/g)
        if (matches) {
            matches = matches.map(el => el.slice(1));
            hideAllButHere(matches);
        }

        $("table tbody").each(function () {
            $(this).find("tr:visible:even").addClass("even").removeClass("odd");
            $(this).find("tr:visible:odd").addClass("odd").removeClass("even");
        });
    });

    function hideAllButHere(names) {
        $('#expoTable > tbody > tr').each(function (element) {
            var name = $(this).children()[1].innerHTML;
            if (!names.includes(name)) {
                $(this).hide();
            } else {
                $(this).show();
            }
        });
    }
});