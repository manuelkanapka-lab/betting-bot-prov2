from playwright.sync_api import sync_playwright

def scrape_site(url):
    odds = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url, timeout=60000)
            page.wait_for_timeout(5000)

            elements = page.query_selector_all("span")

            for el in elements[:50]:
                text = el.inner_text().strip()
                try:
                    value = float(text)
                    if 1.2 < value < 10:
                        odds.append(value)
                except:
                    pass

            browser.close()

        return odds[:10]

    except:
        return []


def get_all_odds():
    return {
        "superbet": scrape_site("https://www.superbet.pl"),
        "sts": scrape_site("https://www.sts.pl"),
        "fortuna": scrape_site("https://www.efortuna.pl")
    }
