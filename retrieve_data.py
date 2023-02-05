from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def retrieve_data(convert):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC%2CETH%2CSOL&convert={convert}&CMC_PRO_API_KEY=4f0a6417-58ab-41f1-8770-6cf42db5d653"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()["data"]
        result = {}
        for currency in data:
            result[currency] = {"price": data[currency]["quote"][convert]["price"]}
        return result
    else:
        raise Exception("Error in retrieving data")

@app.route('/')
def home():
    convert = request.args.get("convert", "USD")
    crypto_data = retrieve_data(convert)
    return jsonify(crypto_data)

if __name__ == '__main__':
    app.run()
