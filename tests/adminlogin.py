import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# USING SCREENSHOT FOLDER AS REGISTRATION TESTS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def save_screenshot(driver, name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filepath = os.path.join(SCREENSHOT_DIR, f"{name}_{timestamp}.png")
    driver.save_screenshot(filepath)
    print("Screenshot saved:", filepath)


class TestAdminLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 5)

    # POSITIVE TEST (Test 1)

    def test_admin_login_positive(self):
        """Admin login with correct credentials"""
        driver = self.driver

        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
        )
        login_button.click()

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("admin@cleancity.com")

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

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("admin@cleancity.com")

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


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdminLogin)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n TEST SUMMARY ")
    print(f"Total tests run: {result.testsRun}")
    print(f"Tests passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests failed: {len(result.failures) + len(result.errors)}")
