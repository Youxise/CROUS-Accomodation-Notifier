import re
import time
import random
from selenium import webdriver
import pygame
from twilio.rest import Client

# Twilio API credentials
account_sid = 'your_sid'
auth_token = 'your_token'
client = Client(account_sid, auth_token)

url = 'City_Selected_URL'

# Selenium chrome settings
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)
browser.implicitly_wait(random.randint(5, 20))  # seconds




# Initialize pygame mixer
pygame.mixer.init()

def test_chargement(url):

    browser.get(url)
    page_source = browser.page_source

    # Regex detecting if there are any accomodation
    match1 = re.search(r'(\d+)\s+logement trouvé', page_source)
    match2 = re.search(r'(\d+)\s+logements trouvés', page_source)
    
    if match1 or match2:

        print('\t FOUND !')
        # Alarm
        pygame.mixer.music.load('alert_sound.mp3')  # Load the sound
        pygame.mixer.music.play(-1)  # Play the sound indefinitely
        # Send SMS to my phone
        message = client.messages.create(    from_='+12085825656',    body=f'Logement CROUS is available !',    to='your_number'    )
        print(message.sid)
        # Call
        # not done yet

        while True:
            time.sleep(1)  # Keep the script running

    else:
        time.sleep(20)
        print('\t Nothing...')
        test_chargement(url)


test_chargement(url)