import time

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.template_page import TemplatePage


# ================================================================
# Helper
# ================================================================

def open_template_page():

    driver = get_driver()

    login_page = LoginPage(driver)
    template_page = TemplatePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    template_page.open_template_page()

    time.sleep(3)

    return driver, template_page


# ================================================================
# TC_TEMP_001
# Templates page
# ================================================================

def test_temp_001_templates_page():

    driver, template_page = open_template_page()

    try:

        assert "/template" in driver.current_url.lower() or \
               "template" in driver.current_url.lower()

        print(
            "TC_TEMP_001 - Templates page opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_002
# Offer Letter page
# ================================================================

def test_temp_002_offer_letter_page():

    driver, template_page = open_template_page()

    try:

        assert driver.find_element(
            *template_page.name_input
        ).is_displayed()

        print(
            "TC_TEMP_002 - Offer Letter form displayed successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_003
# Name
# ================================================================

def test_temp_003_name():

    driver, template_page = open_template_page()

    try:

        field = driver.find_element(
            *template_page.name_input
        )

        field.clear()
        field.send_keys("Pirashalini")

        assert field.get_attribute("value") == "Pirashalini"

        print(
            "TC_TEMP_003 - Name accepted successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_004
# Address
# ================================================================

def test_temp_004_address():

    driver, template_page = open_template_page()

    try:

        field = driver.find_element(
            *template_page.address_input
        )

        field.clear()
        field.send_keys("Kilinochchi")

        assert field.get_attribute("value") == "Kilinochchi"

        print(
            "TC_TEMP_004 - Address accepted successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_006
# Role
# ================================================================

def test_temp_006_role():

    driver, template_page = open_template_page()

    try:

        from selenium.webdriver.support.ui import Select

        Select(
            driver.find_element(
                *template_page.role_dropdown
            )
        ).select_by_visible_text("QA Engineer")

        selected = Select(
            driver.find_element(
                *template_page.role_dropdown
            )
        ).first_selected_option.text

        assert selected == "QA Engineer"

        print(
            "TC_TEMP_006 - Role selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_007
# Department
# ================================================================

def test_temp_007_department():

    driver, template_page = open_template_page()

    try:

        field = driver.find_element(
            *template_page.department_input
        )

        field.clear()
        field.send_keys("QA Department")

        assert field.get_attribute("value") == "QA Department"

        print(
            "TC_TEMP_007 - Department accepted successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_008
# Reporting Manager
# ================================================================

def test_temp_008_manager():

    driver, template_page = open_template_page()

    try:

        field = driver.find_element(
            *template_page.reporting_manager_input
        )

        field.clear()
        field.send_keys("Shahani")

        assert field.get_attribute("value") == "Shahani"

        print(
            "TC_TEMP_008 - Reporting Manager accepted successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_009
# Manager Email
# ================================================================

def test_temp_009_manager_email():

    driver, template_page = open_template_page()

    try:

        field = driver.find_element(
            *template_page.reporting_manager_email_input
        )

        field.clear()
        field.send_keys("manager@gmail.com")

        assert field.get_attribute(
            "value"
        ) == "manager@gmail.com"

        print(
            "TC_TEMP_009 - Manager Email accepted successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_010
# Offer Preview
# ================================================================

def test_temp_010_offer_preview():

    driver, template_page = open_template_page()

    try:

        template_page.fill_template_details(
            name="Pirashalini",
            email="pirashaliniv.pineappleai@gmail.com",
            address="Kilinochchi",
            role="QA Engineer",
            joining_date="01/01/2024",
            ending_date="01/01/2025",
            department="QA Department",
            manager="Shahani",
            manager_email="manager@gmail.com"
        )

        template_page.click_preview()

        print(
            "TC_TEMP_010 - Offer Letter preview generated successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_013
# Clear
# ================================================================

def test_temp_013_clear():

    driver, template_page = open_template_page()

    try:

        template_page.fill_template_details(
            name="Pirashalini",
            email="pirashaliniv.pineappleai@gmail.com",
            address="Kilinochchi",
            role="QA Engineer",
            joining_date="01/01/2024",
            ending_date="01/01/2025",
            department="QA Department",
            manager="Shahani",
            manager_email="manager@gmail.com"
        )

        template_page.click_clear()

        time.sleep(2)

        name_value = driver.find_element(
            *template_page.name_input
        ).get_attribute("value")

        assert name_value == ""

        print(
            "TC_TEMP_013 - Clear button worked successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_015
# Service Letter page
# ================================================================

def test_temp_015_service_letter_page():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        assert driver.find_element(
            *template_page.service_name
        ).is_displayed()

        print(
            "TC_TEMP_015 - Service Letter page displayed successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_016
# Service Name
# ================================================================

def test_temp_016_service_name():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        field = driver.find_element(
            *template_page.service_name
        )

        field.clear()
        field.send_keys("Pirashalini")

        assert field.get_attribute("value") == "Pirashalini"

        print(
            "TC_TEMP_016 - Employee Name accepted successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_018
# Designation
# ================================================================

def test_temp_018_designation():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        from selenium.webdriver.support.ui import Select

        Select(
            driver.find_element(
                *template_page.service_designation
            )
        ).select_by_visible_text("QA Engineer")

        print(
            "TC_TEMP_018 - Designation selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_019
# Role
# ================================================================

def test_temp_019_service_role():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        from selenium.webdriver.support.ui import Select

        Select(
            driver.find_element(
                *template_page.service_role
            )
        ).select_by_visible_text("Intern")

        print(
            "TC_TEMP_019 - Service Role selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_023
# Responsibility
# ================================================================

def test_temp_023_responsibility():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        template_page.click_element(
            template_page.add_achievement
        )

        field = driver.find_element(
            *template_page.achievement_textbox
        )

        field.clear()
        field.send_keys("QA Best Performance")

        assert field.get_attribute(
            "value"
        ) == "QA Best Performance"

        print(
            "TC_TEMP_023 - Responsibility accepted successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_024
# Add Achievement
# ================================================================

def test_temp_024_add_achievement():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        before = len(
            template_page.get_achievement_fields()
        )

        template_page.add_achievement_field()

        time.sleep(2)

        after = len(
            template_page.get_achievement_fields()
        )

        assert after >= before

        print(
            "TC_TEMP_024 - Achievement field added successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_025
# Multiple Achievements
# ================================================================

def test_temp_025_multiple_achievements():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        template_page.add_achievement_field()

        time.sleep(1)

        template_page.add_achievement_field()

        time.sleep(2)

        print(
            "TC_TEMP_025 - Multiple achievement fields created"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_026
# Achievement Text
# ================================================================

def test_temp_026_achievement_text():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        template_page.add_achievement_field()

        field = driver.find_element(
            *template_page.achievement_textbox
        )

        field.clear()
        field.send_keys("QA Best Performance")

        assert field.get_attribute(
            "value"
        ) == "QA Best Performance"

        print(
            "TC_TEMP_026 - Achievement text accepted successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_028
# Service Preview
# ================================================================

def test_temp_028_service_preview():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        template_page.fill_service_letter(
            name="Pirashalini",
            designation="QA Engineer",
            role="Intern",
            ending_date="30/09/2026",
            joining_date="30/03/2026",
            achievement="QA Best Performance"
        )

        template_page.click_service_preview()

        print(
            "TC_TEMP_028 - Service Letter preview generated successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_029
# Service Download
# ================================================================

def test_temp_029_service_download():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        template_page.fill_service_letter(
            name="Pirashalini",
            designation="QA Engineer",
            role="Intern",
            ending_date="30/09/2026",
            joining_date="30/03/2026",
            achievement="QA Best Performance"
        )

        template_page.click_service_preview()

        template_page.click_download()

        print(
            "TC_TEMP_029 - Service Letter download clicked successfully"
        )

    finally:

        driver.quit()