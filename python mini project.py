# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fPGm7em6wYb83SIlEt4yOhLWqzTVGmdE
"""

#project 1
import random

def roll():
  mini_value=1
  maxi_value=6
  roll=random.randint(mini_value,maxi_value)

  return roll
value=roll()
print(value)
while True:
  players=input("enter number oof players that will be playing game(1-4):  ")
  if players.isdigit():
    players=int(players)
    if 2 <= players <=4:
      break
    else:
        print("must be between 2-4")
  else:
    print("invalid number entered ")
maxi_score=50
players_score=[0 for _ in range(players)]

print(players_score)
while max(players_score)<maxi_score:
  for player_idx in range(players):
    print("\nplayer",player_idx+1,"turn has just started\n")
    current_score=0
    while True:
      should_roll=input("would you like to roll(y)")
      if should_roll.lower()!="y":
         break
      value=roll()
      if value==1:
         print("you rolled 1! turn done")
         current_score=0
         break
      else:
        current_score += value
        print("you rolled a ",value)
      print("your score is: ",current_score)
    players_score[player_idx]+=current_score
    print("your total score is:  ",players_score[player_idx])