import os
path=os.getcwd()

class Item:
    def __init__(self,x,y,w,h,img,c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path +"/images/"+img+".png")
        self.c = c
        self.vx = 0
        self.vy = 0
        
    def display(self):
        image(self.img,self.x,self.y,self.w,self.h)
        #dragging functionality coded below. translated from java by tom. error checking for braces by jude.

        #replace boxSize with image size
        if mouseX > bx-boxSize and mouseX < bx+boxSize and mouseY > by-boxSize and mouseY < by+boxSize:
            overBox = True
        if locked == False:
            stroke(255)
            fill(153)
        else:
            stroke(153)
            fill(153)
            overBox = False
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        

#add img
overBox = False
locked = False
xOffset = 0.0
yOffset = 0.0
bx= 0 #change this
by= 0 #change this
boxSize=0 #change this

def mouseClicked(): #make sure this exists
    if overBox == True:
        locked = True
    else:
        locked = false
        
    xOffset = mouseX-bx
    yOffset = mouseY-by

def mouseDragged():
    
    bx = mouseX-xOffset
    by = mouseY-yOffset
    
    Can.x=mouseX
    Can.y=mouseY
    
def mouseReleased(): #make sure this exists
  locked = False

Can=Item(0,0,50,50,"can","plastic and cans")

# class Game:


def draw():
    background(0)
    Can.display()
    
def setup():
    size(800,600)
    background(0)
    bx = width/2
    by = height/2
