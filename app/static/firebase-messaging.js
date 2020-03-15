const config = {
  apiKey: "AIzaSyBA12McSozqdsahbJaVwy8cC0zotHPNFog",
  projectId: "mammoth-ad2e7",
  messagingSenderId: "742699308187",
  appId: "1:742699308187:web:9880d5d8fa92bfe6a6a23e"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();
messaging
  .requestPermission()
  .then(() => {
    console.log("Permission granted");
    return messaging.getToken();
  })
  .then(token => {
    console.log(token);
    fetch("/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subscriber_id: token })
    })
      .then(resp => resp.json())
      .then(json => console.log(json));
  })
  .catch(err => {
    console.log("Permission denied");
    console.log(err);
  });
