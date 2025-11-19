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

This testing cycle for the Clean City Web Application focused on validating the coe user journey, including authentication, form submissions, scheduling pickups, and geneal system responsiveness. Through both manual verification and automated Selenium tests and jest unit testing, we assessed the application's stability, accuracy  of input handling, error-response behaviour. Manual tests complemented automated checks to ensure alignment between expected and actual system behaviour.
Overally the system demonstrates functional readiness in essential areas such as login, navigation and page rendering. Jest unit tests were executed on core logic functions (input validation, date formatting, error-handling utilities). These tests helped expose issues not visible through UI testing alone, especially the inconsistent validation rules and unpedictable handling of malformed inputs.
However, several defects were identified, expecially around the input behaviour, missing validation messages, element locator instability not forgetting core security features also had issues like successfull invalid logins, no notifications on status of the pickup schedule both on user and admin. These issues affect the reliablity and  overall user experience.
Despite the challanges, the application shows good progress toward meeting operational requirements. Addressing the identified defects, improving validation logic, and expanding both Selenium and jest coverage will significantly enhance product reliability and readiness fo the next release cycle.




## Project Overview

**System Under Test:** Clean City Web Applicaton
**Technology Stack:** HTML, CSS, JavaScript  
**Environment:** Chrome Browser, Micosoft Edge, VS Code via liveserver, firefox.

### Features Under Test
    1. Registration
    2. Login
    3. Request Pickup 
    4. Feedback
    5. Admin Login
    6. Manage Requests
    7. Navigation/UI
    8. Security/Validation

    Both positive and negative tests were created on feature
    
## Test Plan

###  Test Objectives
The primary objective of this testing cycle was to evaluate the quality, functionality, performance and the usability of the Clean City Web Application before its release to production. Our testing aimed to:

    1. Verify functional correctness of all CLean City modules.
    2. Confirm user flows behave as expected.
    3. Identify system defects and inconsistencies.
    4. Validate reliability and security of authentication.
    5. Confirm usablity and accessibility standards.
    6. Ensure compliance with project requirements.
- 

### Scope

The testing of the CLean City Application covered:
    1. Manual testing
    2. Selenium AUtomation
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
- Third-party intergrations

Since the application relies on localStoage for data persistence, backend API load testing and database migration were not applicable in this test cycle. Similarly, third-party intergrations were not fully implemented and will be tested in future cycles once the core functionality is stable.

### Tools & Resources

- **Selenium:** Automated UI and end to end testing.
- **Jest:** unit testing for JavaScipt Logic
- **Manual testing:** Functional,UI/UX and exploratory testing
- **VS Code:** Development and test script editing
- **Browser(Chrome/Edge, via VS Code liveserver):** Application testing enviroment
- **Test URL:** "http://localhost:3000"
- **Network:** Standad broadband connection

### Schedule

| Phase | Planned Duration (2025) | Actual Duration | Status |
|-------|------------------|-----------------|--------|
| Phase1: Planning & Setup | Due 5/11/2025 | | Completed |
| Phase2: Test Design $ Early Execution | 11/11/2025 | | Completed |
| Phase3: Final Execution and Reporting| 18/11/2025 | |Completed |


## Risk Analysis

### Risks

| ID | Feature | Risk Description | Likelihood | Impact | Priority | Mitigation Strategy |
|----|---------|------------------|------------|--------|----------|---------------------|
| R001 | Login | The system allows login with invalid password | High | Critical | High | Implement strict backend password verification and proper error messages  |
| R002 | Input | Invalid formats breaks scheduling features | Medium |High | High | Enforce input format validation and use date pciker with proper constrains |
| R003 | Form validation | Missing error messages for required fields | High | Medium | High | Add frontend and backend validation with clear, consistent error messages |
| R004 | UI navigation | Some pages not accessible on smaller screen | Low | Medium | Medium|Test on multiple screen and make UI responsive media queries |
| R005 | Error handling | Erros not properly returned to user or logged | Medium | High | High | Standrdize error handling, log errors, and provide user-friendly messages |
| R006 | Registration | Unegistered users can access the app | High| Critical | High | Add authentication guards, session validation, and route protection on all pages |
| R007 | Admin Functions Access | A valid admin logs in with correct credentials but unable to perform admin functions due to broken endpoints/ UI restrictions | Medium | High | High | Validate admin role mapping, ensure correct permission in backend add tests to confirm admins can perform all admin functions |
| R008 | Responsiveness & UI Scaling | Website does not display properly on different viewports or devices | Medium | Medium | Medium | Test and implement responsive layouts and media queries; validate on multiple devices |
| R009 | Filtering Logic Failure | Filtering requests does not produce correct results | Medium | Medium | Medium | Validate filter logic in frontend and backend; add automated tests for different combinations |
| R010 | Real-time Tracking Failure | Users cannot see live updates of pickup requests | Medium | High | High | Implement WebSocket or polling updates; test real-time status updates in different scenarios |


### Risk Coverage

The testing activities focussed on identifying and evaluating risks that could affect the functionality, security and reliability of the CleanCity App. Each risk was mapped to corresponding test cases to ensure adequate coverage across critical areas including:
**1. Authentication Risks**
- verifying that login, registration and role based actions (admin vs user ) function correctly, including failures such as invalid cedentials or restricted access.

**2. Authorization and Admin Previleges**
- Ensuring that true admins can perform required admin actions while non-admin users restricted.

**3. Functional Risks**
- testing core features such as scheduling pickups, form validation, inputs and request updates to ensure correct workflow behaviour.

**4. Data handling risks**
- confirming correct validation, error messaging and secure handling of user input.

**5. UI/UX risks**
- Ensuring users can navigate the system effectively across different screens and devices.

**6. Operational risks**
- identifying isssues that may arise from backend failures, api timeouts or incomplete system responses

- Tested Risks Percent: 
- Untested Risks Percent: 

# CleanCity Project – Test Cases

## 1. Manual Test Cases

### 1.1 Positive Manual Test Cases

| ID   | Feature | Objective | Expected Result | Actual Result | Status | Risk Link | Assignee |
|------|---------|-----------|----------------|---------------|--------|-----------|-----------|
| M-01 | Registration | Register a new user with valid details | User account created successfully | User account created successfully | Pass  | R006 | Daniel & Excellent |
| M-02 | Login | Login with correct user credentials | User is logged in | user was logged in successfully |Pass  | R001 | Daniel |
| M-03 | Pickup Request | Submit a pickup request with valid inputs | Request submitted successfully | request submitted successfully  | Pass | R003 | Daniel |
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
| M-22 | Registration | Register duplicate user | Error: user already registered |  |  | R006 | Kenedy & Daniel |
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
| S-06 | Registration | Submit registration with empty fields | Registration fails with error |  |  | R003 | Kenedy |
| S-07 | Login | Login with wrong password | Login fails with error |  |  | R001 | Kenedy |
| S-08 | Pickup Request | Submit empty pickup request | Validation error shown |  |  | R003 | Kenedy |
| S-09 | Feedback | Submit empty feedback form | Validation error shown |  |  | R003 | Kenedy |
| S-10 | Admin Update | Update status without selecting request | Error message displayed |  | Failed | R007 | Kenedy |

---

### 2.2 Jest Unit Test Cases

#### Positive Jest Tests

| ID  | Feature | Objective | Expected Result | Actual Result | Status | Risk Link | Assignee |
|-----|---------|-----------|----------------|---------------|--------|-----------|-----------|
| J-01 | Registration | Test success of `registerUser()` | Returns success response |  |  | R006 | Daniel |
| J-02 | Login | Test correct credentials via `loginUser()` | Returns auth token |  |  | R001 | Daniel |
| J-03 | Pickup Request | Test `submitPickup()` with valid data | Request created |  |  | R003 | Daniel |
| J-04 | Feedback | Test `submitFeedback()` | Feedback accepted |  |  | R003 | Daniel |
| J-05 | Admin Login | Test `adminLogin()` authentication | Admin authenticated |  |  | R007 | Daniel |

#### Negative Jest Tests

| ID  | Feature | Objective | Expected Result | Actual Result | Status | Risk Link | Assignee |
|-----|---------|-----------|----------------|---------------|--------|-----------|-----------|
| J-06 | Registration | Register user with empty fields | Error response |  |  | R003 | Kenedy & Daniel |
| J-07 | Login | Wrong password passed to `loginUser()` | Error response |  |  | R001 | Kenedy & Daniel |
| J-08 | Pickup Request | Empty pickup object submitted | Validation error |  |  | R003 | Kenedy & Daniel |
| J-09 | Feedback | Submit empty feedback object | Validation error |  |  | R003 | Kenedy & Daniel |
| J-10 | Admin Update | Admin status update without request ID | Error response |  | Failed | R007 | Kenedy & Daniel |




## Defects

# Manual tests cases

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|-------------|----------|---------|--------|-------------|
| | | | | | |

# Selenium end to end test cases 

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|-------------|----------|---------|--------|-------------|
| | | | | | |

# Jest unit test cases

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|-------------|----------|---------|--------|-------------|
| | | | | | |


## Metrics

- Test Case Pass Percent: 
- Defect Density: 
- Risk Coverage Percent: 
- Regression Success Rate: 

### Defect Summary

- Total Defects Logged: 
- Critical High: 
- Fix Rate: 

## Test Control & Project Management

### Phases

| Phase | Deliverable | Actual Output | Variance | Owner |
|-------|-------------|---------------|----------|-------|
| | | | | |

**Progress Tracking Method:**  
**Change Control Notes:**

## Lessons Learned

- Most Defect Prone Feature: 
- Risk Analysis Impact: 
- Team Communication Effectiveness: 
- Improvements for Next Cycle: 

## Attachments

- 

## Sign Off

| Name | Role | Initials | Date |
|------|------|-----------|------|
| Kenedy Ambila| Test Manager | KA | |
| Daniel Musembi| Risk Analyst | DM | |
| Excellent | Test Executor | EA | |

## Overall Summary

**Statement:** 

**Test Status:** ☐ Completed / ☐ In Progress 






