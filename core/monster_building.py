from core.game_participant import GameParticipant
from abc import ABC, abstractmethod
from random import choice

class Monster_building(GameParticipant, ABC):
  def __init__(self, name):
    super().__init__(name)
    self.weapon = choice(['Knife', 'Sword', 'Axe'])
  def speak(self):
    print(f'{self.name} the {self.type} is angry !')







