document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("change-color").addEventListener("click", function() {
        var radios = document.getElementsByName("bgcolor");
        var selectedColor;

        for (var i = 0; i < radios.length; i++) {
            if (radios[i].checked) {
                selectedColor = radios[i].value;
                break;
            }
        }

        document.body.style.backgroundColor = selectedColor;
    });
});
