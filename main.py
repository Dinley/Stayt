import pygame, sys
Gravity = 1
Speed = 1
State = 0
Score = 0
Level = 0
Tiles = 0

def Gameloop():
 #gameloop goes here
 Print("Worked")
 menu = Input("Please enter where you want to go to: Controls, Main or Tutorial")
 if menu == Controls:
  Controlmenu
 elif menu == Main:
  Break
 elif menu == Tutorial:
  Tutorial
 else:
  menu = Input("Please enter a valid input, where you want to go to: Controls, Main or Tutorial")

def Tutorial():
 Print("Worked")
 menu = Input("Please enter where you want to go to: Controls, Main or Game")
 if menu == Controls:
  Controlmenu
 elif menu == Main:
  Break
 elif menu == Game:
  Gameloop
 else:
  menu = Input("Please enter a valid input, where you want to go to: Controls, Main or Tutorial")

def Mainmenu():
 Print("Welcome to Stayt")
 menu = Input("Please enter where you want to go to: Controls, Game or Tutorial")
 if menu == Controls:
  Controlmenu
 elif menu == Game:
  Gameloop
 elif menu == Tutorial:
  Tutorial
 else:
  menu = Input("Please enter a valid input, where you want to go to: Controls, Main or Tutorial")

def Controlmenu():
  Print("These are the controls")
  Print("Arrows key are to move Up, Down, Left, and Right")
  Print("Press A in order to change to Solid state")
  Print("Press S in order to change to Liquid state")
  Print("Press D in order to change to Gas state")
  Print("Press enter in order to Pause the game")
  menu = Input("Please enter where you want to go to: Controls, Game or Tutorial")
  if menu == Main:
   Break
  elif menu == Game:
   Gameloop
  elif menu == Tutorial:
   Tutorial
  else:
   menu = Input("Please enter a valid input, where you want to go to: Controls, Main or Tutorial")
   
   
   
While yes:  
 While always:  
  Mainmenu
