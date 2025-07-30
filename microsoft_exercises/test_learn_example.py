""" used the given example on the playwright documentation to explore what is - presented in the microsoft learn page.
"""
import re
from playwright.sync_api import Page, expect, sync_playwright

class TestExamples:
    def test_has_title(self, page: Page):
        page.goto("https://playwright.dev/")

        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("Playwright"))
        page.screenshot(path="has_title.png", full_page=True)

    def test_get_started_link(self, page: Page):
        page.goto("https://playwright.dev/")

        # Click the get started link.
        page.get_by_role("link", name="Get started").click()

        # Expects page to have a heading with the name of Installation.
        expect(page.get_by_role("heading", name="Installation")).to_be_visible()
        page.screenshot(path="get_started_link.png", full_page=True)


# Get the device descriptor once at import time
with sync_playwright() as p:
    galaxy = p.devices["Galaxy S24"]
    iphone = p.devices["iPhone 15"]

class TestMobileEmulation:
    def test_has_title(self, page: Page):
        context = page.context.browser.new_context(**galaxy)# ** to match the dict to the parameters
        mobile_page = context.new_page()
        mobile_page.goto("https://playwright.dev/")
        expect(mobile_page).to_have_title(re.compile("Playwright"))
        page.screenshot(path="mobile_has_title.png", full_page=True)
        context.close()

    def test_get_started_link(self, page: Page):
        context = page.context.browser.new_context(**iphone)# ** to match the dict to the parameters
        mobile_page = context.new_page()
        mobile_page.goto("https://playwright.dev/")
        mobile_page.get_by_role("link", name="Get started").click()
        expect(mobile_page.get_by_role("heading", name="Installation")).to_be_visible()
        page.screenshot(path="mobile_get_started_link.png", full_page=True)
        context.close()
