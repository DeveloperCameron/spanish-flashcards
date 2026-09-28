let currentDirection = '';

async function loadWord() {
  const res = await fetch('/api/word');
  const data = await res.json();
  currentDirection = data.direction;
  document.getElementById('prompt').textContent =
    (data.direction === 'es_to_en' ? '🇪🇸 → 🇬🇧 ' : '🇬🇧 → 🇪🇸 ') + data.prompt;
  document.getElementById('answer').value = '';
  document.getElementById('feedback').textContent = '';
}

async function submitAnswer() {
  const answer = document.getElementById('answer').value;
  const res = await fetch('/api/answer', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ answer })
  });
  const data = await res.json();

  const feedback = document.getElementById('feedback');
  if (data.correct) {
    feedback.textContent = '✅ Correct!';
    feedback.style.color = 'green';
  } else {
    feedback.textContent = `❌ Correct answer: ${data.correct_answer}`;
    feedback.style.color = 'red';
  }

  updateStats(data.stats);
  setTimeout(loadWord, 1200);
}

function updateStats(stats) {
  document.getElementById('stats').textContent =
    `Score: ${stats.correct}/${stats.total} · Streak: ${stats.streak}`;
}

document.getElementById('answer').addEventListener('keydown', e => {
  if (e.key === 'Enter') submitAnswer();
});

loadWord();