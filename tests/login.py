import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCleanCityLogin(unittest.TestCase):
# THIS IS A REUSEABLE FUNCTION THAT RUNS BEFORE EVERY TEST CASE
    def setUp(self):
        # Launch Chrome browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        print("\nOpened CleanCity web application.")

        # Adding path for screenshot to automatically take snips of what happens
        self.screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
        print(f"Screenshots will be saved to: {self.screenshot_dir}")

        # Clear cookies to avoid session issues
        self.driver.delete_all_cookies()
# REUSEABLE LOGIN FUNNCTION FOR EVERY LOGIN TESTS DONE
    def login(self, email, password):
        """Creating Reusable login steps"""
        driver = self.driver
        try:
            # Click initial login button
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
            )
            login_button.click()
            print("Clicked Login button to open login form.")
            time.sleep(2)

            # Enter email
            input_email = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "login-email"))
            )
            input_email.clear()
            input_email.send_keys(email)
            print(f"Entered email: {email}")
            time.sleep(2)

            # Enter password
            input_password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "login-password"))
            )
            # clear everything just incase there was prefilled data
            input_password.clear()
            input_password.send_keys(password)
            print(f"Entered password: {password}")
            time.sleep(1)

            # Click login
            login_submit = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-btn"))
            )
            login_submit.click()
            print("Clicked login submit button.")
            time.sleep(2)

        except Exception as e:
            print(f"Error during login steps: {e}")
            raise

    def save_screenshot(self, name):
        """function to save screenshot with timestamp"""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filepath = os.path.join(self.screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")

    def test_positive_login(self):
        """Positive Test: Correct email and password"""
        self.login("user@cleancity.com", "password123")
        driver = self.driver

         # Wait until the URL contains "profile" indicating successful login
        WebDriverWait(driver, 10).until(lambda d: "profile" in d.current_url)
        self.assertIn("profile", driver.current_url, "Login failed — did not reach profile page")

        # Screenshot on success
        self.save_screenshot("positive_login")
        print("Positive login test passed.")

    def test_negative_login_wrong_email(self):
        """Negative Test: Wrong email"""
        self.login("wronguser@cleancity.com", "password123")
        driver = self.driver
        try:
            error_msg = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-msg"))
            )
            self.assertTrue(error_msg.is_displayed(), "Error message not shown for wrong email")
        except Exception as e:
            print(f"Negative test failed: {e} — taking screenshot before failing.")
            self.save_screenshot("negative_wrong_email_failed")
            # fail the test
            raise
        else:
            self.save_screenshot("negative_wrong_email_passed")
            print("Negative login test (wrong email) passed and screenshot saved.")

    def test_negative_login_wrong_password(self):
        """Negative Test: Wrong password"""
        self.login("user@cleancity.com", "wrongpassword")
        driver = self.driver
        try:
            error_msg = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-msg"))
            )
            self.assertTrue(error_msg.is_displayed(), "Error message not shown for wrong password")
        except Exception as e:
            # If error element not found, take screenshot and **fail the test**
            print(f"Negative test failed: {e} — taking screenshot before failing.")
            self.save_screenshot("negative_wrong_password_failed")
            # Fail the test
            raise 
        else:
             # If test passes (error found), take screenshot for logging
            self.save_screenshot("negative_wrong_password_passed")
            print("Negative login test (wrong password) passed and screenshot saved.")
# Runs after each test: closes the browser to avoid any leftover sessions.
    def tearDown(self):
        print("Closing browser...\n")
        self.driver.quit()


if __name__ == "__main__":
    # Run tests and print summary
     # Load all tests from TestCleanCityLogin
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCleanCityLogin)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n TEST SUMMARY ")
    print(f"Total tests run: {result.testsRun}")
    print(f"Tests passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests failed: {len(result.failures) + len(result.errors)}")

