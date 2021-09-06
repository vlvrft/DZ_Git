def thesaurus(*names):
    name = dict()
    for el in sorted(names):
        key = el[0]
        if name.get(key) is None:
            name[key] = [el]
        else:
            name[key].append(el)
    return name


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
