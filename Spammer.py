# Import Selenium and webdriver
import selenium
from selenium import webdriver

# Declare Bot
botDriver = webdriver.Chrome(executable_path = 'C:\chromedriver')
botDriver.get('https://web.whatsapp.com/')

# Some needed variables
continueChatBool = True
Exitbox = 'N'

# Loop for continuity of program
while continueChatBool:
    ChatName = input('Enter the person or group name you want to target: ') # Chat name input
    ChatMsg = input('Enter Chat MEssage: ') # Chat message input
    NOCount = int(input('Enter Count: ')) # Number of times spam input
    input('Enter any key to continue...') # Any input to continue

    user = botDriver.find_element_by_xpath('//span[@title="{}"]'.format(ChatName)) # Guiding bot to victim chat/group
    user.click()
    msg_box = botDriver.find_element_by_class_name('_3u328')

# Spammer
    for i in range(NOCount):
        msg_box.send_keys(ChatMsg)
        button = botDriver.find_element_by_class_name('_3M-N-')
        button.click()
        print('Working...Please Wait')
    Exitbox = input('Do you want to exit?(Y or N)')
    
    # Simple code for a continuity option
    if Exitbox == 'Y' or Exitbox == 'y':
        continueChatBool = False
    else:
        continueChatBool = True
        
