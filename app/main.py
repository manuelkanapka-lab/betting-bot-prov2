from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from app.parser import parse_all
from app.model import find_value_from_manual

app = FastAPI()

HTML = """
<html>
<head>
<title>Betting Bot PRO</title>
<style>
body { background:#0f172a; color:white; font-family:Arial; text-align:center; }
textarea { width:28%; height:200px; margin:5px; }
.container { display:flex; justify-content:center; }
table { margin:auto; border-collapse: collapse; }
td, th { padding:10px; border:1px solid #333; }
.green { color:#00ff88; }
button { padding:10px 20px; margin:20px; }
</style>
</head>

<body>

<h1>📊 VALUE BET SCANNER</h1>

<form method="post">
<div class="container">
<textarea name="superbet" placeholder="Superbet"></textarea>
<textarea name="sts" placeholder="STS"></textarea>
<textarea name="fortuna" placeholder="Fortuna"></textarea>
</div>

<button type="submit">Analizuj</button>
</form>

{content}

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML.replace("{content}", "")


@app.post("/", response_class=HTMLResponse)
def analyze(
    superbet: str = Form(""),
    sts: str = Form(""),
    fortuna: str = Form("")
):
    data = parse_all(superbet, sts, fortuna)
    results = find_value_from_manual(data)

    if not results:
        content = "<p>Brak value betów</p>"
    else:
        content = "<table><tr><th>Mecz</th><th>Typ</th><th>Kurs</th><th>Buk</th><th>Value</th></tr>"

        for r in results:
            content += f"<tr><td>{r['match']}</td><td>{r['type']}</td><td>{r['odd']}</td><td>{r['book']}</td><td class='green'>{r['value']}</td></tr>"

        content += "</table>"

    return HTML.replace("{content}", content)
