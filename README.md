# Mammoth

Lift statuses and notifications for Mammoth Mountain

## More Info

This app shows you the lift statuses for Mammoth Mountain in a mobile-friendly layout. Clients can also subscribe to lift status updates every 10 minutes via Push Notification (supported on iOS and Android). Notifications are supplied via Firebase Cloud Messaging.

All times are in PDT or PST.

## API

### Lifts

The lifts and their statuses.

### Spots Endpoint

`GET /api/lifts`

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
