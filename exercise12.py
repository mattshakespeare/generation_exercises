'''oop'''

#Create vehicle class without attributes
#Extend vehicle class to contain attributes for max speed and colour. Instantiate the class and call the two methods to update the attributes. Print changes.
#Extend the Vehicle class to contain methods for the below. Instantiate the class and call the two methods to update the attributes. Print the changes out.
#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and nothing else. Instantiate a Bus instance and print out the
#attributes.
#Extend the Bus class to also contain an attribute of seating_capacity . Add a method to calculate the price of a ticket. This is calculated as
#seating_capacity * 0.05 , with an extra 10% of the total of seating_capacity * 0.05 on top. Instantiate a Bus instance and print the ticket price.

class Vehicle:
    def __init__(self, max_speed, colour):
        self.max_speed = max_speed
        self.colour = colour
    
    def change_max_speed(self, new_max_speed):
        self.max_speed = new_max_speed
    
    
    def change_colour(self, new_colour):
        self.colour = new_colour

class Bus(Vehicle):
    def __init__(self, max_speed, colour, seating_capacity):
        super().__init__(max_speed, colour)
        self.seating_capacity = seating_capacity
    
    def ticket_price(self):
        ticket_price = (self.seating_capacity * 0.05) * 1.10
        return ticket_price

car = Vehicle(130, 'red')

print(car.max_speed, car.colour)

car.change_max_speed(150)
car.change_colour('Green')

print(car.max_speed, car.colour)

bus = Bus(100, 'Blue', 50)
print(bus.max_speed, bus.colour)

#Use one of the built-in Python functions to print out the underlying object type of the Bus object
print(type(bus))

# Use one of the built-in Python functions to print out if the Bus object is an instance of Vehicle .
print(isinstance(bus,Vehicle))

ticket_price = bus.ticket_price()

print(ticket_price)


