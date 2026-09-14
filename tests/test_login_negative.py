from pages.login_page import LoginPage


# ==================================================
# TC_Login_010
# Verify Login with Invalid Password
# ==================================================

def test_tc_login_010_invalid_password(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Wrong@123"
    )

    assert "dashboard" not in driver.current_url.lower()

    print(
        "TC_Login_010 - Invalid password rejected"
    )


# ==================================================
# TC_Login_011
# Verify Login with Invalid Username
# ==================================================

def test_tc_login_011_invalid_username(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN999",
        "Admin@123"
    )

    assert "dashboard" not in driver.current_url.lower()

    print(
        "TC_Login_011 - Invalid username rejected"
    )


# ==================================================
# TC_Login_012
# Verify Login with Empty Username
# ==================================================

def test_tc_login_012_empty_username(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    # Leave Employee ID empty
    login_page.enter_employee_id("")

    # Enter valid password
    login_page.enter_password("Admin@123")

    # Click Login
    login_page.click_login()

    # Verify Employee ID validation message
    assert login_page.is_employee_id_required_message_displayed()

    # Verify user remains on Login page
    assert "dashboard" not in driver.current_url.lower()

    print(
        "TC_Login_012 - Empty username rejected "
        "with 'Employee ID is required' message"
    )


# ==================================================
# TC_Login_013
# Verify Login with Empty Password
# ==================================================

def test_tc_login_013_empty_password(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    # Enter valid Employee ID
    login_page.enter_employee_id("ADMIN001")

    # Leave Password empty
    login_page.enter_password("")

    # Click Login
    login_page.click_login()

    # Verify Password validation message
    assert login_page.is_password_required_message_displayed()

    # Verify user remains on Login page
    assert "dashboard" not in driver.current_url.lower()

    print(
        "TC_Login_013 - Empty password rejected "
        "with 'Password is required' message"
    )


# ==================================================
# TC_Login_014
# Verify Login with Empty Username and Password
# ==================================================

def test_tc_login_014_empty_username_and_password(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    # Leave Employee ID empty
    login_page.enter_employee_id("")

    # Leave Password empty
    login_page.enter_password("")

    # Click Login
    login_page.click_login()

    # Verify Employee ID validation message
    assert login_page.is_employee_id_required_message_displayed()

    # Verify Password validation message
    assert login_page.is_password_required_message_displayed()

    # Verify user remains on Login page
    assert "dashboard" not in driver.current_url.lower()

    print(
        "TC_Login_014 - Empty username and password rejected "
        "with both required field messages"
    )