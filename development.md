# Development Notes

## Uptime

### What is uptime?

`uptime` should be defined as `(time_normally_open - time_closed) / time_normally_open`.

`time_normally_open` should be defined as the collective time that a lift should be open on a given day. If it's 0, we shouldn't try calculating the `uptime` (some lifts are closed on certain days).

`time_closed` should be defined as the collective time in a state other than 'Open' or 'For Scenic Rides Only' (every other state should be considered closed).

Time could be in minutes for ease of comparison

### Example

In the summer, the Discovery Chair lift should be open from 9AM - 5PM PST daily. That means the `time_normally_open` should be 480 minutes (8 hours).

Let's say that today the Discovery Chair was in the state 'Hold - Weather' from 1PM - 2PM PST. It's `time_closed` was 60 minutes (1 hour). We can then calculate it's `uptime` for the day as `(480 - 60) / 480` or `87.5%`.

### How to

Lift `uptime` should be stored on the `lifts` and updated on a weekly basis from the previous week's `latest_updates`.

For each lift, 