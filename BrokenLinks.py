from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/")

links = driver.find_elements(By.TAG_NAME,"a")

broken_links = []
