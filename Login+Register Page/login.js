import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, ref, update, } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
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

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);
const auth = getAuth();

signIn.addEventListener('click', (d) => {
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;
  var LoginStatus = "Logged in"

  signInWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      // Signed in 
      const user = userCredential.user;

      var dt = Date();
      update(ref(database, 'Users in the system/' + user.uid), {
        LoginTime: dt,
        LoginStatus: LoginStatus,
        email: email
      })
      setTimeout(() => {
        window.location.href = "../homepageWithLogin/homepageWithLogin.html";
      }, 1000);
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;

      alert(errorMessage);
    });

});


