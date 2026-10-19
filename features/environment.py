import os
import re
from pathlib import Path

from playwright.sync_api import sync_playwright

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"


def _safe_filename(value):
    value = re.sub(r"[^A-Za-z0-9_-]+", "_", value).strip("_")
    return value[:100] or "scenario"


def before_scenario(context, scenario):
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    context.playwright = sync_playwright().start()
    headless = os.getenv("HEADLESS", "0").lower() in {"1", "true", "yes"}
    slow_mo = int(os.getenv("SLOW_MO", "400"))
    context.browser = context.playwright.chromium.launch(
        headless=headless,
        slow_mo=slow_mo,
    )
    context.page = context.browser.new_page(
        viewport={"width": 1365, "height": 900}
    )
    context.page.set_default_timeout(10000)


def after_scenario(context, scenario):
    try:
        page = getattr(context, "page", None)
        if page is not None and not page.is_closed():
            screenshot_path = SCREENSHOT_DIR / f"{_safe_filename(scenario.name)}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"Screenshot saved: {screenshot_path}")
    except Exception as exc:
        print(f"Could not save screenshot: {exc}")
    finally:
        browser = getattr(context, "browser", None)
        playwright = getattr(context, "playwright", None)
        if browser is not None:
            try:
                browser.close()
            except Exception:
                pass
        if playwright is not None:
            try:
                playwright.stop()
            except Exception:
                pass
