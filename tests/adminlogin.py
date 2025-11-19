import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Screenshot directory
SCREENSHOT_DIR = "screenshots"

class TestAdminLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 5)

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

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("admin@cleancity.com")

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

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("admin@cleancity.com")

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

    def tearDown(self):
        self.driver.quit()


#  RUN TESTS + SUMMARY 
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdminLogin)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n========== TEST SUMMARY ==========")
    print(f"Total tests run: {result.testsRun}")
    print(f"Tests passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests failed: {len(result.failures) + len(result.errors)}")
    print("=================================\n")
