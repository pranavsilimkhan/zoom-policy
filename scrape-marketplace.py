from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def reject_cookies():
    element = driver.find_element(By.XPATH, '''//*[@id="onetrust-reject-all-handler"]''')
    element.click()

def wait_and_find(xpath):
    return WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
    )

os.environ["PATH"] += ":/Users/pranavsilimkhan/gecko"

driver = webdriver.Firefox()

driver.get("https://marketplace.zoom.us/apps?category=analytics")

reject_cookies()

close = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div/div[1]/span"))
)
close.click()

parent_element = driver.find_element(By.XPATH, '''//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]''')
child_elements = parent_element.find_elements(By.XPATH, "*")

child_elements = parent_element.find_elements(By.XPATH, "*")
# xpath = driver.execute_script("return arguments[0].xpath;", child_elements[2])
# print(xpath)
window_handles = driver.window_handles
for child_element in child_elements:
    child_elements[1].click()

    title_element = wait_and_find('''//*[@id="TitleBox"]''')
    app_name = title_element.text

    scope = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/main/section/aside/div/a[4]"))
    )

    scope.click()

    privacy_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/main/section/div/div/div/div/div[5]/div/div/div/div/a[2]"))
    )

    privacy_button.click()
    time.sleep(2)
    html_content = driver.page_source

    with open(f"./data/analytics/{app_name}.txt", "w") as f:
        f.write(html_content)
    driver.back()
    driver.back()
    time.sleep(2)
# driver.close()