
#Directly access function as data access (sum, multiply)
#Object creation is not required

class python:

    @staticmethod
    def test(a, *b):
        return a + b

print(python.test(1, 2))