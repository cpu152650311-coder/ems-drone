const navToggle = document.querySelector(".nav-toggle");
const siteNav = document.querySelector(".site-nav");

if (navToggle && siteNav) {
  siteNav.id ||= "site-nav";
  navToggle.setAttribute("aria-controls", siteNav.id);

  navToggle.addEventListener("click", () => {
    const isOpen = siteNav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
    navToggle.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
  });

  siteNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      siteNav.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
      navToggle.setAttribute("aria-label", "Open navigation");
    });
  });
}

const modal = document.getElementById("inquiryModal");
const modalClose = modal?.querySelector(".modal-close");
let lastFocusedElement = null;
const pageRegions = [...document.querySelectorAll(".site-header, main, .site-footer")];

function openInquiry() {
  if (!modal) return;
  lastFocusedElement = document.activeElement;
  modal.classList.add("open");
  modal.setAttribute("aria-hidden", "false");
  document.body.classList.add("modal-open");
  pageRegions.forEach((region) => region.setAttribute("inert", ""));
  modalClose?.focus();
}

function closeInquiry() {
  if (!modal) return;
  modal.classList.remove("open");
  modal.setAttribute("aria-hidden", "true");
  document.body.classList.remove("modal-open");
  pageRegions.forEach((region) => region.removeAttribute("inert"));
  lastFocusedElement?.focus();
}

document.querySelectorAll("[data-open-inquiry]").forEach((button) => {
  button.addEventListener("click", openInquiry);
});

modalClose?.addEventListener("click", closeInquiry);
modal?.addEventListener("click", (event) => {
  if (event.target === modal) closeInquiry();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    if (modal?.classList.contains("open")) {
      closeInquiry();
    } else if (siteNav?.classList.contains("open")) {
      siteNav.classList.remove("open");
      navToggle?.setAttribute("aria-expanded", "false");
      navToggle?.setAttribute("aria-label", "Open navigation");
      navToggle?.focus();
    }
  }

  if (event.key === "Tab" && modal?.classList.contains("open")) {
    const focusable = [
      ...modal.querySelectorAll(
        'button:not([disabled]), input:not([disabled]), textarea:not([disabled]), select:not([disabled]), a[href]'
      ),
    ];
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }
});

const INQUIRY_ENDPOINT = "https://inquiry-proxy.workers.dev/";

function submitForm(form) {
  const status = form.querySelector(".form-status");
  const btn = form.querySelector("button[type=submit]");
  const origBtnText = btn?.textContent;

  if (status) {
    status.classList.remove("visible");
    status.textContent = "";
  }

  const data = Object.fromEntries(new FormData(form));
  data.source = window.location.pathname;

  fetch(INQUIRY_ENDPOINT, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((res) => {
      if (!res.ok) throw new Error("Server error " + res.status);
      window.location.href = "/thanks.html";
    })
    .catch(() => {
      if (status) {
        status.textContent = "Submission failed. Please email us directly at inquiry@ems-drone.com.";
        status.classList.add("visible");
      }
    })
    .finally(() => {
      if (btn) btn.textContent = origBtnText;
    });

  if (btn) btn.textContent = "Sending...";
}

const contactForm = document.getElementById("inquiryForm");
if (contactForm) {
  contactForm.addEventListener("submit", (e) => {
    e.preventDefault();
    submitForm(contactForm);
  });
}

document.querySelectorAll("[data-preview-form]").forEach((form) => {
  if (form === contactForm) return;
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    submitForm(form);
  });
});
