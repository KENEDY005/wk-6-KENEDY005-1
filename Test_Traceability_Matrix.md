# CleanCity Project - Test Cases Report

## Environment
**Environment:**
- Chrome
- Firefox
- Microsoft Edge
- Live Server

---

## 1. Manual Test Cases

### 1.1 Positive Test Cases
| ID | Test Case Description | Steps | Expected Result | Severity | Assignee |
|----|---------------------|-------|----------------|---------|--------|
| M-01 | Register a new user | Fill user registration form with valid details and submit | User account created successfully | High | Daniel & Juliet |
| M-02 | Login with correct credentials | Enter valid email and password, click login | User is logged in | High | Daniel |
| M-03 | Submit a pickup request | Fill pickup request form with valid data and submit | Request submitted successfully | Medium | Daniel |
| M-04 | Submit feedback | Enter feedback message and submit | Feedback submitted successfully | Low | Daniel |
| M-05 | Admin login | Enter correct admin credentials | Admin logged in successfully | High | Daniel & Juliet  |
|M-06| Responsiveness to different viewports | Test how the website responds on various viewports| The website should be responsive |High | Juliet |
| M-07 | Filter a request | Filter request based on different criteria | Login as admin and try to filter pickup request based on diferrent combinations| The filter button should work perfectly on different inputs | low | Daniel |
| M-08 | Update pickup requests | update pickup request change it from one state to another | The requests should be updated successfully | medium |Daniel |
| M-09 | Boundary Testing | Test maximum/ minimum no of words feedback input field can take | Enter atleast one word and as many words as possible | low |Juliet |
| M-10 | Data persistence | Reload the page | Submit a request then reload the page | The data entered should remain intact after the page reloads | medium | Daniel | 
| M-11 | Unauthorized admin access | Try to open /admin page without logging in | Redirected to login page or shown an “Access Denied” message | High |
| M-12 | Data persistence after page reload | Submit a pickup request → Reload the page | Request still appears (data saved via localStorage) | Medium |
| M-13 | Filter requests by location | Login as admin → Go to Dashboard → Choose a specific location (e.g., Kenya) | Only requests from the selected location should display | Medium |


### 1.2 Negative Test Cases
| ID | Test Case Description | Steps | Expected Result | Severity | Assignee |
|----|---------------------|-------|----------------|---------|--------|
| M-06 | Register user with empty fields | Submit registration form without details | Error messages shown, registration fails | High | Kenedy & Daniel |
| M-07 | Login with wrong password | Enter valid email but wrong password | Login fails with error | High | Kenedy  |
| M-08 | Submit empty pickup form | Submit pickup form with no data | Validation error shown | Medium | Kenedy |
| M-09 | Submit empty feedback | Submit feedback form with no message | Validation error shown | Low | Kenedy |
| M-10 | Admin update without selecting request | Try to update status without selecting request | Error message displayed | Medium | Daniel |
| M-11 | Register an invalid user | Use an invalid email during registration | Error/ Alert requesting you to enter a valid mail| High | Daniel|
| M-12 | Submit an empty feedback | fill the feedback form but leave the field input blank | Alert/ message requesting you to enter a feedback |Juliet & Kenedy |
| M-13 | Submit feedback while logged out| Log out and try to submit a feedback | Message requiring you to log in | High |Kenedy |
| M -14| Duplicate user registration | Register a user twice using same details and different passwords | Error telling you the user is already registered | High | Kenedy & Daniel | 

---

## 2. Automated Test Cases

### 2.1 Selenium Tests: AUTOMATED END TO END TESTING
#### Positive Test Cases
| ID | Test Case Description | Steps | Expected Result | Severity | Assignee |
|----|---------------------|-------|----------------|---------|--------|
| S-01 | Register a new user | Open registration page, fill valid details, submit | User account created successfully | High | Kenedy  |
| S-02 | Login with correct credentials | Open login page, enter valid credentials, submit | User logged in successfully | High |Kenedy  |
| S-03 | Submit a pickup request | Fill pickup request form with valid data, submit | Request submitted successfully | Medium | Kenedy |
| S-04 | Submit feedback | Fill feedback message, submit | Feedback submitted successfully | Low |Kenedy  |
| S-05 | Admin login | Enter valid admin credentials | Admin logged in successfully | High | Kenedy|

#### Negative Test Cases
| ID | Test Case Description | Steps | Expected Result | Severity | Assignee |
|----|---------------------|-------|----------------|---------|--------|
| S-06 | Register with empty fields | Submit registration with no input | Registration fails with error | High | Kenedy  |
| S-07 | Login with wrong password | Enter wrong password | Login fails with error | High | Kenedy |
| S-08 | Submit empty pickup request | Submit pickup form without data | Validation error shown | Medium | Kenedy |
| S-09 | Submit empty feedback | Submit feedback form with no message | Validation error shown | Low | Kenedy |
| S-10 | Admin update without request | Attempt to update status without selecting request | Error message displayed | Medium |Kenedy  |


### 2.2 Jest Tests: LOGIC AND DATA LAYER
#### Positive Test Cases
| ID | Test Case Description | Test Function | Expected Result | Severity | Assignee |
|----|---------------------|---------------|----------------|---------|--------|
| J-01 | Register new user | `registerUser()` | Success response | High | Daniel  |
| J-02 | Login correct user | `loginUser()` | Auth token received | High | Daniel |
| J-03 | Submit pickup request | `submitPickup()` | Request created | Medium |Daniel  |
| J-04 | Submit feedback | `submitFeedback()` | Feedback accepted | Low | Daniel |
| J-05 | Admin login | `adminLogin()` | Admin authenticated | High | Daniel |

#### Negative Test Cases
| ID | Test Case Description | Test Function | Expected Result | Severity | Assignee |
|----|---------------------|---------------|----------------|---------|---------|
| J-06 | Register with empty fields | `registerUser({})` | Error response | High |Kenedy & Daniel |
| J-07 | Login wrong password | `loginUser(wrongPassword)` | Error response | High |Kenedy & Daniel |
| J-08 | Submit empty pickup | `submitPickup({})` | Validation error | Medium |Kenedy & Daniel |
| J-09 | Submit empty feedback | `submitFeedback({})` | Validation error | Low |Kenedy & Daniel |
| J-10 | Admin update without request | `updateStatus(noSelection)` | Error response | Medium |Kenedy & Daniel |

---

**Note:** All Selenium tests to include wait times of 5 seconds to ensure elements load properly.

