/** sdfwrg */

// JQUERY CONFIRM

function submit_ajax(url,parameters, callback) {
    $.confirm({
        theme: 'material',
        title: 'Confirmación',
        icon: 'fa fa-info-circle',
        content: '¿Seguro que desea realizar la operación?',
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: 'Si',
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url, //window.location.pathname,
                        type: 'POST',
                        data: parameters,
                        dataType: 'json'
                    }).done(function (data) {
                        console.log(data);
                        if (!data.hasOwnProperty('error')) {
                            callback();//location.href = '{{ list_url }}';
                            return false;
                        }
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {
        
                    }); 
                }
            },
            danger:{
                text: 'No',
                btnClass: 'btn-red',
                action: function () {
                    //Node for now
                }
            }
        }

    });
}