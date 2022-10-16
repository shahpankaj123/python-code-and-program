import time
from plyer import notification

while 1>0:
    notification.notify(
    title="!!TAKE REST!!",
    message="Time is Out.Please take rest for 5 min",
    timeout=5)
    time.sleep(60*60)
