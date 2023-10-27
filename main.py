# Author: jedahee 
# Details: This script listen the date and time to execute the notification 
# Last update: 07/07/2022


# ---- Internal modules ----
from Panel import loadObjects

# ---- External modules ----
from plyer import notification
import numpy as np
import time
import datetime

# ---- Variables ----
notifications_list = loadObjects()
notifications_list = notifications_list.tolist()
i = 0
notification_deleted = None
PLAY_NOTIFICATION = 'start'

# ---- Functions ----
def checkDateNotification(notify):
    day, month, year = notify.date.split('/')
    hour, minutes = notify.time.split(':')

    date = datetime.datetime(int(year), int(month), int(day))
    today = datetime.datetime.today()

    if int(day) == int(today.day) and int(month) == int(today.month) and int(year) == int(today.year):
        if (int(hour) < int(today.hour)):
            return False
        elif (int(hour) == int(today.hour)):
            if (int(minutes) < int(today.minute)):
                return False
            elif (int(minutes) == int(today.minute)):
                return PLAY_NOTIFICATION

    elif (date < today):
        return False

    return True

# ---- Main ----
while len(notifications_list) > 0:
    
    for nt in notifications_list:
        if (not checkDateNotification(nt)):
            while (len(notifications_list)-1 < i):
                i-=1

            notification_deleted = notifications_list.pop(i)
            np.save('./data/notifications.npy', notifications_list)
            print("[ELIMINADO] SE HA ELIMINADO LA NOTIFICACIÓN {} [ELIMINADO]".format(notification_deleted.title.upper()))
        
        elif (checkDateNotification(nt) == PLAY_NOTIFICATION):
            notification.notify(title=nt.title,
                                message=nt.message,
                                app_icon='',
                                timeout=nt.timeout,
                                toast=False)
            i+=1
        else:
            i+=1

            
    time.sleep(60)
    print("--")


else:
    print("[ADVERTENCIA] NO HAY NOTIFICACIONES CREADAS [ADVERTENCIA]")
