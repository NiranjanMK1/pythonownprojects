from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import  pytest


class AttachmenType:
    pass


class TestHrm:
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(5)
        status = self.driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()
        if status == True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name= "testLoginScreen",
                          attachment_type= AttachmenType.PNG)
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("Skipping test this mehtod we will implement later")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        actual_title = self.driver.title
        if actual_title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            assert False



