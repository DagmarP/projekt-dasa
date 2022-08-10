# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from carinfo import CarInfo

with open(os.path.join("ptydepe.txt"), "r", encoding="utf-8") as ptydepe:
    ptydepe = ptydepe.read().splitlines()

count = 0
# Strips the newline character
# for line in ptydepe:
#    count += 1
#    print("Řádek {}: {} {}".format(count, line.strip(), 'konec'))

cars = ["Ford", "Volvo", "BMW"]
cars.append("Škoda")
car_infos = []

for car in cars:
    count = count + 1
    car_info = CarInfo(car, count, car.upper())
    car_infos.append(car_info)
    print("Auto {}: {}".format(count, car.upper()))

for item in car_infos:
    print(item)

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
child = myfamily["child1"]["name"]

print(child)

a = 33
b = 200
if b > a:
    print("b is greater than a")

elif b == a:
    print("b is equal to a")
else:
    print("b is lesser than a")
