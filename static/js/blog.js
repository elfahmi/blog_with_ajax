$(document).ready(function () {
    var csrfToken = $("input[name=csrfmiddlewaretoken]").val();

    $("#createButton").click(function () {
        var sereliazedData = $("#createCommForm").serialize();

        dataId = $("#commCard").data('id');

        $.ajax({
            url: '/' + dataId + '/detail/',
            data: sereliazedData,
            type: 'post',
            success: function (response) {
                $("#commList").append(`<div class="alert alert-warning alert-dismissible fade show mt-1" role="alert" style="width: 50rem;" id="pageCard" data-id="` + response.page.id + `"><strong>` + response.page.name + `: </strong>` + response.page.comment + `<button type="button" class="close" data-dismiss="alert" aria-label="Close" data-id="` + response.page.id + `"><span aria-hidden="true">&times;</span></button></div>`)
            }
        });
        $("#createCommForm")[0].reset();
    });

    $("#commList").on('click', 'button.close', function (event) {
        event.stopPropagation();

        var dataId = $(this).data('id');
        console.log(dataId)

        $.ajax({
            url: '/' + dataId + '/delete/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: dataId
            },
            type: 'post',
            success: function () {
                $('#pageCard[data-id="' + dataId + '"]').remove();
            }
        })
    });


});