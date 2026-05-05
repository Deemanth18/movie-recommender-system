---
name: movie-recommender
description: "Recommend movies with similar vibes based on a movie the user liked. Analyzes mood, tone, themes, pacing, and emotional impact to find movies that recreate the same experience."
metadata:
  openclaw:
    requires:
      bins: ["python"]
      env: ["TMDB_API_KEY"]
---

# Movie Vibe Recommender

When the user mentions a movie they liked, watched, or want something similar to, follow these steps:

## Step 1: Analyze the Movie's Vibe

Break down the mentioned movie across these dimensions:
- **Mood & Tone**: dark, uplifting, tense, whimsical, melancholic, euphoric
- **Themes**: love, survival, revenge, self-discovery, justice, isolation, coming-of-age
- **Pacing**: slow burn, fast-paced, meditative, thriller-like, episodic
- **Visual Style**: gritty, colorful, minimalist, grand/epic, intimate
- **Emotional Impact**: tearjerker, adrenaline rush, comfort, thought-provoking, haunting

## Step 2: Generate Recommendations

Recommend **5 movies** that share the same vibe profile (not just the same genre).

For each movie, provide:
1. **Title and Year** with a relevant emoji
2. **"Same vibe:"** — one sentence explaining the shared experience/feeling
3. **Key match** — which vibe dimension matches most strongly

Format example:
```
🌌 Arrival (2016)
Same vibe: Mind-bending sci-fi with a deeply emotional core — the wonder of the unknown meets personal sacrifice.
Key match: Emotional depth + cerebral storytelling
```

## Step 3: Fetch Posters (Optional)

If the TMDB_API_KEY environment variable is set, use the `fetch_posters.py` script to get poster URLs:
```bash
python skills/movie-recommender/scripts/fetch_posters.py "Movie Title" "Year"
```
> Note: Use `python3` on macOS/Linux if `python` is not available.
Include the poster URL in the response if available.

## Step 4: Ask Follow-up

After recommendations, ask the user what they specifically loved about the original movie to refine future suggestions. For example:
- "What drew you in most — the visuals, the story, or the characters?"
- "Want more like this, or want to explore a different vibe?"

## Step 5: Update Memory

After the conversation, update MEMORY.md with:
- The movie the user mentioned (add to Watch History)
- Any vibe preferences learned (add to Vibe Preferences)
- Any directors/genres mentioned (add to relevant sections)

## Handling Edge Cases

- **Movie not recognized**: Ask for confirmation or suggest possible matches
- **Multiple movies mentioned**: Analyze the common vibes across all of them
- **Vague requests** (e.g., "something fun"): Ask clarifying questions about mood and setting
- **Non-English films**: Include recommendations from all languages/cultures if relevant
- **User says they disliked a movie**: Note in MEMORY.md under "Avoids" and offer contrasting vibes

## Response Style

- Keep it conversational, not robotic
- Use emoji to represent vibes (🌌 cosmic, 🔥 intense, 💔 emotional, 😂 comedic, 🎭 dramatic, 🔪 thriller, 🌈 feel-good)
- Cite the year for every movie
- Never spoil plots
