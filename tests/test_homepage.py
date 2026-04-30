from pages.home_page import HomePage

def test_insider_homepage_is_opened(page):
    
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_homepage_opened()
