function newQuote() {
    $(document).ready(function() {
        $.getJSON('https://qlyaou0kc3.execute-api.us-east-1.amazonaws.com/dev/new_quote',
            function (data) {
                $("#quote-text").text(data);
            });
        return false;
    });
}
