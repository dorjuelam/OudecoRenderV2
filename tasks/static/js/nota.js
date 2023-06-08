(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Está seguro de eliminar el Registro?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();

$(document).ready(function() {
    $('#id_opcion').change(function() {
        var opcion_id = $(this).val();

        $.ajax({
            url: '/get_campos_adicionales/',
            data: {
                'opcion_id': opcion_id
            },
            dataType: 'json',
            success: function(data) {
                $.each(data, function(index, field) {
                    var $campo = $('<input>').attr({
                        type: 'text',
                        name: 'campo' + (index+1),
                        value: field,
                        class: 'form-control',
                        placeholder: 'Campo ' + (index+1),
                    });

                    $('#id_campo' + (index+1)).parent().html($campo);
                });
            }
        });
    });
});

$(document).ready(function() {
    $('#id_opcion').change(function() {
        var opcion_id = $(this).val();

        $.ajax({
            url: '/get_campos_adicionales/',
            data: {
                'opcion_id': opcion_id
            },
            dataType: 'json',
            error: function(data) {
                $.each(data, function(index, field) {
                    var $campo = $('<input>').attr({
                        type: 'text',
                        name: 'campo' + (index+1),
                        value: field,
                        class: 'form-control',
                        placeholder: 'Campo ' + (index+1),
                    });

                    $('#id_campo' + (index+1)).parent().html($campo);
                });
            }
        });
    });
});





