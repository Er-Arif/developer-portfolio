const yearEl = document.getElementById("year");
if (yearEl) {
  yearEl.textContent = new Date().getFullYear();
}

const menuToggle = document.getElementById("menuToggle");
const primaryMenu = document.getElementById("primaryMenu");
if (menuToggle && primaryMenu) {
  menuToggle.addEventListener("click", () => {
    const isOpen = primaryMenu.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
  });

  primaryMenu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      primaryMenu.classList.remove("open");
      menuToggle.setAttribute("aria-expanded", "false");
    });
  });
}

const sectionLinks = Array.from(document.querySelectorAll('.menu a[href^="#"]'));
const linkedSections = sectionLinks
  .map((link) => {
    const id = link.getAttribute("href");
    return id ? document.querySelector(id) : null;
  })
  .filter((el) => el && el.tagName.toLowerCase() === "section");

if (sectionLinks.length > 0 && linkedSections.length > 0) {
  const setActive = (sectionId) => {
    sectionLinks.forEach((link) => {
      const match = link.getAttribute("href") === `#${sectionId}`;
      link.classList.toggle("active", match);
      if (match) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        setActive(entry.target.id);
      }
    });
  }, { rootMargin: "-38% 0px -52% 0px", threshold: 0.01 });

  linkedSections.forEach((section) => sectionObserver.observe(section));
}

const scrollBar = document.getElementById("scrollBar");
if (scrollBar) {
  const syncScrollProgress = () => {
    const doc = document.documentElement;
    const max = doc.scrollHeight - doc.clientHeight;
    const pct = max > 0 ? (doc.scrollTop / max) * 100 : 0;
    scrollBar.style.width = `${pct}%`;
  };

  syncScrollProgress();
  window.addEventListener("scroll", syncScrollProgress, { passive: true });
  window.addEventListener("resize", syncScrollProgress);
}

const hero = document.querySelector(".hero");
if (hero && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const applyHeroParallax = () => {
    const top = window.scrollY;
    const maxShift = 28;
    const shift = Math.max(-maxShift, Math.min(maxShift, top * 0.08));
    hero.style.setProperty("--hero-shift", `${shift}px`);
  };

  applyHeroParallax();
  window.addEventListener("scroll", applyHeroParallax, { passive: true });
}

const reveals = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window && reveals.length > 0) {
  reveals.forEach((el, idx) => {
    el.style.transitionDelay = `${Math.min(idx * 45, 220)}ms`;
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        return;
      }
      entry.target.classList.add("is-visible");
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.15 });

  reveals.forEach((el) => observer.observe(el));
} else {
  reveals.forEach((el) => el.classList.add("is-visible"));
}

const copyEmailButton = document.querySelector(".copy-email-btn");
if (copyEmailButton) {
  const statusEl = document.querySelector(".copy-email-status");
  copyEmailButton.addEventListener("click", async () => {
    const email = copyEmailButton.getAttribute("data-email") || "";
    try {
      await navigator.clipboard.writeText(email);
      if (statusEl) {
        statusEl.textContent = "Email copied.";
      }
    } catch {
      if (statusEl) {
        statusEl.textContent = "Could not copy email.";
      }
    }
  });
}
