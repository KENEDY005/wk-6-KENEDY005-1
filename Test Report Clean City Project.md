# 🧪 SOFTWARE TEST REPORT: The testTriad Group

# CLEAN CITY PROJECT 

**Date of report**: 20/11/2025

**Prepared by**: Kenedy Ambila



**Course:** Software Testing & Quality Assurance 

**Module:** Test Management

**Project Type:** Group Assessment: The testTriad 

**Submission Date:** 2025-11-21

## Team Information

| Role | Name | Responsibilities |
|------|------|------------------|
| Test Manager | Kenedy Ambila | Planning, scheduling, coordination, metric tracking |
| Risk Analyst | Daniel Musembi | Risk identification, prioritization, test design linkage |
| Test Executor | Excellent Anjorin  | Execution, evidence capture, defect logging |

## Test Summary Overview
This testing cycle for the Clean City Web Application focused on validating the core user journey, including authentication, form submissions, scheduling pickups, and general system responsiveness. Through both manual verification and automated Selenium tests and Jest unit testing, we assessed the application's stability, accuracy of input handling, and error-response behaviour. Manual tests complemented automated checks to ensure alignment between expected and actual system behaviour.

Overall, the system demonstrates functional readiness in essential areas such as login, navigation, and page rendering. Jest unit tests were executed on core logic functions, including input validation, date formatting, and error-handling utilities. These tests helped uncover issues not visible through UI testing alone, particularly inconsistent validation rules and unpredictable handling of malformed inputs.

However, several defects were identified, especially around input behaviour, missing validation messages, and element locator instability. Core security features also showed major issues, such as successful invalid logins and the absence of notifications on pickup-schedule status for both users and administrators. These issues affect the reliability, security, and overall user experience.

Despite these challenges, the application shows strong progress toward meeting operational requirements. Addressing the identified defects, strengthening validation logic, and expanding both Selenium and Jest test coverage will significantly enhance product reliability and readiness for the next release cycle.



## Project Overview

**System Under Test:** Clean City Web Applicaton
**Technology Stack:** HTML, CSS, JavaScript  
**Environment:** Chrome Browser, Microsoft Edge, Firefox/Mozilla Browser, Visual Studio (VS) Code through live server extension, 

### Features Under Test
    1. Registration
    2. Login
    3. Request Pickup 
    4. Feedback
    5. Admin Login
    6. Manage Requests
    7. Navigation/UI
    8. Security/Validation

    Both positive and negative tests were created on the feature
    
## Test Plan

###  Test Objectives
The primary objective of this testing cycle was to evaluate the quality, functionality, performance and usability of the Clean City Web Application before its production release. Our testing aimed to:

    1. Verify functional correctness of all Clean City modules.
    2. Confirm user flows behave as expected.
    3. Identify system defects and inconsistencies.
    4. Validate reliability and security of authentication.
    5. Confirm usability and accessibility standards.
    6. Ensure compliance with project requirements.
- 

### Scope

The testing of the CLean City Application covered:
    1. Manual testing
    2. Selenium Automation
    3. Jest unit testing
to ensure core functionality, user flows and reliability.

**In Scope:**

- Login & Registration.
- Dashboard & Scheduling waste pickups
- Admin Management
- Notification
- Profile management
- Accessibility & User Authentication

**Out of Scope:**

- Backend API load testing
- Database migration
- Third-party integrations

Since the application relies on local storage for data persistence, backend API load testing and database migration were not applicable in this test cycle. Similarly, third-party integrations were not fully implemented and will be tested in future cycles once the core functionality is stable.

### Tools & Resources

- **Selenium:** Automated UI and end-to-end testing.
- **Jest:** unit testing for JavaScript Logic
- **Manual testing:** Functional, UI/UX and exploratory testing
- **VS Code:** Development and test script editing
- **Browser(Chrome/Edge, via VS Code liveserver):** Application testing enviroment
- **Test URL:** "http://localhost:3000"
- **Network:** Standad broadband connection

### Schedule

| Phase | Planned Duration (2025) | Actual Duration | Status |
|-------|------------------|-----------------|--------|
| Phase1: Planning & Setup | Due 5/11/2025 |8/11/2025 | Completed |
| Phase2: Test Design $ Early Execution | 11/11/2025 |17/11/2025 | Completed |
| Phase3: Final Execution and Reporting| 18/11/2025 |20/11/2025 |Completed |


## Risk Analysis

### Risks

| ID | Feature | Risk Description | Likelihood | Impact | Priority | Mitigation Strategy |
|----|---------|------------------|------------|--------|----------|---------------------|
| R001 | Login | The system allows login with invalid password | High | Critical | High | Implement strict backend password verification and proper error messages  |
| R002 | Input | Invalid formats break scheduling features | Medium |High | High | Enforce input format validation and use date picker with proper constraints |
| R003 | Form validation | Missing error messages for required fields | High | Medium | High | Add frontend and backend validation with clear, consistent error messages |
| R004 | UI navigation | Some pages not accessible on smaller screen | Low | Medium | Medium|Test on multiple screen and make UI responsive media queries |
| R005 | Error handling | Errors not properly returned to user or logged | Medium | High | High | Standardise error handling, log errors, and provide user-friendly messages |
| R006 | Registration | Unregistered users can access the app | High| Critical | High | Add authentication guards, session validation, and route protection on all pages |
| R007 | Admin Functions Access | A valid admin logs in with correct credentials but is unable to perform admin functions due to broken endpoints/ UI restrictions | Medium | High | High | Validate admin role mapping, ensure correct permission in backend, add tests to confirm admins can perform all admin functions |
| R008 | Responsiveness & UI Scaling | Website does not display properly on different viewports or devices | Medium | Medium | Medium | Test and implement responsive layouts and media queries; validate on multiple devices |
| R009 | Filtering Logic Failure | Filtering requests does not produce correct results | Medium | Medium | Medium | Validate filter logic in frontend and backend; add automated tests for different combinations |
| R010 | Real-time Tracking Failure | Users cannot see live updates of pickup requests | Medium | High | High | Implement WebSocket or polling updates; test real-time status updates in different scenarios |


### Risk Coverage

The testing activities focused on identifying and evaluating risks that could affect the functionality, security and reliability of the CleanCity App. Each risk was mapped to corresponding test cases to ensure adequate coverage across critical areas, including:
**1. Authentication Risks**
- verifying that login, registration and role-based actions (admin vs user ) function correctly, including failures such as invalid credentials or restricted access.

**2. Authorisation and Admin Privileges**
- Ensuring that true admins can perform required admin actions while non-admin users are restricted.

**3. Functional Risks**
- testing core features such as scheduling pickups, form validation, inputs and request updates to ensure correct workflow behaviour.

**4. Data handling risks**
- confirming correct validation, error messaging and secure handling of user input.

**5. UI/UX risks**
- Ensuring users can navigate the system effectively across different screens and devices.

**6. Operational risks**
- identifying issues that may arise from backend failures, api timeouts or incomplete system responses

- Tested Risks Percent (%): 
- Untested Risks Percent (%):
# CleanCity Project – Test Cases

## 1. Manual Test Cases

### 1.1 Positive Manual Test Cases

| ID   | Feature | Objective | Expected Result | Actual Result | Status | Risk Link | Assignee |
|------|---------|-----------|----------------|---------------|--------|-----------|-----------|
| M-01 | Registration | Register a new user with valid details | User account created successfully | User account created successfully | Pass  | R006 | Daniel & Excellent |
| M-02 | Login | Login with correct user credentials | User is logged in | user was logged in successfully |Pass  | R001 | Daniel |
| M-03 | Pickup Request | Submit a pickup request with valid inputs | Request submitted successfully and appears on the user's my requests page | request submitted successfully and appears on the user's my requests page | Failed | R003 | Daniel |
| M-04 | Feedback | Submit feedback with valid message | Feedback submitted successfully | feedback submitted | Pass | R003 | Daniel |
| M-05 | Admin Login | Login as admin using correct credentials | Admin logged in successfully | admin duties displayed | pass | R007 | Daniel & Excellent |
| M-06 | Responsiveness | Test system responsiveness across viewports | The website should be responsive | web not responsive on small devices  | failed  | R008 | Excellent |
| M-07 | Filtering | Filter request based on criteria | Filter works correctly for all inputs |  filter function displayed wrong info | failed | R009 | Daniel |
| M-08 | Update Requests | Change pickup request status | Request updated successfully | update was successfull  | pass | R007 | Daniel |
| M-09 | Boundary Testing | Test min/max words in feedback field | Input accepts min and max allowed words | accepts as many words as possible | passed | R003 | Excellent |
| M-10 | Data Persistence | Reload page after submitting request | Data remains intact after reload | user data cleared when the page is reloaded |failed  | R005 | Daniel |
| M-11 | Data Integrity | Logout after login | Session data is cleared upon logout |  session is cleared |Passed  | R006 | Excellent |
| M-12 | Request Tracking | Track pickup request progress | User sees real-time progress | no display of request progress  |failed  | R010 | Excellent & Daniel |
| M-14 | Status Notification | Update request status and notify users | User + admin get status change notification | notification not displayed |failed  | R007 | Kenedy |

---

### 1.2 Negative Manual Test Cases

| ID  | Feature | Objective | Expected Result | Actual Result | Status | Risk Link | Assignee |
|------|---------|-----------|----------------|---------------|--------|-----------|-----------|
| M-15 | Registration | Register user with empty form fields | Error messages shown, registration fails | required name and email  | passed | R003 | Kenedy & Daniel |
| M-16 | Login | Login with wrong password | Login fails with error | users were logged in with incorrect email  | fail  | R001 | Kenedy |
| M-17 | Pickup Request | Submit empty pickup form | Validation error should appear | validation errors displayed | passed | R003 | Kenedy |
| M-18 | Feedback | Submit feedback with empty message | Validation error shown |empty feedback was rejected  | passed  | R003 | Kenedy |
| M-16 | Admin Update | Update request without selecting a request | Error message displayed | required to update select a request first |passed  | R007 | Daniel |
| M-19 | Registration | Register with invalid email format | Error requiring valid email | invalid emails were registered | passed | R003 | Daniel |
| M-20 | Feedback | Submit feedback form with blank input | Prompt to enter feedback | promted to enter feedback  | passed | R003 | Excellent & Kenedy |
| M-21 | Feedback | Submit feedback while logged out | User asked to log in | sessions were cleared and unable to access feedback | passed | R006 | Kenedy |
| M-22 | Registration | Register duplicate user | Error: user already registered |  system shifts to existing user, asking to update credentials| passed | R006 | Kenedy & Daniel |
| M-23 | Date Validation | Submit feedback with invalid date | Error: enter a valid date | accepts even past dates  | failed  | R002 | Excellent |

---

## 2. Automated Test Cases

### 2.1 Selenium End-to-End Test Cases (E2E)

#### Positive Selenium Tests

| ID  | Feature | Objective | Expected Result | Actual Result | Status | Risk Link | Assignee |
|-----|---------|-----------|----------------|---------------|--------|-----------|-----------|
| S-01 | Registration | Register a new user using UI | User account created successfully | user account created successfuly  | pass  | R006 | Kenedy |
| S-02 | Login | Login using valid credentials | User logged in successfully | login was successful | pass  | R001 | Kenedy |
| S-03 | Pickup Request | Submit a valid pickup request | Request submitted successfully | submitted successfully  |pass  | R003 | Kenedy |
| S-04 | Feedback | Submit valid feedback | Feedback submitted successfully | feedback sent  |pass  | R003 | Kenedy |
| S-05 | Admin Login | Login using admin credentials | Admin logged in successfully | successful | pass | R007 | Kenedy |

#### Negative Selenium Tests

| ID  | Feature | Objective | Expected Result | Actual Result | Status | Risk Link | Assignee |
|-----|---------|-----------|----------------|---------------|--------|-----------|-----------|
| S-06 | Registration | Submit registration with empty fields | Registration fails with error | user was required to enter the missing parts.   | passed | R003 | Kenedy |
| S-07 | Login | Login with wrong password | Login fails with error |user granted access and directed to profile  | fail | R001 | Kenedy |
| S-08 | Pickup Request | Submit empty pickup request | Validation error shown | user requied to fill the missing fields  | passed | R003 | Kenedy |
| S-09 | Feedback | Submit empty feedback form | Validation error shown | user required to enter feedback  | passed  | R003 | Kenedy |
| S-10 | Admin Update | Update status without selecting request | Error message displayed | the admin dashboard aint working | Failed | R007 | Kenedy |

---

### 2.2 Jest Unit Test Cases

#### Positive Jest Tests

| ID  | Feature | Objective | Expected Result | Actual Result | Status | Risk Link | Assignee |
|-----|---------|-----------|----------------|---------------|--------|-----------|-----------|
| J-01 | Registration | Test success of `registerUser()` | Returns success response | success  | passed | R006 | Daniel |
| J-02 | Login | Test correct credentials via `loginUser()` | Returns auth token | user granted access | passed | R001 | Daniel |
| J-03 | Pickup Request | Test `submitPickup()` with valid data | Request created | request created | passed | R003 | Daniel |
| J-04 | Feedback | Test `submitFeedback()` | Feedback accepted | feedback accepted  | passed  | R003 | Daniel |
| J-05 | Admin update requests | login as admit and update status of a pickup  | update sucessfull | admin actions aint possible | failed  | R007 | Kenedy |

#### Negative Jest Tests

| ID  | Feature | Objective | Expected Result | Actual Result | Status | Risk Link | Assignee |
|-----|---------|-----------|----------------|---------------|--------|-----------|-----------|
| J-06 | Registration | Register user with empty fields | Error response | error message requiring use to fill the empty parts  | passed | R003 | Kenedy & Daniel |
| J-07 | Login | login with empty password fields | Error response |user required to fill the fields  | passed  | R001 | Kenedy & Daniel |
| J-08 | Pickup Request | Empty pickup object submitted | Validation error | required to complete the pickup details except for more description which was optional | passed  | R003 | Kenedy & Daniel |
| J-09 | Feedback | Submit empty feedback object | Validation error | feedback field required to be filled  |  passed | R003 | Kenedy & Daniel |
| J-10 | Admin Update | Admin status update without request ID | Error response | no admin actions can be performed just a page is visible | Failed | R007 | Kenedy & Daniel |




## Defects

# Manual test cases

| ID       | Issue Title                                                                   | Severity | Risk ID  | Status   | GitHub Link                                                                                                                                          |
| -------- | ----------------------------------------------------------------------------- | -------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| M-06     | UI Responsiveness Issues on Mobile (Overlapping Elements)                     | High     | R008     | OPEN     | [https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/12#issue-3639719086](https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/12#issue-3639719086) |
| M-12     | Request Tracking Not Working (User Cannot View Submitted Requests)            | High     | R010     | OPEN     | [https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/13#issue-3642580849](https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/13#issue-3642580849) |
| M-23     | Date Validation Accepts Invalid/Past Dates (5+ Years Old)                     | High     | R002     | OPEN     | [https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/15#issue-3642717970](https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/15#issue-3642717970) |
| **M-31** | **Pickup Request Not Displayed in “My Requests” After Successful Submission** | **High** | **R011** | **OPEN** | **[https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/21](https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/21)**                               |
| **M-32** | **Data Not Persisting After Page Reload (Submitted Request Data Cleared)**    | **High** | **R012** | **OPEN** | **[https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/23](https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/23)**                               |


# Selenium end-to-end test cases 

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|-------------|----------|---------|--------|-------------|
| S-005  | Admin Login Allows Access with Invalid Password | high | R007 | open | https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/19#issue-3643268825 |
| S-008 | Pickup Scheduling Accepts Past Dates | High | R-002 | open | https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/18#issue-3643246195 |
| S-06 | Registration Succeeds with Invalid Email | High | R006 |open | https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/17#issue-3643147546 |
| S-06 | Weak Password Accepted During Registration | High | R-005 | open | https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/16#issue-3643066921 |
| S-005 | login page does not block repeated invalid attempts (Brute Force vulnerability) | high | R007 |copen | https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/22#issue-3648471206 |


# Jest unit test cases

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|-------------|----------|---------|--------|-------------|
| J-10 | Admin Page: Update Status Button Not Behaving Correctly |Critical | R007 | open | https://github.com/KENEDY005/wk-6-KENEDY005-1/issues/20#issue-3648382455 |


## Metrics

- Test Case Pass Percent:
- 
      - Manual: 18/23 = 78.2 %
  
      - Selenium: 5/10 = 50%
  
      - Jest: 9/10 = 90%

### Defect Summary

- Total Defects Logged: 11
- Critical High: 11
- Fix Rate: 0%. The defects havent been fixed yet. This cycle only focussed on identifying them no fixing was required.

## Test Control & Project Management

# Phases

| Phase                                 | Deliverable                                                   | Actual Output                             | Variance     | Owner              |
| ------------------------------------- | ------------------------------------------------------------- | ----------------------------------------- | ------------ | ------------------ |
| Phase1: Planning & Setup              | Project plan, test strategy, and environment setup            | Test plan created; environment ready      | 3 days delay | Kenedy Ambila      |
| Phase2: Test Design & Early Execution | Test cases, test scripts, and initial execution results       | Test cases executed; early defects logged | 6 days delay | The testTriad Team |
| Phase3: Final Execution and Reporting | Final test execution, defect reports, and test summary report | All tests executed; report submitted      | 2 days delay | The testTriad Team |


**Progress Tracking Method:**  
**Change Control Notes:**

## Lessons Learned

- Most Defect Prone Feature: Login and registration features: Users were able to login using invalid credential, non existent emails and username and were also able to register members with invalid emails: This affect the security of users and the organization.
- Risk Analysis Impact: 
- Team Communication Effectiveness: Communication is key. Any time there was lack of communication we lagged behind the schedule. 
- Improvements for Next Cycle: Expand automated Selenium and Jest coverage.Implement stricter risk-based test planning, standardize error handling, and maintain robust logging for future releases.

## Attachments
- Please find screenshots of automated selenium test in the tests folder > screenshots
- for jest and manual testing find them on raised issues

## Sign Off

| Name | Role | Initials | Date |
|------|------|-----------|------|
| Kenedy Ambila| Test Manager | KA | 20/11/2025 |
| Daniel Musembi| Risk Analyst | DM | 20/11/2025 |
| Excellent Anjorin | Test Executor | EA | 20/11/2025 |

## Overall Summary


**Statement:** 

The Clean City application underwent a comprehensive testing cycle involving manual, Selenium, and Jest unit tests to assess core functionality, security, validation accuracy, and overall user experience. The system demonstrates strong foundational progress, with major user flows such as registration, login, request submission, and feedback functioning as intended in many scenarios. Automated unit tests achieved high reliability, confirming that core logic modules behave correctly under both positive and negative conditions.

However, critical defects were identified—particularly around authentication, input validation, date handling, admin privileges, UI responsiveness, and security vulnerabilities such as allowing invalid logins and accepting brute-force attempts. These issues significantly impact the system’s stability and readiness for real-world use. Addressing these defects, strengthening validation mechanisms, improving user feedback messages, and enhancing admin features will be essential for the next development cycle. Overall, the application is progressing well but requires focused improvement in high-risk areas before production readiness.

**Test Status:** 

**Completed **



















