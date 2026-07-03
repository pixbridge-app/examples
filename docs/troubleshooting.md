# Troubleshooting

## Phone Cannot Reach the Server

Use your computer's local network IP address instead of `localhost` from a phone.

Example:

```text
http://YOUR_LOCAL_IP:8000/check-parking
```

## Check Wi-Fi

Your phone and computer must be on the same Wi-Fi network.

## Check the Bearer Token

The demo server expects:

```text
Authorization: Bearer demo-token
```

In PixBridge, store only:

```text
demo-token
```

## Check the Multipart Field Name

The uploaded image field name must be:

```text
image
```

## Check Firewall or Network Access

If requests still fail, check your computer firewall settings and make sure port `8000` is reachable on your local network.
