from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def retrieve_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC%2CETH%2CSOL&convert=USD&CMC_PRO_API_KEY=4f0a6417-58ab-41f1-8770-6cf42db5d653"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()["data"]
        result = {}
        for currency in data:
            result[currency] = {"price": data[currency]["quote"]["USD"]["price"]}
        return result
    else:
        raise Exception("Error in retrieving data")

@app.route('/')
def home():
    crypto_data = retrieve_data()
    return jsonify(crypto_data)

if __name__ == '__main__':
    app.run()
