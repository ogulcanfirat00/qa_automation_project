from pages.careers_page import CareersPage


def test_quality_assurance_jobs_list_is_visible(page):
    careers_page = CareersPage(page)

    careers_page.open()
    careers_page.verify_careers_page_opened()    
    careers_page.check_quality_assurance_team()      
    careers_page.click_quality_assurance_team()   
    careers_page.verify_jobs_list_visible()
    careers_page.verify_all_jobs_match_expected_criteria()
    
def test_apply_button_redirects_to_lever_form(page):
    careers_page = CareersPage(page)

    careers_page.open()
    careers_page.verify_careers_page_opened()
    careers_page.check_quality_assurance_team()
    careers_page.click_quality_assurance_team()
    careers_page.verify_jobs_list_visible()
    careers_page.click_first_apply_and_verify_lever_redirect()
    
    