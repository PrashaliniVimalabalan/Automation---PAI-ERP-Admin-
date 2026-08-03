from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.template_page import TemplatePage
import time


def test_template_page():

    driver = get_driver()

    login_page = LoginPage(driver)
    template_page = TemplatePage(driver)

    # ==================================
    # LOGIN
    # ==================================

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    # ==================================
    # OPEN TEMPLATE PAGE
    # ==================================

    template_page.open_template_page()

    # ==================================
    # OFFER LETTER
    # ==================================

    print("Testing Offer Letter...")

    template_page.fill_template_details(
        name="Pirashalini",
        email="pirashaliniv.pineappleai@gmail.com",
        address="Jaffna",
        role="QA Engineer",
        joining_date="01/01/2024",
        ending_date="01/01/2025",
        department="QA Department",
        manager="Arpitha",
        manager_email="Arpithahr.pineappleai@gmail.com"
    )

    template_page.click_preview()

    time.sleep(3)

    print("Offer Letter Completed")

    template_page.open_service_letter()

    template_page.fill_service_letter(
        name="Pirashalini",
        designation="QA Engineer",
        role="Intern",
        ending_date="10/06/2026",
        joining_date="10/06/2025",
        achievement="Automated test cases using Selenium."
    )

    template_page.click_service_preview()

    driver.quit()