# create one list
my_list = ["mango", "banana", "grapes", "orange", "guava", "grapefruit"]

def get_fruit(fruit):
    if fruit[0] == "g":
        return fruit

if __name__ == "__main__":
    # use map function to apply get_fruit to each element in my_list
    result = map(get_fruit, my_list)

    for fruit in result:
        if fruit is not None:
            print(fruit)