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
        window.location.href = "../login";
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
