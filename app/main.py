from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.parser import get_odds
from app.model import find_value_bets
from app.bankroll import calculate_stake

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    odds = get_odds()
    analysis = find_value_bets(odds)
    stake = calculate_stake(100)

    html = """
    <h1>🔥 Betting Bot PRO</h1>
    <h3>Rekomendowana stawka: {} zł</h3>
    <table border="1" cellpadding="10">
    <tr><th>Kurs</th><th>Prawdopodobieństwo</th><th>EV</th></tr>
    """.format(stake)

    for a in analysis:
        color = "green" if a["ev"] > 0 else "red"
        html += f"<tr><td>{a['odds']}</td><td>{a['prob']}</td><td style='color:{color}'>{a['ev']}</td></tr>"

    html += "</table>"

    return html
