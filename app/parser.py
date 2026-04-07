from playwright.sync_api import sync_playwright

def get_odds():
    odds = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://www.superbet.pl", timeout=60000)
            page.wait_for_timeout(5000)

            elements = page.query_selector_all("span")

            for el in elements[:30]:
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
        return [1.5, 2.0, 2.5]
