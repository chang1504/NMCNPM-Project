import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestLoginIntegration(unittest.TestCase):
    def setUp(self):
        options = Options()
        # Nếu chạy trên WSL hoặc CI/CD, nên bật headless để tránh lỗi GUI
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8000/lab04/index.html")  

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("valid_user")
        driver.find_element(By.ID, "password").send_keys("valid_pass")
        driver.find_element(By.ID, "login-btn").click()

        self.assertIn("dashboard.html", driver.current_url)

    def test_login_fail(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("wrong_user")
        driver.find_element(By.ID, "password").send_keys("wrong_pass")
        driver.find_element(By.ID, "login-btn").click()

        error = driver.find_element(By.ID, "message").text
        self.assertIn("Invalid", error)

    def test_login_empty_input(self):
        driver = self.driver
        driver.find_element(By.ID, "login-btn").click()

        error = driver.find_element(By.ID, "message").text
        self.assertIn("Username/password required", error)


if __name__ == "__main__":
    unittest.main()