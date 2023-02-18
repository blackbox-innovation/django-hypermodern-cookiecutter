import jquery from "jquery";
import select2 from "select2";

window.jQuery = jquery;
window.$ = jquery;

// Hook up select2 to jQuery
select2(jquery);

// add german language
jquery.fn.select2.amd.define("select2/i18n/de", [], function () {
  // German
  return {
    errorLoading: function () {
      return "Die Ergebnisse konnten nicht geladen werden.";
    },
    inputTooLong: function (args) {
      var overChars = args.input.length - args.maximum;

      return "Bitte höchstens " + overChars + " Zeichen eingeben";
    },
    inputTooShort: function (args) {
      var remainingChars = args.minimum - args.input.length;

      return "Bitte mindestens " + remainingChars + " Zeichen eingeben";
    },
    loadingMore: function () {
      return "Lade mehr Ergebnisse…";
    },
    maximumSelected: function (args) {
      var message = "Sie können nur " + args.maximum + " Element";

      if (args.maximum != 1) {
        message += "e";
      }

      message += " auswählen";

      return message;
    },
    noResults: function () {
      return "Keine Übereinstimmungen gefunden";
    },
    searching: function () {
      return "Suche…";
    },
    removeAllItems: function () {
      return "Entferne alle Elemente";
    },
  };
});

// https://stackoverflow.com/questions/65658432/select2-change-event-does-not-trigger-htmx
window.addEventListener("DOMContentLoaded", () => {
  window.$("select").on("select2:select", function _() {
    window.$(this).closest("select").get(0).dispatchEvent(new Event("change"));
  });

  // https://stackoverflow.com/questions/67988846/htmx-onload-on-full-page-load-and-on-after-swap
  document.body.addEventListener("htmx:load", () => {
    // look up all elements with the django-select2 class on it within the element
    window.$(".django-select2").djangoSelect2();
    window.$("select").on("select2:select", function _() {
      window
        .$(this)
        .closest("select")
        .get(0)
        .dispatchEvent(new Event("change"));
    });
  });
});
