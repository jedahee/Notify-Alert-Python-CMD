# Author: jedahee 
# Details: This class is the notification 
# Last update: 07/07/2022

# ---- External modules ----
from datetime import date

class Notify:

    # ---- Contructor ----
    def __init__(self):
        self._title = ''
        self._message = ''
        self._timeout = 10
        self._date = date.today()
        self._time = "16:00"
        self._repeat = 0
        self._difference = 0

    # ---- Str method ----
    def __str__(self):
        return """
               +-------------------------------------------------------------+
               |                         NOTIFICACIÓN                        |
               +-------------------------------------------------------------+
               | Titulo: {}
               | Desc.: {}
               | Duración: {} 
               | Fecha: {}
               | Hora: {}
               | Num. Rep.: {} 
               | Entre Rep.: {}
               +-------------------------------------------------------------+
               
               
               """.format(self.title, self.message, self.timeout, self.date, self.time, self.repeat, self.difference)

    # ---- Getters ----
    
    @property
    def title(self):
        return self._title
    
    @property
    def message(self):
        return self._message
    
    @property
    def timeout(self):
        return self._timeout
    
    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def repeat(self):
        return self._repeat

    @property
    def difference(self):
        return self._difference
    
    # ---- Setters ----
    
    @title.setter
    def title(self, title):
        self._title = title
    
    @message.setter
    def message(self, message):
        self._message = message

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout

    @date.setter
    def date(self, date):
        self._date = date

    @time.setter
    def time(self, time):
        self._time = time

    @repeat.setter
    def repeat(self, repeat):
        self._repeat = repeat

    @difference.setter
    def difference(self, difference):
        self._difference = difference