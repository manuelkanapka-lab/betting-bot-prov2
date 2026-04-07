def find_value_from_manual(data):
    if len(data) < 2:
        return []

    match = data[0]["match"]

    best = {"1": 0, "X": 0, "2": 0}
    source = {"1": "", "X": "", "2": ""}

    for b in data:
        for k in ["1", "X", "2"]:
            if b[k] > best[k]:
                best[k] = b[k]
                source[k] = b["bookmaker"]

    results = []

    for k in ["1", "X", "2"]:
        avg = sum(b[k] for b in data) / len(data)
        value = (best[k] / avg) - 1

        if value > 0.03:
            results.append({
                "match": match,
                "type": k,
                "odd": best[k],
                "book": source[k],
                "value": round(value, 3)
            })

    return results
