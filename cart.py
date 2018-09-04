from customer import Customer

class Cart:

    def __init__(self, car_type, total_cost):
        self._car_type = car_type
        self._total_cost = total_cost
        
    def get_car_type(self):
        return self._car_type
        
    def get_total_cost(self):
        return self._total_cost
        
    def set_car_type(self, car_type):
        self._car_type = car_type
        
    def set_total_cost(self, total_cost):
        self._total_cost = Customer._rental_period * Car._rental_fee
