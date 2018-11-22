console.log("Client running");

window.onload = function(){

    // obtener productos
    const divInventario = document.getElementById('divInventario');
    const obtenerInventario = document.getElementById('btnObtenerProductos');
    obtenerInventario.addEventListener('click', function() {
    console.log("asdasd");
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