🧪 TryTestingThis.com Login Page Automation

📋 Project Overview

This project automates the Login Page functionality of TryTestingThis.com using Selenium WebDriver with Python. 

It follows the Page Object Model (POM) design pattern for better code reusability and maintenance.

The framework uses PyTest for test execution and PyTest-HTML for generating detailed HTML reports.

It verifies that the login process works successfully using valid credentials and generates a detailed HTML report with test results.


🧰 Tools and Technologies Used

Programming Language: Python

Automation Framework: PyTest

Automation Tool: Selenium WebDriver

Design Pattern: Page Object Model (POM)

Reporting Tool: PyTest-HTML

Browser: Google Chrome


📂 Project Structure

TryTestingThis.com-Login-Page-Automation/

│

├── base_pages/

│   └── login_page.py          # Page Object Model for Login Page

│

├── test_cases/

│   └── login_test.py          # Test script for login functionality

│

├── reports/

│   └── report1.html           # Generated HTML test report

│

├── screenshots/

│   └── successful_login.png   # Screenshot after successful login

│

└── requirements.txt           # Dependencies list


✅ Test Scenario – Verify Successful Login

| Step | Action                                                | Expected Result                            |

| 1    | Launch the site `https://trytestingthis.netlify.app/` | Login page should open                     |

| 2    | Enter username `test`                                 | Username entered successfully              |

| 3    | Enter password `test`                                 | Password entered successfully              |

| 4    | Click the Login button                                | User is redirected to success page         |

| 5    | Verify message "Successful"                           | Login confirmed                            |

| 6    | Capture screenshot                                    | Screenshot saved in `/screenshots/` folder |



📊 Test Execution Summary

| Result    | Count | Duration |

| ✅ Passed  | 1     | 00:00:16 |

| ❌ Failed  | 0     | —        |

| ⏩ Skipped | 0     | —        |



🧠 Key Highlights

Implemented Page Object Model (POM) structure

Developed using Selenium WebDriver and Python

Managed execution with PyTest framework

Generated HTML Reports for test results

Captured screenshot after successful login


👩‍💻 Author

Usha Nazare

| Project Type           | Practice Project   |

Aspiring Automation Tester | Selenium with Python Enthusiast





