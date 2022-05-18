name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

#Adding whitespace to string
print("\tPython")

print("Language:\nPython..")

favorite_languange = ' python '
favorite_languange.rstrip()
favorite_languange.strip()
favorite_languange.strip()

#LISTS
bicycles = ['trek', 'cannondale', 'redline', 'specalized']
print(bicycles[0])
print(bicycles[-1])

#Modify LISTS
bicycles[0] = 'ducati'
print(bicycles)
#Adding - end
bicycles.append('ducati')
print(bicycles)
#insert
bicycles.insert(0, 'ducati')
print(bicycles)
#remove
del bicycles[0]
print(bicycles)

bicycles.pop()
print(bicycles)

bicycles.pop(1)
print(bicycles)


bicycles.remove('ducati')
print(bicycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

cars.reverse()
print(cars)
print(len(cars))
