document.addEventListener("DOMContentLoaded", () => {
  gsap.registerPlugin(ScrollTrigger);

  // ======= CARD SCROLL ANIMATION =======
  const cards = gsap.utils.toArray(".feature-card");

  gsap.set(cards, { opacity: 0, scale: 0.9, xPercent: -50, yPercent: -50 });

  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: ".features",
      start: "top top",
      end: "+=4000",  // ⏩ a little faster now
      scrub: 1,
      pin: true,
      pinSpacing: true,
      markers: false,
    },
  });

  // Step 1: sequential fade/appear (slightly faster)
  cards.forEach((card, i) => {
    const showTime = i * 1.2;  // faster than before
    const hideTime = showTime + 0.9;
    tl.to(card, { opacity: 1, scale: 1, duration: 0.8, ease: "power2.out" }, showTime);
    if (i < cards.length - 1) {
      tl.to(card, { opacity: 0, duration: 0.6, ease: "power2.in" }, hideTime);
    }
  });

  // Step 2: spread out final grid
  const spreadLabel = cards.length * 1.4 + 0.5;
  tl.addLabel("spread", spreadLabel);
  tl.to(cards, {
    opacity: 1,
    scale: 1,
    duration: 1.4,
    ease: "power3.out",
    stagger: 0.15,
    x: (i) => (i % 2 === 0 ? -180 : 180),
    y: (i) => (i < 2 ? -120 : 120),
  }, "spread");

  tl.to(".feature-stack", { scale: 0.95, duration: 1.2, ease: "power1.out" }, "spread+=0.4");

  // ======= SMOOTH FADE-IN ON SCROLL (Intersection Observer) =======
  const observerOptions = {
    threshold: 0.4,
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("show");
      }
    });
  }, observerOptions);

  document.querySelectorAll(".fade-in").forEach((el) => {
    observer.observe(el);
  });
});

// ===== AUTH MODAL LOGIC =====
const modal = document.getElementById("authModal");
const loginBtn = document.querySelector(".login-btn");
const closeBtn = document.getElementById("closeModal");
const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");

// Open modal (default = login)
loginBtn.addEventListener("click", () => {
  modal.style.display = "flex";
  loginForm.style.display = "block";
  registerForm.style.display = "none";
  document.body.style.overflow = "hidden";
});

// Close modal
closeBtn.addEventListener("click", () => {
  modal.style.display = "none";
  document.body.style.overflow = "auto";
});
// ===== "Get Started" button opens Register form =====
const getStartedBtn = document.querySelector(".cta-btn");

getStartedBtn.addEventListener("click", (e) => {
  e.preventDefault(); // prevent navigation
  modal.style.display = "flex";
  loginForm.style.display = "none";
  registerForm.style.display = "block";
  document.body.style.overflow = "hidden";
});
    

// Switch between forms
document.getElementById("switchToRegister").addEventListener("click", (e) => {
  e.preventDefault();
  loginForm.style.display = "none";
  registerForm.style.display = "block";
});

document.getElementById("switchToLogin").addEventListener("click", (e) => {
  e.preventDefault();
  registerForm.style.display = "none";
  loginForm.style.display = "block";
});

// ===== SEND TO BACKEND =====

// Login
document.getElementById("loginSubmit").addEventListener("click", async () => {
  const username = document.getElementById("loginUsername").value.trim();
  const password = document.getElementById("loginPassword").value.trim();

  const res = await fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const data = await res.json();
  alert(data.message || "Login attempted");
});

// Register
document.getElementById("registerSubmit").addEventListener("click", async () => {
  const username = document.getElementById("registerUsername").value.trim();
  const email = document.getElementById("registerEmail").value.trim();
  const password = document.getElementById("registerPassword").value.trim();

  const res = await fetch("/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, email, password })
  });

  const data = await res.json();
  alert(data.message || "Registration attempted");
});

// Guest Login
document.getElementById("guestLogin").addEventListener("click", () => {
  alert("Guest mode activated!");
  modal.style.display = "none";
});

