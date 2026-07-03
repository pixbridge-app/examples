# Bearer Token

The FastAPI demo server expects this Authorization header for POST endpoints:

```text
Authorization: Bearer demo-token
```

In PixBridge, store only the token value:

```text
demo-token
```

PixBridge should add the `Bearer` prefix when it sends the request.

Do not commit real production tokens to this repository. Use placeholder values in public examples.
