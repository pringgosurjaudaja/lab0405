from customer import Customer
from Car import Car

class RentalSystem():
    def __init__(self,cars,admins):
        self._cars = cars
        self._cars_rented = 0
        self._admins= admins

    def get_cars(self):
        return self._cars
    def add_cars_rented(self):
        self._cars_rented = self._cars_rented+1
    def get_admins(self):
        return self._admins
    def set_admins(admins):
        self._admins = admins
    def bookCar(self,Car,Customer):
        #cost = Car.rental_fee
        cost = Car.rental_fee() * Customer._rental_period
        if ((Car.get_type == "Large" or Car.get_type == "Premium") and Customer.get_rental_period>7):
            cost = cost * 0.95
        Customer.set_total_cost(cost)
        print(Customer)
        print("Car Details")
        print(Car)
        print("Total Fee: $", cost)
        print("\n")
        self.add_cars_rented()
    def __str__(self):
        return "Car Rental System \nTotal Car being Rented: "+format(self._cars_rented)
