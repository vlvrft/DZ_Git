def sh_gen(items1, items2):
    k = len(items1) - len(items2)
    if k > 0:
        for _ in range(k):
            items2.append(None)
    for tutor, klass in zip(items1, items2):
        yield (tutor, klass)


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Александр', 'Екатерина']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

my_gen = sh_gen(tutors, klasses)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
