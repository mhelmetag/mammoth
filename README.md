# Mammoth

Lift statuses and notifications for Mammoth Mountain

## More Info

This app shows you the lift statuses for Mammoth Mountain in a mobile-friendly layout. Clients can also subscribe to lift status updates every 10 minutes via Push Notification (supported on iOS and Android). Notifications are supplied via Firebase Cloud Messaging.

All times are in PDT or PST.

`SEASON` ENV key can be summer or winter. That will change whether the updated or seeded lift info is for that specific season.

Remember to load env variables (through something like `source development.sh`) or set them before starting the server.

You'll also probably have to change the firebase config in the static firebase messaging and messaging service worker files (`app/static/firebase*`).

## Dev Setup

### Simple Local

```sh
pipenv shell
pipenv sync
source development.sh
uvicorn web:app
```

### Fake Mammoth API (For Testing Notifications)

```sh
# with standard web:app running in a different window/process
uvicorn fake:app
# in another window/process
python app/jobs/updated_lift_statuses.py
```

## API

### Lifts

The lifts and their statuses.

### Spots Endpoint

`GET /api/lifts?season=Winter`

```json
{
  "lifts": [
    {
      "id": 1,
      "name": "Broadway Express 1",
      "status": "Closed",
      "kind": "Quad",
      "last_updated": "2020-03-15T13:05:00+00:00"
    }
  ]
}
```

## Credits

Icons made by [Freepik](https://www.flaticon.com/authors/freepik) from [Flaticon](https://www.flaticon.com).
