#!/usr/bin/env python3

import urllib.request
import json

spaceweb = 'http://api.open-notify.org/astros.json'

groundctrl = urllib.request.urlopen(spaceweb)

# print(groundctrl.headers)

helmet = groundctrl.read()

# print(helmet)

helmetson = json.loads(helmet.decode('utf-8'))

print(helmetson)

print("Number of people in space: {}".format(helmetson["number"]))

for person in helmetson["people"]:
    # print their name
    #if "-" in person["name"]:
    #    person["name"].replace("-", " ")
        
    list_names = person["name"].split()
    print(list_names)
    print(list_names[-1])