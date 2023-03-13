import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, set, ref, update } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
import { getAuth, createUserWithEmailAndPassword, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-auth.js";

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
                window.location.href = "Login+Register Page/Login.html";
            }, 1000);
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;

            alert(errorMessage);
        });

});
