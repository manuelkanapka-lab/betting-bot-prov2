import requests
from bs4 import BeautifulSoup

def get_odds():
    url = "https://www.superbet.pl"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        odds = []
        for tag in soup.find_all("span")[:20]:
            text = tag.text.strip()
            if text.replace(".", "").isdigit():
                odds.append(float(text))

        return odds[:10]

    except:
        return [1.5, 2.0, 2.5]  # fallback
