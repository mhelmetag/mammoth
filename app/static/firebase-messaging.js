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

messaging.onMessage((payload) => createNotification(payload));

const createNotification = (payload) => {
  const content = document.querySelector("#content");
  const section = content.parentNode;

  let notification = document.createElement("div");
  notification.className = "notification is-primary";
  const notificationText = payload.notification.body || "Some lifts have updated statuses";
  notification.innerText = `${notificationText}. Refresh the page to see more.`;

  section.insertBefore(notification, content);

  setTimeout(() => { notification.remove() }, 5000);
};
