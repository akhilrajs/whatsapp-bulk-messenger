# Whataspp Bulk Messenger
# @author - akhilrajs
# https://github.com/akhilrajs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote  
from time import sleep
import message
import get_numbers


css_selector = "._2x4bz > div:nth-child(2)"
driver = webdriver.Firefox()

msg = message.msg
msg = quote(msg)
phone = get_numbers.phone

driver.get("https://web.whatsapp.com")  
sleep(2)
failed_list = []
for index, number in enumerate(phone, 1):
    url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + msg
    driver.get(url)
    TRIES = 30

    sleep(3)  
    for i in range(TRIES):
        try:
            driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
            driver.execute_script("window.onbeforeunload = function() {};")
            print (f'Sent to {index} : {number}')
            break
        except:
            print("not yet")
            sleep(1)
        
    else:
        failed_list.append(number)
    
print ("Done")

if (len(failed_list)==0):
    print (f'Message successfully sent to all {len(phone)} numbers.')
else:
    print (f'Message sent to all numbers EXCEPT:')
    for number in failed_list:
        print (number)
    
driver.quit()