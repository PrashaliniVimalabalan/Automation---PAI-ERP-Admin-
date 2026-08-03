# PAI ERP Automation Testing Framework

## Project Overview

This project contains automated test scripts developed for the **PAI ERP System** using Selenium WebDriver with Python and PyTest following the Page Object Model (POM) design pattern.

The framework automates major modules of the ERP system including:

* Login Management
* Dashboard
* Employee Management
* Leave Management
* Settings Management
* Template Management
* Attendance Filtering
* Form Validations

---

## Technology Stack

* Python 3.13
* Selenium WebDriver
* PyTest
* PyTest HTML Reports
* Page Object Model (POM)
* Git & GitHub

---

## Project Structure

```text
PAI ERP/
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── employee_page.py
│   ├── leave_page.py
│   ├── setting_page.py
│   └── template_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_dashboard.py
│   ├── test_employee.py
│   ├── test_leave.py
│   ├── test_settings.py
│   └── test_template.py
│
├── utils/
│   └── driver_setup.py
│
├── reports/
│
└── README.md
```

---

## Features Automated

### Login Module

* Valid Login
* Invalid Login
* Empty Credentials Validation

### Dashboard Module

* Dashboard Verification
* Attendance View All
* Employee Attendance Filter
* Status Filter
* Date Range Filter
* Clear Filter
* Logout Functionality

### Employee Module

* Add Employee
* Employee Information Validation
* Employee Search
* Employee Profile Verification
* Document Upload

### Leave Module

* Apply Leave
* Leave Status Verification
* Leave Approval Flow

### Settings Module

* Add Role
* View Role
* Edit Role
* Delete Role
* Confirmation Popup Validation

### Template Module

#### Offer Letter

* Generate Offer Letter
* Form Validation
* Preview Functionality

#### Service Letter

* Generate Service Letter
* Role Selection
* Achievement Section
* Preview Functionality
* Download Functionality

---

## Test Execution

Run all tests:

```bash
pytest
```

Run specific test:

```bash
pytest tests/test_employee.py -s
```

Run with HTML Report:

```bash
pytest --html=reports/report.html
```

---

## Reporting

The framework supports HTML report generation using PyTest HTML.

Example:

```bash
pytest --html=reports/report.html --self-contained-html
```

Generated reports include:

* Test Execution Summary
* Passed Test Cases
* Failed Test Cases
* Execution Time
* Error Logs

---

## Design Pattern

This framework follows the Page Object Model (POM) approach:

* Improved code maintainability
* Better reusability
* Easy locator management
* Scalable automation structure

---

## Author

**Pirashalini Vimalabalan**

QA Engineer Intern - Pineapple AI PVT

University of Vavuniya

Sri Lanka
