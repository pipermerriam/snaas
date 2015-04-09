$(function() {
    var textArea = $("#plainText");
    var snorseArea = $("#snorseText");

    var snorseIt = function(event) {
        $.ajax(
            "/api/v1/snorse/", {
                method: 'POST',
                data: textArea.val(),
                success: function(data, textStatus, jqXHR) {
                    snorseArea.val(data);
                }
            }
        );
    };

    var desnorseIt = function(event) {
        $.ajax(
            "/api/v1/desnorse/", {
                method: 'POST',
                data: snorseArea.val(),
                success: function(data, textStatus, jqXHR) {
                    textArea.val(data);
                }
            }
        );
    };

    textArea.on("blur keyup", snorseIt);
    snorseArea.on("blur keyup", desnorseIt);
    snorseIt();
});
