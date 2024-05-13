document.addEventListener("DOMContentLoaded", function () {
    var registrarBtn = document.getElementById("registrarBtn");
    registrarBtn.addEventListener("click", function () {
        validarMatricula();
    });
});

function validarMatricula() {
    var certificado = document.getElementById("certificado").value;
    var comprobante = document.getElementById("comprobante").value;
    var conducta = document.getElementById("conducta").checked;
    var mensajeError = document.getElementById("mensajeError");
    var mensajePago = document.getElementById("mensajePago");
    var mensajeDocumentos = document.getElementById("mensajeDocumentos");

    if (!conducta || (!certificado && !comprobante)) {
        mensajeError.style.display = "none";
        mensajePago.style.display = !conducta ? "block" : "none";
        mensajeDocumentos.style.display = (certificado || comprobante) ? "none" : "block";
    } else {
        mensajeError.style.display = "none";
        mensajePago.style.display = "none";
        mensajeDocumentos.style.display = "none";
        console.log("Matrícula realizada correctamente.");
    }
}
