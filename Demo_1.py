from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://www.yatra.com/")

#mouse hover action
act =ActionChains(driver)
driver.implicitly_wait(4)
my_account = driver.find_element(By.XPATH,"//li[@id='userLoginBlock']/a")
driver.implicitly_wait(4)
my_booing = driver.find_element(By.XPATH,"//span[@class='linkPartR']/a[1]")
act.move_to_element(my_account).move_to_element(my_booing).click().perform()

time.sleep(3)
driver.quite()