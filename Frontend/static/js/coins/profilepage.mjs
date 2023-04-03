import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, ref, update, onValue } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut, setPersistence, browserSessionPersistence } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-auth.js";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAUfijsgUQsPpdx5A21wO0wCS1qRkwh5o0",
  authDomain: "cryptobuds-ba428.firebaseapp.com",
  databaseURL: "https://cryptobuds-ba428-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "cryptobuds-ba428",
  storageBucket: "cryptobuds-ba428.appspot.com",
  messagingSenderId: "72206190161",
  appId: "1:72206190161:web:bc8dbb3bf116fcc69fda70",
  measurementId: "G-BVXDMYJR2K"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
const coinRef = ref(db, 'users');
const auth = getAuth();
onAuthStateChanged(auth, (user) => {
  if (user) {
    const uid = user.uid;
    onValue(coinRef, (snapshot) => {
      const data = snapshot.val();
      getValues(data, uid)
    });
  }
});

function getValues(data, uid) {
  wallet_coins = data[uid].wallet_coins
  var username = data[uid].username
  var datecreated = data[uid].date_created
  var wallet_coins = data[uid].wallet_coins

  var ada = wallet_coins.ADA
  var usd = wallet_coins.USD
  var bnb = wallet_coins.BNB
  var btc = wallet_coins.BTC
  var doge = wallet_coins.DOGE
  var eth = wallet_coins.ETH
  var sol = wallet_coins.SOL

  document.getElementById('email').innerHTML = username
  document.getElementById('registered').innerHTML = datecreated
  document.getElementById('ADAquantity').innerHTML = ada.qty
  document.getElementById('BNBquantity').innerHTML = bnb.qty
  document.getElementById('BTCquantity').innerHTML = btc.qty
  document.getElementById('DOGEquantity').innerHTML = doge.qty
  document.getElementById('ETHquantity').innerHTML = eth.qty
  document.getElementById('SOLquantity').innerHTML = sol.qty
  document.getElementById('USDquantity').innerHTML = usd.qty
}

setTimeout(() => {
  addListener()
}, 1000);

function addListener(){
  logout.addEventListener('click', (f) => {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        update(ref(db, 'Users in the system/' + user.uid), {
          LoginStatus: "Logged Off",
          LoginTime: "NIL"
        })
      } 
    });
  
    signOut(auth).then(() => {
      // Sign-out successful.
      setTimeout(() => {
        alert("Signed out!")
        window.location.href = "../login";
    }, 1000);
    }).catch((error) => {
      // An error happened.
    });
  
  });
}



