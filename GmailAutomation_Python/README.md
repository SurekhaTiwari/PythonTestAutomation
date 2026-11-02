# Gmail Automation - Python, Selenium and Pytest

This project automates the following flow:

1. Open the Gmail landing page.
2. Click **Sign in**.
3. Switch to the newly opened browser tab.
4. Wait for the **Email or phone** field.
5. Assert that the field is visible.

## Prerequisites

- Python 3.9 or later
- Visual Studio Code
- Google Chrome
- VS Code Python extension

Selenium 4.27 uses Selenium Manager to obtain a compatible ChromeDriver automatically in most standard setups. An internet connection may be required the first time it runs.

## 1. Open the project in VS Code

Extract the ZIP file, then in VS Code choose **File → Open Folder** and select the `GmailAutomation_Python` folder.

## 2. Create and activate a virtual environment

Open **Terminal → New Terminal** in VS Code.

### macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows (PowerShell)

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:

```bat
venv\Scripts\activate.bat
```

## 3. Install the dependencies

With the virtual environment activated, run:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 4. Select the Python interpreter in VS Code

1. Press `Cmd+Shift+P` on macOS or `Ctrl+Shift+P` on Windows.
2. Search for **Python: Select Interpreter**.
3. Select the interpreter inside this project's `venv` folder.

## 5. Run the test

In the VS Code terminal, from the project root, run:

```bash
python -m pytest
```

To run only this test:

```bash
python -m pytest tests/test_gmail_signin.py
```

A successful run should report **1 passed**. Chrome will open, perform the steps, and close after the test finishes.

## Project structure

```text
GmailAutomation_Python/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── tests/
    └── test_gmail_signin.py
```

## Notes

- The test checks visibility only; it does not enter an email address or sign in.
- The test uses explicit waits so it can handle normal page-loading delays.
- Google may change its page layout or sign-in flow. If that happens, the locator or expected window count may need updating.
- If Chrome does not start, confirm Chrome is installed and that the computer can access the internet so Selenium Manager can resolve the driver.
