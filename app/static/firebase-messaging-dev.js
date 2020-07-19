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
messaging
  .requestPermission()
  .then(() => {
    return messaging.getToken();
  })
  .then((token) => {
    fetch("/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subscriber_id: token }),
    })
      .then((resp) => resp.json())
      .then((json) => json);
  })
  .catch((err) => err);

messaging.onMessage((message) => createNotification(message));

const createNotification = (message) => {
  const content = document.querySelector("#content");
  const section = content.parentNode;

  let notification = document.createElement("div");
  notification.className = "notification is-primary";
  notification.innerText = message;

  section.insertBefore(notification, content);
};
