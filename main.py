import time
from moduls.models.CoinbasePro import PublicAPI as CBPublicAPI
from flask import Flask, render_template
from devtools import debug

flask_app = Flask(__name__)


@flask_app.route('/')
def index():
    localtime = time.asctime(time.localtime(time.time()))
    print(f"navštívené: / a objednávky skontrolované v čase: {localtime}")
    api = CBPublicAPI()
    price = api.getTicker("BTC-EUR")
    return render_template('home.html', price=price, localtime=localtime)


@flask_app.route('/history')
def history():
    localtime = time.asctime(time.localtime(time.time()))
    print(
        f"navštívené: /history a objednávky skontrolované v čase: {localtime}")
    api = CBPublicAPI()
    history1 = api.getHistoricalData("BTC-EUR", 60)
    history = history1[::-1].to_numpy()
    # print(history)
    price = api.getTicker("BTC-EUR")

    return render_template('history.html', price=price, localtime=localtime, history=history)


if __name__ == '__main__':
    flask_app.run(debug=True)
