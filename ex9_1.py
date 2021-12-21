class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant=restaurant_name
        self.cuisine=cuisine_type
    def desribe_restaurant(self):
        print(f"Welcome to restaurant {self.restaurant}")
        print(f"The cuisine we serve is {self.cuisine}")
    def open_restaurant(self):
        print("The restaurant is open now!")

my_restaurant=Restaurant('Home\'s flavor','Pizza')
my_restaurant.desribe_restaurant()
my_restaurant.open_restaurant()
