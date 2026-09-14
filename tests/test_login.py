from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# ==================================================
# TC_Login_001
# Verify Login Page Loads
# ==================================================

def test_tc_login_001_login_page_loads(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    assert login_page.is_login_page_displayed()

    print(
        "TC_Login_001 - Login page loaded successfully"
    )


# ==================================================
# TC_Login_002
# Verify Company Logo is Displayed
# ==================================================

def test_tc_login_002_company_logo_displayed(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    assert login_page.is_company_logo_displayed()

    print(
        "TC_Login_002 - Company logo displayed successfully"
    )


# ==================================================
# TC_Login_003
# Verify Employee ID and Password are Visible
# ==================================================

def test_tc_login_003_employee_id_password_visible(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    assert login_page.is_employee_id_displayed()
    assert login_page.is_password_displayed()

    print(
        "TC_Login_003 - Employee ID and Password fields displayed"
    )


# ==================================================
# TC_Login_004
# Verify Password is Masked
# ==================================================

def test_tc_login_004_password_masked(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    login_page.enter_password("Admin@123")

    assert login_page.is_password_masked()

    print(
        "TC_Login_004 - Password is masked"
    )


# ==================================================
# TC_Login_005
# Verify Remember Me Checkbox is Displayed
# ==================================================

def test_tc_login_005_remember_me_checkbox(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    assert login_page.is_remember_me_displayed()

    print(
        "TC_Login_005 - Remember Me checkbox displayed"
    )


# ==================================================
# TC_Login_006
# Verify Login Button is Visible and Enabled
# ==================================================

def test_tc_login_006_login_button_visible_enabled(driver):

    login_page = LoginPage(driver)

    login_page.open_url()

    # Verify Login button is visible
    assert login_page.is_login_button_displayed()

    # Enter valid credentials
    login_page.enter_employee_id("ADMIN001")
    login_page.enter_password("Admin@123")

    # Verify Login button is enabled
    assert login_page.is_login_button_enabled()

    print(
        "TC_Login_006 - Login button displayed "
        "and enabled after valid input"
    )


# ==================================================
# TC_Login_007
# Verify Valid Login
# ==================================================

def test_tc_login_007_valid_login(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    assert dashboard_page.is_dashboard_displayed()

    print(
        "TC_Login_007 - Valid login successful"
    )


# ==================================================
# TC_Login_008
# Verify Redirect to Dashboard
# ==================================================

def test_tc_login_008_redirect_to_dashboard(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    assert dashboard_page.is_dashboard_displayed()

    assert "dashboard" in driver.current_url.lower()

    print(
        "TC_Login_008 - Redirected to Dashboard successfully"
    )


# ==================================================
# TC_Login_015
# Verify Remember Me with Valid Login
# ==================================================

def test_tc_login_015_remember_me_with_valid_login(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open_url()

    # Verify Remember Me is displayed
    assert login_page.is_remember_me_displayed()

    # Select Remember Me
    login_page.click_remember_me()

    # Login with valid credentials
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    # Verify successful login
    assert dashboard_page.is_dashboard_displayed()

    print(
        "TC_Login_015 - Remember Me selected "
        "and valid login successful"
    )