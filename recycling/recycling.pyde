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
        self.vx=0 # so the item stops moving
        self.vy=0
        

#add img
overBox = False
locked = False
xOffset = 0.0
yOffset = 0.0
bx= 0 #change this
by= 0 #change this
boxSize=0 #change this


def mousePressed(): #make sure this exists
    locked = True
    # Checking the x and y coordinates for each item so each one can be dragged individually
    for item in game.items:
        if mouseX > item.x and mouseY > item.y and mouseX <= item.x+item.w and mouseY <= item.y+item.h:
            game.itemClicked=item

def mouseDragged():
    if game.itemClicked is not None:
        game.itemClicked.vx=mouseX-pmouseX # previous mouseX so that it saves the change in X value
        game.itemClicked.vy=mouseY-pmouseY
    
def mouseReleased(): #make sure this exists
  locked = False

class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        # Creating an items list for level 1
        Can=Item(0,0,70,70,"can","plastic and cans")
        Water=Item(60,0,70,70,"alain","plastic and cans")
        Chopsticks=Item(120,0,70,70,"chopsticks","general")
        Tissue=Item(180,0,70,70,"tissue","general")
        self.items=[Can,Water,Chopsticks,Tissue]
        self.itemsClicked=None
        
    def display(self):
        for item in self.items:
            item.display()
            item.update()
game=Game(800,600)

def draw():
    background(0)
    game.display()
    
def setup():
    size(800,600)
    background(0)
    bx = width/2
    by = height/2
