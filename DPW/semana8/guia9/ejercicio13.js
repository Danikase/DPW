document.addEventListener("DOMContentLoaded", function () {
    var calcularBtn = document.getElementById("calcularBtn");
    calcularBtn.addEventListener("click", function () {
        calcularAreaYPerimetro();
    });
});

function calcularAreaYPerimetro() {
    var largo = parseFloat(document.getElementById("largo").value);
    var ancho = parseFloat(document.getElementById("ancho").value);
    
    var area = largo * ancho;
    var perimetro = 2 * (largo + ancho);
    var resultadoHTML = "<h2>Resultados:</h2>";
    resultadoHTML += "<p>Área del rectángulo: " + area.toFixed(2) + "</p>";
    resultadoHTML += "<p>Perímetro del rectángulo: " + perimetro.toFixed(2) + "</p>";

    document.getElementById("resultado").innerHTML = resultadoHTML;
}
