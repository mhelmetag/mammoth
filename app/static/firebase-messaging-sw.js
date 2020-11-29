importScripts("https://www.gstatic.com/firebasejs/7.11.0/firebase-app.js");
importScripts(
  "https://www.gstatic.com/firebasejs/7.11.0/firebase-messaging.js"
);

const config = {
  apiKey: "AIzaSyBA12McSozqdsahbJaVwy8cC0zotHPNFog",
  authDomain: "mammoth-ad2e7.firebaseapp.com",
  databaseURL: "https://mammoth-ad2e7.firebaseio.com",
  projectId: "mammoth-ad2e7",
  storageBucket: "mammoth-ad2e7.appspot.com",
  messagingSenderId: "742699308187",
  appId: "1:742699308187:web:9880d5d8fa92bfe6a6a23e",
};
firebase.initializeApp(config);

const messaging = firebase.messaging();
