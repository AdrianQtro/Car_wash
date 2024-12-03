
#Comprensión de diccionarios:
words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words if len(word) > 5} 
print(word_lengths)


#Comprensión de listas:
numbers = [1, 2, 3, 4]
squares = [x**2 for x in numbers if x % 2 == 0]  # [4, 16]
print(squares)

#Reduce
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)  # 10
print(total)

#filter
numbers = [5, 7, 9, 2]
filtered = filter(lambda x: x > 5, numbers)  # [7, 9]
print(list(filtered))

#map
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)  # [1, 4, 9, 16]
print(list(squared))