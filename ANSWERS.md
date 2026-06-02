# ANSWERS.md

## 1. How to run

**Requirements:** Python 3.8+, a free GNews API key from https://gnews.io (free tier: 100 requests/day, no credit card needed)

```bash
git clone https://github.com/YOUR_USERNAME/pulsemap.git
cd pulsemap

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```

Create a `.env` file in the root folder (use `.env.example` as a template):
```
GNEWS_API_KEY=your_key_here
```

Then run:
```bash
python app.py
```

Open your browser at **http://127.0.0.1:5000**

---

## 2. Stack choice

**Python + Flask + Vanilla JS**

I chose Python because the core of this project is sentiment analysis, and VADER is a Python library with no strong equivalent in other languages. Flask was the right backend choice because this app is essentially a lightweight API wrapper — it fetches from external APIs, runs sentiment scoring, and serves JSON to the frontend. Flask does this with minimal boilerplate and is easy to run on a fresh machine with one command.

On the frontend, vanilla JS with Plotly was enough. The choropleth map Plotly provides would have taken significantly more effort to replicate from scratch in D3 or similar tools.

A worse choice would have been Node.js + Express. Not because it can't handle the backend routing, but because I would have had to either find an inferior sentiment library or run a Python subprocess just for VADER, which adds unnecessary complexity and a second runtime dependency for whoever is running the project.

---

## 3. One real edge case

**What happens when a country has no English-language news?**

In `app.py` lines 28–30, after fetching news, the code checks if the returned articles list is empty:

if not news:
    sentiment = 0
    sentiment_label = "Neutral"

Without this check, the line directly below — 
`sum([get_score(n) for n in news]) / len(news)` — 
would throw a `ZeroDivisionError` and crash the server with a 500 error. This is not a rare case, smaller or less covered countries often return zero English articles from GNews. The frontend also handles this gracefully by showing "No recent English news found" instead of an empty list, so the user always gets a clear response.

---

## 4. AI usage

I used ChatGPT in this project as a learning guide while building it.

**Where I used it:**
- Setting up the project structure (Flask app factory, services folder layout, understanding the APIs useful to this project.)
- Understanding how to load API keys securely from a .env file using python-dotenv instead of hardcoding them
- Fixing a ZeroDivisionError when news articles came back empty
- Majority of the frontend: I find frontend taxing, and I get nitpicky and take a lot of time while hand coding front end. ChatGPT helped me with adding a loading state, Enter key support, recent search history, and clickable article links.
- Refining the files code by fixing indendations, more meaningful variable names and suggesting shorter altervaives to exisiting code.

**Something I changed from the AI output:**

When I asked for help with the visualization, ChatGPT initially suggested displaying country sentiment as a bar chart comparing countries side by side. I decided against this and pushed for an interactive world heatmap instead. I've worked with heatmaps in previous projects and wanted to apply that in a real-time context, a world map makes the sentiment data feel geographical and intuitive in a way a bar chart doesn't. The heatmap also scales better visually as more countries get searched. This was my own decision and I'm glad I pushed for it.

---

## 5. Honest gap

The world heatmap loads with hardcoded dummy sentiment values for 15 countries. This means the colors on first load are illustrative, not real a user who doesn't search anything will see data that doesn't reflect actual current news.

With another day, I would replace the static data with a startup routine that fetches and caches real sentiment scores for the 30 most searched countries when the Flask app first launches. I would store the results in memory with a timestamp, and refresh them every few hours in a background thread. This would make the initial heatmap meaningful and live rather than decorative.