console.log("Client running");

window.onload = function(){




    // Crear un nuevo producto
    const agregarProducto = document.getElementById('btnAgregarProducto');
    agregarProducto.addEventListener('click', function() {
        const btnNombre = document.getElementById('textFormNombre');
        const btnCantidad = document.getElementById('textFormCantidad');
        const btnObservaciones = document.getElementById('textFormObservaciones');
        formElements = {
            "nombre": btnNombre.value,
            "cantidad": btnCantidad.value,
            "observaciones": btnObservaciones.value
        }

        console.log(formElements)

        fetch('producto', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json; charset=utf-8"
            },
            body: JSON.stringify(formElements)
        }).then(response => {
            return response.json();
        }).then(data => {
            console.log(data);
        }).catch(err => {
            console.log(err);
        });
    });



    // obtener productos
    const divInventario = document.getElementById('divInventario');
    const obtenerInventario = document.getElementById('btnObtenerInventario');
    obtenerInventario.addEventListener('click', function() {  
        fetch('productos', {
            method: 'GET',
        }).then(response => {
            return response.json();
        }).then(data => {
            var htmlStr = "";
            for(var i = 0; i < data.length; i++){
                htmlStr += "Nombre: " + data[i]['nombre'] + "<br>";
                htmlStr += "Cantidad: " + data[i]['cantidad'] + "<br>";
                htmlStr += "Observaciones: " + data[i]['observaciones'] + "<br><br>";
            }
            divInventario.innerHTML = htmlStr;
            console.log(htmlStr);
        }).catch(err => {
            console.log(err);
        });
    });



}