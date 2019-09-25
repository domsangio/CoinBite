# This will be the main class to pull the data from CoinBase. This might not be the 
# best way to get the information, but CoinBase is the current App that i use to
# buy/sell crypto already

from coinbase.wallet.client import Client

api_key_file = open(".coinbase_key", "r")
api_secret_file = open(".coinbase_secret", "r")

api_key = api_key_file.readline()
api_secret = api_secret_file.readline()

api_key_file.close()
api_secret_file.close()

client = Client(api_key, api_secret)

def getCryptoBuyPrice(coin, currency):
    response = client.get_buy_price(currency_pair = "" + coin + "-" + currency)
    return response['amount']

def getCryptoSellPrice(coin, currency):
    response = client.get_sell_price(currency_pair = "" + coin + "-" + currency)
    return response['amount']

def getCryptoSpotPrice(coin, currency):
    response = client.get_spot_price(currency_pair = "" + coin + "-" + currency)
    return response['amount']

def getTime():
    return client.get_time()

print(getCryptoBuyPrice("BTC", "USD"))
print(getCryptoSellPrice("BTC", "USD"))
print(getCryptoSpotPrice("BTC", "USD"))
print(getTime())
