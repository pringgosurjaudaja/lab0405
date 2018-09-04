class Customer(object):

    def __init__(self, name, age, licence_num, email, rental_period, pickup_loc, drop_loc):
        self._name = name
        self._age = age
        self._licence_num= licence_num
        self._email = email
        self._rental_period = rental_period
        self._pickup_loc = pickup_loc
        self._drop_loc = drop_loc
        self._total_cost = 0


    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_licence_num(self):
        return self._licence_num

    def get_email(self):
        return self._email

    def get_rental_period(self):
        return self._rental_period

    def get_pickup_loc(self):
        return self._pickup_loc

    def get_drop_loc(self):
        return self._drop_loc

    def get_total_cost(self):
        return self._total_cost

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_licence_num(self, licence_num):
        self._licence_num = licence_num

    def set_email(self, email):
        self._email = email

    def set_rental_period(self, rental_period):
        self._rental_period = rental_period

    def set_pickup_loc(self, pickup_loc):
        self._pickup_loc = pickup_loc

    def set_drop_loc(self, drop_loc):
        self._drop_loc = drop_loc

    def set_total_cost(self, total_cost):
        self._total_cost = total_cost

    def __str__(self):
        return format(self._name) +"\nAge: "+ format(self._age)+"\nLicense Number: "+format(self._licence_num)+"\nEmail: "+ format(self._email)+"\nBooking Duration: "+format(self._rental_period)+"\nPickup Location: "+ format(self._pickup_loc)+"\nDrop Location: "+format(self._drop_loc)
