import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/")

links = driver.find_elements(By.TAG_NAME,"a")

broken_links = []

for link in links:
    url = link.get_attribute("href")
    if url == None or url == " ":
        continue
    try:
        response = requests.head(url,timeout= 10)
        if response.status_code >= 400:
            print(f"Broken link {url} : {response.status_code}")
            broken_links.append(url)
    except requests.exceptions.RequestException as e:
        print(f" Error with link {url}: {e}")
        broken_links.append(url)

print(f"Broken links : {len(broken_links)}")
