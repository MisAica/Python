people = {'users': {'John': 19, 'Emily': 21, 'Sarah': 25, 'Tom': 18}}

for name in people['users']:
    if people['users'][name] > 19:
        print(name)