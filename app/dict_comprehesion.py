import random
# forma tradicional de realizar un diccionario
dict = {}
for i in range(1,5):
  dict[i] = i * 2
print(dict)
# dictionary comprehension 
dict_2 = {llave: valor*2 for llave, valor in dict.items()}
print(dict)

coutries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in coutries:
  population[country] = random.randint(1,100)
print(population)


population_v2 = {country: random.randint(1,100)for country in coutries}
print(population_v2)


names = ['nico','zule','santi']
ages = [12,56,98]
print(list(zip(names,ages)))

text = 'hola soy nicolas'
unique = {c: c.upper()  for c in text if c in 'aeiou'}
print(unique)

text = 'hola soy nicolas'
unique = {c: c.upper()  for c in text if c in 'aeiou'}
print(unique)