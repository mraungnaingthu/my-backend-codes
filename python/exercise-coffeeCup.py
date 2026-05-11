# cup, water is boiled or not ?
# if boiled, then pour into cup, if not, boil water first and wait, then pour into cup
# also need milk and sugar, if customer want pour them and give to customer
# if customer no need milk and sugar, just pour boil water and coffee into cup and give to customer

class CoffeeCup:
    def __init__(self, water_boiled=False, milk=False, sugar=False):
        self.water_boiled = water_boiled
        self.milk = milk
        self.sugar = sugar

    def boil_water(self):
        if not self.water_boiled:
            print("Boiling water...")
            self.water_boiled = True
        else:
            print("Water is already boiled.")

    def pour_into_cup(self, milk_status, sugar_status):
        if self.water_boiled and (milk_status == "yes" or sugar_status == "yes"):
            print("Pouring water into the cup and also...")
            self.add_milk()
            self.add_sugar()
            print("Added ingredients altogether with the water. and now ready for the coffee")
        else:
            print("Pouring water into the cup without any additional ingredients. and now ready for the coffee")

    def add_milk(self):
        if self.milk:
            print("Adding milk to the coffee...")
        else:
            print("No milk needed.")

    def add_sugar(self):
        if self.sugar:
            print("Adding sugar to the coffee...")
        else:
            print("No sugar needed.")

    def make_coffee(self):

        milk_status = input("Do you want milk in your coffee? (yes/no): ").strip().lower()
        if milk_status == "yes":
            self.milk = True
        else:
            self.milk = False

        sugar_status = input("Do you want sugar in your coffee? (yes/no): ").strip().lower()
        if sugar_status == "yes":
            self.sugar = True
        else:
            self.sugar = False

        self.boil_water()
        self.pour_into_cup(milk_status, sugar_status)

if __name__ == "__main__":
    coffee_cup = CoffeeCup()
    coffee_cup.make_coffee()