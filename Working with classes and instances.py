#  One of the things you can do is modify the attributes
# associated with a particular instance. You can modify the attributes of an
# instance directly or write methods that update attributes in specific ways.

# Lets use example of a car class:

class Car():
 """A simple attempt to represent a car."""
 def __init__(self, make, model, year):
     """Initialize attributes to describe a car."""
     self.make = make
     self.model = model
     self.year = year

 def get_descriptive_name(self):
     """Return a neatly formatted descriptive name."""
     long_name = str(self.year) + ' ' + self.make + ' ' + self.model
     return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Every attribute in a class needs an initial value, even if that value is 0 or an
# empty string.
# In some cases, such as when setting a default value, it makes
# sense to specify this initial value in the body of the __init__() method; if
# you do this for an attribute, you don’t have to include a parameter for that
# attribute.

#Let’s add an attribute called odometer_reading that always starts with a
#value of 0. We’ll also add a method read_odometer() that helps us read each
#car’s odometer:
def __init__(self, make, model, year):
 """Initialize attributes to describe a car."""
 self.make = make
 self.model = model
 self.year = year
 self.odometer_reading = 0

 def read_odometer(self):
     """Print a statement showing the car's mileage."""
     print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car.read_odometer()

#This time when Python calls the __init__() method to create a new
#instance, it stores the make, model, and year values as attributes like
#it did in the previous example. Then Python creates a new attribute
#called odometer_reading and sets its initial value to 0

# MODIFYING ATTRIBUTE VALUES
# you can either: (1) change the value directly through an instance,
# (2) set the value through a method
# (3) increment the value (add a certain amount to it) through a method

# (1):
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# This line tells Python to take the instance
# my_new_car, find the attribute odometer_reading associated with it, and set the
# value of that attribute to 23

# (2):
#  helpful to have methods that update certain attributes for you.
# Instead of accessing the attribute directly, you pass the new value to a
# method that handles the updating internally

    def update_odometer(self, mileage):
     """Set the odometer reading to the given value."""
     self.odometer_reading = mileage
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# This method takes in a mileage value and stores it in self.odometer_reading.
# We call update_odometer() and give it 23 as an argument (corresponding
# to the mileage parameter in the method definition). It sets the odometer
# reading to 23, and read_odometer() prints the reading.

def update_odometer(self, mileage):
 """
 Set the odometer reading to the given value.
 Reject the change if it attempts to roll the odometer back.
 """
 if mileage >= self.odometer_reading:
    self.odometer_reading = mileage
 else:
    print("You can't roll back an odometer!")
# We can extend the method update_odometer() to do additional work
# every time the odometer reading is modified. Let’s add a little logic to
# make sure no one tries to roll back the odometer reading above.

# (3):
    def increment_odometer(self, miles):
     """Add the given amount to the odometer reading."""
     self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# We created a new method increment_odometer() which takes in a number of miles,
# and adds this value to self.odometer_reading.
# Then we created  a used car,
# my_used_car. We set its odometer to 23,500 by calling update_odometer() and
# passing it at 23500
# On the last lines we call increment_odometer() and pass it 100 to add
# the 100 miles that we drove between buying the car and registering it