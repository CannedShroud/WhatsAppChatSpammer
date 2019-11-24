import selenium
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import time

botDriver = webdriver.Chrome(executable_path = 'C:\chromedriver')
botDriver.get('https://web.whatsapp.com/')


continueChatBool = True
Exitbox = 'N'

while continueChatBool:
    ChatName = input('Enter the person or group name you want to target: ')
    ChatMsg = input('Enter Chat MEssage: ')
    NOCount = int(input('Enter Count: '))
    input('Enter any key to continue...')

    user = botDriver.find_element_by_xpath('//span[@title="{}"]'.format(ChatName))
    user.click()
    msg_box = botDriver.find_element_by_class_name('_3u328')

    for i in range(NOCount):
        msg_box.send_keys(ChatMsg)
        button = botDriver.find_element_by_class_name('_3M-N-')
        button.click()
        print('Working...Please Wait')
    Exitbox = input('Do you want to exit?(Y or N)')
    if Exitbox == 'Y' or Exitbox == 'y':
        continueChatBool = False
    else:
        continueChatBool = True
        