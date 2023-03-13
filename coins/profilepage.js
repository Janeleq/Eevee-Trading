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
  console.log(data[uid])
  var user = data[uid]
  var dateRegistered = user.DateRegistered
  var start = dateRegistered.indexOf('GMT')
  var dateRegistered = dateRegistered.substring(0, start)
  console.log(dateRegistered)
  var ada = user.Ada
  var bc = user.Bc
  var bnb = user.Bnb
  var btc = user.Btc
  var doge = user.Doge
  var eth = user.Eth
  var sol = user.Sol
  var email = user.Email

  document.getElementById('email').innerHTML = 'Email: ' + email
  document.getElementById('registered').innerHTML = 'Last Registered: ' + dateRegistered
  document.getElementById('ADAquantity').innerHTML = ada
  document.getElementById('BNBquantity').innerHTML = bnb
  document.getElementById('BTCquantity').innerHTML = btc
  document.getElementById('DOGEquantity').innerHTML = doge
  document.getElementById('ETHquantity').innerHTML = eth
  document.getElementById('SOLquantity').innerHTML = sol
  document.getElementById('BCquantity').innerHTML = bc
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
        window.location.href = "../Login+Register Page/Login.html";
    }, 1000);
    }).catch((error) => {
      // An error happened.
    });
  
  });
}
setTimeout(() => {
  addResetListener()
}, 1000);

function addResetListener(){
  reset.addEventListener('click',(g)=> {
  onAuthStateChanged(auth, (user) => {
    if (user) {
      const uid = user.uid;
      update(ref(db, 'All users in database/' + user.uid), {
        Eth: 0,
        Bc: 5000,
        Ada: 0,
        Bnb: 0,
        Btc:0,
        Doge:0,
        Sol:0,

      })
      alert('Successfully Reset!')
    } 
  });
})
}
