from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.setting_page import SettingsPage
import time


def test_settings_page():

    driver = get_driver()

    login_page = LoginPage(driver)
    settings_page = SettingsPage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    # Open Settings Page
    settings_page.open_settings_page()

    # Add Role
    settings_page.add_role(
        "Web Admin"
    )


    # View Role
    settings_page.view_role()

    # Back
    settings_page.click_back_button()

    # Edit Role
    settings_page.edit_role(
        "Senior Web Admin"
    )

    # Delete Role
    settings_page.delete_role()

    print("Settings Page Tested Successfully")

    time.sleep(5)

    driver.quit()