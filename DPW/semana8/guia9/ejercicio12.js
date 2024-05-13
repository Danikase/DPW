document.addEventListener("DOMContentLoaded", function () {
    var calcularBtn = document.getElementById("calcularBtn");
    calcularBtn.addEventListener("click", function () {
        calcularGanancias();
    });
});

function calcularGanancias() {
    var ahorroMensual = parseFloat(document.getElementById("ahorroMensual").value);
    var ganancias3Meses = calcularGanancia(ahorroMensual, 3);
    var ganancias6Meses = calcularGanancia(ahorroMensual, 6);
    var ganancias12Meses = calcularGanancia(ahorroMensual, 12);

    var resultadoHTML = "<h2>Ganancias:</h2>";
    resultadoHTML += "<p>Ganancias a 3 meses: $" + ganancias3Meses.toFixed(2) + "</p>";
    resultadoHTML += "<p>Ganancias a 6 meses: $" + ganancias6Meses.toFixed(2) + "</p>";
    resultadoHTML += "<p>Ganancias a 12 meses: $" + ganancias12Meses.toFixed(2) + "</p>";

    document.getElementById("resultado").innerHTML = resultadoHTML;
}

function calcularGanancia(ahorroMensual, meses) {
    var interesMensual = 0.035; // 3.5%
    var ganancia = 0;
    
    for (var i = 0; i < meses; i++) {
        ganancia += ahorroMensual * interesMensual;
    }
    
    return ganancia;
}