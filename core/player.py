from abc import ABC, abstractmethod

class GameParticipant(ABC):
  def __init__(self, name, hp, speed, power, armor_rating):
    self.name = name
    self.hp = hp
    self.speed = speed
    self.power= power
    self.armor_rating = armor_rating
  @abstractmethod
  def speak(self):
    pass
  @abstractmethod
  def attack(self):
    pass
    super().__init__()

  

