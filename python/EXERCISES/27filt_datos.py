# FILTRANDO DATOS
# con list comprehensions y con high order function

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    }
]

def run():

    # personas con conocimiento en python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == 'python']

    # personas que trabajan en platzi
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == 'Platzi']
   
    # personas mayores de 18 años
    adults = list(filter(lambda worker: worker["age"] > 18, DATA)) #muestra todo el dic por pers.
    adults = list(map(lambda worker: worker["name"], adults)) # muestra solo el nombre por pers.

    # personas mayores a 70 años
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    #se crea una nueva caracteristica dentro de los dict de cada persona (old)


    # CADA VARIABLE ANTERIOR PERO CON PROCESO DIFERENTE:

    all_python_devs2 = list(filter(lambda worker: worker["language"] == 'python', DATA))
    all_python_devs2 = list(mapmap(lambda worker: worker["name"], all_python_devs2))

    all_platzi_workers2 = list(filter(lambda worker: worker["organization"] == 'Platzi', DATA))
    all_platzi_workers2 = list(map(lambda worker: worker["name"], all_platzi_workers2))

    adults2 = [worker["name"] for worker in DATA if worker["age"] > 18]

    old_people2 = [worker["name"] for worker in DATA if worker["age"] > 70]


    # --- verificacion ---
    for worker in old_people2:
        print(worker)

if __name__ == '__main__':
    run()
