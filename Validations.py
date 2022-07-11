# Author: jedahee 
# Details: This script validate inputs for a corrert answer 
# Last update: 07/07/2022

# ---- External modules ----
import datetime

class Validations:
    
    # ---- Contructor ----
    def __init__(self):
        pass
    
    # ---- Methods ----

    # Method that control input that must be a number 
    def controlNumber(self, text=">>", min_range=-1, max_range=-1, opc=-1):
        op = opc
        is_number = False

        if (min_range==-1 or max_range==-1):
            while (not is_number):
                try:
                    op = int(input(text))
                    is_number = True

                    if (min_range != -1 or max_range != -1) and (op < min_range or op > max_range):
                        print('[ERROR] El rango de números válidos es entre {} y {} [ERROR]\n'.format(min_range, max_range))

                except ValueError:
                    print('[ERROR] TIenes que introducir un número [ERROR]\n')
                    is_number = False  

            return op
        else:
            while (op < min_range or op > max_range):
                try:
                    op = int(input(text))

                    if (op < min_range or op > max_range):
                        print('[ERROR] El rango de números válidos es entre {} y {} [ERROR]\n'.format(min_range, max_range))

                except ValueError:
                    print('[ERROR] TIenes que introducir un número [ERROR]\n')

            return op

    # Method that control input that must be a correct date 
    def controlDate(self, text=">>"):
        is_valid_date = False

        while (not is_valid_date):
            try:
                opc = input(text)
                is_valid_date = True
                day, month, year = opc.split('/')        
                date = datetime.datetime(int(year), int(month), int(day))
                today = datetime.datetime.today()

                if int(day) == int(today.day) and int(month) == int(today.month) and int(year) == int(today.year):
                    return opc
                elif (date < today):
                    print('[ERROR] La fecha no puede ser inferior a la fecha de hoy [ERROR]\n')
                    is_valid_date = False

            except ValueError:
                print('[ERROR] La fecha debe ser válida [ERROR]\n')
                is_valid_date = False

        return opc

    # Method that control input that must be a correct time
    def controlTime(self, text=">>"):
        is_valid_time = False

        while (not is_valid_time):
            try:
                opc = input(text)
                is_valid_time = True
                hour, min= opc.split(':')        
                datetime.time(int(hour), int(min), 0)
            except ValueError:
                print('[ERROR] La hora debe ser válida [ERROR]\n')
                is_valid_time = False

        return opc