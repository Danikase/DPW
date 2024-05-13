function realizarOperacion() {
    var numero1 = parseFloat(document.getElementById("numero1").value);
    var numero2 = parseFloat(document.getElementById("numero2").value);
    var operacion = document.getElementById("operacion").value;
    var resultado = 0;

    switch (operacion) {
        case "sumar":
            resultado = numero1 + numero2;
            break;
        case "restar":
            resultado = numero1 - numero2;
            break;
        case "multiplicar":
            resultado = numero1 * numero2;
            break;
        case "dividir":
            if (numero2 !== 0) {
                resultado = numero1 / numero2;
            } else {
                alert("No se puede dividir por cero.");
            }
            break;
        default:
            alert("Operación no válida.");
    }

    document.getElementById("resultado").innerText = "El resultado de la operación es: " + resultado;
}
