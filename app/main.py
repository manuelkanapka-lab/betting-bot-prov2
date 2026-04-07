from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.parser import get_odds_superbet, get_odds_sts
from app.model import find_value_bets
from app.bankroll import calculate_stake

app = FastAPI()

HTML = """
<html>
<head>
<title>REAL Betting Bot</title>
<style>
body { background:#0f172a; color:white; font-family:Arial; text-align:center; }
table { margin:auto; border-collapse: collapse; }
td, th { padding:10px; border:1px solid #333; }
.green { color:#00ff88; }
button { padding:10px 20px; margin:20px; }
</style>
</head>

<body>
<h1>💰 REAL VALUE BET BOT</h1>

<form method="get">
<button type="submit">Skanuj rynek</button>
</form>

{content}

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    book_a = get_odds_superbet()
    book_b = get_odds_sts()

    value_bets = find_value_bets(book_a, book_b)
    stake = calculate_stake(100)

    if not value_bets:
        content = "<p>Brak value betów</p>"
    else:
        content = f"<h3>Stawka: {stake} zł</h3>"
        content += "<table><tr><th>Superbet</th><th>STS</th><th>Value</th></tr>"

        for bet in value_bets:
            content += f"<tr><td>{bet['book_a']}</td><td>{bet['book_b']}</td><td class='green'>{bet['value']}</td></tr>"

        content += "</table>"

    return HTML.replace("{content}", content)
