def calculate_ev(odds, probability):
    return (odds * probability) - 1


def find_value_bets(odds_list):
    results = []

    for odds in odds_list:
        prob = 1 / odds
        boosted_prob = prob * 1.15  # poprawiony model
        ev = calculate_ev(odds, boosted_prob)

        if ev > 0:
            results.append({
                "odds": odds,
                "prob": round(boosted_prob, 2),
                "ev": round(ev, 3)
            })

    return results
