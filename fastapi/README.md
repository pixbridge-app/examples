# FastAPI Demo Server

This demo server shows how a PixBridge-compatible backend can accept an image upload and return JSON values that can be mapped in the PixBridge mobile UI.

## Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Test Health

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

## Bearer Token

Use this demo header when calling POST endpoints:

```text
Authorization: Bearer demo-token
```

In PixBridge, store only the token value:

```text
demo-token
```
