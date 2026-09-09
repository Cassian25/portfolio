from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    raise SystemExit(
        "Playwright not installed. Run:\n"
        "  pip install playwright\n"
        "  playwright install chromium\n"
        "Then run this script again."
    )

DESIGNS_DIR = Path(__file__).parent
OUTPUT_DIR = DESIGNS_DIR / "screenshots"
DESIGNS = [f"{i}-design" for i in [
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
    "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth",
    "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth",
]]


def capture_all():
    OUTPUT_DIR.mkdir(exist_ok=True)
    viewport = {"width": 1920, "height": 1200}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport=viewport, device_scale_factor=2)

        for slug in DESIGNS:
            html_path = DESIGNS_DIR / f"{slug}.html"
            if not html_path.exists():
                print(f"Skip missing: {html_path.name}")
                continue

            file_url = html_path.resolve().as_uri()
            page.goto(file_url, wait_until="networkidle")
            page.wait_for_timeout(1500)

            design_dir = OUTPUT_DIR / slug
            design_dir.mkdir(exist_ok=True)

            pages = page.locator("section.page")
            count = pages.count()
            for i in range(count):
                section = pages.nth(i)
                section.scroll_into_view_if_needed()
                page.wait_for_timeout(400)
                out = design_dir / f"page-{i + 1}.png"
                section.screenshot(path=str(out))
                print(f"Saved {out.relative_to(DESIGNS_DIR)}")

            full_out = design_dir / "full-document.png"
            page.screenshot(path=str(full_out), full_page=True)
            print(f"Saved {full_out.relative_to(DESIGNS_DIR)}")

        browser.close()

    print(f"\nDone. Screenshots in: {OUTPUT_DIR}")


if __name__ == "__main__":
    capture_all()
