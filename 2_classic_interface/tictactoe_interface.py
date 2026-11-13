#Créé le 10 Avril 2023
from turtle import *
from ion import *
from kandinsky import get_pixel,fill_rect,draw_string
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
  goto(x,y),setheading(0),backward(30),right(90),color('blue')
  pendown(),circle(30)

def croix(x,y):
  goto(x,y),setheading(0),color('red'),pendown()
  right(45),backward(42),fd(84),backward(42),right(90),backward(42),fd(84)

def croixgagne(xa,ya,xb,yb):
  global vicroix
  global game
  color('black'),pensize(6),penup()
  goto(xa,ya)
  pendown(),goto(xb,yb)
  fill_rect(5,93,210,40,'black')
  draw_string("Les croix gagnent !",15,103,'red')
  sleep(2)
  vicroix+=1
  game+=1

def rondgagne(xa,ya,xb,yb):
  global virond
  global game
  color('black'),pensize(6),penup()
  goto(xa,ya)
  pendown(),goto(xb,yb)
  fill_rect(5,93,210,40,'black')
  draw_string("Les ronds gagnent !",15,103,'blue')
  sleep(2)
  virond+=1
  game+=1

def egalite():
  global egal
  global game
  fill_rect(61,98,100,30,'black')
  draw_string("Egalité !",66,103)
  sleep(2)
  egal+=1
  game+=1

def abandon():
  global game
  fill_rect(61,98,100,30,'black')
  draw_string("Abandon !",66,103)
  sleep(2)
  game+=1

co1,co2,co3=35,111,185
tux1,tux2,tux3,tuy1,tuy2,tuy3=-125,-49,25,76,0,-76
vicroix,virond,game,egal=0,0,1,0
c1,c2=(255,0,0),(0,0,255)
switch,restart=1,True
while restart:
  fill_rect(0,0,320,222,'white'),  fill_rect(222,0,99,222,'orange')
  fill_rect(71,0,5,222,'black'),fill_rect(145,0,5,222,'black'),fill_rect(0,71,222,5,'black'),fill_rect(0,145,222,5,'black')
  draw_string("Partie",230,5),draw_string("numéro:",230,23),draw_string(str(game),230,41)
  draw_string("Victoire",230,70),draw_string("croix: "+str(vicroix),230,95),draw_string("ronds: "+str(virond),230,120)
  draw_string("Egalité:",230,150),draw_string(str(egal),230,168)
  pensize(5),speed(10),hideturtle()
  coup=0
  one,two,three,four,five,six,seven,eight,nine=True,True,True,True,True,True,True,True,True
  while True:
    penup()
    if keydown(KEY_ONE):
      if one:
        choix(tux1,tuy3)
        one=False
    elif keydown(KEY_TWO):
      if two:
        choix(tux2,tuy3)
        two=False
    elif keydown(KEY_THREE):
      if three:
        choix(tux3,tuy3)
        three=False
    elif keydown(KEY_FOUR):
      if four:
        choix(tux1,tuy2)
        four=False
    elif keydown(KEY_FIVE):
      if five:
        choix(tux2,tuy2)
        five=False
    elif keydown(KEY_SIX):
      if six:
        choix(tux3,tuy2)
        six=False
    elif keydown(KEY_SEVEN):
      if seven:
        choix(tux1,tuy1)
        seven=False
    elif keydown(KEY_EIGHT):
      if eight:
        choix(tux2,tuy1)
        eight=False
    elif keydown(KEY_NINE):
      if nine:
        choix(tux3,tuy1)
        nine=False
    if get_pixel(co1,co1)==(c1) and get_pixel(co2,co1)==(c1) and get_pixel(co3,co1)==(c1):
      croixgagne(tux1-30,tuy1,tux3+30,tuy1)
      break
    if get_pixel(co1,co2)==(c1) and get_pixel(co2,co2)==(c1) and get_pixel(co3,co2)==(c1):
      croixgagne(tux1-30,tuy2,tux3+30,tuy2)
      break
    if get_pixel(co1,co3)==(c1) and get_pixel(co2,co3)==(c1) and get_pixel(co3,co3)==(c1):
      croixgagne(tux1-30,tuy3,tux3+30,tuy3)
      break
    if get_pixel(co1,co1)==(c1) and get_pixel(co1,co2)==(c1) and get_pixel(co1,co3)==(c1):
      croixgagne(tux1,tuy1+30,tux1,tuy3-30)
      break
    if get_pixel(co2,co1)==(c1) and get_pixel(co2,co2)==(c1) and get_pixel(co2,co3)==(c1):
      croixgagne(tux2,tuy1+30,tux2,tuy3-30)
      break
    if get_pixel(co3,co1)==(c1) and get_pixel(co3,co2)==(c1) and get_pixel(co3,co3)==(c1):
      croixgagne(tux3,tuy1+30,tux3,tuy3-30)
      break
    if get_pixel(co1,co1)==(c1) and get_pixel(co2,co2)==(c1) and get_pixel(co3,co3)==(c1):
      croixgagne(tux1-30,tuy1+30,tux3+30,tuy3-30)
      break
    if get_pixel(co3,co1)==(c1) and get_pixel(co2,co2)==(c1) and get_pixel(co1,co3)==(c1):
      croixgagne(tux3+30,tuy1+30,tux1-30,tuy3-30)
      break
    if get_pixel(co1-30,co1)==(c2) and get_pixel(co2-30,co1)==(c2) and get_pixel(co3-30,co1)==(c2):
      rondgagne(tux1-30,tuy1,tux3+30,tuy1)
      break
    if get_pixel(co1-30,co2)==(c2) and get_pixel(co2-30,co2)==(c2) and get_pixel(co3-30,co2)==(c2):
      rondgagne(tux1-30,tuy2,tux3+30,tuy2)
      break
    if get_pixel(co1-30,co3)==(c2) and get_pixel(co2-30,co3)==(c2) and get_pixel(co3-30,co3)==(c2):
      rondgagne(tux1-30,tuy3,tux3+30,tuy3)
      break
    if get_pixel(co1-30,co1)==(c2) and get_pixel(co1-30,co2)==(c2) and get_pixel(co1-30,co3)==(c2):
      rondgagne(tux1,tuy1+30,tux1,tuy3-30)
      break
    if get_pixel(co2-30,co1)==(c2) and get_pixel(co2-30,co2)==(c2) and get_pixel(co2-30,co3)==(c2):
      rondgagne(tux2,tuy1+30,tux2,tuy3-30)
      break
    if get_pixel(co3-30,co1)==(c2) and get_pixel(co3-30,co2)==(c2) and get_pixel(co3-30,co3)==(c2):
      rondgagne(tux3,tuy1+30,tux3,tuy3-30)
      break
    if get_pixel(co1-30,co1)==(c2) and get_pixel(co2-30,co2)==(c2) and get_pixel(co3-30,co3)==(c2):
      rondgagne(tux1-30,tuy1+30,tux3+30,tuy3-30)
      break
    if get_pixel(co3-30,co1)==(c2) and get_pixel(co2-30,co2)==(c2) and get_pixel(co1-30,co3)==(c2):
      rondgagne(tux3+30,tuy1+30,tux1-30,tuy3-30)
      break
    if coup==9:
      egalite()
      break
    if keydown(KEY_BACK):
      restart=False
    if keydown(KEY_OK):
      abandon()
      break
