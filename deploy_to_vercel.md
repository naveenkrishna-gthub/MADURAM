# How to Deploy to Vercel (100% Free & Zero Setup)

Because this game is built entirely with client-side HTML, CSS, JavaScript, and MediaPipe CDN, **it requires NO server backend** and can be deployed directly to Vercel for free in under 1 minute!

---

## Option 1: Drag-and-Drop Deploy (Easiest — No Git required)

1. Go to **[https://vercel.com](https://vercel.com)** and log in (with your GitHub, Google, or email).
2. Install the free Vercel CLI (or open your terminal):
   ```bash
   npx vercel
   ```
3. When prompted:
   - Set up and deploy? **Yes (`y`)**
   - Which scope? **Your account**
   - Link to existing project? **No (`n`)**
   - Project name? **aadum-madhirkkum-pinne-kaikkum** (or any name)
   - In which directory? **`./`** (press Enter)
   - Want to modify settings? **No (`n`)**
4. Done! Vercel will give you a live production link like:
   👉 `https://aadum-madhirkkum-pinne-kaikkum.vercel.app`

---

## Option 2: Deploy with GitHub (Best for teamwork)

1. Create a new repository on **GitHub** (e.g., `ai-facial-arena`).
2. Push this folder to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of AI expression game"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ai-facial-arena.git
   git push -u origin main
   ```
3. Go to **[https://vercel.com/new](https://vercel.com/new)**.
4. Click **Import** next to your GitHub repository.
5. Click **Deploy** (keep default settings).
6. In 15 seconds, your site is live with **HTTPS** enabled!

---

## Why Vercel is Perfect for This Project:
- **Automatic HTTPS (`https://`)**: Browsers require HTTPS to allow webcam camera access on phones and other laptops. Vercel provides this automatically for free.
- **Zero Server Costs**: Completely serverless static hosting.
- **Instant Updates**: Whenever you push changes, Vercel updates the live site instantly.
