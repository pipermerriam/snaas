$(function() {
    var textArea = $("#plainText");
    var snorseText = $("#snorseText");

    var snorseIt = function(event) {
        $.ajax(
            "/api/v1/snorse/", {
                method: 'POST',
                data: textArea.val(),
                success: function(data, textStatus, jqXHR) {
                    snorseText.html(data);
                }
            }
        );
    };

    textArea.on("blur change keyup", snorseIt);
    snorseIt();
});
