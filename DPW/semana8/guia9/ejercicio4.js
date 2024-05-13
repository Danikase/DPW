function generarTabla() {

    var numero = parseInt(document.getElementById("numero").value);

    var tablaResultado = document.getElementById("tablaResultado");

    tablaResultado.innerHTML = "";

    for (var i = 1; i <= 10; i++) {
        var resultado = numero * i;
        tablaResultado.innerHTML += "<tr><td>" + numero + " x " + i + "</td><td>=</td><td>" + resultado + "</td></tr>";
    }
}

