from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver=webdriver.Chrome()


baseurl="https://web.whatsapp.com/"

driver.get(baseurl) 
time.sleep(10)

# Open the file in read mode
with open('contact.csv', newline='') as file:
    readContact = csv.reader(file)
    for phone, msg in readContact:
        phonenum = phone
        message = msg

        sameTab=(baseurl+"/send?phone="+str(phonenum))
        driver.get(sameTab)

        time.sleep(8)
        content=driver.switch_to.active_element
        content.send_keys(message)
        content.send_keys(Keys.RETURN)
        time.sleep(8)