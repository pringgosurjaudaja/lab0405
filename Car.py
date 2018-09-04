#from abc import ABCMeta, abstractmethod

class Car(object):
    def __init__(self,registration,year,model,make,type):
        self._model = model
        self._registration = registration
        self._year = year
        self._make = make
        self._type = type

    def get_model(self):
        return self._model
    def set_model(model):
        self._model = model
    def get_registration(self):
        return self._registration
    def set_registration(registration):
        self._registration = registration
    def get_year(self):
        return self._year
    def set_year(year):
        self._year = year
    def get_make(self):
        return self._make
    def set_make(make):
        self._make = make
    def get_type(self):
        return self._type
    def set_type(type):
        self._type = type
    def __str__(self):
        return "Type: "+format(self._type) +"\n"+"Make: "+format(self._make)+"\n"+"Model: "+format(self._model)+"\n"+"Year: "+format(self._year)+"\n"+"Registration: "+format(self._registration)+"\n"
    #@abstractmethod
    def rental_fee(self):
        if(self._type=="Small"):
            return 70
        if(self._type=="Medium"):
            return 100
        if(self._type=="Large"):
            return 120
        if(self._type=="Premium"):
            return 150
