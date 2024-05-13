document.addEventListener("DOMContentLoaded", function () {
    var generarTablaBtn = document.getElementById("generarTablaBtn");
    generarTablaBtn.addEventListener("click", function () {
        generarTabla();
    });
});

function generarTabla() {
    var numFilas = document.getElementById("numFilas").value;
    var numColumnas = document.getElementById("numColumnas").value;
    var anchoBorde = document.getElementById("anchoBorde").value;

    var tablaHTML = "<table style='border-collapse: collapse; border: " + anchoBorde + "px solid black;'>";

    for (var i = 0; i < numFilas; i++) {
        tablaHTML += "<tr>";
        for (var j = 0; j < numColumnas; j++) {
            tablaHTML += "<td style='border: " + anchoBorde + "px solid black;'>Celda " + (i + 1) + "-" + (j + 1) + "</td>";
        }
        tablaHTML += "</tr>";
    }

    tablaHTML += "</table>";

    document.getElementById("tablaGenerada").innerHTML = tablaHTML;
}
