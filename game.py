from random import choice
from random import randint
from core.player import Player
from core.goblin import Goblin
from core.orc import Orc
from time import sleep
class Game:
  def start(self):
      self.show_menu()
  def show_menu(self):
    print(f'Game Menu\n\n1. Play\n2. Exit')
    choice = input()
    if choice == '1':
      self.battle(self.create_player(input('Enter player name ')), self.choose_random_monster())
    elif choice == '2':
      print('end game !')
      return
  def create_player(self, player_name):
    return Player(player_name)
  def choose_random_monster(self):
    return choice([Goblin, Orc])(choice(['bob', 'tom']))
  def battle(self, player, monster):
    self.player = player
    self.monster = monster
    player_roll_dice = self.roll_dice(6)
    monster_roll_dice = self.roll_dice(6)
    if self.player.speed + player_roll_dice > self.monster.speed + monster_roll_dice or self.player.speed + player_roll_dice == self.monster.speed + monster_roll_dice:
      current_player = self.player
    elif self.player.speed + player_roll_dice < self.monster.speed + monster_roll_dice:
      current_player = self.monster
    game_codition = True
    while game_codition:
      print(f"{current_player.name}'s tor !")
      dice = self.roll_dice(20)
      print(f'{current_player.speed + dice}, ">" , {self.switch_player(current_player).armor_rating}')
      attack_condition = (current_player.speed + dice) > (self.switch_player(current_player).armor_rating)
      if attack_condition:
        current_player.attack(self.switch_player(current_player), self.roll_dice(6))
        print(f"{current_player.name} atack !")
        sleep(1)
      else:
        print('fail')
      self.print_status()
      current_player = self.switch_player(current_player)
      game_codition = player.hp > 0 and monster.hp > 0
    print(self.switch_player(current_player).name, 'won!')
  @staticmethod
  def roll_dice(sides):
    return randint(1, sides)
  def switch_player(self, current_player):
    if current_player is self.player:
      return self.monster
    else:
      return self.player
  def print_status(self):
    print(f'player hp: {self.player.hp}, player armor_rating: {self.player.armor_rating}')
    print(f'monster hp: {self.monster.hp}, monster armor_rating: {self.monster.armor_rating}')