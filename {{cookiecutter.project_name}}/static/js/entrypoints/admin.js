import $ from "jquery";
import * as Ladda from "ladda";

window.Ladda = Ladda;
window.$ = $;

document.addEventListener("DOMContentLoaded", () => {
  // use Ladda for all forms
  Ladda.bind("*[type=submit]");
});

// handle bfcache
window.addEventListener("pageshow", (event) => {
  // restore Ladda buttons if user hits back button
  if (event.persisted) {
    Ladda.stopAll();
  }
});
