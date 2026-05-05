# 🎬 CineMatch — AI Movie Vibe Recommender

> **Tell me a movie you loved. I'll find movies that feel the same way.**

CineMatch is an AI-powered Telegram bot that recommends movies based on **vibes** — not just genres. It understands the mood, tone, pacing, and emotional impact of movies to find ones that recreate the same experience.

Built with [OpenClaw](https://openclaw.ai) for the **Clash of the Claws** hackathon (PRISM, SRI-B) — Theme 2: Daily Utility.

---

## ✨ What Makes CineMatch Different?

Most movie recommenders match by genre or ratings. CineMatch matches by **feelings**.

| Traditional Recommender | CineMatch |
|---|---|
| "You liked Interstellar → here are more sci-fi movies" | "You liked Interstellar → here are movies with the same cosmic awe + emotional father-daughter story" |
| Genre-based matching | Vibe-based matching (mood, tone, pacing, visual style, emotional impact) |
| Static suggestions | Learns your taste over time |
| One-time use | Daily evening movie picks |

---

## 🚀 How It Works

### Step 1: Send a Movie Name
Message CineMatch on Telegram with any movie you enjoyed.

### Step 2: Get Vibe-Matched Recommendations
CineMatch analyzes the movie's vibe across 5 dimensions and recommends 5 movies that recreate the same experience.

### Step 3: Refine Your Taste
Tell CineMatch what you specifically loved — it remembers and personalizes future recommendations.

### Example Conversation

```
You:  "I just watched Interstellar and loved it"

CineMatch: 🌌 If you loved Interstellar, here are movies with the same vibe:

1. 🌌 Arrival (2016)
   Same vibe: Mind-bending sci-fi with deep emotional core
   Key match: Emotional depth + cerebral storytelling

2. 🚀 The Martian (2015)
   Same vibe: Space survival with optimistic problem-solving
   Key match: "Humanity at its best" feeling

3. 🌊 Contact (1997)
   Same vibe: Cosmic awe with father-daughter emotional thread
   Key match: Wonder of the unknown

4. 🎭 Inception (2010)
   Same vibe: Nolan's layered storytelling with time manipulation
   Key match: Mind-bending narrative

5. 🌑 Gravity (2013)
   Same vibe: Visceral space isolation and survival
   Key match: Pure cinematic immersion

What drew you in most — the visuals, the story, or the characters?
```

---

## 📱 Supported Channels

| Channel | Status | How to Use |
|---------|--------|------------|
| **Telegram** | ✅ Active | Search for your bot on Telegram and start chatting |
| **WhatsApp** | 🔜 Coming Soon | Will be added in a future update via OpenClaw's WhatsApp adapter |
| **Terminal** | ✅ Active | Use `openclaw chat` for local testing |

---

## 🧠 Key Features

- **🎭 Vibe Matching** — Analyzes mood, tone, themes, pacing, visual style, and emotional impact
- **🧠 Memory** — Remembers your taste profile across conversations (stored in `MEMORY.md`)
- **🍿 Evening Picks** — Proactively suggests a movie every evening at 7 PM via `HEARTBEAT.md`
- **🖼️ Movie Posters** — Fetches poster images from TMDB API
- **🌍 Multi-Language** — Recommends movies across all languages and cultures
- **💬 Conversational** — Asks follow-up questions to refine your preferences
- **🆓 100% Free** — Uses free LLM models via OpenRouter, free TMDB API, free Telegram Bot API

---

## 🏗️ Architecture

```
User's Phone (Telegram/WhatsApp)
        │
        ▼
  OpenClaw Gateway  ←→  LLM (Meta Llama 3.3 70B / Google Gemma 27B — FREE)
        │
        ├── SOUL.md     → Agent personality (film-savvy, vibe-aware)
        ├── MEMORY.md   → Your taste profile (learns over time)
        ├── HEARTBEAT.md → Proactive evening movie suggestions
        └── SKILL.md    → Movie recommendation logic
                │
                └── fetch_posters.py → TMDB API for poster images
```

**OpenClaw 5-Layer Stack:**

| Layer | Component | Role |
|-------|-----------|------|
| 1 | Communication | Telegram Bot (+ WhatsApp coming soon) |
| 2 | Channel Adapter | OpenClaw built-in adapters |
| 3 | Gateway | OpenClaw Gateway (Node.js) |
| 4 | Pi Engine | LLM reasoning (free via OpenRouter) |
| 5 | Skill Execution | `movie-recommender` skill + TMDB poster script |

---

## 🛠️ Setup Guide (for Developers)

### Prerequisites

| Tool | Version | How to Get |
|------|---------|------------|
| **Node.js** | ≥ 22 | [nodejs.org](https://nodejs.org) |
| **Python** | ≥ 3.8 | [python.org](https://python.org) |
| **OpenClaw CLI** | Latest | `npm install -g openclaw@latest` |

### Step 1: Clone the Repository

```bash
git clone https://github.com/akash-s-ksgd/movie-recommender-system.git
cd movie-recommender-system
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Get Your Free API Keys

You need **2 free API keys** (the LLM is free and needs no key):

| Key | Where to Get It | Cost |
|-----|-----------------|------|
| **TMDB API Key** | [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api) | Free |
| **Telegram Bot Token** | Message [@BotFather](https://t.me/botfather) on Telegram → `/newbot` | Free |

### Step 4: Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and paste your keys:
```env
TMDB_API_KEY=your_tmdb_key_here
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

### Step 5: Set Up OpenClaw

```bash
# Set your workspace
openclaw config set agents.defaults.workspace .
openclaw config set gateway.mode local

# Set free LLM model (no API key needed!)
openclaw models set "openrouter/meta-llama/llama-3.3-70b-instruct:free"
openclaw models fallbacks add "openrouter/google/gemma-3-27b-it:free"

# Add your Telegram bot
openclaw channels add --channel telegram --token "YOUR_BOT_TOKEN_HERE" --name "CineMatch Bot"
```

### Step 6: Start the Bot

```bash
openclaw gateway start
```

Now message your Telegram bot with a movie name! 🎬

### Optional: Test Locally First

```bash
# Test in terminal (no Telegram needed)
openclaw chat

# Test poster fetching
python .openclaw/skills/movie-recommender/scripts/fetch_posters.py "Interstellar" "2014"
```

---

## 📁 Project Structure

```
movie-recommender-system/
├── .openclaw/                      ← OpenClaw agent configuration
│   ├── SOUL.md                     ← Agent personality (enthusiastic film buff)
│   ├── AGENTS.md                   ← Rules & boundaries
│   ├── MEMORY.md                   ← User taste profile (evolves over time)
│   ├── USER.md                     ← User info (name, timezone)
│   ├── HEARTBEAT.md                ← Proactive tasks (evening movie pick)
│   └── skills/
│       └── movie-recommender/
│           ├── SKILL.md            ← Core recommendation logic
│           └── scripts/
│               └── fetch_posters.py  ← TMDB poster URL fetcher
├── memory/                         ← Daily interaction logs (auto-generated)
├── legacy/                         ← Original TF-IDF recommender (preserved)
│   ├── app/                        ← Old Streamlit frontend
│   ├── src/                        ← Old Python ML backend
│   └── data/                       ← MovieLens dataset
├── .env                            ← Your API keys (git-ignored)
├── .env.example                    ← Template showing required keys
├── package.json                    ← Node.js project metadata
├── requirements.txt                ← Python dependencies
├── .gitignore                      ← Git ignore rules
└── README.md                       ← This file
```

---

## 🛠️ Tech Stack

| Component | Technology | Cost |
|-----------|-----------|------|
| AI Agent Platform | [OpenClaw](https://openclaw.ai) | Free |
| LLM (Primary) | Meta Llama 3.3 70B via [OpenRouter](https://openrouter.ai) | Free |
| LLM (Fallback) | Google Gemma 3 27B via OpenRouter | Free |
| Messaging | Telegram Bot API | Free |
| Movie Data & Posters | [TMDB API](https://themoviedb.org) | Free |
| Poster Fetcher | Python + requests | Free |
| Runtime | Node.js ≥ 22 | Free |

**Total cost: $0** 💸

---

## 🧩 How the Vibe Matching Works

When you mention a movie, CineMatch analyzes it across **5 vibe dimensions**:

| Dimension | Example (Interstellar) |
|-----------|----------------------|
| **Mood & Tone** | Awe-inspiring, emotionally heavy |
| **Themes** | Love, survival, time, sacrifice |
| **Pacing** | Slow burn with intense climax |
| **Visual Style** | Grand/epic, stunning cinematography |
| **Emotional Impact** | Tearjerker with cosmic wonder |

It then finds movies that score similarly across these dimensions — not just movies in the same genre.

---

## 🔮 Roadmap

- [x] Core vibe-matching skill
- [x] Telegram bot integration
- [x] Persistent memory (taste profile)
- [x] Proactive evening suggestions
- [x] TMDB poster fetching
- [x] Free LLM via OpenRouter
- [ ] WhatsApp integration
- [ ] Discord bot support
- [ ] Watch party coordination
- [ ] Streaming platform availability check
- [ ] Group taste profile merging

---

## 📋 Hackathon Info

| Detail | Info |
|--------|------|
| **Hackathon** | Clash of the Claws (PRISM, SRI-B) |
| **Theme** | Theme 2 — Daily Utility |
| **Problem** | Finding the right movie is a daily struggle. Genre-based recommendations miss the point — CineMatch matches by vibes. |
| **Team** | Akash S |
| **Deadline** | May 8, 2026 |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details.

---

**Made with 🎬 by [Akash S](https://github.com/akash-s-ksgd)**
