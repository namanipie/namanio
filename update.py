import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# We will inject the new scripts and logic.

# 1. Update CSS variables in body to allow GSAP to scrub them.
html = re.sub(r"background: var\(--ground\)(.*?);", r"background: var(--ground-current, var(--ground)) \1;", html)

# Add CSS for tracker and reveals
css_additions = """
/* ── scroll animations & tracker ────────────────────────────────────── */
.reveal-text {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
  opacity: 0;
  transform: translateY(30px);
}
.reveal-fade {
  opacity: 0;
  transform: translateY(20px);
}
#section-tracker {
  position: fixed;
  bottom: 32px;
  right: var(--gutter);
  font-family: var(--f-mono);
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--ink-faint);
  z-index: 900;
  mix-blend-mode: difference;
  transition: opacity 0.3s;
}
"""
html = html.replace("/* ── layout ────────────────────────────────────────────────────────── */", css_additions + "\n/* ── layout ────────────────────────────────────────────────────────── */")


# Add tracker element
html = html.replace("<nav>", '<div id="section-tracker">01 / top</div>\n\n<nav>')

# Inject classes for GSAP targeting
html = html.replace('class="hero-heading"', 'class="hero-heading reveal-text"')
html = html.replace('class="hero-sub"', 'class="hero-sub reveal-fade"')
html = html.replace('class="section-heading"', 'class="section-heading reveal-text"')
html = html.replace('class="eyebrow"', 'class="eyebrow reveal-fade"')
html = html.replace('class="l-item"', 'class="l-item reveal-fade"')
html = html.replace('class="op-card"', 'class="op-card reveal-fade"')
html = html.replace('class="fp-content"', 'class="fp-content reveal-fade"')
html = html.replace('class="fp-visual"', 'class="fp-visual reveal-fade"')
html = html.replace('class="links-list"', 'class="links-list reveal-fade"')

# Add parallax classes to visual wall images
html = re.sub(r'<img src="(.*?)" alt="(.*?)" loading="lazy">', r'<img src="\1" alt="\2" loading="lazy" class="parallax-img">', html)


# Add scripts
scripts = """
<script src="https://unpkg.com/@studio-freight/lenis@1.0.39/dist/lenis.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>

<script>
/* ── smooth scroll & gsap setup ────────────────────────────────────── */
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  mouseMultiplier: 1,
  smoothTouch: false,
  touchMultiplier: 2,
  infinite: false,
})

lenis.on('scroll', ScrollTrigger.update)

gsap.ticker.add((time)=>{
  lenis.raf(time * 1000)
})
gsap.ticker.lagSmoothing(0)

/* ── scroll animations ─────────────────────────────────────────────── */
const mm = gsap.matchMedia();

mm.add("(prefers-reduced-motion: no-preference)", () => {
  
  // 1. Color atmosphere continuous shift
  // Shifts background ground color as we scroll down
  gsap.to("body", {
    "--ground-current": "#120e17", // subtly violet
    ease: "none",
    scrollTrigger: {
      trigger: "#projects",
      start: "top bottom",
      end: "bottom top",
      scrub: true
    }
  });
  
  gsap.to("body", {
    "--ground-current": "#0b0a0e", // back to dark
    ease: "none",
    scrollTrigger: {
      trigger: "#links",
      start: "top bottom",
      end: "bottom top",
      scrub: true
    }
  });

  // 2. Parallax
  gsap.utils.toArray('.parallax-img').forEach(img => {
    gsap.to(img, {
      yPercent: 15,
      scale: 1.05,
      ease: "none",
      scrollTrigger: {
        trigger: img.parentElement,
        start: "top bottom",
        end: "bottom top",
        scrub: true
      }
    });
  });

  // 3. Reveals
  gsap.utils.toArray('.reveal-text').forEach(el => {
    gsap.to(el, {
      opacity: 1,
      y: 0,
      duration: 1,
      ease: "power3.out",
      scrollTrigger: {
        trigger: el,
        start: "top 85%",
      }
    });
  });

  gsap.utils.toArray('.reveal-fade').forEach(el => {
    gsap.to(el, {
      opacity: 1,
      y: 0,
      duration: 1,
      ease: "power2.out",
      scrollTrigger: {
        trigger: el,
        start: "top 85%",
      }
    });
  });
  
  // 4. Section Tracker
  const sections = document.querySelectorAll('section');
  const tracker = document.getElementById('section-tracker');
  
  sections.forEach((sec, i) => {
    ScrollTrigger.create({
      trigger: sec,
      start: "top center",
      end: "bottom center",
      onEnter: () => updateTracker(i + 1, sec.id),
      onEnterBack: () => updateTracker(i + 1, sec.id)
    });
  });
  
  function updateTracker(num, name) {
    const padded = num.toString().padStart(2, '0');
    gsap.to(tracker, { opacity: 0, duration: 0.2, onComplete: () => {
      tracker.innerText = `${padded} / ${name}`;
      gsap.to(tracker, { opacity: 1, duration: 0.2 });
    }});
  }

});
</script>
"""

html = html.replace("</body>", scripts + "\n</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
