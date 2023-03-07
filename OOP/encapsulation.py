class Cinema:
    def __init__(self, rooms, popcorn, owner):
        # public member
        self.rooms = rooms
        # protected member
        self._popcorn = popcorn
        # private member
        self.__owner = owner

    def getOwner(self):
        print(self.__owner)

show = Cinema('five rooms', 2000, 'Amina')
show.getOwner()
print(show._popcorn)
print(show.rooms)
