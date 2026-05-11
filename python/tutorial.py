"""a = [[96], [69]]
print(map(str, a))
print(list(map(str, a)))

my_str = ["orange", "mango", "potato"]
my_new_str = [i[0]*2 for i in my_str]
print(my_new_str)"""

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
    return numbers < 50

filtered_numbers = filter(lesser, numbers)
print(list(filtered_numbers))

print(list(map(lesser, numbers)))