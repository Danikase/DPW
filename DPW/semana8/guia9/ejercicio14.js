document.addEventListener("DOMContentLoaded", function () {
    var calcularBtn = document.getElementById("calcularBtn");
    calcularBtn.addEventListener("click", function () {
        calcularCalificacionFinal();
    });
});

function calcularCalificacionFinal() {
    var calificacionParcial1 = parseFloat(document.getElementById("parcial1").value);
    var calificacionParcial2 = parseFloat(document.getElementById("parcial2").value);
    var calificacionParcial3 = parseFloat(document.getElementById("parcial3").value);
    var calificacionExamenFinal = parseFloat(document.getElementById("examenFinal").value);
    var calificacionTrabajoFinal = parseFloat(document.getElementById("trabajoFinal").value);
    
    var promedioParciales = (calificacionParcial1 + calificacionParcial2 + calificacionParcial3) / 3;
    
    var calificacionFinal = (promedioParciales * 0.55) + (calificacionExamenFinal * 0.30) + (calificacionTrabajoFinal * 0.15);

    var resultadoHTML = "<h2>Calificación Final:</h2>";
    resultadoHTML += "<p>El promedio de las calificaciones parciales es: " + promedioParciales.toFixed(2) + "</p>";
    resultadoHTML += "<p>La calificación final del alumno es: " + calificacionFinal.toFixed(2) + "</p>";

    document.getElementById("resultado").innerHTML = resultadoHTML;
}