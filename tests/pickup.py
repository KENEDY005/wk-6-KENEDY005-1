import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# Use same screenshot folder
SCREENSHOT_DIR = os.path.join(os.getcwd(), "screenshots")

class TestSchedulePickup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 5)

        # Login first
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
        )
        login_btn.click()

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("calmo@cleancity.com")

        password = self.wait.until(EC.presence_of_element_located((By.ID, "login-password")))
        password.send_keys("123")

        submit = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit.click()
        time.sleep(2)

        # Navigate to Schedule Pickup
        schedule_pickup_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[2]'))
        )
        schedule_pickup_btn.click()

    def save_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        if not os.path.exists(SCREENSHOT_DIR):
            os.makedirs(SCREENSHOT_DIR)
        filepath = os.path.join(SCREENSHOT_DIR, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")

    # POSITIVE TEST

    def test_positive_schedule_pickup(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "home-name"))).send_keys("Calmo Wamafuacha")
        self.driver.find_element(By.ID, "home-email").send_keys("calmo@cleancity.com")
        self.driver.find_element(By.ID, "home-location").send_keys("Nairobi")
        self.driver.find_element(By.ID, "home-waste").send_keys("Hazardous")
        self.driver.find_element(By.ID, "home-date").send_keys("2025-12-31")
        self.driver.find_element(By.ID, "home-desc").send_keys("Kindly come prepared…")

        submit = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit.click()

        success_msg = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Your waste pickup request has been submitted!')]"))
        )

        self.save_screenshot("pickup_positive")
        self.assertEqual(success_msg.text, "Your waste pickup request has been submitted!")

    # NEGATIVE TESTS

    def test_negative_missing_fullname(self):
        self.driver.find_element(By.ID, "home-email").send_keys("calmo@cleancity.com")
        self.driver.find_element(By.ID, "home-location").send_keys("Nairobi")
        self.driver.find_element(By.ID, "home-waste").send_keys("Hazardous")
        self.driver.find_element(By.ID, "home-date").send_keys("2025-12-31")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

        validation = self.driver.find_element(By.ID, "home-name").get_attribute("validationMessage")
        self.save_screenshot("missing_fullname")
        self.assertIn("Please fill out this field", validation)

    def test_negative_missing_email(self):
        self.driver.find_element(By.ID, "home-name").send_keys("Calmo")
        self.driver.find_element(By.ID, "home-location").send_keys("Nairobi")
        self.driver.find_element(By.ID, "home-waste").send_keys("Hazardous")
        self.driver.find_element(By.ID, "home-date").send_keys("2025-12-31")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

        validation = self.driver.find_element(By.ID, "home-email").get_attribute("validationMessage")
        self.save_screenshot("missing_email")
        self.assertIn("Please fill out this field", validation)

    def test_negative_missing_location(self):
        self.driver.find_element(By.ID, "home-name").send_keys("Calmo")
        self.driver.find_element(By.ID, "home-email").send_keys("calmo@cleancity.com")
        self.driver.find_element(By.ID, "home-waste").send_keys("Hazardous")
        self.driver.find_element(By.ID, "home-date").send_keys("2025-12-31")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

        validation = self.driver.find_element(By.ID, "home-location").get_attribute("validationMessage")
        self.save_screenshot("missing_location")
        self.assertIn("Please select an item in the list", validation)

    def test_negative_missing_waste_type(self):
        self.driver.find_element(By.ID, "home-name").send_keys("Calmo")
        self.driver.find_element(By.ID, "home-email").send_keys("calmo@cleancity.com")
        self.driver.find_element(By.ID, "home-location").send_keys("Nairobi")
        self.driver.find_element(By.ID, "home-date").send_keys("2025-12-31")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

        validation = self.driver.find_element(By.ID, "home-waste").get_attribute("validationMessage")
        self.save_screenshot("missing_waste_type")
        self.assertIn("Please select an item in the list", validation)

    def test_negative_missing_date(self):
        self.driver.find_element(By.ID, "home-name").send_keys("Calmo")
        self.driver.find_element(By.ID, "home-email").send_keys("calmo@cleancity.com")
        self.driver.find_element(By.ID, "home-location").send_keys("Nairobi")
        self.driver.find_element(By.ID, "home-waste").send_keys("Hazardous")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

        validation = self.driver.find_element(By.ID, "home-date").get_attribute("validationMessage")
        self.save_screenshot("missing_date")
        self.assertIn("Please fill out this field", validation)

    def test_negative_invalid_email(self):
        self.driver.find_element(By.ID, "home-name").send_keys("Calmo")
        self.driver.find_element(By.ID, "home-email").send_keys("josegmail.com")
        self.driver.find_element(By.ID, "home-location").send_keys("Nairobi")
        self.driver.find_element(By.ID, "home-waste").send_keys("Hazardous")
        self.driver.find_element(By.ID, "home-date").send_keys("2025-12-31")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

        validation = self.driver.find_element(By.ID, "home-email").get_attribute("validationMessage")
        self.save_screenshot("invalid_email")
        self.assertIn("Please include an '@' in the email address", validation)

    def test_negative_invalid_domain(self):
        self.driver.find_element(By.ID, "home-name").send_keys("Calmo")
        self.driver.find_element(By.ID, "home-email").send_keys("jose@12?.com")
        self.driver.find_element(By.ID, "home-location").send_keys("Nairobi")
        self.driver.find_element(By.ID, "home-waste").send_keys("Hazardous")
        self.driver.find_element(By.ID, "home-date").send_keys("2025-12-31")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

        validation = self.driver.find_element(By.ID, "home-email").get_attribute("validationMessage")
        self.save_screenshot("invalid_domain")
        self.assertIn("should not contain the symbol", validation)

    def test_negative_invalid_date(self):
        """Negative Test: Past dates should not be allowed"""
        past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        self.driver.find_element(By.ID, "home-name").send_keys("Calmo")
        self.driver.find_element(By.ID, "home-email").send_keys("calmo@cleancity.com")
        self.driver.find_element(By.ID, "home-location").send_keys("Nairobi")
        self.driver.find_element(By.ID, "home-waste").send_keys("Hazardous")
        self.driver.find_element(By.ID, "home-date").send_keys(past_date)

        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button').click()

        validation = self.driver.find_element(By.ID, "home-date").get_attribute("validationMessage")
        self.save_screenshot("invalid_date")
        self.assertIn("Please enter a valid date", validation)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSchedulePickup)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n TEST SUMMARY ")
    print(f"Total tests run: {result.testsRun}")
    print(f"Tests passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests failed: {len(result.failures) + len(result.errors)}")

