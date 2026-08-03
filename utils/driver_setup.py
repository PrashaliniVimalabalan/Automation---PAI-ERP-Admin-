from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():

    options = Options()

    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-password-generation")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    return driver