# Complex Wallet Microservice
import stripe 

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

topUpWalletURL = "http://localhost:5004/topup"

def checkWallet():
    # if wallet enough $$, make the transaction by calling UpdateWallet function and notify user of sucess

    
    if __:
        return jsonify (
            {
                "code": 200,
                "data":
                {
                    "status": ""
                }
                "message": "Sucessful Transaction!"
            }
        )

    # else, reject the transaction and notify user
    return jsonify(
        {
            "code": 404,
            "message": "Unsucessful Transaction!"
        }
    )
    

def topUpWallet():
    invoke
