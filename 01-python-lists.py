#!/usr/bin/env python3
"""Python Training | Alta3 Research | rzfeeser@alta3.com"""

fruits = ["pineapple", "peach"]

veggies = ["zucchini", "asparagus", fruits]

meats = ["beef", "pork", "grouse", "turkey", "chicken", "fish"]

print(meats[2][1])

new_meat = input("What meat do you want to add?: ")

meats.append(new_meat)
meats.reverse()
# meats.sort()
print(sorted(meats))

meats.pop()

print(meats)
