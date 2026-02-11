def array_of_names(persons):
    names = []
    for first in persons:
        last = persons[first]
        full_name = first.capitalize() + " " + last.capitalize()
        names.append(full_name)
    return names


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))