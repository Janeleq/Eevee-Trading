# Complex Wallet Microservice



def checkWallet():
    # if wallet enough $$, make the transaction by calling UpdateWallet function and notify user of sucess

    
    if __:
        return jsonify (
            {
                "code": 200,
                "data":
                {
                    "status": "suce"
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
    

def UpdateWallet():
