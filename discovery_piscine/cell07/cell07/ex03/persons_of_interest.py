def get_birth_year(person):
    return person["date_of_birth"]

def famous_births(people):
    sorted_people = sorted(people.values(), key=get_birth_year)
    for person in sorted_people:
        name = person["name"]
        year = person["date_of_birth"]
        print(name + " is a great scientist born in " + year + ".")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)