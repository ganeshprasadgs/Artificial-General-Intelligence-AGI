import tkinter as tk
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

def delay(x):
    time.sleep(x)

def log_a_call_salesforce():
    # Get Web Chrome driver
    driver = webdriver.Chrome()

    # Maximize Driver Window
    driver.maximize_window()

    # Open our targeted webpage on driver
    driver.get("https://www.salesforce.com/in/")
    delay(2)

    # Shadow element Travesing
    shadow_root0=driver.find_element('css selector',"hgf-c360nav[locale='in']").shadow_root
    shadow_root0.find_element('css selector', ".utility-icons-items.login").click()
    delay(1)
    shadow_root1=shadow_root0.find_element('css selector',"hgf-c360login[aria-haspopup='true']").shadow_root
    delay(2)

    # Get login Page
    shadow_root1.find_element('css selector',"hgf-popover:nth-child(2)>div:nth-child(2)>div:nth-child(2)>a:nth-child(2)>h4:nth-child(1)").click()
    delay(5)

    # Enter username in Login Page
    driver.find_element('xpath'," //input[@id='password']").send_keys('Saurabh@123')
    delay(2)

    #Enter Password in Login Page
    driver.find_element('xpath', "//input[@id='username']").send_keys('radkesaurabh1999-lem3@force.com')
    delay(2)

    # Try to Login
    driver.find_element('xpath',"//input[@id='Login']").click()
    delay(10)

    # After Succesfull Login gor to Leads Section
    driver.find_element('xpath',"//span[@aria-description='Show more My Leads records']").click()
    delay(10)

    # Select the desired lead to log a Call
    driver.find_element('xpath',"//a[@title='James Wheel']").click()
    delay(5)

    # Log a call
    driver.find_element('xpath',"//span[@value='LogACall']").click()


    # Enter text message nedd to send with Log
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div[1]/section/div[2]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div[1]/section/div/section/div/div/div/div/div/div[2]/div[1]/div/div/div/div/textarea"))).send_keys("Are you looking to by 100 widgets")
    delay(3)

    # Finally Send the LOG
    driver.find_element(By.XPATH,"//button[@class='slds-button slds-button--brand cuf-publisherShareButton uiButton']").click()
    delay(20)


root=tk.Tk() # use to create new chat nav
root.geometry('350x450+30+400')
def getresult(message):
    arr=message.split(" ")
    if arr[0]=="Log":
        textarea.insert('end',message)
        textarea.insert("end", "\nBot : Processing.... ")
        log_a_call_salesforce()
    else:textarea.insert("end", "\nInvalid Input")


def botReply():
    question=query.get()
    textarea.insert("end","\nYou : "+question)
    query.delete(0, "end")
    getresult(question)



root.title("Chat Bot for new prompt")
root.config(bg="aquamarine")
# Headear Logo
head=tk.PhotoImage(file='head1.png')
Insert_head=tk.Label(root,image=head)
Insert_head.config(bg='aquamarine')
Insert_head.pack()

#Frame[Conatiner for message]
Centeral_frame=tk.Frame(root)
Centeral_frame.pack()
scrol=tk.Scrollbar(Centeral_frame)
scrol.pack(side='right')

#Text area
textarea=tk.Text(Centeral_frame,font=('time new roman',10,'bold'),height=10,yscrollcommand=scrol.set)
textarea.pack(side='left')
scrol.config(command=textarea.yview)

#Enter message
query=tk.Entry(root,font=('verdana',10,'bold'),width=30)
query.pack(pady=15)

#Buttom
btn = tk.Button(root, text = 'Send !', bd = '5',command = botReply)
btn.pack()
root.mainloop() # use to hold our