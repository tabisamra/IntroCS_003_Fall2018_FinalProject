import os
path=os.getcwd()

class Item:
    def __init__(self,x,y,w,h,img,c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path +"/images"+img+".png")
        self.c = c
    
    def display(self):
        image(self.img,self.x,self.y,self.w,self.h)
        

#add img
overBox = False
locked = False
xOffset = 0.0
yOffset = 0.0

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

mousePressed(): #make sure this exists
    if overBox == True:
        locked = True
    else:
        locked = false
        
    xOffset = mouseX-bx
    yOffset = mouseY-by; 

mouseDragged():
  if locked == True:
    bx = mouseX-xOffset
    by = mouseY-yOffset
    
mouseReleased(): #make sure this exists
  locked = False
    
    

# class Game:


def draw():
    background(0)
    
def setup():
    size(800,600)
    background(0)
    bx = width/2
    by = height/2
