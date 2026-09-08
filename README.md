# ColdLedger Black Box Prototype

This package contains the complete source for the interactive ColdLedger website prototype.

## Run locally

No build step or external dependencies are required for the website itself.

1. Extract the ZIP file.
2. Open `dist/index.html` in a web browser.
3. Use the sidebar to navigate between the prototype screens.

For a local web server, run this command from the extracted folder:

```bash
python3 -m http.server 8000 --directory dist
```

Then open `http://localhost:8000`.

## Included files

- `dist/index.html`: complete interactive website, styling and JavaScript
- `.openai/hosting.json`: deployment configuration
- `render_screens.py`: optional utility used to render the prototype screens as images
- `.gitignore`: repository exclusions

The website uses fictional demonstration data for shipment CL-2409-018.
