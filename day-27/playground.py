# def add(b, *args, a):
#     sum = 0
#     for n in args:
#         sum += n
#
#     return sum + a + b
#
# print(add(7,90,8,8,8,8,8,7,a=8))
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#
#     print(n)
#
# calculate(5, add = 7, multiply = 8)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.make)