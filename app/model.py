def find_value_bets(data):
    results = []

    sb = data["superbet"]
    sts = data["sts"]
    fort = data["fortuna"]

    for i in range(min(len(sb), len(sts), len(fort))):
        odds = {
            "superbet": sb[i],
            "sts": sts[i],
            "fortuna": fort[i]
        }

        best_book = max(odds, key=odds.get)
        best_odd = odds[best_book]

        avg = sum(odds.values()) / 3
        value = (best_odd / avg) - 1

        if value > 0.03:
            results.append({
                "best_book": best_book,
                "odd": best_odd,
                "value": round(value, 3)
            })

    return results
