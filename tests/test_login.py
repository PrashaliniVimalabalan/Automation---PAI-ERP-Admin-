from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time


def test_valid_login():

    driver = get_driver()

    try:
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        # Open Login Page
        login_page.open_url()

        # Login
        login_page.login("ADMIN001", "Admin@123")

        # Wait for dashboard load
        time.sleep(3)

        # Dashboard Validation
        assert dashboard_page.is_dashboard_displayed

        print("Login Successful")

        # Logout
        dashboard_page.click_logout()

        time.sleep(2)

        print("Logout Successful")

    finally:
        # Close Browser always
        driver.quit()