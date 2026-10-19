# Python BDD Automation Framework

A starter UI automation framework using Python, Behave (Cucumber-style BDD), and Playwright.

## Setup (Windows PowerShell)

Extract the ZIP, open PowerShell in the extracted project folder, then run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

If activation is blocked by PowerShell policy, run `python -m pip install -r requirements.txt` without activating the environment.

## Run tests

```powershell
# All 10 scenarios
python -m behave

# Smoke tests
python -m behave --tags=@smoke

# One feature file
python -m behave features/01_login_success.feature

# One specific scenario
python -m behave --tags=@login_success

# Cart tests
python -m behave --tags=@cart

# Checkout tests
python -m behave --tags=@checkout

# Negative tests
python -m behave --tags=@negative

# JSON report
New-Item -ItemType Directory -Force reports
python -m behave -f pretty -f json -o reports/behave-report.json
```

## Browser settings

Visible Chromium and 400 ms slow motion are enabled by default. To run headless:

```powershell
$env:HEADLESS="1"
python -m behave --tags=@smoke
```

Change the speed with `SLOW_MO` (milliseconds):

```powershell
$env:SLOW_MO="800"
python -m behave --tags=@login_success
```

Screenshots are saved under `screenshots/` after each scenario.

## Demo site

The sample tests use https://www.saucedemo.com/ and its public demo credentials:
- `standard_user` / `secret_sauce`
- `locked_out_user` / `secret_sauce`

These are demo tests, not production tests. An internet connection is required, and website changes can require locator updates.
