import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, ref, update, onValue } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut, setPersistence, browserSessionPersistence } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-auth.js";


// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBdBlsdTCADW3JrpXohnMBPMa9TgmCnG0M",
  authDomain: "crypto-buddies-a8d5c.firebaseapp.com",
  databaseURL: "https://crypto-buddies-a8d5c-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "crypto-buddies-a8d5c",
  storageBucket: "crypto-buddies-a8d5c.appspot.com",
  messagingSenderId: "1058373755726",
  appId: "1:1058373755726:web:04f25e1ecc36c3213a341f"
};


const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
const coinRef = ref(db, 'All users in database');
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
  document.getElementById('wallet').innerHTML = ' ' + data[uid].Bc
  document.getElementById('qty').innerHTML = ' ' + data[uid].Eth
}

setTimeout(() => {
  addBuyEvent()
}, 1000);

setTimeout(() => {
  addSellEvent()
}, 1000);

function addBuyEvent() {
  buy.addEventListener('click', (d) => {
    var quantityBought = Number(document.getElementById('transactionqty').value)
    var balance = Number(document.getElementById('qty').textContent)
    var price = document.getElementById('price').textContent
    var totalCost = quantityBought * Number(price)
    var tv = Number(document.getElementById('wallet').textContent) - totalCost
    tv = tv.toFixed(2)
    if (tv >= 0) {
      onAuthStateChanged(auth, (user) => {
        if (user) {
          var totaleth = quantityBought + balance
          update(ref(db, 'All users in database/' + user.uid), {
            Eth: totaleth,
            Bc: tv,
          })
          alert('Successfully Bought!')
        }
      });
    }
    else {
      alert("Not enough Bcs")
    }
  })
}


function addSellEvent() {
  sell.addEventListener('click', (e) => {
    var quantitySold = Number(document.getElementById('transactionqty').value)
    var balance = Number(document.getElementById('qty').textContent)
    var price = document.getElementById('price').textContent
    var totalCost = quantitySold * Number(price)
    var tv = Number(document.getElementById('wallet').textContent) + totalCost
    tv = tv.toFixed(2)
    if (balance - quantitySold >= 0) {
      onAuthStateChanged(auth, (user) => {
        if (user) {
          var totaleth = balance - quantitySold
          update(ref(db, 'All users in database/' + user.uid), {
            Eth: totaleth,
            Bc: tv,
          })
          alert("Successfully Sold!")
        }
      });
    }
    else {
      alert("Not enough quantity")
    }
  })
}



setTimeout(() => {
  addListener()
}, 1000);

function addListener(){
  logout.addEventListener('click', (f) => {
    //record before signing off
    onAuthStateChanged(auth, (user) => {
      if (user) {
        const uid = user.uid;
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
        window.location.href = "../Login+Register Page/Login.html";
    }, 1000);
    }).catch((error) => {
      // An error happened.
    });
  
  });
}