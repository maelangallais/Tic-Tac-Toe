#Créé le 03 Avril 2023
from turtle import *
from ion import *
from kandinsky import get_pixel,fill_rect
from time import sleep

def choix(x,y):
  global coup
  global switch
  coup+=1
  if switch==1:
    croix(x,y)
    switch=2
  elif switch==2:
    rond(x,y)
    switch=1

def rond(x,y):
  goto(x,y)
  setheading(0)
  backward(30)
  right(90)
  color('blue')
  pendown()
  circle(30)

def croix(x,y):
  goto(x,y)
  setheading(0)
  color('red')
  pendown()
  right(45)
  backward(42)
  fd(84)
  backward(42)
  right(90)
  backward(42)
  fd(84)

def croixgagne():
  penup()
  goto(-85,-10)
  write("Les croix gagnent !")

def rondgagne():
  penup()
  goto(-85,-10)
  write("Les ronds gagnent !")

def egalite():
  penup()
  goto(-35,-10)
  write("Egalite !")

def abandon():
  penup()
  goto(-40,-10)
  write("Abandon !")

switch=1
restart=True
while restart:
  fill_rect(0,0,320,222,'white')
  fill_rect(104,0,5,222,'black')
  fill_rect(211,0,5,222,'black')
  fill_rect(0,71,320,5,'black')
  fill_rect(0,145,320,5,'black')
  pensize(5)
  speed(10)
  hideturtle()
  coup=0
  one=True
  two=True
  three=True
  four=True
  five=True
  six=True
  seven=True
  eight=True
  nine=True
  while True:
    penup()
    if keydown(KEY_ONE):
      if one:
        choix(-107,-75)
        one=False
    elif keydown(KEY_TWO):
      if two:
        choix(0,-75)
        two=False
    elif keydown(KEY_THREE):
      if three:
        choix(107,-75)
        three=False
    elif keydown(KEY_FOUR):
      if four:
        choix(-107,0)
        four=False
    elif keydown(KEY_FIVE):
      if five:
        choix(0,0)
        five=False
    elif keydown(KEY_SIX):
      if six:
        choix(107,0)
        six=False
    elif keydown(KEY_SEVEN):
      if seven:
        choix(-107,75)
        seven=False
    elif keydown(KEY_EIGHT):
      if eight:
        choix(0,75)
        eight=False
    elif keydown(KEY_NINE):
      if nine:
        choix(107,75)
        nine=False
    if get_pixel(53,36)==(255,0,0) and get_pixel(160,36)==(255,0,0) and get_pixel(267,36)==(255,0,0):
      penup()
      goto(-137,75)
      color('black')
      pendown()
      goto(137,75)
      croixgagne()
      sleep(2)
      break
    if get_pixel(53,111)==(255,0,0) and get_pixel(160,111)==(255,0,0) and get_pixel(267,111)==(255,0,0):
      penup()
      goto(-137,0)
      color('black')
      pendown()
      goto(137,0)
      croixgagne()
      sleep(2)
      break
    if get_pixel(53,186)==(255,0,0) and get_pixel(160,186)==(255,0,0) and get_pixel(267,186)==(255,0,0):
      penup()
      goto(-137,-75)
      color('black')
      pendown()
      goto(137,-75)
      croixgagne()
      sleep(2)
      break
    if get_pixel(53,36)==(255,0,0) and get_pixel(53,111)==(255,0,0) and get_pixel(53,186)==(255,0,0):
      penup()
      goto(-107,105)
      color('black')
      pendown()
      goto(-107,-105)
      croixgagne()
      sleep(2)
      break
    if get_pixel(160,36)==(255,0,0) and get_pixel(160,111)==(255,0,0) and get_pixel(160,186)==(255,0,0):
      penup()
      goto(0,105)
      color('black')
      pendown()
      goto(0,-105)
      croixgagne()
      sleep(2)
      break
    if get_pixel(267,36)==(255,0,0) and get_pixel(267,111)==(255,0,0) and get_pixel(267,186)==(255,0,0):
      penup()
      goto(107,105)
      color('black')
      pendown()
      goto(107,-105)
      croixgagne()
      sleep(2)
      break
    if get_pixel(53,36)==(255,0,0) and get_pixel(160,111)==(255,0,0) and get_pixel(267,186)==(255,0,0):
      penup()
      goto(-137,105)
      color('black')
      pendown()
      goto(137,-105)
      croixgagne()
      sleep(2)
      break
    if get_pixel(267,36)==(255,0,0) and get_pixel(160,111)==(255,0,0) and get_pixel(53,186)==(255,0,0):
      penup()
      goto(137,105)
      color('black')
      pendown()
      goto(-137,-105)
      croixgagne()
      sleep(2)
      break
    if get_pixel(53,6)==(0,0,255) and get_pixel(160,6)==(0,0,255) and get_pixel(267,6)==(0,0,255):
      penup()
      goto(-137,75)
      color('black')
      pendown()
      goto(137,75)
      rondgagne()
      sleep(2)
      break
    if get_pixel(53,81)==(0,0,255) and get_pixel(160,81)==(0,0,255) and get_pixel(267,81)==(0,0,255):
      penup()
      goto(-137,0)
      color('black')
      pendown()
      goto(137,0)
      rondgagne()
      sleep(2)
      break
    if get_pixel(53,156)==(0,0,255) and get_pixel(160,156)==(0,0,255) and get_pixel(267,156)==(0,0,255):
      penup()
      goto(-137,-75)
      color('black')
      pendown()
      goto(137,-75)
      rondgagne()
      sleep(2)
      break
    if get_pixel(53,6)==(0,0,255) and get_pixel(53,81)==(0,0,255) and get_pixel(53,156)==(0,0,255):
      penup()
      goto(-107,105)
      color('black')
      pendown()
      goto(-107,-105)
      rondgagne()
      sleep(2)
      break
    if get_pixel(160,6)==(0,0,255) and get_pixel(160,81)==(0,0,255) and get_pixel(160,156)==(0,0,255):
      penup()
      goto(0,105)
      color('black')
      pendown()
      goto(0,-105)
      rondgagne()
      sleep(2)
      break
    if get_pixel(267,6)==(0,0,255) and get_pixel(267,81)==(0,0,255) and get_pixel(267,156)==(0,0,255):
      penup()
      goto(107,105)
      color('black')
      pendown()
      goto(107,-105)
      rondgagne()
      sleep(2)
      break
    if get_pixel(53,6)==(0,0,255) and get_pixel(160,81)==(0,0,255) and get_pixel(267,156)==(0,0,255):
      penup()
      goto(-137,105)
      color('black')
      pendown()
      goto(137,-105)
      rondgagne()
      sleep(2)
      break
    if get_pixel(267,6)==(0,0,255) and get_pixel(160,81)==(0,0,255) and get_pixel(53,156)==(0,0,255):
      penup()
      goto(137,105)
      color('black')
      pendown()
      goto(-137,-105)
      rondgagne()
      sleep(2)
      break
    if coup==9:
      egalite()
      sleep(2)
      break
    if keydown(KEY_BACK):
      restart=False
    if keydown(KEY_OK):
      abandon()
      sleep(2)
      break
