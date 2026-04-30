# Insider QA Automation Project

This project implements an end-to-end automated testing solution for the Insider career page using Playwright and Python.

The solution covers UI automation, CI/CD integration, reporting, and AI-assisted development practices.

## Tech Stack

- Python 3.13
- Playwright
- Pytest
- Pytest-HTML
- GitHub Actions (CI/CD)

## Test Scope

1. Verify Insider homepage loads correctly
2. Navigate to Careers page and filter Quality Assurance roles
3. Validate job listings (Position, Department, Location)
4. Verify Apply button redirects to Lever application form

## Project Structure

pages/
    home_page.py
    careers_page.py

tests/
    test_homepage.py
    test_careers.py

conftest.py
pytest.ini
.github/workflows/

## How to Run

Install dependencies:
pip install -r requirements.txt
Run tests:
pytest
Run with report:
pytest --html=reports/report.html --self-contained-html

## CI/CD

GitHub Actions is configured to:

- Run tests on pull requests
- Execute Playwright tests in headless mode
- Generate HTML reports
- Upload test artifacts (reports & screenshots)

## Reporting

Test execution results include:

- Pass/Fail status
- Execution duration
- Detailed failure logs
- Screenshots attached for failed tests

AI-Supported Test Automation Approach

AI was used during the development of this project to improve efficiency and solution quality across multiple stages:

Test Design & Planning
AI assisted in interpreting the assignment requirements and breaking them down into testable scenarios (homepage validation, job filtering, and application flow).
Locator Strategy Optimization
AI helped identify more stable and maintainable selectors (e.g., avoiding brittle XPath and using role-based or attribute-based locators).
Framework Structuring (POM)
AI supported structuring the project using the Page Object Model (POM) to improve readability, reusability, and maintainability.
Debugging & Error Resolution
AI was used to diagnose issues such as:
Playwright strict mode violations
CI failures (headless mode issues)
URL normalization problems
CI/CD Integration
AI guided the setup of GitHub Actions workflow for automated test execution and artifact publishing.
Reporting Enhancements
AI contributed to implementing screenshot capture on failure and embedding evidence into HTML reports.