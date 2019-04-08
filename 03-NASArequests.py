#!/usr/bin/env python3

import requests

r = requests.get('http://api.open-notify.org/astros.json').json()

#helmetson = r.json()

for person in r["people"]:      # for person in helmetson["people"]:      
    list_names = person["name"].split()
    print(list_names)
    print(list_names[-1])
