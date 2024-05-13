document.addEventListener("DOMContentLoaded", function () {
    var registrarBtn = document.getElementById("registrarBtn");
    registrarBtn.addEventListener("click", function () {
        validarCampos();
    });
});

function validarCampos() {
    var nombre = document.getElementById("nombre").value.trim();
    var apellido = document.getElementById("apellido").value.trim();
    var edad = document.getElementById("edad").value.trim();
    var email = document.getElementById("email").value.trim();
    var mensajeError = document.getElementById("mensajeError");

    if (nombre === "" || apellido === "" || edad === "" || email === "") {
        mensajeError.style.display = "block";
    } else {
        mensajeError.style.display = "none";
        console.log("Estudiante registrado:", nombre, apellido, edad, email);
    }
}
