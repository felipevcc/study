"""
Ejemplo con json

import json

def es_par(num):
    return num%2 == 0

def run():
    with open("./data.json", "r") as f:
        DATA = json.load(f)
        all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
        all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
        adults = list(filter(lambda worker: worker['age'] > 18, DATA))
        adults_name = list(map(lambda worker: worker['name'], adults))
        old_people = list(map(lambda worker: worker, DATA))

        print(all_python_devs)
        print(all_Platzi_workers)
        print(adults_name)
        print(old_people)

if __name__ == '__main__':
    run()
    
"""