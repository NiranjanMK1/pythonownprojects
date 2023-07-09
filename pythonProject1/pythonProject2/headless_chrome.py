from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service_obj = Service(r"C:\Newfolder\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj,options=chrome_options)
    return driver

driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
print(driver.title)
assert driver.title == "nopCommerce demo stor"