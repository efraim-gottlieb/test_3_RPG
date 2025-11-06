from abc import ABC, abstractmethod

class GameParticipant(ABC):
  def __init__(self, name):
    self.name = name.capitalize()
  @abstractmethod
  def speak(self):
    pass
  @abstractmethod
  def attack(self):
    pass
    super().__init__()