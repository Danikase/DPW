function calcularArea() {
    var radio = document.getElementById("radio").value;
    var area = Math.PI * Math.pow(radio, 2);
    document.getElementById("resultado").innerText = "El área del círculo es: " + area.toFixed(2);
}
