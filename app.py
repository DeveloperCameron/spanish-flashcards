from flask import Flask, jsonify, request, render_template
import json
import random

app = Flask(__name__)

with open('vocab.json', encoding='utf-8') as f:
    VOCAB = json.load(f)

# In-memory session state (resets when the server restarts — fine for v1)
weights = {i: 1 for i in range(len(VOCAB))}
current = {"index": None, "direction": None}
stats = {"correct": 0, "total": 0, "streak": 0}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/word')
def get_word():
    index = random.choices(range(len(VOCAB)), weights=[weights[i] for i in range(len(VOCAB))])[0]
    direction = random.choice(['es_to_en', 'en_to_es'])
    current['index'] = index
    current['direction'] = direction

    word = VOCAB[index]
    prompt = word['es'] if direction == 'es_to_en' else word['en']

    return jsonify({"prompt": prompt, "direction": direction})


@app.route('/api/answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    user_answer = data.get('answer', '').strip().lower()

    index = current['index']
    direction = current['direction']
    word = VOCAB[index]
    correct_answer = word['en'] if direction == 'es_to_en' else word['es']

    is_correct = user_answer == correct_answer.lower()

    stats['total'] += 1
    if is_correct:
        stats['correct'] += 1
        stats['streak'] += 1
        weights[index] = max(1, weights[index] - 1)
    else:
        stats['streak'] = 0
        weights[index] += 3  # missed words show up more often

    return jsonify({
        "correct": is_correct,
        "correct_answer": correct_answer,
        "stats": stats
    })


@app.route('/api/stats')
def get_stats():
    return jsonify(stats)


if __name__ == '__main__':
    app.run(debug=True)