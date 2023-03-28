# Price Microservice to show different CC prices on simulator page
# Activated upon entering simulator -> /simulator
import requests


var coinInfoUrl = 'https://min-api.cryptocompare.com/data/all/coinlist?';



# invoke Crytocompare API to get different pricing according to specific CC
@app.route("/prices")
def get_all_prices():
    booklist = Book.query.all()
    if len(booklist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "prices": [book.json() for book in booklist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no prices available."
        }
    ), 404
