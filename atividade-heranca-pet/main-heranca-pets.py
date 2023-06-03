from animal import Animal
from cachorro import Cachorro
from pet import Pet

animais = [
	Animal("Lobo Cinza", "Canis lupus"),
	Animal("Lobo do Ártico", "Canis lupus arctos"),
	Animal("Lobo Vermelho", "Canis rufus"),
]

cachorros = [
	Cachorro("Pinscher"),
	Cachorro("Labrador"),
	Cachorro("Linguiceta")
]

pets = [
	Pet("Otto")
]

seres = animais + cachorros + pets

for animal in animais:
	animal.morrer()
	print(animal)

print("-="*20)

for cachorro in cachorros:
	print(cachorro.latir())
	print(cachorro)

print("-="*20)

for pet in pets:
	print(pet.latir())
	pet.morrer()
	print(pet)

print("-="*20)


for ser in seres:
	print(ser)