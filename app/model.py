def calculate_value(odd_a, odd_b):
    return (odd_a / odd_b) - 1


def find_value_bets(book_a, book_b):
    results = []

    for i in range(min(len(book_a), len(book_b))):
        a = book_a[i]
        b = book_b[i]

        value = calculate_value(a, b)

        if value > 0.03:
            results.append({
                "book_a": a,
                "book_b": b,
                "value": round(value, 3)
            })

    return results
