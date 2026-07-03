from typing import Any

from fastapi import FastAPI, File, Header, HTTPException, UploadFile, status


app = FastAPI(title="PixBridge Demo API")

DEMO_TOKEN = "demo-token"
MAX_UPLOAD_SIZE_BYTES = 5 * 1024 * 1024


def verify_bearer_token(authorization: str | None) -> None:
    expected = f"Bearer {DEMO_TOKEN}"
    if authorization != expected:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing Bearer token",
        )


async def validate_image_upload(image: UploadFile) -> int:
    allowed_content_types = {"application/octet-stream"}
    if (
        image.content_type
        and not image.content_type.startswith("image/")
        and image.content_type not in allowed_content_types
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file must be an image or binary file",
        )

    size = 0
    while True:
        chunk = await image.read(1024 * 1024)
        if not chunk:
            break
        size += len(chunk)
        if size > MAX_UPLOAD_SIZE_BYTES:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail="Uploaded image is too large",
            )

    if size == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded image is empty",
        )

    return size


async def require_demo_upload(
    image: UploadFile,
    authorization: str | None,
) -> int:
    verify_bearer_token(authorization)
    return await validate_image_upload(image)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "name": "PixBridge Demo API",
        "message": "Send a multipart image field named image to a demo POST endpoint.",
    }


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/check-image")
async def check_image(
    image: UploadFile = File(...),
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    image_size_bytes = await require_demo_upload(image, authorization)
    return {
        "received": True,
        "filename": image.filename or "demo-image.jpg",
        "content_type": image.content_type,
        "image_size_bytes": image_size_bytes,
        "message": "Demo image received.",
    }


@app.post("/check-parking")
async def check_parking(
    image: UploadFile = File(...),
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    await require_demo_upload(image, authorization)
    return {
        "vehicle": {
            "plate": "DEMO-1234",
            "registered": True,
            "type": "demo-car",
        },
        "confidence": 0.98,
        "message": "Demo vehicle is registered.",
    }


@app.post("/ocr-demo")
async def ocr_demo(
    image: UploadFile = File(...),
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    await require_demo_upload(image, authorization)
    return {
        "text": "DEMO TEXT",
        "confidence": 0.96,
        "language": "en",
        "blocks": 2,
    }


@app.post("/classify-image")
async def classify_image(
    image: UploadFile = File(...),
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    image_size_bytes = await require_demo_upload(image, authorization)
    return {
        "label": "demo-object",
        "category": "demo-category",
        "confidence": 0.94,
        "image_size_bytes": image_size_bytes,
    }
