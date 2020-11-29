importScripts("https://www.gstatic.com/firebasejs/7.11.0/firebase-app.js");
importScripts(
  "https://www.gstatic.com/firebasejs/7.11.0/firebase-messaging.js"
);

const config = {
  apiKey: "AIzaSyAv-Owl1J3LpQ0xi8oKwk3RgX_97IQarJI",
  authDomain: "mammoth-dev.firebaseapp.com",
  databaseURL: "https://mammoth-dev.firebaseio.com",
  projectId: "mammoth-dev",
  storageBucket: "mammoth-dev.appspot.com",
  messagingSenderId: "948031423183",
  appId: "1:948031423183:web:f426dec7e2613d516b2dba",
};
firebase.initializeApp(config);

const messaging = firebase.messaging();
