document.addEventListener("DOMContentLoaded", function () {
    var calcularBtn = document.getElementById("calcularBtn");
    calcularBtn.addEventListener("click", function () {
        calcularArea();
    });
});

function calcularArea() {
    var radio = parseFloat(document.getElementById("radio").value);

    if (!isNaN(radio) && radio > 0) {
        var area = Math.PI * Math.pow(radio, 2);
        document.getElementById("resultado").innerText = "El área del círculo es: " + area.toFixed(2);
    } else {
        document.getElementById("resultado").innerText = "Por favor, ingrese un valor válido para el radio.";
    }
}
