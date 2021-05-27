# Meeting Alert 

Webhooks for letting the office know when you are in a meeting or on a call. 

Will be a single slash command: 

```
/inmeeting
```

used to control a light wired up to a raspberry pi. 

Middleware loaded to pi use to communicate with Slack vis websocket.  


Start systemd service with: 

- Copy the service file via: `sudo cp busylight.service /etc/systemd/system/busylight.service`.
- Start the service sudo systemctl start busylight (to see if it is correctly copied and can start). If you want, you can use `sudo systemctl status busylight` to verify the status of the service.
- Enable the service: `sudo systemctl enable busylight`.


