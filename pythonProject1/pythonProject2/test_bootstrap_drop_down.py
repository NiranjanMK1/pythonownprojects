import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
import os
def test_anj():
    ser_obj = Service(r"C:\Newfolder\chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    driver.get("https://s3.ajnaview.net/login")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@name='email']").send_keys("niranjanumk@gmail.com")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("welComeajNa91$")
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH,"//div[@role='button']//div[2]/p[2]").click()
    time.sleep(5)
    print(driver.find_element(By.XPATH,r"/html/body/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/p[3]").text)
    print(driver.find_element(By.XPATH,r"/html/body/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/table/tbody/tr[2]/td[1]").text)
    print(driver.find_element(By.XPATH,r"/html/body/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/table/tbody/tr[2]/td[2]").text)
    print(driver.find_element(By.XPATH,r"/html/body/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/table/tbody/tr[3]/td[1]").text)
    print(driver.find_element(By.XPATH,r"/html/body/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/table/tbody/tr[3]/td[2]").text)
    assert driver.find_element(By.XPATH,r"/html/body/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/p[3]").text