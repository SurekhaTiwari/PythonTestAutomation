# Web Application Functional Testing — Python + Selenium + Pytest

A small classroom project for VS Code using https://the-internet.herokuapp.com.

## Requirements
- Python 3.10+ and Google Chrome
- VS Code with Microsoft Python extension

## Mac setup
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

## Windows setup (PowerShell)
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v
```

Select the `.venv` Python interpreter in VS Code via Command Palette → Python: Select Interpreter.
Run individual tests from the VS Code Testing sidebar or with `python -m pytest tests/test_login.py -v`.

## Test cases
- `test_valid_login`: valid credentials and secure-page navigation
- `test_invalid_login`: two invalid credential combinations via `pytest.mark.parametrize`
- `test_checkboxes_and_dropdown`: checkbox state and `Select`
- `test_javascript_confirm`: JavaScript confirm dialog and dismiss
- `test_multiple_windows`: open, switch, close, and return
- `test_iframe`: switch into an iframe and read its content

## Selenium topics
Browser lifecycle, ID/CSS/XPath/link-text/tag locators, element methods, explicit waits, dropdowns, alerts, multiple windows, iframes, assertions, POM, pytest fixtures, parametrization, screenshots on test failure.

## Notes
- There are **7 Pytest executions** because invalid login runs twice.
- The site is public and can change. The iframe editor is loaded from an external resource and may be blocked by some networks.
- ChromeDriver is managed by Selenium Manager; internet access may be needed for initial setup.
- Tests have not been executed against the live site in this environment.
