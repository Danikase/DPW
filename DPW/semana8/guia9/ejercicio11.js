document.addEventListener("DOMContentLoaded", function () {
    var calcularBtn = document.getElementById("calcularBtn");
    calcularBtn.addEventListener("click", function () {
        calcularDescuento();
    });
});

function calcularDescuento() {
    var totalCompra = parseFloat(document.getElementById("totalCompra").value);
    
    var descuento = totalCompra * 0.15;
    
    var montoAPagar = totalCompra - descuento;
    
    var resultadoHTML = "<h2>Resultado:</h2>";
    resultadoHTML += "<p>Total de la compra: $" + totalCompra.toFixed(2) + "</p>";
    resultadoHTML += "<p>Descuento (15%): $" + descuento.toFixed(2) + "</p>";
    resultadoHTML += "<p>Monto a Pagar: $" + montoAPagar.toFixed(2) + "</p>";

    document.getElementById("resultado").innerHTML = resultadoHTML;
}
