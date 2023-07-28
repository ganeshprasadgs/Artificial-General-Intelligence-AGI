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
import re
import datetime

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

inputs = input("Enter a Prompt : ")

print('According to wikipedia .....')
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

# Navigate to the chat.forefront.ai website
driver.get("https://chat.forefront.ai/")

#inputs = "How old is the actor in Mace Windu who played Star Wars"
final_input = inputs + " according to https://www.wikipedia.org/ wanted only birth year no need of age. use only keywords 'alive' or 'dead' accordingly"
#print(final_input)

chat_input = '//div[@role="textbox"]'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(final_input)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,chat_input))).send_keys(Keys.RETURN)


# Wait for the response to load
time.sleep(5)
WebDriverWait(driver,5000).until(EC.element_to_be_clickable((By.XPATH,"//p[@class='text-xs md:text-sm font-medium text-th-primary-light']")))
generated_text = driver.find_element(By.XPATH,"//div[@class='post-markdown flex flex-col gap-4 text-th-primary-dark text-base']")

# WebDriverWait(driver,5000).until(EC.element_to_be_clickable((By.XPATH,"//p[@class='text-xs md:text-sm font-medium text-th-primary-light']")))

print(generated_text.text)

if "alive" in generated_text.text.lower():
    birth_year = re.search(r'\b\d{4}\b',generated_text.text).group()
    #print(birth_year)

    if birth_year:
        birth_year = int(birth_year)
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        print("The current age is:", age)
    else:
        print("No birth year found.")
elif "dead" in generated_text.text.lower():
    print("Person is Deceased according to wikipedia")

# Close the browser
driver.quit()