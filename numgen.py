from random import randint as rand


class generatenumber:

    @classmethod

    def generate(cls, amount, minRange, maxRange):
        if type(amount) != int:
            print("Amount must be an integer")
        elif amount == 0:
            print("Amount must be greater than 0")
        counter = 0
        while amount != counter:
            number = rand(minRange, maxRange)
            counter += 1
            if number > maxRange:
                print("Amount cannot exceed the maximum range")
            elif amount == -1:
                print("Amount cannot be a negative integer")
            print(number)


number = generatenumber.generate(5, 10, 50)