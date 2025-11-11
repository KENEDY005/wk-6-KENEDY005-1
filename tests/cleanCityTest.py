"""
CleanCity Selenium Tests
------------------------
This test file checks if your CleanCity app works correctly.
It tests:
- User registration and login
- Pickup requests
- Feedback form
- Admin functions
"""

import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class CleanCityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Open Chrome browser and go to the app
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://localhost:3000")
        # Create folder for screenshots if a test fails
        cls.screenshot_dir = "screenshots"
        os.makedirs(cls.screenshot_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        # Close the browser after all tests
        cls.driver.quit()

    def take_screenshot(self, name):
        # Take a screenshot if something goes wrong
        file_path = os.path.join(self.screenshot_dir, f"{name}.png")
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved: {file_path}")

    # -----------------------------
    # Positive Tests
    # -----------------------------
    def test_1_homepage_loads(self):
        """Check if homepage opens"""
        try:
            self.assertIn("CleanCity", self.driver.title)
        except:
            self.take_screenshot("homepage_loads")
            raise

    def test_2_register_user(self):
        """Register a new user"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Register").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "name").send_keys("John Tester")
            self.driver.find_element(By.NAME, "email").send_keys("john@test.com")
            self.driver.find_element(By.NAME, "password").send_keys("pass123")
            self.driver.find_element(By.NAME, "confirmPassword").send_keys("pass123")
            self.driver.find_element(By.ID, "register-form").submit()
            time.sleep(2)
            msg = self.driver.find_element(By.ID, "register-success").text
            self.assertIn("Registration successful", msg)
        except:
            self.take_screenshot("register_user")
            raise

    def test_3_login_user(self):
        """Login with correct email and password"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Login").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "email").send_keys("john@test.com")
            self.driver.find_element(By.NAME, "password").send_keys("pass123")
            self.driver.find_element(By.ID, "login-form").submit()
            time.sleep(2)
            # Check if dashboard page loaded
            self.assertIn("dashboard", self.driver.page_source.lower())
        except:
            self.take_screenshot("login_user")
            raise

    def test_4_submit_pickup_request(self):
        """Submit a pickup request"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Request Pickup").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "fullName").send_keys("John Tester")
            self.driver.find_element(By.NAME, "location").send_keys("Nairobi")
            self.driver.find_element(By.NAME, "wasteType").send_keys("Plastic Waste")
            self.driver.find_element(By.NAME, "preferredDate").send_keys("2025-11-10")
            self.driver.find_element(By.ID, "pickup-form").submit()
            time.sleep(1)
            msg = self.driver.find_element(By.ID, "success-message").text
            self.assertIn("Request submitted successfully", msg)
        except:
            self.take_screenshot("submit_pickup")
            raise

    def test_5_submit_feedback(self):
        """Submit feedback"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Feedback").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "message").send_keys("Good service!")
            self.driver.find_element(By.ID, "feedback-submit").click()
            time.sleep(1)
            msg = self.driver.find_element(By.ID, "feedback-success").text
            self.assertIn("Thank you for your feedback", msg)
        except:
            self.take_screenshot("submit_feedback")
            raise

    # -----------------------------
    # Negative Tests
    # -----------------------------
    def test_6_login_wrong_password(self):
        """Login with wrong password should fail"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Login").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "email").send_keys("john@test.com")
            self.driver.find_element(By.NAME, "password").send_keys("wrongpass")
            self.driver.find_element(By.ID, "login-form").submit()
            time.sleep(2)
            msg = self.driver.find_element(By.ID, "login-error").text
            self.assertIn("Invalid email or password", msg)
        except:
            self.take_screenshot("login_wrong_password")
            raise

    def test_7_empty_pickup_form(self):
        """Try to submit pickup form empty"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Request Pickup").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "pickup-form").submit()
            time.sleep(1)
            err = self.driver.find_element(By.ID, "name-error").text
            self.assertIn("Full name is required", err)
        except:
            self.take_screenshot("empty_pickup_form")
            raise

    def test_8_empty_feedback(self):
        """Try to submit feedback without message"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Feedback").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "feedback-submit").click()
            time.sleep(1)
            err = self.driver.find_element(By.ID, "feedback-error").text
            self.assertIn("Feedback message is required", err)
        except:
            self.take_screenshot("empty_feedback")
            raise

    # -----------------------------
    # Admin Tests
    # -----------------------------
    def test_9_admin_login(self):
        """Admin login"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Admin Login").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "email").send_keys("admin@cleancity.com")
            self.driver.find_element(By.NAME, "password").send_keys("admin123")
            self.driver.find_element(By.ID, "admin-login-form").submit()
            time.sleep(2)
            self.assertIn("Admin Dashboard", self.driver.page_source)
        except:
            self.take_screenshot("admin_login")
            raise

    def test_10_admin_update_status(self):
        """Admin updates a request status"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Manage Requests").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "request-id").send_keys("1")
            self.driver.find_element(By.NAME, "status").send_keys("Completed")
            self.driver.find_element(By.ID, "update-status-btn").click()
            time.sleep(1)
            msg = self.driver.find_element(By.ID, "status-update-success").text
            self.assertIn("Status updated successfully", msg)
        except:
            self.take_screenshot("admin_update_status")
            raise

    def test_11_admin_update_without_request(self):
        """Admin tries to update without selecting request"""
        try:
            self.driver.find_element(By.LINK_TEXT, "Manage Requests").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "update-status-btn").click()
            time.sleep(1)
            err = self.driver.find_element(By.ID, "status-update-error").text
            self.assertIn("Select a request first", err)
        except:
            self.take_screenshot("admin_update_no_request")
            raise

if __name__ == "__main__":
    # Run all the tests and store results
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(CleanCityTests)
    result = test_runner.run(test_suite)

    # Print a simple summary
    total = result.testsRun
    failed = len(result.failures)
    errors = len(result.errors)
    passed = total - failed - errors

    print("\n" + "="*50)
    print("🧾 CLEAN CITY TEST SUMMARY")
    print("="*50)
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"⚠️ Errors: {errors}")
    print(f"🧪 Total tests: {total}")
    print("="*50)

    # Automatically open screenshots folder after tests
    try:
        screenshots_path = os.path.abspath(CleanCityTests.screenshot_dir)
        print(f"\n📂 Opening screenshots folder: {screenshots_path}")
        os.startfile(screenshots_path)  # Works on Windows
    except Exception as e:
        print(f"⚠️ Could not open screenshots folder automatically: {e}")
