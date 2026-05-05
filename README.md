# MovieClaw — AI Movie Vibe Recommender 🎬

An **OpenClaw-powered AI agent** that recommends movies based on vibes, not just genres. Tell it a movie you loved, and it finds movies that recreate the same experience — the same mood, tone, pacing, and emotional impact.

Built for the **Clash of the Claws** hackathon (PRISM, SRI-B) — Theme 2: Daily Utility.

## 🎯 How It Works

```
You (Telegram): "I just watched Interstellar and loved it"

MovieClaw: 🌌 If you loved Interstellar, here are movies with the same vibe:

1. 🌌 Arrival (2016) — Mind-bending sci-fi with deep emotional core
2. 🚀 The Martian (2015) — Space survival with optimistic problem-solving  
3. 🌊 Contact (1997) — Cosmic awe with father-daughter emotional thread
4. 🎭 Inception (2010) — Nolan's layered storytelling with time manipulation
5. 🌑 Gravity (2013) — Visceral space isolation and survival

What drew you in most — the visuals, the story, or the characters?
```

## 🏗️ Architecture

```
User's Phone (Telegram) → OpenClaw Gateway → LLM (Gemini/OpenAI) → MovieClaw Skill
                                                    ↕
                                              MEMORY.md (learns your taste)
                                              HEARTBEAT.md (daily suggestions)
```

**OpenClaw 5-Layer Stack:**

| Layer | Component | Role |
|-------|-----------|------|
| 1 | Communication | Telegram Bot |
| 2 | Channel Adapter | OpenClaw built-in Telegram adapter |
| 3 | Gateway | OpenClaw Gateway (Node.js) |
| 4 | Pi Engine | LLM reasoning (Gemini Flash / OpenAI) |
| 5 | Skill Execution | `movie-recommender` skill + TMDB poster script |

## ✨ Features

- **Vibe Matching**: Goes beyond genre — matches mood, tone, pacing, visual style, emotional impact
- **Persistent Memory**: Remembers your taste profile across sessions (MEMORY.md)
- **Proactive Suggestions**: Sends a "Tonight's Pick" every evening via HEARTBEAT.md
- **Poster Display**: Fetches movie posters from TMDB API
- **Multi-Language**: Recommends movies across all languages and cultures
- **Conversational**: Asks follow-ups to refine your preferences

## 🚀 Setup

### Prerequisites
- **Node.js** ≥ 22 ([download](https://nodejs.org))
- **Python 3** (for TMDB poster helper script)
- **OpenClaw CLI**: `npm install -g openclaw@latest`

### 1. Clone & Configure

```bash
git clone https://github.com/akash-s-ksgd/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```env
GEMINI_API_KEY=your_gemini_api_key_here
TMDB_API_KEY=your_tmdb_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```

**Where to get keys:**
- **Gemini API Key** (free): [Google AI Studio](https://aistudio.google.com/apikey)
- **TMDB API Key** (free): [TMDB Developer](https://www.themoviedb.org/settings/api)
- **Telegram Bot Token**: Message [@BotFather](https://t.me/botfather) on Telegram

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run OpenClaw Onboard

```bash
openclaw onboard
```

Follow the wizard to:
- Set your LLM provider (Gemini / OpenAI)
- Connect your Telegram bot

### 5. Start the Agent

```bash
openclaw gateway start
```

Now message your Telegram bot with a movie name!

## 📁 Project Structure

```
├── .openclaw/
│   ├── SOUL.md                    ← Agent personality
│   ├── AGENTS.md                  ← Rules & boundaries
│   ├── MEMORY.md                  ← User taste profile (evolves)
│   ├── USER.md                    ← User info
│   ├── HEARTBEAT.md               ← Proactive scheduled tasks
│   └── skills/
│       └── movie-recommender/
│           ├── SKILL.md           ← Vibe-matching recommendation skill
│           └── scripts/
│               └── fetch_posters.py  ← TMDB poster URL fetcher
├── memory/                        ← Daily interaction logs
├── legacy/                        ← Original TF-IDF recommender (preserved)
├── README.md
├── .env.example
├── requirements.txt
└── .gitignore
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| AI Agent Platform | OpenClaw |
| LLM | Google Gemini Flash (free tier) |
| Messaging | Telegram Bot API |
| Movie Data | TMDB API |
| Poster Fetcher | Python + requests |
| Runtime | Node.js ≥ 22 |

## 📋 Hackathon Info

- **Hackathon**: Clash of the Claws (PRISM, SRI-B)
- **Theme**: Theme 2 — Daily Utility
- **Problem**: Finding the right movie to watch is a daily decision. Most recommenders match by genre or ratings. MovieClaw matches by *vibes* — the actual feeling and experience of watching a movie.

## 📄 License

MIT
