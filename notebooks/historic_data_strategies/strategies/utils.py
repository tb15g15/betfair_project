def lay_hedge_threshold(bp, c):
	return (bp - 1) * (1 - c) ** 2 + 1

def back_hedge_threshold(lp, c):
	return (c ** 2 - 2 * c + lp) / (1 - c) ** 2

def lay_hedge_stake(bp, bs, lp, c):
    return (((bp - 1) * bs * (1 - c)) + bs) / (lp)

def win_payout(row):
    "DF transformation"
    if row['stake_2'] == 0:
        val = - row['stake_1']
        
    else:
        back_payout = (row['price_1'] * row['stake_1']) - row['stake_1']
        lay_payout = - ((row['price_2'] -1) * row['stake_2'])
        
        val = (back_payout +lay_payout) * 0.95
        
    return round(val, 2)

def lose_payout(row):
    "DF transformation"
    if row['stake_2'] == 0:
        val = - row['stake_1']
        
    else:
        back_payout = - row['stake_1']
        lay_payout = row['stake_2'] 
        
        val = (back_payout + lay_payout) * 0.95
        
    return round(val, 2)
    