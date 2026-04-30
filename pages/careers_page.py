from playwright.sync_api import Page, expect
from config import Config


class CareersPage:
    
    URL = Config.CAREERS_URL
    
    def __init__(self, page: Page):
        self.page = page
        
    def open(self):
        self.page.goto(self.URL, wait_until="domcontentloaded")
        
    def verify_careers_page_opened(self):
        expect (self.page).to_have_url(self.URL)
        
        container_career = self.page.locator(".insiderone-icon-cards-container")
        expect(container_career).to_be_visible()
        expect(container_career.get_by_text("Explore open roles", exact=False)).to_be_visible()
        
    def check_quality_assurance_team(self):
        self.page.get_by_text("See all teams", exact=False).click()
        expect(self.page.get_by_text("Quality Assurance", exact=False)).to_be_visible()
    
    def click_quality_assurance_team(self):
        qa_open_positions_link = self.page.locator(
            '[data-department="Quality Assurance"] a[href*="jobs.lever.co"]'
        )
        
        expect(qa_open_positions_link).to_be_visible(timeout=10000)
        qa_open_positions_link.click()
        
        expect(
            self.page.locator(".posting-category-title")
        ).to_contain_text("Quality Assurance")
          
        
    def verify_jobs_list_visible(self):
        job_postings = self.page.locator(".postings-group")
        expect(job_postings).to_be_visible()
        
        posting_count = job_postings.count()
        print(f"Number of job postings found: {posting_count}")
        assert posting_count > 0, f"Expected at least one job posting, but found {posting_count}"
    
    def verify_all_jobs_match_expected_criteria(self):
        postings = self.page.locator(".posting")

        posting_count = postings.count()
        assert posting_count > 0, "Expected at least one job posting, but no postings were found."

        for index in range(posting_count):
            posting = postings.nth(index)

            title = posting.locator('[data-qa="posting-name"]').first.inner_text()
            categories = posting.locator(".posting-categories").first.inner_text()

            combined_text = f"{title}\n{categories}"
            combined_upper = combined_text.upper()

            assert "QUALITY ASSURANCE" in combined_upper or "QA" in combined_upper, (
                f"Job {index + 1} position does not contain Quality Assurance or QA.\n"
                f"Actual:\n{combined_text}"
            )

            assert "ISTANBUL" in combined_upper, (
                f"Job {index + 1} location does not contain Istanbul.\n"
                f"Actual:\n{combined_text}"
            )
    
    def click_first_apply_and_verify_lever_redirect(self):
        apply_button = self.page.get_by_role("link", name="Apply").first
        expect(apply_button).to_be_visible(timeout=10000)
        apply_button.scroll_into_view_if_needed()
        apply_button.click()
        
        
        apply_button = self.page.get_by_role("link", name="Apply for this job", exact=False).first
        expect(apply_button).to_be_visible(timeout=10000)
        
        apply_button.click()
        self.page.wait_for_timeout(5000)
        expect(self.page.locator("form")).to_be_visible(timeout=10000)


       

     
        