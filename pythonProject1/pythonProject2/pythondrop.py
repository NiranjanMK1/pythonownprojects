from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Newfolder\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
# driver.find_element(By.XPATH, "//a[@class='btn btn-black navbar-btn']").click()
# driver.implicitly_wait(5)
# drp_element = driver.find_element(By.XPATH,"//select[@id='input-country']")
# selecting = Select(drp_element)
# selecting.select_by_visible_text("Albania")
print(driver.window_handles)
act = ActionChains()
act.move_to_element().move_to_element().click().perform()
act.context_click()
act.k