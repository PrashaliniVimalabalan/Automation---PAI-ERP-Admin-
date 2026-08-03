from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.setting_page import SettingsPage
import time

def test_empty_role_name():

    driver = get_driver()

    login_page = LoginPage(driver)
    settings_page = SettingsPage(driver)

    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    settings_page.open_settings_page()

    settings_page.add_role("")

    print("Empty Role Name Validation Tested")

    driver.quit()

