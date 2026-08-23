import requests

def get_crypto_price(coin="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        price = response.json()[coin]['usd']
        return f"The current price of {coin.capitalize()} is ${price} USD."
    return "Error fetching data."

if __name__ == "__main__":
    print(get_crypto_price("bitcoin"))
