# PixBridge Examples

PixBridge is a Camera-to-API client. It sends a captured mobile image to your server API, receives JSON, and displays selected response values in the app.

This repository is a public example pack. It contains:

- `fastapi/`: a demo API server
- `templates/`: importable preset templates
- `responses/`: sample JSON responses
- `docs/`: short setup notes

This repository does not contain the PixBridge mobile app source code.

Start with [docs/quick-start.md](docs/quick-start.md).

The files in `templates/` can be imported as PixBridge response setting presets. The files in `responses/` are sample server responses only.

## Run the FastAPI Demo Server

```bash
cd fastapi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

The demo API accepts multipart image uploads with the image field name `image`.

Use this demo Authorization header:

```text
Authorization: Bearer demo-token
```

## Demo Endpoints

- `GET /`
- `GET /health`
- `POST /check-image`
- `POST /check-parking`
- `POST /ocr-demo`
- `POST /classify-image`

All POST endpoints return demo JSON responses only. Uploaded images are validated and read for size checks, but they are never stored.
