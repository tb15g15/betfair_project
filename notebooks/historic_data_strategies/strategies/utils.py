def lay_hedge_max_lp(bp, c):
	return (bp - 1) * (1 - c) ** 2 + 1

def back_hedge_min_bp(lp, c):
	return (c ** 2 - 2 * c + lp) / (1 - c) ** 2