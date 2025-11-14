import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCleanCityRegistration(unittest.TestCase):
    def setUp(self):
        # Launch Chrome browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        print("\nOpened CleanCity web application for Registration Tests.")

        # Screenshots directory
        self.screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
        print(f"Screenshots will be saved to: {self.screenshot_dir}")

        # Clear cookies
        self.driver.delete_all_cookies()

    def register_user(self, name, email, password):
        """Reusable function to fill registration form and submit"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        try:
            # Navigate to registration page
            register_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[9]'))
            )
            register_link.click()
            print("Clicked registration link.")
            time.sleep(1)

            # Name
            input_name = wait.until(EC.presence_of_element_located((By.ID, "register-name")))
            input_name.clear()
            input_name.send_keys(name)
            print(f"Entered name: {name}")
            time.sleep(1)

            # Email
            input_email = driver.find_element(By.ID, "register-email")
            input_email.clear()
            input_email.send_keys(email)
            print(f"Entered email: {email}")
            time.sleep(1)

            # Password
            input_password = driver.find_element(By.ID, "register-password")
            input_password.clear()
            input_password.send_keys(password)
            print(f"Entered password: {password}")
            time.sleep(1)

            # Submit registration
            submit_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button')
            submit_btn.click()
            print("Clicked register submit button.")
            time.sleep(2)
        except Exception as e:
            print(f"Error during registration steps: {e}")
            self.save_screenshot("registration_error")
            raise

    def save_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filepath = os.path.join(self.screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")

    # Positive Test: Valid information entered
    def test_positive_registration(self):
        """Positive Test: Valid registration details"""
        self.register_user("John Doe", "john@example.com", "password123")
        self.save_screenshot("positive_registration_passed")
        print("Positive registration test passed.")

    # Negative Tests
    def test_negative_missing_name(self):
        """Negative Test: Missing name field"""
        self.register_user("", "noname@example.com", "password123")
        input_name = self.driver.find_element(By.ID, "register-name")
        validation_msg = input_name.get_attribute("validationMessage")
        print(f"Validation message: {validation_msg}")
        self.assertEqual(validation_msg, "Please fill out this field.")
        self.save_screenshot("negative_missing_name")

    def test_negative_invalid_email(self):
        """Negative Test: Invalid email format"""
        self.register_user("Invalid Email", "invalidemail.com", "password123")
        input_email = self.driver.find_element(By.ID, "register-email")
        validation_msg = input_email.get_attribute("validationMessage")
        print(f"Validation message: {validation_msg}")
        expected_msg = "Please include an '@' in the email address. 'invalidemail.com' is missing an '@'."
        self.assertEqual(validation_msg, expected_msg)
        self.save_screenshot("negative_invalid_email")

    def test_negative_missing_email(self):
        """Negative Test: Missing email field"""
        self.register_user("No Email", "", "password123")
        input_email = self.driver.find_element(By.ID, "register-email")
        validation_msg = input_email.get_attribute("validationMessage")
        print(f"Validation message: {validation_msg}")
        self.assertEqual(validation_msg, "Please fill out this field.")
        self.save_screenshot("negative_missing_email")
    
    def test_negative_invalid_domain(self):
        """Negative Test: Invalid email domain"""
        self.register_user("Invalid Domain", "jose@12?.com", "password123")
        input_email = self.driver.find_element(By.ID, "register-email")
        validation_msg = input_email.get_attribute("validationMessage")
        print(f"Validation message: {validation_msg}")
        expected_msg = "A part following '@' should not contain the symbol '?'."
        self.assertEqual(validation_msg, expected_msg)
        self.save_screenshot("negative_invalid_domain")

    def test_negative_weak_password(self):
        """Negative Test: Weak password (<3 chars)"""
        self.register_user("Weak Password", "weak@example.com", "pw")
        input_password = self.driver.find_element(By.ID, "register-password")
        validation_msg = input_password.get_attribute("validationMessage")
        print(f"Validation message: {validation_msg}")
        # Customize based on your form's password rules
        expected_msg = "Please lengthen this text to 3 characters or more (you are currently using 2 characters)."
        self.assertEqual(validation_msg, expected_msg)
        self.save_screenshot("negative_weak_password")

    def tearDown(self):
        print("Closing browser...\n")
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCleanCityRegistration)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n TEST SUMMARY ")
    print(f"Total tests run: {result.testsRun}")
    print(f"Tests passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests failed: {len(result.failures) + len(result.errors)}")
