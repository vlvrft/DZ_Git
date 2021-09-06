def num_translate(eng):
    nums = {'zero' : 'ноль',
            'one': 'один',
            'two' : 'два',
            'three' : 'три',
            'four' : 'четыре',
            'five' : 'пять',
            'six' : 'шесть',
            'seven' : 'семь',
            'eight' : 'восемь',
            'nine' : 'девять',
            'ten' : 'десять'}
    if eng.istitle() and nums.get(eng.lower()):
        return nums.get(eng.lower()).title()
    else:
        return nums.get(eng)

print(num_translate('Six'))