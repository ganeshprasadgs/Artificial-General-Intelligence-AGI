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


#inputs = 'Add Ganesh Prasad at Amazon as the new lead'
inputs = input("Enter a Prompt : ")

final_input = inputs + "in (Salesforce: https://www.salesforce.com/in/).  provide all exact parameters list first name, last name, role and company from the text above like single variable value only"
print('Sure')

driver.get("https://chat.forefront.ai/")
while True:
    # Navigate to the chat.forefront.ai website
    


    chat_input = '//div[@role="textbox"]'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(final_input)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(Keys.RETURN)


    # Wait for the response to load
    time.sleep(5)

    # Find the generated text and print it
    WebDriverWait(driver,5000).until(EC.element_to_be_clickable((By.XPATH,"//p[@class='text-xs md:text-sm font-medium text-th-primary-light']")))
    generated_text = driver.find_element(By.XPATH,"//div[@class='post-markdown flex flex-col gap-4 text-th-primary-dark text-base']")

    # WebDriverWait(driver,5000).until(EC.element_to_be_clickable((By.XPATH,"//p[@class='text-xs md:text-sm font-medium text-th-primary-light']")))
    if '\"' in generated_text.text:
        driver.get("https://chat.forefront.ai/")
    else:
        break


print(generated_text.text)

# Extracting first name
first_name = re.findall(r'First Name:\s*(\w+)', generated_text.text)[0]

# Extracting last name
last_name = re.findall(r'Last Name:\s*(\w+)', generated_text.text)[0]

# Extracting role
role = re.findall(r'Role:\s*(\w+)', generated_text.text)[0]

# Extracting company
company = re.findall(r'Company:\s*(\w+)', generated_text.text)[0]
#print("First Name:", first_name)
#print("Last Name:", last_name)
#print("Role:", role)
#print("Company:", company)


driver.quit()
time.sleep(1)
#Define Chrome Options
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path
options.add_argument("user-data-dir=" +  chrome_user_data_directory) 
options.add_argument("--start-maximized") 
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_argument("--headless")
# Set up the Chrome driver
driver = webdriver.Chrome(service=chrome_driver_path, options=options)


driver.get("https://login.salesforce.com/?locale=in")

username = 'gs.ganesh2k2-zqcm@force.com'
passwords = 'GP@200210'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@id = "username"]'))).send_keys(username)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@id = "password"]'))).send_keys(passwords)


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@id = "Login"]'))).click()

#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//a[@title = "Leads"]')))

driver.get("https://customcode.lightning.force.com/lightning/o/Lead/new?count=2&nooverride=1&useRecordTypeCheck=1&navigationLocation=LIST_VIEW&backgroundContext=%2Flightning%2Fpage%2Fhome")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@placeholder ="First Name"]'))).send_keys(first_name)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@placeholder ="Last Name"]'))).send_keys(last_name)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@name ="Title"]'))).send_keys(role)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@name ="Company"]'))).send_keys(company)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[@name = "SaveEdit"]'))).click()
time.sleep(10)



# Close the browser
driver.quit()