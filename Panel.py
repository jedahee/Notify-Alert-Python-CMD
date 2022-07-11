# Author: jedahee 
# Details: This script manage the notificatiosn created
# Last update: 07/07/2022

# ---- Internal modules ----
from Notify import Notify
from Validations import Validations

# ---- External modules ----
import sys
import numpy as np
import datetime

# ---- Functions ----

# Function for print the menu and options
def print_menu():
    print(""" 
 /$$   /$$             /$$     /$$  /$$$$$$            /$$$$$$  /$$                       /$$    
| $$$ | $$            | $$    |__/ /$$__  $$          /$$__  $$| $$                      | $$    
| $$$$| $$  /$$$$$$  /$$$$$$   /$$| $$  \__//$$   /$$| $$  \ $$| $$  /$$$$$$   /$$$$$$  /$$$$$$  
| $$ $$ $$ /$$__  $$|_  $$_/  | $$| $$$$   | $$  | $$| $$$$$$$$| $$ /$$__  $$ /$$__  $$|_  $$_/  
| $$  $$$$| $$  \ $$  | $$    | $$| $$_/   | $$  | $$| $$__  $$| $$| $$$$$$$$| $$  \__/  | $$    
| $$\  $$$| $$  | $$  | $$ /$$| $$| $$     | $$  | $$| $$  | $$| $$| $$_____/| $$        | $$ /$$
| $$ \  $$|  $$$$$$/  |  $$$$/| $$| $$     |  $$$$$$$| $$  | $$| $$|  $$$$$$$| $$        |  $$$$/
|__/  \__/ \______/    \___/  |__/|__/      \____  $$|__/  |__/|__/ \_______/|__/         \___/  
                                            /$$  | $$                                            
                                           |  $$$$$$/                                            
                                            \______/ 

 /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/

[1] => Ver notificaciones
[2] => Añadir notificación
[3] => Modificar notificación
[4] => Eliminar notificación
[{}] => Salir y guardar
    """.format(OPC_EXIT))

# Function that create a notification object and add it to notification_list
def addNotification(notifications_list):
        notify = Notify()
        notify.title = input('Titulo >> ')
        notify.message = input('Descripción >> ')
        notify.timeout = utils.controlNumber(text='Duración >> ', min_range=0, max_range=10000)
        notify.date = utils.controlDate(text='Fecha (dd/mm/aaaa) >> ')
        notify.time = utils.controlTime(text='Hora (hh:mm) >> ')
        notify.repeat = utils.controlNumber(text='Num. Repeticiones (0 por defecto) >> ', min_range=0, max_range=40)
        
        if notify.repeat > 0:
            notify.difference = utils.controlNumber(text='Tiempo (en minutos) entre repeticiones >> ', min_range=0, max_range=60)
            notifications_list.append(notify)

            for i in range(notify.repeat):
                notify_copy = Notify()
                notify_copy.title = notify.title
                notify_copy.message = notify.message
                notify_copy.timeout = notify.timeout
                notify_copy.date = notify.date
                notify_copy.repeat = notify.repeat
                notify_copy.difference = notify.difference

                if i == 0:
                    notify_copy.time = notify.time
                    
                elif i > 0:
                    notify_copy.time = last_time
                
                day, month, year = notify_copy.date.split('/')
                hour, minutes = notify_copy.time.split(':')
                date = datetime.datetime(int(year), int(month), int(day))
                fullDate = datetime.datetime(date.year,date.month,date.day, int(hour), int(minutes),0)
                fullDate_Diff = fullDate + datetime.timedelta(minutes=notify_copy.difference)
                                
                notify_copy.date = str(fullDate_Diff.day) + "/" + str(fullDate_Diff.month) + "/" + str(fullDate_Diff.year)
                notify_copy.time = str(fullDate_Diff.hour).rjust(2, '0') + ":" + str(fullDate_Diff.minute).rjust(2, '0')
                
                last_time = notify_copy.time
                
                notifications_list.append(notify_copy)

        else:
            notify.difference = 0
            notifications_list.append(notify)
        
        return notifications_list

# This function delete the notifications that are same
def delDuplicate_full():
    notifications_list_copy = []
    
    for nt in notifications_list:
        can_append = True
        
        if len(notifications_list_copy) == 0:
            notifications_list_copy.append(nt)
        else:
            for nt_copy in notifications_list_copy:
                if nt_copy.title == nt.title and nt_copy.message == nt.message:
                    can_append = False
            
            if can_append is True:
                notifications_list_copy.append(nt)
    
    return notifications_list_copy

# This function delete the notifications that are same that notification parameter
def delDuplicate(nt):
    notifications_list_copy = []

    for notify in  notifications_list:
        can_append = True

        if notify.title == nt.title and notify.message == nt.message:
            can_append = False
    
        if can_append is True:
            notifications_list_copy.append(nt)

    return notifications_list_copy


# Function that show all notifications
def showNotifications():
    notifications_list_copy = delDuplicate_full()

    if len(notifications_list) > 0:
        for notify in notifications_list_copy:
            print(notify)
    else:
        print('\n[ADVERTENCIA] No existen notificaciones [ADVERTENCIA]\n')

# Function that show all notifications in a short way
def showNotifications_short():
    notifications_list_copy = delDuplicate_full()
    i = 0

    if len(notifications_list) > 0:
        if i == 0:
            print('')

        for notify in notifications_list_copy:
            print("    [{}] => {}".format(i, notify.title))
            i+=1
        
        print('')

    else:
        print('\n[ADVERTENCIA] No existen notificaciones [ADVERTENCIA]\n')


# Function that delete a notification object and return it
def delNotify(index):
    i = 0
    nt_del = notifications_list.pop(index)

    while i < len(notifications_list):
        if nt_del.title == notifications_list[i].title and nt_del.message == notifications_list[i].message:
            notifications_list.pop(i)
        else:
            i+=1
            
    return nt_del

# Function that edit a notification
def modNotify(index, notifications_list):
    print("\n-- MODIFICANDO NOTIFICACIÓN --\n")
    nt = notifications_list[index]
    notifications_list = delDuplicate(nt)
    notifications_list = addNotification(notifications_list)

    return notifications_list, nt

# Function that execute the option selected
def execOption(opc, notifications_list):
    if opc == 1:
        showNotifications()
    
    elif opc == 2:
        notifications_list = addNotification(notifications_list)
    
    elif opc == 3:
        showNotifications_short()

        if len(notifications_list) > 0:
            nt_mod = utils.controlNumber("Select index >> ", 0, len(notifications_list)-1)
            notifications_list, nt = modNotify(nt_mod, notifications_list)
            print("\n[MODIFICADO] " + nt.title + " [MODIFICADO]\n")
            

    elif opc == 4:
        showNotifications_short()

        if len(notifications_list) > 0:
            nt_del = utils.controlNumber("Select index >> ", 0, len(notifications_list)-1)
            print("\n[ELIMINADO] " + delNotify(nt_del).title + " [ELIMINADO]\n")
    
    elif opc == OPC_EXIT:
        print("\n################\n Hasta luego! :) \n################")
        exit()
    
    return notifications_list

# Function that exit the program
def exit():
    saveChanges()
    sys.exit()

# Function that save notifications_list in a file
def saveChanges():
    np.save('./data/notifications.npy', notifications_list)

# Function that load notifications_list from a file
def loadObjects():
    try:
        np.load('./data/notifications.npy', allow_pickle=True)
    except FileNotFoundError:
        return np.array([])

    return np.load('./data/notifications.npy', allow_pickle=True)
    

# ---- Main ----
                                                                                   
if __name__ == '__main__':
    # -- Variables --
    opc = ''
    notifications_list = []
    last_time = ''
    utils = Validations()
    OPC_EXIT = 5
    
    # -- Calls --
    notifications_list = loadObjects()
    notifications_list = notifications_list.tolist()

    # -- Run script --
    while (opc != OPC_EXIT):
        print_menu()
        opc = utils.controlNumber('Select number >> ', 1, 5)
        notifications_list = execOption(opc, notifications_list)