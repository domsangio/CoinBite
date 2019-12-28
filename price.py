def get_cb_fee(price):
    if price < 10.99:
        return .99
    elif price < 26.49:
        return 1.49
    elif price < 51.99:
        return 1.99
    elif price < 78.05:
        return 2.99
    else:
        return 3.99 # Unsure of overflow  
        # Some shit with spillage and stuff, buy less than this  

class Order:
    def __init__(self, buy_price):
        self.buy_price = buy_price
        self.fees = get_cb_fee(buy_price)
    
    def get_current_profit(self):
        # curr_price = get durrent price
        fee = get_cb_fee(curr_price)
        return curr_price - fee - self.fees - self.buy_price
    




