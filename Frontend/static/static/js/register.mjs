import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, set, ref, update } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
import { getAuth, createUserWithEmailAndPassword, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-auth.js";

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


// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);
const auth = getAuth();

signUp.addEventListener('click', (e) => {

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var bc = 5000;
    var eth = 0;
    var btc = 0;
    var bnb = 0;
    var doge = 0;
    var sol = 0;
    var ada = 0;
    var dt = Date();

    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 

            const user = userCredential.user;
            set(ref(database, 'All users in database/' + user.uid), {
                Email: email,
                Bc: bc,
                DateRegistered: dt,
                Eth: eth,
                Btc: btc,
                Bnb: bnb,
                Doge: doge,
                Sol: sol,
                Ada: ada,
            })


            setTimeout(() => {
                alert('user created!');
                window.location.href = "/login";
            }, 1000);
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;

            alert(errorMessage);
        });

});
