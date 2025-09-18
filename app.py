from flask import Flask, render_template
from web3 import Web3

INFURA_URL = "https://mainnet.infura.io/v3/5355f85ab8064f66a932a2c3be26626d"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/wallet")
def wallet():
    if w3.is_connected():
        network_status = "connected to sopelia"
    else:
        network_status = "not connected"
    return render_template("wallet.html", status=network_status)

if __name__ == "__main__":
    app.run(debug=True)
