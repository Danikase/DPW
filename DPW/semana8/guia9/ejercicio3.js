document.addEventListener("DOMContentLoaded", function () {
    var votosA = parseInt(prompt("Ingrese la cantidad de votos para el Candidato A:"));
    var votosB = parseInt(prompt("Ingrese la cantidad de votos para el Candidato B:"));
    var votosC = parseInt(prompt("Ingrese la cantidad de votos para el Candidato C:"));

    var totalVotos = votosA + votosB + votosC;

    var porcentajeA = (votosA / totalVotos) * 100;
    var porcentajeB = (votosB / totalVotos) * 100;
    var porcentajeC = (votosC / totalVotos) * 100;

    var ctx = document.getElementById('graficoPastel').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Candidato A', 'Candidato B', 'Candidato C'],
            datasets: [{
                label: 'Porcentaje de Votos',
                data: [porcentajeA.toFixed(2), porcentajeB.toFixed(2), porcentajeC.toFixed(2)],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(54, 162, 235, 0.5)',
                    'rgba(255, 206, 86, 0.5)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            title: {
                display: true,
                text: 'Resultados de Elecciones'
            }
        }
    });

    document.getElementById("totalVotos").innerText = "Total de votos: " + totalVotos;
});
