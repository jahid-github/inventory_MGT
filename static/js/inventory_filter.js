/*
  Frontend-only inventory filtering.
  Backend note: server-side search can replace this later; keep data-* attributes on cards/rows for progressive enhancement.
*/

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    var searchInput = document.getElementById("inventory-search");
    var categoryFilter = document.getElementById("category-filter");
    var statusFilter = document.getElementById("status-filter");
    var cards = Array.prototype.slice.call(document.querySelectorAll("[data-inventory-card]"));
    var emptyState = document.getElementById("inventory-filter-empty");

    if (!cards.length) {
      return;
    }

    [searchInput, categoryFilter, statusFilter].forEach(function (control) {
      if (control) {
        control.addEventListener("input", applyFilters);
        control.addEventListener("change", applyFilters);
      }
    });

    applyFilters();

    function applyFilters() {
      var query = normalize(searchInput ? searchInput.value : "");
      var category = normalize(categoryFilter ? categoryFilter.value : "");
      var status = normalize(statusFilter ? statusFilter.value : "");
      var visibleCount = 0;

      cards.forEach(function (card) {
        var searchableText = normalize([
          card.dataset.name,
          card.dataset.category,
          card.dataset.status,
          card.dataset.location,
          card.dataset.serial
        ].join(" "));
        var cardCategory = normalize(card.dataset.category);
        var cardStatus = normalize(card.dataset.status);

        var matchesSearch = !query || searchableText.indexOf(query) !== -1;
        var matchesCategory = !category || cardCategory === category;
        var matchesStatus = !status || cardStatus === status;
        var shouldShow = matchesSearch && matchesCategory && matchesStatus;

        card.classList.toggle("is-hidden", !shouldShow);
        if (shouldShow) {
          visibleCount += 1;
        }
      });

      if (emptyState) {
        emptyState.hidden = visibleCount !== 0;
      }
    }

    function normalize(value) {
      return String(value || "").trim().toLowerCase();
    }
  });
})();
