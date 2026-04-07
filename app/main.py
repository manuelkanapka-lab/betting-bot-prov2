from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.parser import get_odds
from app.model import find_value_bets
from app.bankroll import calculate_stake

app = FastAPI()

HTML = """
<html>
<head>
<title>Betting Bot PRO</title>
<style>
body { font-family: Arial; background: #111; color: white; text-align: center; }
table { margin: auto; border-collapse: collapse; }
td, th { padding: 10px; border: 1px solid #444; }
.green { color: #00ff88; }
.red { color: #ff4d4d; }
button { padding: 10px 20px; font-size: 16px; }
</style>
</head>

<body>
<h1>🔥 Betting Bot PRO</h1>

<form method="get">
<button type="submit">Pobierz kursy</button>
</form>

{content}

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    odds = get_odds()
    analysis = find_value_bets(odds)
    stake = calculate_stake(100)

    table = "<h3>Stawka: {} zł</h3>".format(stake)
    table += "<table><tr><th>Kurs</th><th>Prob</th><th>EV</th></tr>"

    for a in analysis:
        table += f"<tr><td>{a['odds']}</td><td>{a['prob']}</td><td class='green'>{a['ev']}</td></tr>"

    table += "</table>"

    return HTML.replace("{content}", table)
