#Créé le 15 Avril 2024
from math import pi,cos,sin
from kandinsky import fill_rect as fr,draw_string as ds,set_pixel as sp
from ion import keydown as kd
from time import sleep as sl

slct,itfc=(0,255,0),(255,181,59)
n,wh=(0,)*3,(255,)*3
re,bl,gr=(255,0,0),(0,0,255),(0,200,0)
cl=[[re,gr],[(150,0,0),(0,150,0)]]
pos=[0,75,150]

pl,vc,vr=1,0,0

def paradroi(x,y,w,h,c):
 for a in range(w):
  for b in range(h):
   x+=1;sp(x,y,c)
  x,y=x-h+1,y+1
def paragau(x,y,w,h,c):
 for a in range(w):
  x,y=x-h-1,y+1
  for b in range(h):
   x+=1;sp(x,y,c)
def cercle(cx,cy,r,c):
 for i in range(4*r*pi):
  x,y=cx+cos(i)*r,cy+sin(i)*r
  fr(int(x),int(y),1,-2*int(sin(i)*r),c)
def croix(x,y,c=0):
 w,h,c=55,8,1 if c==3 else 0
 paradroi(x+5,y+7,w,h,cl[c][0]),paragau(x+65,y+6,w,h,cl[c][0])
def rond(x,y,c=0):c=1 if c==7 else 0;cercle(x+36,y+36,30,cl[c][1])

def win(w,c,p=0):
 global game,vc,vr
 def l(x,y,d):
  if d==1:w,h,plx,ply=212,12,4,29
  elif d==2:w,h,plx,ply=12,212,29,4
  fr(x+plx,y+ply,w,h,n)
 if w==1:l(pos[0],pos[p],w)
 elif w==2:l(pos[p],pos[0],w)
 elif w==3:paradroi(pos[0]+5,pos[0]+15,190,20,n)
 elif w==4:paragau(pos[2]+65,pos[0]+15,190,20,n)
 sl(2);fr(0,0,320,222,itfc)
 ds("Victoire des ",60,102)
 if c==1:ds("croix !",190,102);vc+=1
 elif c==2:ds("ronds !",190,102);vr+=1
 sl(3);game=False

while True:
 fr(0,0,320,222,wh),fr(220,0,100,222,itfc),fr(0,220,222,2,itfc)
 for i in range(2):fr(pos[i+1]-5,0,5,220,n)
 for i in range(2):fr(0,pos[i+1]-5,220,5,n)
 ds("Morpion ",223,10,itfc),ds("V3",298,10,itfc)
 ds("Joueur: ",225,60),ds("Coups:",225,90)
 ds("Croix:"+str(vc),225,140,re)
 ds("Ronds:"+str(vr),225,170,gr)
 jeu,dspl=[[0]*3 for i in range(3)],[[0]*3 for i in range(3)]
 x,y,px,py=1,1,1,1
 coup,game,new=0,True,True
 while game:
  if new:
   new=False
   if pl==1:ds(str(pl),295,60,re)
   elif pl==2:ds(str(pl),295,60,gr)
   ds(str(coup),285,90)
   fr(pos[px],pos[py],70,70,wh)
   if jeu[py][px] in [1,2,3]:croix(pos[px],pos[py],jeu[py][px])
   elif jeu[py][px] in [5,6,7]:rond(pos[px],pos[py],jeu[py][px])
   fr(pos[x],pos[y],70,70,slct)
   if jeu[y][x] in [1,2,3]:croix(pos[x],pos[y],jeu[y][x])
   elif jeu[y][x] in [5,6,7]:rond(pos[x],pos[y],jeu[y][x])
   sl(0.1)

  if kd(0) and x>0:x,px,py,new=x-1,x,y,True
  elif kd(1) and y>0:y,px,py,new=y-1,x,y,True
  elif kd(2) and y<2:y,px,py,new=y+1,x,y,True
  elif kd(3) and x<2:x,px,py,new=x+1,x,y,True
  elif kd(4)or kd(52):
   if jeu[y][x]==0:
    new,coup,px,py=True,coup+1 if pl==2 else coup,x,y;sl(0.1),fr(pos[x],pos[y],70,70,wh)
    if pl==1:
     croix(pos[x],pos[y])
     for a in range(3):
      for b in range(3):
       if jeu[b][a] in [1,2,3]:jeu[b][a]+=1
       if jeu[b][a]==3:croix(pos[a],pos[b],jeu[b][a])
       elif jeu[b][a]==4:jeu[b][a]=0;fr(pos[a],pos[b],70,70,wh)
     jeu[y][x],pl=1,2
    elif pl==2:
     rond(pos[x],pos[y])
     for a in range(3):
      for b in range(3):
       if jeu[b][a] in [5,6,7]:jeu[b][a]+=1
       if jeu[b][a]==7:rond(pos[a],pos[b],jeu[b][a])
       elif jeu[b][a]==8:jeu[b][a]=0;fr(pos[a],pos[b],70,70,wh)
     jeu[y][x],pl=5,1
    dspl=[[0]*3 for i in range(3)]
    for a in range(3):
     for b in range(3):
      if jeu[b][a] in [1,2,3]:dspl[b][a]=1
      if jeu[b][a] in [5,6,7]:dspl[b][a]=2
    for col in range(1,3):
     for a in range(3):
      if all(dspl[a][i]==col for i in range(3)):win(1,col,a)
      if all(dspl[i][a]==col for i in range(3)):win(2,col,a)
     if all(dspl[i][i]==col for i in range(3)):win(3,col)
     if dspl[0][2]==dspl[1][1]==dspl[2][0]==col:win(4,col)
