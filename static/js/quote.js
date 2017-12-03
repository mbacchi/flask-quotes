function newQuote() {
    $(document).ready(function() {
        $.getJSON('/new_quote',
            function (data) {
                $("#quote-text").text(data);
            });
        return false;
    });
}
