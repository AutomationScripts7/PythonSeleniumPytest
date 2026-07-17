
# Access function with class directly
#Object creation is not required

class python:

    num = 7

    @classmethod
    def test(cls):
        print(cls.num)

python.test()


#Both can be called without creating an object.
# The difference is that a class method works with class-level data using cls, whereas a static method is an independent utility function and
# doesn’t use either self or cls.