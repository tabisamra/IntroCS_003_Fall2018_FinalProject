import os
path=os.getcwd()

class Item:
    def __init__(self,x,y,w,h,img,c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path +"/images/"+img+".png")
        self.c = c #c is type - 1 for general, 2 for plastic/can, 3 for paper 
        self.vx = 0
        self.vy = 0
        
    def display(self):
        image(self.img,self.x,self.y,self.w,self.h)
        #dragging functionality coded below. translated from java by tom. error checking for braces by jude.

        #replace objSize with image size
        if mouseX > bx-objSize and mouseX < bx+objSize and mouseY > by-objSize and mouseY < by+objSize:
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
        self.checkWin()
    
    def checkWin(self):
        if self.y > 200:
            if self.c == 1 and 0 <= self.x <= 270:
                #no longer display object -- how?
                game.points += 1 #add one point only -- how?
                # print(game.points)
            if self.c == 2 and 270<self.x<= 540:
                #no longer display object -- how?
                game.points += 1 #add one point only -- how?
                # print(game.points)
            if self.c == 3 and 540 < self.x <=800:
                #no longer display object -- how?
                game.points += 1 #add one point only -- how?
                # print(game.points)
#add img
overBox = False
locked = False
xOffset = 0.0
yOffset = 0.0
bx= 0 #change this
by= 0 #change this
objSize=0 #change this


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
        can = Item(0,0,70,70,"can",2)
        water = Item(60,0,70,70,"alain",2)
        chopsticks=Item(120,0,70,70,"chopsticks",1)
        tissue=Item(180,0,70,70,"tissue",1)
        self.items=[can,water,chopsticks,tissue]
        self.itemsClicked=None
        self.points = 0
        
    def display(self):
        for item in self.items:
            item.display()
            item.update()
        image(loadImage(path +"/images/"+"trashcan.png"),800,600)

game=Game(800,600)

def draw():
    background(0)
    game.display()
    
def setup():
    size(800,600)
    image(loadImage(path +"/images/"+"trashcan.png"),800,600,0,0)
    bx = width/2
    by = height/2
