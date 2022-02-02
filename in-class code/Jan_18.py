class Person:
    
    # the ="" means full_name is optional if not variable is sent in.
    # I could have had __init__(self, full_name) so full_name was NOT optional. It was required.
    def __init__(self, full_name=""):
        self.full_name = full_name
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def get_restaurants(self):
        return self.restaurants

    def get_favorite_restaurant(self):
        best = -1
        favorite = Restaurant()



class Restaurant:

    def __init__(self, name="", cuisine="", price=0, rating=0):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating

    def __str__(self):
        return self.name

jim = Person()
print(jim)

# don't do this, but there will NOT be an error but you can add an attribute.
# That is assuming full_name wasn't in the constructor. I added to this code after I commented here.
jim.full_name = "Jim Johnson"
print(jim.full_name)

heather = Person()
print(heather)

george = Person("George Gershwin")
print(george.full_name)





