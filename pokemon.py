class Pokemon:
    def __init__(self, name, level, element, evolution={}, ko=False):
        self.name = name
        self.level = level
        self.element = element
        self.current_xp = 0  # pokemon current xp
        self.cap_level = level * 10  # reaching it gave one more level
        self.give_xp = level * 5  # xp the pokemon give when he is ko
        self.maximum_hp = 20 + self.level * 2
        self.current_hp = self.maximum_hp
        self.attack = 5 + self.level * 1
        self.defense = int(self.level / 2)
        self.speed = 10 + self.level * 3
        self.ko = False
        self.evolution = evolution

    def __repr__(self):
        # in order to pokemon be called by their name
        return '{} '.format(self.name)

    def lose_health(self, hp):
        self.current_hp -= hp
        # Avoid current hp being < 0
        if self.current_hp < 0:
            self.current_hp = 0
        print("{} now has {} health.\n".format(self.name, self.current_hp))

    def regaining_hp(self, hp):
        self.current_hp += hp
        self.current_hp = self.maximum_hp if self.current_hp > self.maximum_hp else self.current_hp
        print("{} now has {} health".format(self.name, self.current_hp))

    def knock_out(self):
        self.ko = True
        print("{} is KO.".format(self.name))

    def revive(self):
        # Reviving a pokemon
        self.ko = False
        self.current_hp = self.maximum_hp
        print("{} has revived.".format(self.name))

    def gain_xp_and_level(self, other_pokemon):
        # Xp Gaining > Level increased > Evolution
        # Xp gaining by putting KO an other pokemon
        self.current_xp += other_pokemon.give_xp
        print('{} gains {} xp.'.format(self.name, other_pokemon.give_xp))
        if self.current_xp >= self.cap_level:
            self.level += 1
            self.current_xp -= self.cap_level  # current xp reset after gaining a level
            print('{} upgrade to level {}!'.format(self.name, self.level))
            # Stat increased after level up
            self.attack += 2
            self.defense += 1
            self.maximum_hp += 3
            self.current_hp += 3
            self.cap_level = self.level * 10
            self.give_xp = self.level * 5
            # Pokemon evolving if reaching the right level
            for name in self.evolution.keys():
                if self.level >= self.evolution[name]:
                    previous_name = self.name
                    self.name = name
                    del self.evolution[name]
                    print('{} evolves to {}!!!'.format(previous_name, self.name))
                    # Stat increased after evolving
                    self.attack += 4
                    self.defense += 2
                    self.maximum_hp += 6
                    self.current_hp += 6
                    print('{} gets +4 attack, +2 defense and +6 Hp.'.format(self.name))
                    break

    def attacking(self, other_pokemon):
        # Preventing KO pokemon to be able to attack
        if self.ko == True:
            print('{} is KO, he can\'t attack.'.format(self.name))
        elif other_pokemon.ko == True:
            print('{} is KO, he can\'t be attacked.'.format(other_pokemon.name))
        else:
            # Resolving damage by taking account of pokemon type
            print('{} attacks {}.'.format(self.name, other_pokemon.name))
            damage_deal = self.attack
            if self.element == 'water':
                if other_pokemon.element == 'fire':
                    damage_deal *= 2
                elif other_pokemon.element == 'grass':
                    damage_deal /= 2
            elif self.element == 'fire':
                if other_pokemon.element == 'grass':
                    damage_deal *= 2
                elif other_pokemon.element == 'water':
                    damage_deal /= 2
            elif self.element == 'grass':
                if other_pokemon.element == 'water':
                    damage_deal *= 2
                elif other_pokemon.element == 'fire':
                    damage_deal /= 2
            damage_deal -= other_pokemon.defense
            print('{} takes {} damage.'.format(other_pokemon.name, damage_deal))
            # Using lose_health method to apply hp loss
            other_pokemon.lose_health(damage_deal)
            # Pokemon KO if his hp reach 0
            if other_pokemon.current_hp <= 0:
                other_pokemon.knock_out()
                self.gain_xp_and_level(other_pokemon)


def fighting(first_pkmn, second_pkmn):
    # Allowing a fight until one pokemon is KO
    # Determine which pokemon play first, the one with the higher speed stat
    # Then they attack alternately
    who_start_attacking = first_pkmn.speed - second_pkmn.speed
    if who_start_attacking >= 0:
        while first_pkmn.ko == False and second_pkmn.ko == False:
            first_pkmn.attacking(second_pkmn)
            second_pkmn.attacking(first_pkmn)
    elif who_start_attacking < 0:
        while first_pkmn.ko == False and second_pkmn.ko == False:
            second_pkmn.attacking(first_pkmn)
            first_pkmn.attacking(second_pkmn)


class Trainer(Pokemon):
    def __init__(self, name, pokemon_team=[]):
        self.name = name
        self.potions = 2
        self.pokemon_team = pokemon_team
        self.active_pokemon = self.pokemon_team[0]

    def use_potion(self):
        # can only use potion if got some in inventory and pokemon not ko
        if self.potions > 0 and self.active_pokemon.current_hp > 0:
            self.active_pokemon.current_hp += 10
            self.potions -= 1
            # potion can't give more hp than pokemon maximum health
            if self.active_pokemon.current_hp > self.active_pokemon.maximum_hp:
                self.active_pokemon.current_hp = self.active_pokemon.maximum_hp
            print('{} get 10 hp back'.format(self.active_pokemon))
        # if the pokemon is KO or don't have potion - not working
        else:
            print("You don't have any potion left in your inventory and/or your pokemon is KO.")

    def switch_pokemon(self, pkmn):
        # Changing active pokemon
        if pkmn in self.pokemon_team:
            self.active_pokemon = pkmn
            print("{} is now currently active.".format(pkmn))
        else:
            print("You don't have this pokemon in your team.")

    def attack_trainer(self, other_trainer):
        # Trainer active pokemon attacking an other active pokemon trainer
        # When your pokemon his ko, input to switch it, does it without input for the other trainer
        print('{} attacks {}.'.format(self.name, other_trainer.name))
        while True:
            # Need to know when all trainer pokemon are ko to end the fight
            self_count = 0
            other_count = 0
            for poke in self.pokemon_team:
                if poke.ko == True:
                    self_count += 1
            for poke in other_trainer.pokemon_team:
                if poke.ko == True:
                    other_count += 1
            if self_count == len(self.pokemon_team):
                print('The fight is over. {} has no more pokemon able to fight.'.format(self.name))
                print('{} defeats {}, congratulations!'.format(other_trainer.name, self.name))
                break
            if other_count == len(other_trainer.pokemon_team):
                print('The fight is over. {} has no more pokemon able to fight.'.format(other_trainer.name))
                print('{} defeats {}, congratulations!'.format(self.name, other_trainer.name))
                break
            # Fighting resolution
            if self.active_pokemon.ko == False:
                fighting(self.active_pokemon, other_trainer.active_pokemon)
            # Input to switch pokemon when the active one is KO
            else:
                print('{} is KO, he can\'t attack.'.format(self.active_pokemon.name))
                print('You must switch of active pokemon, with which one do you want to fight: ')
                new_active_pokemon = input()
                for poke in self.pokemon_team:
                    if poke.name == new_active_pokemon:
                        self.switch_pokemon(poke)
            index_pokemon = other_trainer.pokemon_team.index(other_trainer.active_pokemon)
            # Switching automatically for the other trainer
            if other_trainer.active_pokemon.ko == True and index_pokemon < len(other_trainer.pokemon_team)-1:
                other_trainer.switch_pokemon(other_trainer.pokemon_team[index_pokemon+1])


