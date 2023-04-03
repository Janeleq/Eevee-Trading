import time
import pyrebase
import os, sys
from os import environ
import helpers
import requests
import threading
import pika
import json

firebase_config = {
    "apiKey": "AIzaSyAUfijsgUQsPpdx5A21wO0wCS1qRkwh5o0",
    "authDomain": "cryptobuds-ba428.firebaseapp.com",
    "databaseURL": "https://cryptobuds-ba428-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "cryptobuds-ba428",
    "storageBucket": "cryptobuds-ba428.appspot.com",
    "messagingSenderId": "72206190161",
    "appId": "1:72206190161:web:bc8dbb3bf116fcc69fda70",
    "measurementId": "G-BVXDMYJR2K"
}
fb = pyrebase.initialize_app(firebase_config)
database = fb.database()




def checkOrderStatus():
    threading.Timer(1.0, checkOrderStatus).start()
    id = helpers.retrieveHelperVal('uID','helpers.txt')
    orderlist = database.child('users').child(id).child('orders').get()
    print(orderlist)

checkOrderStatus()
