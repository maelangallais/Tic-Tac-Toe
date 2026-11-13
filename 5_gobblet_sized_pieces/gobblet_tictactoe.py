#Créé le 02 Juillet 2024
from math import pi,cos,sin
from kandinsky import fill_rect as fr,draw_string as ds,set_pixel as sp
from ion import keydown as kd
from time import sleep as sl

slct,itfc=(0,255,0),(255,181,59)
n,wh=(0,)*3,(255,)*3
re,gr,bl=(255,0,0),(0,200,0),(0,0,255)
cl=[re,gr]
pos=[0,75,150]
np=24

pl,vc,vr,dr=1,0,0,0

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
def rond(cx,cy,r,c):
 m=16 if r<21 else 4
 for i in range(m*r*pi):
  x,y=cx+cos(i)*r,cy+sin(i)*r
  fr(int(x),int(y),1,-2*int(sin(i)*r),c)
def draw(x,y):
 if jeu[y][x]==0:return
 r,c=30-3*(9-(jeu[y][x]%10)),0 if jeu[y][x]<10 else 1
 rond(pos[x]+36,pos[y]+36,r,cl[c])

def win(w,c,p=0):
 global game,vc,vr
 if c==3:ds("Egalité !",115,102);dr+=1;sl(3);game=False;return
 fr(pos[x],pos[y],70,70,wh),draw(x,y)
 def l(x,y,d):
  if d==1:w,h,plx,ply=212,12,4,29
  elif d==2:w,h,plx,ply=12,212,29,4
  fr(x+plx,y+ply,w,h,n)
 if w==1:l(pos[0],pos[p],w)
 elif w==2:l(pos[p],pos[0],w)
 elif w==3:paradroi(pos[0]+5,pos[0]+15,190,20,n)
 elif w==4:paragau(pos[2]+65,pos[0]+15,190,20,n)
 sl(3);fr(0,0,320,222,itfc)
 ds("Victoire des ",55,102)
 if c==1:ds("rouges !",185,102);vc+=1
 elif c==2:ds("verts !",180,102);vr+=1
 sl(2);game=False

def ok():
 global new,coup,px,py,pl
 nx=ny=1
 ch=nch=True
 fr(pos[x],pos[y],70,70,wh)
 for i in range(2):fr(pos[x]+(i+1)*np-2,pos[y],2,70,n)
 for i in range(2):fr(pos[x],pos[y]+(i+1)*np-2,70,2,n)
 vc=jeu[y][x]%10
 while ch:
  if nch:
   nch=False
   #Prendre en compte les pions qu'on n'a plus
   for a in range(3):
    for b in range(3):
     va=a*3+b+1
     c=0 if vc+1>va else 1
     if va not in lp[pl-1]:c=0
     cx,cy=pos[x]+b*np,pos[y]+a*np
     fr(cx,cy,22,22,cl[c])
     if ny*3+nx+1==va:fr(pos[x]+nx*np,pos[y]+ny*np,22,22,n)
     ds(str(va),cx+6,cy+2)
   sl(0.1)
  if kd(0)and nx>0:nx,nch=nx-1,True
  elif kd(1)and ny>0:ny,nch=ny-1,True
  elif kd(2)and ny<2:ny,nch=ny+1,True
  elif kd(3)and nx<2:nx,nch=nx+1,True
  elif kd(17):new=True;return
  elif kd(4)or kd(52):
   va=ny*3+nx+1
   c=0 if vc+1>va else 1
   if va not in lp[pl-1]:c=0
   if c==1:
    lp[pl-1].remove(va)
    jeu[y][x]=(pl-1)*10+va
    ch=False
   else:new=True;return
 px,py,new=x,y,True
 coup,pl=coup+1 if pl==2 else coup,1 if pl==2 else 2
 ds(str(coup),285,90)
 if pl==1:ds(str(pl),295,60,re)
 elif pl==2:ds(str(pl),295,60,gr)
 #Vérification de victoire
 dspl=[[0]*3 for i in range(3)]
 for a in range(3):
  for b in range(3):
   if jeu[b][a]==0:continue
   if jeu[b][a]<10:dspl[b][a]=1
   if jeu[b][a]>10:dspl[b][a]=2
 for col in range(1,3):
  for a in range(3):
   if all(dspl[a][i]==col for i in range(3)):win(1,col,a)
   if all(dspl[i][a]==col for i in range(3)):win(2,col,a)
  if all(dspl[i][i]==col for i in range(3)):win(3,col)
  if dspl[0][2]==dspl[1][1]==dspl[2][0]==col:win(4,col)
 #Vérification de défaite
 lv=9
 for a in range(3):
  for b in range(3):
   lv=min(jeu[a][b],lv)
 if len(lp[pl-1])==0:win(9,3)
 hv=lp[pl-1][len(lp[pl-1])-1]
 if hv<=lv:win(9,1-(pl-1)+1)

while True:
 fr(0,0,320,222,wh),fr(220,0,100,222,itfc),fr(0,220,222,2,itfc)
 for i in range(2):fr(pos[i+1]-5,0,5,220,n)
 for i in range(2):fr(0,pos[i+1]-5,220,5,n)
 ds("Morpion ",223,10,itfc),ds("V4",298,10,itfc)
 ds("Joueur:",225,60),ds(str(pl),295,60,cl[pl-1]),ds("Coups:0",225,90)
 ds("Rouges:"+str(vc),225,130,re)
 ds("Verts :"+str(vr),225,160,gr)
 ds("Egals :"+str(dr),225,190,bl)
 jeu,dspl=[[0]*3 for i in range(3)],[[0]*3 for i in range(3)]
 lp=[[i for i in range(1,10)]for i in range(2)]
 x=y=px=py=1
 coup,game,new=0,True,True
 while game:
  if new:
   new=False
   fr(pos[px],pos[py],70,70,wh),draw(px,py)
   fr(pos[x],pos[y],70,70,slct),draw(x,y)
   sl(0.1)

  if kd(0)and x>0:x,px,py,new=x-1,x,y,True
  elif kd(1)and y>0:y,px,py,new=y-1,x,y,True
  elif kd(2)and y<2:y,px,py,new=y+1,x,y,True
  elif kd(3)and x<2:x,px,py,new=x+1,x,y,True
  elif kd(4)or kd(52):ok()
