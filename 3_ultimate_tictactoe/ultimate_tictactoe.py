#Cree le 8 Octobre 2023
from math import pi,cos,sin
from kandinsky import fill_rect,draw_string,set_pixel
from ion import keydown
from time import sleep

selection=(0,255,0)
interface=(255,181,59)
n=(0,0,0)
bleu=(0,0,255)
rouge=(255,0,0)
vert=(0,200,0)
blanc=(255,255,255)

grand=[0,75,150]
petit=[0,24,48,75,99,123,150,174,198]

joueur=1
vc,vr,eq=0,0,0

def paradroi(x,y,w,h,c):
  for a in range(w):
    for b in range(h):
      x+=1
      set_pixel(x,y,c)
    x-=h
    y+=1
    x+=1
def paragau(x,y,w,h,c):
  for a in range(w):
    x-=h
    y+=1
    x-=1
    for b in range(h):
      x+=1
      set_pixel(x,y,c)

def cercle(cx,cy,r,c):
   for rep in range(4*r*pi):
    adj=cos(rep)*r
    x=cx+adj
    opp=sin(rep)*r
    y=cy+opp
    fill_rect(int(x),int(y),1,-2*int(opp),c)

def croix(x,y,p):
  if p==1:w,h,pxp,pyp=16,4,20,3
  elif p==2:w,h,pxp,pyp=55,8,60,7
  paradroi(x,y+pyp,w,h,rouge)
  paragau(x+pxp,y+pyp-1,w,h,rouge)
def rond(x,y,p):
  if p==1:r=8
  elif p==2:r=30
  cercle(x+11,y+11,r,vert)

def l(x,y,d,m):
  if d==1:w,h,plx,ply=60*m,4*m,5,9
  elif d==2:w,h,plx,ply=4*m,60*m,9,5
  fill_rect(x+plx,y+ply,w,h,n)

def victoire(e):
  global vc,vr,eq
  sleep(2)
  fill_rect(0,0,320,222,interface)
  if e!=0:
    draw_string("Victoire des ",60,102)
    if e==1:
      draw_string("croix !",190,102)
      vc+=1
    elif e==2:
      draw_string("ronds !",190,102)
      vr+=1
  else:
    draw_string("Egalité !",115,108)
    eq+=1
  sleep(3)

while True:
  fill_rect(0,0,320,222,blanc)
  fill_rect(220,0,100,222,interface)
  fill_rect(0,220,222,2,interface)
  for i in range(9):
    fill_rect(0,petit[i]-2,220,2,bleu)
  for i in range(9):
    fill_rect(petit[i]-2,0,2,220,bleu)
  for i in range(2):
    fill_rect(grand[i+1]-5,0,5,220,n)
  for i in range(2):
    fill_rect(0,grand[i+1]-5,220,5,n)
  draw_string("Morpion ",223,10,interface)
  draw_string("V2",298,10,interface)
  draw_string("Joueur: ",225,60)
  draw_string("Coups:",225,90)
  draw_string("Croix:"+str(vc),225,140,rouge)
  draw_string("Ronds:"+str(vr),225,170,vert)
  draw_string("Egal :"+str(eq),225,200,bleu)
  jeu=[[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]]
  gjeu=[[0,0,0],
        [0,0,0],
        [0,0,0]]
  xj,yj,x,y=1,1,1,1
  pxj,pyj,px,py=xj,yj,x,y
  coup=0
  game=True
  new=True
  ok=False
  while game:
    if new:
      new=False
      if joueur==1:draw_string(str(joueur),295,60,rouge)
      elif joueur==2:draw_string(str(joueur),295,60,vert)
      draw_string(str(coup),285,90)
      if not ok:
        fill_rect(petit[pxj*3+px],petit[pyj*3+py],22,22,blanc)
        if jeu[pyj*3+py][pxj*3+px]==1:croix(petit[pxj*3+px],petit[pyj*3+py],1)
        elif jeu[pyj*3+py][pxj*3+px]==2:rond(petit[pxj*3+px],petit[pyj*3+py],1)
      else:ok=False
      fill_rect(petit[xj*3+x],petit[yj*3+y],22,22,selection)
      if jeu[yj*3+y][xj*3+x]==1:croix(petit[xj*3+x],petit[yj*3+y],1)
      elif jeu[yj*3+y][xj*3+x]==2:rond(petit[xj*3+x],petit[yj*3+y],1)
      pxj,pyj=xj,yj
      sleep(0.1)

    if keydown(4)or keydown(52):
      if jeu[yj*3+y][xj*3+x]==0:
        ok=True
        if joueur==2:coup+=1
        fill_rect(petit[xj*3+x],petit[yj*3+y],22,22,blanc)
        if joueur==1:
          croix(petit[xj*3+x],petit[yj*3+y],1)
          jeu[yj*3+y][xj*3+x]=1
          joueur=2
        elif joueur==2:
          rond(petit[xj*3+x],petit[yj*3+y],1)
          jeu[yj*3+y][xj*3+x]=2
          joueur=1
        pxj,pyj=xj,yj
        r,s=x,y
        x,y=1,1
        new=True
        sleep(0.1)
      for a in range(1,3):
        for b in range(3):
          for c in range(3):
            for d in range(3):
              if jeu[c*3+d][b*3]==a and jeu[c*3+d][b*3+1]==a and jeu[c*3+d][b*3+2]==a:
                l(petit[b*3],petit[c*3+d],1,1)
                sleep(1)
                fill_rect(grand[b],grand[c],70,70,blanc)
                if a==1:croix(grand[b]+5,grand[c],2)
                elif a==2:rond(grand[b]+25,grand[c]+25,2)
                gjeu[c][b]=a
                for e in range(3):
                  for f in range(3):
                    jeu[pyj*3+e][pxj*3+f]=3
            for e in range(3):
              if jeu[c*3][b*3+e]==a and jeu[c*3+1][b*3+e]==a and jeu[c*3+2][b*3+e]==a:
                l(petit[b*3+e],petit[c*3],2,1)
                sleep(1)
                fill_rect(grand[b],grand[c],70,70,blanc)
                if a==1:croix(grand[b]+5,grand[c],2)
                elif a==2:rond(grand[b]+25,grand[c]+25,2)
                gjeu[c][b]=a
                for e in range(3):
                  for f in range(3):
                    jeu[pyj*3+e][pxj*3+f]=3
            if jeu[c*3][b*3]==a and jeu[c*3+1][b*3+1]==a and jeu[c*3+2][b*3+2]==a:
              paradroi(petit[b*3]+3,petit[c*3]+5,60,5,n)
              sleep(1)
              fill_rect(grand[b],grand[c],70,70,blanc)
              if a==1:croix(grand[b]+5,grand[c],2)
              elif a==2:rond(grand[b]+25,grand[c]+25,2)
              gjeu[c][b]=a
              for e in range(3):
                for f in range(3):
                  jeu[pyj*3+e][pxj*3+f]=3
            if jeu[c*3+2][b*3]==a and jeu[c*3+1][b*3+1]==a and jeu[c*3][b*3+2]==a:
              paragau(petit[b*3]+67,petit[c*3]+5,60,5,n)
              sleep(1)
              fill_rect(grand[b],grand[c],70,70,blanc)
              if a==1:croix(grand[b]+5,grand[c],2)
              elif a==2:rond(grand[b]+25,grand[c]+25,2)
              gjeu[c][b]=a
              for e in range(3):
                for f in range(3):
                  jeu[pyj*3+e][pxj*3+f]=3
            eg,cr,ro=0,0,0
            for i in range(3):
              for j in range(3):
                if jeu[b*3+i][c*3+j]==1 or jeu[b*3+i][c*3+j]==2:
                  eg+=1
                if jeu[b*3+i][c*3+j]==1:
                  cr+=1
                if jeu[b*3+i][c*3+j]==2:
                  ro+=1
            if eg==9:
              if cr>ro:croix(grand[c]+5,grand[b],2)
              elif ro>cr:rond(grand[c]+25,grand[b]+25,2)
              gjeu[c][b]=a
          if gjeu[b][0]==a and gjeu[b][1]==a and gjeu[b][2]==a:
            l(grand[0]+15,grand[b]+20,1,3)
            victoire(a)
            game=False
          elif gjeu[0][b]==a and gjeu[1][b]==a and gjeu[2][b]==a:
            l(grand[b]+20,grand[0]+15,2,3)
            victoire(a)
            game=False
        if gjeu[0][0]==a and gjeu[1][1]==a and gjeu[2][2]==a:
          paradroi(grand[0]+5,grand[0]+15,190,20,n)
          victoire(a)
          game=False
        elif gjeu[0][2]==a and gjeu[1][1]==a and gjeu[2][0]==a:
          paragau(grand[2]+65,grand[0]+15,190,20,n)
          victoire(a)
          game=False
        if game:
          for o in range(3):
            for p in range(3):
              f=0
              if gjeu[o][p]!=0:f+=1
              if f==9:
                victoire(0)
                game=False
      if gjeu[s][r]==0:
        xj,yj=r,s
      else:
        for k in reversed(range(3)):
          for m in reversed(range(3)):
            if gjeu[k][m]==0:
              xj,yj=m,k
    elif keydown(1):
      px,py=x,y
      if y>0:y-=1
      new=True
    elif keydown(2):
      px,py=x,y
      if y<2:y+=1
      new=True
    elif keydown(3):
      px,py=x,y
      if x<2:x+=1
      new=True
    elif keydown(0):
      px,py=x,y
      if x>0:x-=1
      new=True
