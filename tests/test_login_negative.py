from pages.login_page import LoginPage


def test_invalid_username(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN999",
        "Admin@123"
    )

    assert "dashboard" not in driver.current_url.lower()
    print("Invalid username")

def test_invalid_password(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Wrong@123"
    )

    assert "dashboard" not in driver.current_url.lower()
    print("Invalid Password")

def test_invalid_username_and_password(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN999",
        "Wrong@123"
    )

    assert "dashboard" not in driver.current_url.lower()
    print("Invalid username and password")

