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
    },
]


def start():
    # workers_python = [i["name"] for i in DATA if i["language"] == "python"]
    workers_python = list(map(lambda x: x["name"], list(
        filter(lambda x: x["language"] == "python", DATA))))
    # platzi_workers = [i["name"] for i in DATA if i["organization"] == "Platzi"]
    platzi_workers = list(map(lambda x: x["name"], list(
        filter(lambda x: x["organization"] == "Platzi", DATA))))
    # adults_workers = list(filter(lambda x: x["age"] > 30, DATA))
    adults_workers = [i["name"] for i in DATA if i["age"] > 30]
    # adults_workers = list(map(lambda x: x["name"], adults_workers))
    # old_people = list(map(lambda x: x | {"old": x["age"] > 70}, DATA))
    # old_people = [i["name"] for i in DATA if i["age"] > 70]
    # print(workers_python)
    # print(platzi_workers)
    # print(adults_workers)
    # print(old_people)


if (__name__ == "__main__"):
    start()
