document.addEventListener("DOMContentLoaded", function () {
    var calcularBtn = document.getElementById("calcularBtn");
    calcularBtn.addEventListener("click", function () {
        calcularSueldo();
    });
});

function calcularSueldo() {
    var nombre = document.getElementById("nombre").value;
    var direccion = document.getElementById("direccion").value;
    var telefono = document.getElementById("telefono").value;
    var salario = parseFloat(document.getElementById("salario").value);

    var renta = salario * 0.10;
    var afp = salario * 0.05;
    var fsv = salario * 0.08;

    var salarioNeto = salario - renta - afp - fsv;

    var resultadoHTML = "<h2>Resultados:</h2>";
    resultadoHTML += "<p>Nombre: " + nombre + "</p>";
    resultadoHTML += "<p>Dirección: " + direccion + "</p>";
    resultadoHTML += "<p>Teléfono: " + telefono + "</p>";
    resultadoHTML += "<p>Salario Neto: $" + salarioNeto.toFixed(2) + "</p>";
    resultadoHTML += "<p>Total de Descuentos:</p>";
    resultadoHTML += "<ul>";
    resultadoHTML += "<li>Renta: $" + renta.toFixed(2) + "</li>";
    resultadoHTML += "<li>AFP: $" + afp.toFixed(2) + "</li>";
    resultadoHTML += "<li>FSV: $" + fsv.toFixed(2) + "</li>";
    resultadoHTML += "</ul>";

    document.getElementById("resultado").innerHTML = resultadoHTML;
}
