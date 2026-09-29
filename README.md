# Spanish Flashcards 🇪🇸

A vocabulary quiz app I built to practice my own Spanish learning. It quizzes you on Spanish-English word pairs and prioritizes words you get wrong, so you spend more time on what you actually need to review.

## Features
- Quizzes in both directions — Spanish to English and English to Spanish
- Tracks score and streak per session
- Weighted repetition: missed words show up more often until you get them right
- Simple, editable vocabulary list (`vocab.json`) — add your own words anytime

## Tech Stack
- **Backend:** Python, Flask — serves the quiz logic and vocab data through a small REST API
- **Frontend:** Vanilla HTML, CSS, JavaScript — no frameworks
- **Data:** Vocabulary stored in a plain JSON file, so it's easy to read and extend without a database

## How it works
The frontend asks the backend for a word (`/api/word`), which picks one using a weighted random choice — words answered incorrectly are more likely to come up again soon. When you submit an answer (`/api/answer`), the backend checks it, adjusts that word's weight, and returns whether you were right along with the correct answer and updated stats.

## Project Structure
spanish-flashcards/
├── app.py # Flask app: routes, quiz logic, weighting
├── vocab.json # Spanish-English word pairs
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Quiz page
└── static/
└── script.js # Frontend logic (fetches words, submits answers)

## Setup (to run locally)

1. Clone this repo
2. Create a virtual environment and activate it:
```bash
   python3 -m venv venv
   source venv/bin/activate
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Run the app:
```bash
   python app.py
```
5. Open `http://127.0.0.1:5000` in your browser

## Why I built this
I'm a Computer Science student at Central Texas College, learning Spanish on the side. I wanted a quiz tool that focuses more on the words I actually struggle with instead of quizzing everything equally, and building it myself was a good excuse to practice Python and Flask.

## Possible improvements
- Save progress between sessions instead of resetting on server restart
- Add word categories (verbs, food, travel, etc.) to quiz by topic
- Deploy it live so it's accessible without running it locally
