document.addEventListener("DOMContentLoaded", () => {
  const navbarBurgers = Array.prototype.slice.call(
    document.querySelectorAll(".navbar-burger"),
    0
  );

  if (navbarBurgers.length > 0) {
    navbarBurgers.forEach((el) => {
      el.addEventListener("click", () => {
        const targetId = el.dataset.target;
        const target = document.getElementById(targetId);

        el.classList.toggle("is-active");
        target.classList.toggle("is-active");
      });
    });
  }
});
