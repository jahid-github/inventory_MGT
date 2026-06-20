/*
  Global JavaScript for the IoT Lab Inventory frontend.
  Backend note: these behaviors do not depend on models and are safe for template-only pages.
*/

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    initThemeToggle();
    initSidebar();
    initDropdowns();
    initLoadingForms();
  });

  function initThemeToggle() {
    var root = document.documentElement;
    var savedTheme = localStorage.getItem("iot_lab_theme");
    var initialTheme = savedTheme || "light";
    var buttons = document.querySelectorAll("[data-theme-toggle]");

    root.setAttribute("data-theme", initialTheme);
    buttons.forEach(function (button) {
      button.setAttribute("aria-pressed", String(initialTheme === "dark"));
      button.addEventListener("click", function () {
        var nextTheme = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", nextTheme);
        localStorage.setItem("iot_lab_theme", nextTheme);
        buttons.forEach(function (toggle) {
          toggle.setAttribute("aria-pressed", String(nextTheme === "dark"));
        });
      });
    });
  }

  function initSidebar() {
    var openButton = document.querySelector("[data-sidebar-toggle]");
    var closeButton = document.querySelector("[data-sidebar-close]");

    if (openButton) {
      openButton.addEventListener("click", function () {
        document.body.classList.add("sidebar-open");
      });
    }

    if (closeButton) {
      closeButton.addEventListener("click", function () {
        document.body.classList.remove("sidebar-open");
      });
    }

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        document.body.classList.remove("sidebar-open");
      }
    });
  }

  function initDropdowns() {
    var dropdowns = document.querySelectorAll("[data-dropdown]");

    dropdowns.forEach(function (dropdown) {
      var toggle = dropdown.querySelector("[data-dropdown-toggle]");
      if (!toggle) {
        return;
      }

      toggle.addEventListener("click", function (event) {
        event.stopPropagation();
        var isOpen = dropdown.classList.toggle("open");
        toggle.setAttribute("aria-expanded", String(isOpen));
      });
    });

    document.addEventListener("click", function () {
      dropdowns.forEach(function (dropdown) {
        dropdown.classList.remove("open");
        var toggle = dropdown.querySelector("[data-dropdown-toggle]");
        if (toggle) {
          toggle.setAttribute("aria-expanded", "false");
        }
      });
    });
  }

  function initLoadingForms() {
    var forms = document.querySelectorAll("[data-loading-form]");

    forms.forEach(function (form) {
      form.addEventListener("submit", function () {
        if (!form.checkValidity()) {
          return;
        }

        var buttons = form.querySelectorAll("button[type='submit']");
        buttons.forEach(function (button) {
          var loadingText = button.getAttribute("data-loading-text");
          button.disabled = true;
          button.classList.add("is-loading");
          if (loadingText) {
            button.dataset.originalText = button.textContent;
            button.textContent = loadingText;
          }
        });
      });
    });
  }
})();
