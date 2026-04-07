from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Betting Bot działa ✅</h1>
    <p>W następnym kroku dodamy analizę kursów.</p>
    """
