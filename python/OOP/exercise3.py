class A:
    def __init__(self, a):
        print("Inside Class A")
        self.a = a
    print("End of Class A")

    def alpha(self):
        return self.a + 1


print(dir(A))
print("Instantiating Class A")
a = A(5)
print(a.alpha())

