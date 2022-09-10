from pokemon import Pokemon

class Salameche(Pokemon):
    def __init__(self, level):
        super().__init__('Salamèche', level, 'fire', evolution={'Reptincel':12, 'Dracaufeu':25})
        
class Carapuce(Pokemon):
    def __init__(self, level):
        super().__init__('Carapuce', level, 'water', evolution={'Carabaff':14, 'Tortank':24})

class Bulbizare(Pokemon):
    def __init__(self, level):
        super().__init__('Bulbizare', level, 'grass', evolution={11:'Herbizare', 27:'Florizare'})