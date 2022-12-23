class Restaurant(): 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restauracja nazywa się "{self.restaurant_name}"')
        print(f'Restauracja serwuje kuchnię {self.cuisine_type}')

    def open_restaurant(self):
        print("Restauracja otwarta jest od pon. do pt. w godzinach 7:00 - 20:00")

#kuciak = Restaurant('w dupie na oto','chińską')
#kuciak.describe_restaurant()
#kuciak.open_restaurant()
