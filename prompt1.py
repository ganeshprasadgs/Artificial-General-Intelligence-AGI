import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import os
import time
from selenium.webdriver.common.by import By
import regex as re

chrome_driver_path = Service(os.path.join(os.getcwd(),r"GoogleChromePortable64\chromedriver.exe"))
chrome_binary_path = os.path.join(os.getcwd(),r"GoogleChromePortable64\App\Chrome-bin\chrome.exe")
chrome_user_data_directory = os.path.join(os.getcwd(),r"GoogleChromePortable64\Data\profile\Default")

#Define Chrome Options
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path
options.add_argument("user-data-dir=" +  chrome_user_data_directory) 
options.add_argument("--start-maximized") 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--headless")
# Set up the Chrome driver
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

# Navigate to the chat.forefront.ai website
driver.get("https://chat.forefront.ai/")


#inputs ="Find me a house in Italy that works for 4. My budget is 800k"
inputs = input("Enter a Prompt : ")

final_input = inputs + ". extract all the exact parameters from the text above like variable single value"
print('Sure')

chat_input = '//div[@role="textbox"]'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(final_input)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(Keys.RETURN)


# Wait for the response to load
time.sleep(5)

# Find the generated text and print it
WebDriverWait(driver,5000).until(EC.element_to_be_clickable((By.XPATH,"//p[@class='text-xs md:text-sm font-medium text-th-primary-light']")))
generated_text = driver.find_element(By.XPATH,"//div[@class='post-markdown flex flex-col gap-4 text-th-primary-dark text-base']")

print(generated_text.text)


para_list = generated_text.text.split('\n')
#print(para_list)

for item in para_list:
    if "location" in item.lower():
        location = item.split(": ")[1]
    elif "budget" in item.lower():
       budget = item.split(": ")[1].replace(",", "").replace("$", "")
    elif "occupancy" in item.lower() or "occupants" in item.lower() or "bedrooms" in item.lower():
        occupants = item.split(": ")[1].split()[0]


time.sleep(1)
# Close the browser
driver.quit()

#Define Chrome Options
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path
options.add_argument("user-data-dir=" +  chrome_user_data_directory) 
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
#options.add_argument("--headless")

# Set up the Chrome driver
driver = webdriver.Chrome(service=chrome_driver_path, options=options)
#Navigate to the redfin website
driver.get("https://www.redfin.com/")


chat_input = "//input[@id='search-box-input'][@placeholder='City, Address, School, Agent, ZIP']"
WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(location)
WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(Keys.RETURN)
try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="Price"]')))
except:
    locations = driver.find_elements('xpath','//div[text()="Places"]/..//div[text()="Places"]/..//div[@class="item-sub-title item-sub-title-show-sections item-sub-title-city"]')
    location_names = []
    for l in locations:
       location_names.append(l.get_attribute('innerHTML'))
    print(location_names)
    location = input("select a location : " + str(location_names) + " : ")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//button[@title ="Close"]'))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(location)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(Keys.RETURN)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="Price"]')))
    
s_url = driver.current_url
if 'filter' in s_url.lower():
    s_url = s_url.split('/filter')[0]
s_url += '/filter/max-price='+budget+',min-beds='+occupants

driver.get(s_url)
time.sleep(5)

# Close the browser
driver.quit()