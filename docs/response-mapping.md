# Response Mapping

PixBridge maps values from a JSON response by key.

For nested JSON objects, use dot notation.

## Template Sections

- `server`: Values to enter when creating or editing a PixBridge server address.
- `responsePreset`: The app-importable response setting preset data.
- `responseMappings`: A readable summary of which JSON response keys should be displayed, including label, type, and order.
- `responses/*.json`: Sample server responses used to check that the mapping keys exist.

`responseMappings` is documentation-friendly metadata. In the current PixBridge app, preset import uses `responsePreset`.

Example response:

```json
{
  "vehicle": {
    "plate": "DEMO-1234",
    "registered": true
  },
  "confidence": 0.98
}
```

Example keys:

- `vehicle.plate`
- `vehicle.registered`
- `confidence`

Use value types supported by PixBridge templates:

- `string`
- `int`
- `double`
- `boolean`

Some PixBridge versions may support array-style dot notation, such as:

```text
vehicles.0.type
```

Check your PixBridge version before relying on array indexes in mappings.
