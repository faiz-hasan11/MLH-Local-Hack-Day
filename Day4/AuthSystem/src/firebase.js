import firebase from "firebase"
const firebaseApp = firebase.initializeApp({
  apiKey: "AIzaSyDecpB6UXTihyh4CM03G3Rr0IUhIJkljGk",
  authDomain: "authsystem-8df39.firebaseapp.com",
  projectId: "authsystem-8df39",
  storageBucket: "authsystem-8df39.appspot.com",
  messagingSenderId: "828133763755",
  appId: "1:828133763755:web:980a81f1da545043e225ee",
  measurementId: "G-C14DPGHYBM"
});

const auth = firebase.auth()

export { auth }
