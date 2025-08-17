
// Für Fade-in
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add("visible");
      }, 100); // Verzögerung in ms
    }
  });
});

document.querySelectorAll(".fade-in").forEach(el => observer.observe(el));


// Fade-in nach kurzer Verzögerung nur im mainWrapper starten
window.addEventListener("DOMContentLoaded", () => {
    const mainWrapper = document.querySelector(".main-wrapper");
    requestAnimationFrame(() => {
        mainWrapper.classList.remove("visible");
    });

  // Alle internen Links abfangen
  const links = document.querySelectorAll("a[href]");
  links.forEach(link => {
    link.addEventListener("click", function (e) {
      const target = this.href;

      // Ignoriere externe Links oder solche mit target="_blank"
      if (
        target !== window.location.href &&
        this.getAttribute("target") !== "_blank" &&
        target.startsWith(window.location.origin)
      ) {
        e.preventDefault();

        // Fade-out aktivieren
        mainWrapper.classList.remove("visible");
        mainWrapper.classList.add("invisible");

        // Nach Timeout zur neuen Seite wechseln
        setTimeout(() => {
          window.location.href = target;
        }, 1600); // Zeit muss zum CSS passen + etwas Puffer
      }
    });
  });
});