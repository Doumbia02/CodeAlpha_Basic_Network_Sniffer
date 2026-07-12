# 🎣 Phishing Awareness Training

A self-contained security awareness training module on phishing attacks — built as a **19-slide presentation** plus a **standalone interactive quiz** for hands-on reinforcement.

> Recognize the red flags. Resist the pressure. Report before you regret it.

---

## 📦 What's in this repo

| Path | What it is |
|---|---|
| [`presentation/Phishing-Awareness-Training.pptx`](./presentation/Phishing-Awareness-Training.pptx) | Full training deck (PowerPoint, 19 slides) |
| [`interactive-quiz/index.html`](./interactive-quiz/index.html) | Standalone, click-through quiz with instant scoring — works offline, no build step |
| `docs/screenshots/` | Preview images of the deck |

---

## 📽️ Presentation contents

1. **What is phishing?** — definition, and why it targets people, not systems
2. **Why phishing keeps winning** — current stats (CISA, FBI IC3, IBM, KnowBe4)
3. **Six faces of phishing** — email, spear phishing, whaling, smishing, vishing, quishing
4. **Anatomy of a phishing email** — an annotated, red-flagged example
5. **Spotting a fake website** — URL tricks, page-level warning signs
6. **Social engineering tactics** — urgency, authority, fear, greed, trust
7. **Two real breach case studies** — the 2017 Google Docs worm, and the 2023 MGM Resorts help-desk vishing attack
8. **Best practices** — a clear Do / Don't checklist
9. **Incident response** — what to do in the first minutes after a click
10. **3-question scenario quiz** — with answer + explanation slides
11. **Key takeaways**

### Preview

<table>
<tr>
<td><img src="docs/screenshots/01-title.jpg" width="400"/></td>
<td><img src="docs/screenshots/02-email-anatomy.jpg" width="400"/></td>
</tr>
<tr>
<td><img src="docs/screenshots/03-social-engineering.jpg" width="400"/></td>
<td><img src="docs/screenshots/04-quiz-slide.jpg" width="400"/></td>
</tr>
</table>

---

## 🧠 Interactive quiz

The PPTX quiz slides are static (great for a live/group session), so `interactive-quiz/index.html` adds a genuinely clickable version for self-paced or async learning:

- 5 realistic scenarios (BEC gift-card scam, smishing, vishing/help-desk, spoofed brand email, malicious app permissions)
- Instant right/wrong feedback with a plain-English explanation for each answer
- Progress bar + final score summary
- Zero dependencies — a single HTML file, works by double-clicking it or via GitHub Pages

### Run it locally
```bash
# just open it in a browser
open interactive-quiz/index.html      # macOS
start interactive-quiz/index.html     # Windows
xdg-open interactive-quiz/index.html  # Linux
```

### Or host it with GitHub Pages
1. Go to **Settings → Pages** in this repo
2. Set the source to the `main` branch, `/interactive-quiz` folder (or copy `index.html` to the repo root if you want it at the site's base URL)
3. Your quiz will be live at `https://<your-username>.github.io/<repo-name>/`

---

## 🎯 Intended audience

Employees or students with no security background — onboarding sessions, annual compliance refreshers, or a quick lunch-and-learn.

## 📚 Sources

Statistics cited in the deck are drawn from: CISA, the FBI Internet Crime Complaint Center (IC3) 2024 Annual Report, IBM's *Cost of a Data Breach Report 2025*, and KnowBe4's *2025 Phishing by Industry Benchmarking Report*. Case studies reference public reporting on the 2017 Google Docs phishing worm and the 2023 MGM Resorts breach.

## 📝 License

Content is provided under the [MIT License](./LICENSE) — feel free to reuse, adapt, and redistribute for your own training programs, with attribution appreciated.

---

<sub>Built with [pptxgenjs](https://gitbrent.github.io/PptxGenJS/) and vanilla HTML/CSS/JS.</sub>
