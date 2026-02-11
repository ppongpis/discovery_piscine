def find_redhead(family):
    redheads = []
    for name in family:
        if family[name] == "red":
            redheads.append(name)
    return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_redhead(dupont_family))