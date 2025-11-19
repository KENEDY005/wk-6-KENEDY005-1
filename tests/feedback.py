import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Screenshot directory – same location as other tests
SCREENSHOT_DIR = "screenshots"

class TestFeedbackSubmission(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 5)

    def take_screenshot(self, name):
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        filename = os.path.join(SCREENSHOT_DIR, f"{name}_{time.strftime('%Y%m%d-%H%M%S')}.png")
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")

    def login_user(self):
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[8]'))
        )
        login_btn.click()

        email = self.wait.until(EC.presence_of_element_located((By.ID, "login-email")))
        email.send_keys("calmo@cleancity.com")

        password = self.wait.until(EC.presence_of_element_located((By.ID, "login-password")))
        password.send_keys("123")

        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit_btn.click()
        time.sleep(2)

    def open_feedback_page(self):
        feedback_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/nav/div/div/a[7]'))
        )
        feedback_btn.click()
        time.sleep(1)

    # POSITIVE TEST

    def test_positive_feedback_submission(self):
        """Submit feedback with correct details."""
        self.login_user()
        self.open_feedback_page()

        self.driver.find_element(By.ID, "feedback-request-id").send_keys("R001")
        self.driver.find_element(By.ID, "feedback-text").send_keys(
            "Kindly keep time and return my previous bin."
        )

        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit_btn.click()

        success_msg = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Thank you for your feedback')]"))
        )

        self.take_screenshot("feedback_positive")
        self.assertIn("Thank you for your feedback", success_msg.text)

    # NEGATIVE TESTS

    def test_negative_missing_request_id(self):
        """Missing request ID should show validation message."""
        self.login_user()
        self.open_feedback_page()

        text_field = self.driver.find_element(By.ID, "feedback-text")
        text_field.send_keys("Missing request ID test.")

        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button')
        submit_btn.click()

        request_field = self.driver.find_element(By.ID, "feedback-request-id")
        validation_msg = request_field.get_attribute("validationMessage")

        self.take_screenshot("feedback_missing_request_id")
        self.assertIn("Please fill out this field", validation_msg)

    def test_negative_missing_feedback_text(self):
        """Missing feedback text should show validation message."""
        self.login_user()
        self.open_feedback_page()

        request_id = self.driver.find_element(By.ID, "feedback-request-id")
        request_id.send_keys("R001")

        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/form/button')
        submit_btn.click()

        feedback_field = self.driver.find_element(By.ID, "feedback-text")
        validation_msg = feedback_field.get_attribute("validationMessage")

        self.take_screenshot("feedback_missing_text")
        self.assertIn("Please fill out this field", validation_msg)

    def test_negative_invalid_request_id(self):
        """Invalid request ID such as T01@ should trigger custom validation message."""
        self.login_user()
        self.open_feedback_page()

        request_id = self.wait.until(
            EC.presence_of_element_located((By.ID, "feedback-request-id"))
        )
        request_id.send_keys("T01@")  # INVALID format

        feedback_text = self.driver.find_element(By.ID, "feedback-text")
        feedback_text.send_keys("Testing invalid ID format.")

        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/form/button'))
        )
        submit_btn.click()

        # Custom error message displayed on page
        error_msg = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Invalid request ID')]")
            )
        )

        self.take_screenshot("feedback_invalid_request_id_custom")
        self.assertIn("Invalid request ID", error_msg.text)

    def tearDown(self):
        self.driver.quit()


#  RUN TESTS + SUMMARY 
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFeedbackSubmission)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n TEST SUMMARY ")
    print(f"Total tests run: {result.testsRun}")
    print(f"Tests passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests failed: {len(result.failures) + len(result.errors)}")
