import random

def get_odds_superbet():
    return [round(random.uniform(1.5, 3.0), 2) for _ in range(10)]

def get_odds_sts():
    return [round(random.uniform(1.5, 3.0), 2) for _ in range(10)]
