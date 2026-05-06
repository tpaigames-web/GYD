# GYD Marketing · 管一点营销

Single-page scroll-driven marketing site for **GYD Marketing** (Johor Bahru, Malaysia).

Built with vanilla HTML + GSAP ScrollTrigger + Lenis (smooth scroll). The mascot
animation is a 55-frame PNG flipbook driven by the user's scroll position
(Apple-style image sequence).

## Project structure

```
.
├── index.html              # the whole site, single file
├── Cow_transparent/        # 55 mascot frames (cow_00.png .. cow_54.png) — transparent
├── remove_bg.py            # one-shot script that produced Cow_transparent/ from the original Cow/
└── README.md
```

## Local preview

```bash
python -m http.server 5173
# then open http://localhost:5173
```

## Deploy on GitHub Pages

1. Create a new **public** repository on https://github.com/new (e.g. `gyd-site`).
2. Push this folder to it (see commands below).
3. In the repo, go to **Settings → Pages** → **Source: Deploy from a branch** → **Branch: `main` / `(root)`** → **Save**.
4. Wait ~2 min. Site goes live at `https://<your-username>.github.io/<repo-name>/`.

### One-time push commands

Replace `<your-username>` and `<repo-name>` below.

```bash
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```
