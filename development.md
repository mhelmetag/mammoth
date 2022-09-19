# Development Notes

## Uptime

### What is uptime?

`uptime` should be defined as `(time_normally_open - time_closed) / time_normally_open`.

`time_normally_open` should be defined as the collective time that a lift should be open on a given day. If it's 0, we shouldn't try calculating the `uptime` (some lifts are closed on certain days).

`time_closed` should be defined as the collective time in a state other than 'Open' or 'For Scenic Rides Only' (every other state should be considered closed).

Time could be in minutes for ease of comparison

### Example

In the summer, the Discovery Chair lift should be open from 9AM - 5PM PDT daily. That means the `time_normally_open` should be 480 minutes (8 hours).

Let's say that today the Discovery Chair was in the state 'Hold - Weather' from 1PM - 2PM PST. It's `time_closed` was 60 minutes (1 hour). We can then calculate it's `uptime` for the day as `round(((480 - 60) / 480) * 100)` or `88`.

### Gathering test data

```sql
select
  id,
  created_at at time zone 'utc' at time zone 'pdt' as created_at,
  updates
from latest_updates;
```

This query has a least a few lifts that were closed for weather on 2021-07-19.

```sql
select row_to_json(lift_data) from (
  select
    created_at at time zone 'utc' at time zone 'pdt' as created_at,
    updates
  from latest_updates
  where created_at
    between '2021-07-19 00:00' and '2021-07-20 00:00'
) lift_data;
```

Then replace `\n` with `,\n` and wrap in `[]` to make it an array.
