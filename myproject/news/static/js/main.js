document.addEventListener("DOMContentLoaded", function () {
    // Smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute("href"))
                .scrollIntoView({ behavior: "smooth" });
        });
    });

    // Contact form
    const form = document.getElementById("contactForm");
    const status = document.getElementById("msg-status");
    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            status.textContent = "✅ Xabar yuborildi!";
            status.style.color = "#00e6e6";
            form.reset();
        });
    }
});
