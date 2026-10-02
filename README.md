# Selenium Python Demo

This project demonstrates a basic Selenium + pytest browser test.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
pytest -q
```

The test opens Google in Chrome and checks that the page title contains "Google".
