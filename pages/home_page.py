from playwright.sync_api import Page, expect
from config import Config


class HomePage:
    URL = Config.BASE_URL

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def verify_homepage_opened(self):
        expect(self.page).to_have_url(Config.BASE_URL)
        
        # Navigation links
        navigation = self.page.locator("#navigation")
        expect(navigation).to_be_visible()
        expect(self.page.locator("#navigation img").first).to_be_visible()

        expect(navigation.get_by_text("Platform", exact=True).first).to_be_visible()
        expect(navigation.get_by_text("Industries", exact=True).first).to_be_visible()
        expect(navigation.get_by_text("Customers", exact=True).first).to_be_visible()
        expect(navigation.get_by_text("Resources", exact=True).first).to_be_visible()
        expect(self.page.get_by_text("Agentic Customer Engagement Platform", exact=False)).to_be_visible()
        
        expect(self.page.get_by_role("link", name="Platform Tour").first).to_be_visible()
        expect(self.page.get_by_role("link", name="Get a demo").first).to_be_visible()
        
        # Sections
        sections = self.page.locator("section")
        expect(sections.first).to_be_visible()
        
        section_count = sections.count()
        assert section_count > 3, f"Expected more than 3 sections, but found {section_count}"
        
        # Footer
        footer = self.page.locator("footer")
        footer.scroll_into_view_if_needed()
        expect(footer).to_be_visible()