def calculate_stake(bankroll, percent=0.2, max_bets=5):
    total = bankroll * percent
    per_bet = total / max_bets
    return round(per_bet, 2) 
