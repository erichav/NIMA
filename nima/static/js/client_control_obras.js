console.log("Client running");

window.onload = function(){
    // Crear una nueva obra
    const agregarObra = document.getElementById('btnAgregarObra');
    agregarObra.addEventListener('click', function() {
        const txtNombre = document.getElementById('textFormNombre');
        const txtLocalizacion = document.getElementById('textFormLocalizacion');
        const txtComentarios = document.getElementById('textFormComentarios');
        formElements = {
            "nombre": txtNombre.value,
            "ubicacion": txtLocalizacion.value,
            "comentarios": txtComentarios.value
        }

        console.log(formElements)

        fetch('obra', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json; charset=utf-8"
            },
            body: JSON.stringify(formElements)
        }).then(response => {
            return response.json();
        }).then(data => {
            console.log(data);
            alert("Obra agregada satisfactoriamente.");
            document.getElementById('textFormNombre').value='';
            document.getElementById('textFormLocalizacion').value='';
            document.getElementById('textFormComentarios').value='';
        }).catch(err => {
            console.log(err);
        });
    });


    // Crear un nuevo trabajador
    const agregarTrabajador = document.getElementById('btnAgregarTrabajador');
    agregarTrabajador.addEventListener('click', function() {
        const txtObra = document.getElementById('textFormObra');
        const txtTrabajador = document.getElementById('textFormNombreTrabajador');
        const txtRol = document.getElementById('textFormRol');
        const txtCuenta = document.getElementById('textFormCuenta');
        const txtNSS = document.getElementById('textFormNSS');
        formElements = {
            "obra": txtObra.value,
            "nombre": txtTrabajador.value,
            "rol": txtRol.value,
            "no_cuenta": txtCuenta.value,
            "nss": txtNSS.value
        }

        console.log(formElements)

        fetch('trabajador', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json; charset=utf-8"
            },
            body: JSON.stringify(formElements)
        }).then(response => {
            return response.json();
        }).then(data => {
            console.log(data);
            alert("Trabajador agregado satisfactoriamente.");
            document.getElementById('textFormObra').value='';
            document.getElementById('textFormNombreTrabajador').value='';
            document.getElementById('textFormRol').value='';
            document.getElementById('textFormCuenta').value='';
            document.getElementById('textFormNSS').value='';
        }).catch(err => {
            console.log(err);
        });
    });



}