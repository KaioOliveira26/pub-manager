$.ajax({
  method: "GET",
  url: "/average-sales/",
  headers: { "X-CSRFToken": csrftoken },
  success: function (response) {
    const averageSales = response.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
    $("#blockAverageSales").html(`<h2 style='color:green;'>${averageSales}</h2>`);
  },
  error: function (error_data) {
    console.log("error");
    console.log(error_data);
  },
});


const createChart = (endpoint, chartid,chartcanva ) => {
  let ctx = document.getElementById(chartid);
  ctx.innerHTML = "";
  $(`#${chartid}`).append(
    `<canvas id=${chartcanva} width="100%" height="60vh"></canvas>`
  );
  let chart = {
    type: "bar",
    min: 0,
    title: "default title",
    data: [],
    labels: [],
    backgroundColors: [
      "rgba(255, 99, 132, 0.7)",
      "rgba(54, 162, 235, 0.7)",
      "rgba(255, 206, 86, 0.7)",
      "rgba(75, 192, 192, 0.7)",
      "rgba(153, 102, 255, 0.7)",
      "rgba(255, 159, 64, 0.7)",
    ],
  };

  $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
      if ("title" in data) {
        chart.title = data.title;
      }
      if ("values" in data) {
        chart.data = data.values;
      }
      if ("labels" in data) {
        chart.labels = data.labels;
      }
      if ("backgroundColors" in data) {
        chart.backgroundColors = data.backgroundColors;
      }

      let ctx = document.getElementById(chartcanva);
      let myChart = new Chart(ctx, {
        type: chart.type,
        data: {
          labels: chart.labels,
          datasets: [
            {
              label: chart.title,
              data: chart.data,
              backgroundColor: chart.backgroundColors,
            },
          ],
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  suggestedMin: chart.min,
                },
              },
            ],
          },
        },
      });
    },

    error: function (error_data) {
      console.log("error");
      console.log(error_data);
    },
  });
};
