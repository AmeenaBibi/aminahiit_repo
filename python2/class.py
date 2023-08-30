class House:
    def __init__(self, location, bedrooms, sitting_rooms, price):
        self.location = location
        self.bedrooms = bedrooms
        self.sittingrooms = sitting_rooms
        self.price = price

    def get_location(self):
        return self.location
    def get_bedroom(self):
        return self.bedrooms
    def get_sittingrooms(self):
        return self.sittingrooms
    def get_price(self):
        return self.price
    
    def __str__(self):
        return f"""The house on the market is located in {self.location} with {self.bedrooms} bedrooms,
{self.sittingrooms} sitting rooms and costs {self.price}."""
    
my_house = House("the city", 4, 3, 100000)

print(my_house.get_location())
print(my_house.get_bedroom())
print(my_house.get_sittingrooms())
print(my_house.get_price())
print(str(my_house))