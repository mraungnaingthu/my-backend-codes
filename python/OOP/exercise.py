from pandas.core.window.doc import kwargs_scipy


class House:
    num_rooms = 5
    bathrooms = 2

    def costEvaluation(self, rate):
        return rate * self.num_rooms * self.bathrooms

house = House()
print(house.num_rooms)
print(House.num_rooms)
print(house.costEvaluation(2000))

house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

House.num_rooms = 10
print(house.num_rooms)
print(House.num_rooms)