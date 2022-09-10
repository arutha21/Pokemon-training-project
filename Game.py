from pokemon import Pokemon, fighting, Trainer
from pokemon_list import *

# The Game, trying everything



carapuce = Carapuce(level=8)
salameche = Salameche(level=8)
bulbizare = Bulbizare(level=8)
carapuce2 = Carapuce(level=8)
salameche2 = Salameche(level=8)
bulbizare2 = Bulbizare(level=8)

print(salameche)
print(type(salameche))
print(type(str(salameche)))
print(carapuce.defense)

ludo = Trainer('Ludo',[carapuce, salameche, bulbizare])
Jess = Trainer('Jess',[salameche2, carapuce2, bulbizare2])

print(ludo.pokemon_team)
ludo.attack_trainer(Jess)





