
#Data hide
#Data (variables) and Methods (Functions) keeping safe in a class

#Data protection and we cannot access data directly

#we can access via Methods and Object

#Direct access - not a encapsulation
#Method through access - Encapsulation

class Bank_account:

    def __init__(self, balance):
        self.__balance = balance        #  __ underscore for > private variable

    def balance_check(self):
        return self.__balance

obj = Bank_account(5000)
print(obj.balance_check())