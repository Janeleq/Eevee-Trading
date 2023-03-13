import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, ref, update, onValue } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut, setPersistence, browserSessionPersistence } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-auth.js";

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