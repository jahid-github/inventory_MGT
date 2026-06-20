/*
  Chart.js demo charts for dashboard pages.
  Backend note: set window.dashboardChartData from a Django view before this script to replace dummy values.
*/

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    renderBorrowedTrend();
    renderAdminMostBorrowed();
  });

  function renderBorrowedTrend() {
    var canvas = document.getElementById("borrowedTrendChart");
    if (!canvas) {
      return;
    }

    var dataSource = window.dashboardChartData || {};
    var labels = dataSource.borrowedLabels || ["Jan", "Feb", "Mar", "Apr", "May", "Jun"];
    var values = dataSource.borrowedByMonth || [4, 6, 8, 5, 9, 11];

    renderChart(canvas, {
      type: "line",
      data: {
        labels: labels,
        datasets: [{
          label: "Borrowed items",
          data: values,
          borderColor: "#2563eb",
          backgroundColor: "rgba(37, 99, 235, 0.14)",
          tension: 0.35,
          fill: true
        }]
      }
    });
  }

  function renderAdminMostBorrowed() {
    var canvas = document.getElementById("adminBorrowedChart");
    if (!canvas) {
      return;
    }

    var dataSource = window.dashboardChartData || {};
    var chartData = dataSource.adminMostBorrowed || {
      labels: ["Arduino", "ESP32", "DHT22", "Raspberry Pi", "Relay Kit"],
      values: [18, 16, 13, 10, 8]
    };

    renderChart(canvas, {
      type: "bar",
      data: {
        labels: chartData.labels,
        datasets: [{
          label: "Borrow count",
          data: chartData.values,
          backgroundColor: ["#2563eb", "#0f766e", "#b45309", "#6d28d9", "#be123c"],
          borderRadius: 6
        }]
      }
    });
  }

  function renderChart(canvas, config) {
    if (!window.Chart) {
      drawCanvasFallback(canvas, "Chart.js will render here when loaded.");
      return;
    }

    new window.Chart(canvas, {
      type: config.type,
      data: config.data,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
            labels: {
              boxWidth: 12
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              precision: 0
            }
          }
        }
      }
    });
  }

  function drawCanvasFallback(canvas, message) {
    var context = canvas.getContext("2d");
    if (!context) {
      return;
    }

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "#64748b";
    context.font = "14px sans-serif";
    context.fillText(message, 16, 32);
  }
})();
