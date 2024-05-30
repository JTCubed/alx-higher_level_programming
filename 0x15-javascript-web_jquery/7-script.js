$(function() {
    const charr = $("#character")

    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: function(charrs) {
            $("#character").text(charrs.name);
        }
    });
});
