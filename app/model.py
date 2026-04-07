def calculate_ev(odds, probability):
    return (odds * probability) - 1


def find_value_bets(odds_list):
    results = []

    for odds in odds_list:
        prob = 1 / odds
        ev = calculate_ev(odds, prob * 1.1)  # sztuczne +10%

        results.append({
            "odds": odds,
            "prob": round(prob, 2),
            "ev": round(ev, 3)
        })

    return results
