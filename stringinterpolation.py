person = '%s\'s age is %d'
print(person % ('Bill',55))

print()

#new style
person='{name}\'s age is {age}'
print(person.format(name='Bill',age=55))
print(person.format(name='Steve', age=50))

#formatted string literal python 3.6+
name='Mark'
age=30
person=f'{name}\'s age is {age}'
print(person)

