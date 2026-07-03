# Quick Start

## Run the Demo Server

```bash
cd fastapi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Find Your Local IP Address on macOS

Use one of these commands:

```bash
ipconfig getifaddr en0
```

or:

```bash
ifconfig | grep "inet "
```

Use the local network IP address for your computer, such as `192.168.1.25`.

## Configure PixBridge

Use your computer's local network IP address instead of `localhost` when connecting from a phone.

Import one of the files in `templates/` as a PixBridge response setting preset. The files in `responses/` are sample server responses and are not preset import files.

In PixBridge, create or edit a server address with these values:

| Setting | Value |
| --- | --- |
| Method | `POST` |
| Encoding | `multipart/form-data` |
| Image field name | `image` |
| Bearer token value | `demo-token` |

Replace `YOUR_LOCAL_IP` with your computer's local network IP address.

Example parking demo URL:

```text
http://YOUR_LOCAL_IP:8000/check-parking
```

Example OCR demo URL:

```text
http://YOUR_LOCAL_IP:8000/ocr-demo
```

Example classification demo URL:

```text
http://YOUR_LOCAL_IP:8000/classify-image
```

The template response preset fields can be used to map displayed JSON values.

## Authorization

Use this Bearer token value in PixBridge:

```text
demo-token
```

PixBridge should send it as:

```text
Authorization: Bearer demo-token
```

## Multipart Image Field

Set the multipart image field name to:

```text
image
```

## Example Response Keys

Useful demo keys to map include:

- `vehicle.plate`
- `vehicle.registered`
- `confidence`
- `message`
- `text`
- `language`
- `label`
- `image_size_bytes`
