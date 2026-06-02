# PulseMap Pro 🌍

A web app that combines **REST Countries API**, **GNews API**, and **VADER sentiment analysis** to show the emotional tone of global news — visualized as an interactive world heatmap.

Search any country to see its latest headlines and whether the news is positive, neutral, or negative.

---

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/pulsemap.git
cd pulsemap
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the root folder:
```
GNEWS_API_KEY=your_key_here
```

Get a free key at https://gnews.io (free tier: 100 requests/day).

Replace your free key with 'your_key_here' in the .env file.

### 5. Run the app
```bash
python app.py
```

Open your browser at **http://127.0.0.1:5000**

---

## Features
- 🌍 Interactive world heatmap (green = positive, red = negative news)
- 🔍 Search any country by name
- 📰 Live top headlines with clickable links
- 😊 Sentiment score + label (Positive / Neutral / Negative)
- 🕐 Recent search history
- ⚠️ Handles slow API, network errors, and bad input gracefully

## APIs Used
- [REST Countries](https://restcountries.com) — country data & flags
- [GNews](https://gnews.io) — live news headlines
- [VADER Sentiment](https://github.com/cjhutto/vaderSentiment) — sentiment scoring
