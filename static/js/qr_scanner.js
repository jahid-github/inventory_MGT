/*
  QR scanner placeholder.
  Backend note: connect html5-qrcode or another scanner library here when QR workflows are approved.
*/

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    var qrAreas = document.querySelectorAll("[data-qr-scanner]");

    qrAreas.forEach(function (area) {
      var button = area.querySelector("[data-qr-start]");
      if (!button) {
        return;
      }

      button.addEventListener("click", function () {
        button.textContent = "Scanner not connected";
        button.disabled = true;

        var note = document.createElement("p");
        note.className = "muted-text";
        note.textContent = "QR scanning is a frontend placeholder. Add html5-qrcode initialization in static/js/qr_scanner.js.";
        area.appendChild(note);
      });
    });
  });
})();
