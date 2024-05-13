document.addEventListener("DOMContentLoaded", function () {
    var calcularBtn = document.getElementById("calcularBtn");
    calcularBtn.addEventListener("click", function () {
        calcularComisiones();
    });
});

function calcularComisiones() {
    var sueldoBase = parseFloat(document.getElementById("sueldoBase").value);
    var venta1 = parseFloat(document.getElementById("venta1").value);
    var venta2 = parseFloat(document.getElementById("venta2").value);
    var venta3 = parseFloat(document.getElementById("venta3").value);

    var comisionTotal = (venta1 + venta2 + venta3) * 0.1;

    var sueldoTotal = sueldoBase + comisionTotal;

    var resultadoHTML = "<h2>Resultados:</h2>";
    resultadoHTML += "<p>Sueldo Base: $" + sueldoBase.toFixed(2) + "</p>";
    resultadoHTML += "<p>Total de Comisión del Mes: $" + comisionTotal.toFixed(2) + "</p>";
    resultadoHTML += "<p>Sueldo Total: $" + sueldoTotal.toFixed(2) + "</p>";

    document.getElementById("resultado").innerHTML = resultadoHTML;
}
