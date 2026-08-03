from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage
from pages.add_employee_page import AddEmployeePage
import time


def test_add_employee():

    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    add_employee_page = AddEmployeePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Employee Page
    employee_page.open_employee_page()

    # Click New Employee
    employee_page.click_new_employee()

    # =========================
    # STEP 1
    # =========================

    add_employee_page.fill_personal_information(
        " Nilaksan",
        "Male",
        "27-02-2000",
        "+94 77 9458933",
        "Kandy",
        "Nilaksan2@gmail.com",
        "Nilak#4534",
        "Nilaksank"
    )
    add_employee_page.click_create_button()

    time.sleep(3)

    # =========================
    # STEP 2
    # =========================

    add_employee_page.fill_education_information(
        qualification="Bachelor's Degree",
        institute="University of Morotowa",
        year="2026",
        position="QA Intern",
        company="PineAppleAI",
        experience="2"
    )

    add_employee_page.click_continue_button()

    time.sleep(3)

    # =========================================
    # STEP 3
    # =========================================

    add_employee_page.upload_documents(
        r"C:\Users\Dell\Documents\nic.pdf",
        r"C:\Users\Dell\Documents\birth.pdf",
        r"C:\Users\Dell\Documents\education.pdf"
    )

    add_employee_page.fill_work_information(
        joining_date="30/03/2025",
        designation="QA Engineer",
        role="Employee",
        management_role="Senior",
        reporting_manager="Arpitha"
    )

    add_employee_page.click_save_employee()
    print("Employee Added Successfully")

    driver.quit()