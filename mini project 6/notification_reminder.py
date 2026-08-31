#drink water reminder in every 1 hr 
#plyer library to get notification in desktop 

import time
from plyer import notification

def water_reminer():
    while True:
        notification.notify(
            title = "Drink Water Reminder",
            message = "It's time to drink water! Stay hydrated.",
            timeout = 5
        )
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)

water_reminer()