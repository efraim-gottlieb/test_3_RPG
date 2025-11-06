from core.monster_building import Monster_building
from random import randint

class Orc(Monster_building):
  def __init__(self, name):
    super().__init__(name)
    self.hp = 50
    self.type = 'orc'
    self.speed = randint(5, 10)
    self.power = randint(10, 15)
    self.armor_rating = randint(2, 8)
  def attack(self, player_to_attack, dice):
    weapon_damage = {'Knife' : 0.5, 'Sword' : 1, 'Axe' : 1.5}
    damage_weight = weapon_damage[self.weapon]
    player_to_attack.hp -= damage_weight * (self.power + dice)