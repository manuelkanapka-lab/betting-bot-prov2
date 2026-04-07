from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.parser import get_all_odds
from app.model import find_value_bets
from app.bankroll import calculate_stake

app = FastAPI()

HTML = """
<html>
<head>
<meta http-equiv="refresh" content="30">
<title>FINAL BOT</title>

<style>
body { background:#0f172a; color:white; text-align:center; font-family:Arial; }
table { margin:auto; border-collapse: collapse; }
td, th { padding:10px; border:1px solid #333; }
.green { color:#00ff88; }
</style>
</head>

<body>

<h1>🚀 FINAL VALUE BET BOT</h1>

{content}

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    data = get_all_odds()
    bets = find_value_bets(data)
    stake = calculate_stake(100)

    if not bets:
        content = "<p>Brak okazji</p>"
    else:
        content = f"<h3>Stawka: {stake} zł</h3>"
        content += "<table><tr><th>Bukmacher</th><th>Kurs</th><th>Value</th></tr>"

        for b in bets:
            content += f"<tr><td>{b['best_book']}</td><td>{b['odd']}</td><td class='green'>{b['value']}</td></tr>"

        content += "</table>"

    return HTML.replace("{content}", content)
