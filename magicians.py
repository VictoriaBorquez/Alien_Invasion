magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

for value in range(1, 5): # de 1 a 4
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2,11,2)) #numeros pares, comienza en 2, llega hasta 10 y va de 2 en 2
print(even_numbers)


squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #de  0 a 2
print(players[:4]) #de  0 a 3
print(players[2:]) #de  2 a n
print(players[-3:]) #de  2 a n
print(players[:]) #todo
