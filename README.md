# airefinery-app

This folder contains a small starter app to connect to the `airefinery-sdk` repository cloned next to it.

Quick setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Install the local SDK in editable mode (from the sibling folder):

```powershell
pip install -e "..\airefinery-sdk"
```

3. Run the starter app:

```powershell
python main.py
```

Notes
- The example `main.py` contains a placeholder import and connection snippet. Adjust imports and client code to match the SDK package and API once verified.
- If the SDK is published on PyPI, you can instead `pip install airefinery-sdk` (replace with actual package name if different).
