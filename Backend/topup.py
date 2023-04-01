from flask import redirect, request, url_for, render_template, Flask, jsonify
import stripe

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')

app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51Mqv3mL81p6Fg6ebcfrJYprowuiyEYky8iILawOUGwdd7WEjxkQk6hJRfSXm02XdbgzBU0qGmhJxoA737LI0mDcm004m87jVGX'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51Mqv3mL81p6Fg6ebxNqIERpNmaW1FIyE0Ps6EH6A3UHKI9pMVIlUR6ExCmOwlrrBXArZPTLu0GnF8wOppX16g2qq00hB17R6OX'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route("/processtopup", methods = ['GET', 'POST'])
def topUpWallet():
    
    status = '\n --- Bringing you to top-up page ---'
    try: 
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                    'price': 'price_1MqvPOL81p6Fg6ebILbmwrSq',
                    'quantity': 1,
                }],
            mode='payment',
            success_url=url_for('processTopUp', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('profile', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        )
    except Exception as e:
        return str(e)
    # render_template( 
    #         'coins/profilepage.html',
    #         checkout_session_id=session['id'],
    #         checkout_public_key=['STRIPE_PUBLIC_KEY']
    #         )

    return redirect(session.url, code=303)
    # return redirect("https://buy.stripe.com/test_00g5nJ2nW3GC1zO288")
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

@app.route('/thanks')
def processTopUp():
    session_id = request.args.get("session_id")
    print(session_id)
    line_items = stripe.checkout.Session.list_line_items(session_id)
    top_up_amt = line_items['data'][0].amount_total/100
    # top_up_amt is preset to 1 and stripe ensure no -ve numbers can be entered, so there wont be any human errors
    if top_up_amt != 0:
        status = jsonify (
            {
                'code': 200
            }
            
        )
        print('Top Up Amount: ', top_up_amt)
        return render_template('thanks.html', status = status, top_up_amt = top_up_amt)
    else:
        status = 'Error! Try topping up again!'
        profile_page_URL = "http://localhost:5000/profile"
        return redirect(profile_page_URL)


@app.route("/profile")
def profile():
    profile_page_URL = "http://localhost:5000/profile"
    return redirect(profile_page_URL)

if __name__ == '__main__':
    app.run(port=5005, debug=True)