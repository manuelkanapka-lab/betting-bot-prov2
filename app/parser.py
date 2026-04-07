import re

def extract_odds(text):
    # znajdź wszystkie liczby typu 1.50, 2.75 itd
    return [float(x) for x in re.findall(r"\d+\.\d+", text)]


def extract_teams(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    teams = []
    for line in lines:
        if len(line.split()) >= 1 and not re.search(r"\d", line):
            teams.append(line)

    # bierz pierwsze 2 sensowne linie jako mecz
    if len(teams) >= 2:
        return f"{teams[0]} vs {teams[1]}"
    return "Unknown match"


def parse_bookmaker(text, name):
    odds = extract_odds(text)
    match = extract_teams(text)

    if len(odds) >= 3:
        return {
            "bookmaker": name,
            "match": match,
            "1": odds[0],
            "X": odds[1],
            "2": odds[2]
        }

    return None


def parse_all(superbet, sts, fortuna):
    data = []

    sb = parse_bookmaker(superbet, "Superbet")
    st = parse_bookmaker(sts, "STS")
    fo = parse_bookmaker(fortuna, "Fortuna")

    for x in [sb, st, fo]:
        if x:
            data.append(x)

    return data
