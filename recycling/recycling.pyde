import os
add_library("minim")
path=os.getcwd()
player = Minim(this)

class Item:
    def __init__(self,x,y,w,h,img,c):
        self.x = x
        self.x_o = x
        self.y = y
        self.y_o = y
        self.w = w
        self.h = h
        self.img = loadImage(path +"/images/"+img+".png")
        self.c = c #c is type - 1 for general, 2 for plastic/can, 3 for paper 
        self.vx = 0
        self.vy = 0
        self.correctSound = player.loadFile(path+"/sounds/correct.mp3")
        self.wrongSound = player.loadFile(path+"/sounds/wrong.mp3")

        
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
        
    def correct(self):
        game.points += 10
        game.items.remove(self)
        self.correctSound.rewind()
        self.correctSound.play()
    
    def wrong(self):
        game.points -= 5
        self.x = self.x_o
        self.y = self.y_o
        self.wrongSound.rewind()
        self.wrongSound.play()
    
    def checkWin(self):
        if self.y > 250:
            if self.c == 1 and 0 <= self.x <= 270:
                self.correct()
                
            elif self.c == 1 and self.x > 270:
                self.wrong()
                
            if self.c == 2 and 270<self.x<= 540:
                self.correct()
                
            elif self.c == 2 and (0< self.x <= 270 or self.x>540):
                self.wrong()
                
            if self.c == 3 and 540 < self.x <=800:
                self.correct()
                
            elif self.c == 3 and (self.x < 540):
                self.wrong()

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
        # game.itemClicked.x=mouseX # previous mouseX so that it saves the change in X value
        # game.itemClicked.y=mouseY
        game.itemClicked.vx=2*(mouseX-pmouseX) # previous mouseX so that it saves the change in X value
        game.itemClicked.vy=2*(mouseY-pmouseY)
    
def mouseReleased(): #make sure this exists
  locked = False

class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        # Creating an items list for level 1
        can = Item(0,0,80,80,"can",2)
        water = Item(70,0,80,80,"alain",2)
        chopsticks=Item(140,0,80,80,"chopsticks",1)
        tissue=Item(210,0,80,80,"tissue",1)
        foil = Item(290,0,80,80,"foil",1)
        paper = Item(380,0,80,80,"paper",3)
        perrier = Item(460,0,80,80,"perrier",1)
        self.items=[can,water,chopsticks,tissue,foil,paper,perrier]
        self.itemsClicked=None
        self.points = 0
        self.bg = loadImage(path +"/images/"+"trashcan.png")
        self.music = player.loadFile(path+"/sounds/background.mp3")
        self.music.setVolume(0.1)
        self.music.play()
        
    def display(self):
        image(self.bg,0,0)
        for item in self.items:
            item.display()
            item.update()
game=Game(800,600)

def setup():
    size(800,600)
    global f
    f = createFont("Helvetica",16,True)

def draw():
    background(0)
    game.display()
    global f
    textFont(f,36)
    fill(255,0,0)
    textAlign(RIGHT)                     
    text("Score: "+str(game.points),750,50)

    
    bx = width/2
    by = height/2
