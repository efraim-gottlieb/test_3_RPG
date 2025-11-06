from core.game_participant import GameParticipant
from random import choice
from random import randint

class Player(GameParticipant):
  def __init__(self, name):
    super().__init__(name)
    self.profession = choice(['fighter', 'healer'])
    self.hp = 50
    if self.profession == 'healer':
      self.hp += 10
    self.speed = randint(5, 10)
    self.power = randint(5, 10)
    if self.profession == 'fighter':
      self.power += 2
    self.armor_rating = randint(5, 10)
  def attack(self, player_to_attack, dice):
    player_to_attack.hp -= (self.power + dice)
  def speak(self):
    print(f'{self.name} is speak !')