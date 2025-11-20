import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

<<<<<<< HEAD
# USING SCREENSHOT FOLDER AS REGISTRATION TESTS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def save_screenshot(driver, name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filepath = os.path.join(SCREENSHOT_DIR, f"{name}_{timestamp}.png")
    driver.save_screenshot(filepath)
    print("Screenshot saved:", filepath)

=======
# Screenshot directory
SCREENSHOT_DIR = "screenshots"
>>>>>>> b0dcdb2738f8a53562a61d872c31a06be7e7aba0

class TestAdminLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 5)

<<<<<<< HEAD
    # POSITIVE TEST (Test 1)

    def test_admin_login_positive(self):
        """Admin login with correct credentials"""
        driver = self.driver

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
        )
        login_button.click()
=======
    def take_screenshot(self, name):
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        filename = os.path.join(SCREENSHOT_DIR, f"{name}_{time.strftime('%Y%m%d-%H%M%S')}.png")
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")

    #  POSITIVE TEST 
    def test_admin_login_positive(self):
        """Admin login with correct credentials."""
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
        )
        login_btn.click()
>>>>>>> b0dcdb2738f8a53562a61d872c31a06be7e7aba0

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("admin@cleancity.com")

<<<<<<< HEAD
        password = driver.find_element(By.ID, "login-password")
        password.send_keys("admin123")

        submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button')
        submit.click()

        time.sleep(1)
        save_screenshot(driver, "admin_positive_login")

        self.assertIn("profile", driver.current_url)

    # NEGATIVE TEST 1 (Test 2)
    # Wrong password

    def test_admin_wrong_password(self):
        """Admin login with wrong password"""
        driver = self.driver

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
        )
        login_button.click()
=======
        password = self.wait.until(EC.presence_of_element_located((By.ID, "login-password")))
        password.send_keys("admin123")

        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit_btn.click()
        time.sleep(2)

        self.take_screenshot("admin_positive_login")
        self.assertIn("profile", self.driver.current_url)

    #  NEGATIVE TESTS 
    def test_admin_wrong_password(self):
        """Admin login with wrong password."""
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
        )
        login_btn.click()
>>>>>>> b0dcdb2738f8a53562a61d872c31a06be7e7aba0

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("admin@cleancity.com")

<<<<<<< HEAD
        password = driver.find_element(By.ID, "login-password")
        password.send_keys("wrongpass")

        submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button')
        submit.click()

        error_msg = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Invalid email or password')]"))
        )

        save_screenshot(driver, "admin_wrong_password")
        self.assertEqual(error_msg.text, "Invalid email or password")

    # NEGATIVE TEST 2 (Test 3)
    # INVALID EMAIL FORMAT

    def test_admin_invalid_email_format(self):
        """Invalid email format should trigger HTML validation"""
        driver = self.driver

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
        )
        login_button.click()

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("admin.com")

        # Click submit
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

        validation_msg = email.get_attribute("validationMessage")
        save_screenshot(driver, "admin_invalid_email_format")

        self.assertIn("Please include an '@' in the email address. 'admin.com' is missing an '@'.", validation_msg)

    # NEGATIVE TEST 3 (Test 4)
    # MULTIPLE WRONG ATTEMPTS (NO LOCKOUT)

    def test_admin_multiple_wrong_attempts(self):
        """Test three consecutive wrong login attempts"""
        driver = self.driver

        for attempt in range(1, 4):
            print(f"\nAttempt {attempt} of 3")

            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
            )
            login_button.click()

            email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
            email.clear()
            email.send_keys("admin@cleancity.com")

            password = driver.find_element(By.ID, "login-password")
            password.clear()
            password.send_keys("wrongpass123")

            driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

            error_msg = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Invalid email or password')]"))
            )

            save_screenshot(driver, f"admin_wrong_attempt_{attempt}")

            self.assertEqual(error_msg.text, "Invalid email or password")

            # Return to homepage for next attempt
            driver.get("http://localhost:3000/")

=======
        password = self.wait.until(EC.presence_of_element_located((By.ID, "login-password")))
        password.send_keys("wrongpass")

        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit_btn.click()

        error_msg = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Invalid email or password')]"))
        )
        self.take_screenshot("admin_wrong_password")
        self.assertIn("Invalid email or password", error_msg.text)

    def test_admin_invalid_email_format(self):
        """Admin login with invalid email format should trigger HTML validation."""
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
        )
        login_btn.click()

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("admin.com")  # Invalid email

        password = self.wait.until(EC.presence_of_element_located((By.ID, "login-password")))
        password.send_keys("admin123")

        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit_btn.click()
        time.sleep(1)

        email_field = self.driver.find_element(By.ID, "login-email")
        validation_msg = email_field.get_attribute("validationMessage")

        self.take_screenshot("admin_invalid_email_format")
        self.assertIn("Please include an '@' in the email address", validation_msg)
>>>>>>> b0dcdb2738f8a53562a61d872c31a06be7e7aba0

    def tearDown(self):
        self.driver.quit()


<<<<<<< HEAD
=======
#  RUN TESTS + SUMMARY 
>>>>>>> b0dcdb2738f8a53562a61d872c31a06be7e7aba0
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdminLogin)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

<<<<<<< HEAD
    print("\n TEST SUMMARY ")
    print(f"Total tests run: {result.testsRun}")
    print(f"Tests passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests failed: {len(result.failures) + len(result.errors)}")
=======
    print("\n========== TEST SUMMARY ==========")
    print(f"Total tests run: {result.testsRun}")
    print(f"Tests passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests failed: {len(result.failures) + len(result.errors)}")
    print("=================================\n")
>>>>>>> b0dcdb2738f8a53562a61d872c31a06be7e7aba0
