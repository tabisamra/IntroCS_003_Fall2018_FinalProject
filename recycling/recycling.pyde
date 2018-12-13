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
        
    def correct1(self):
        game.points += 10
        self.correctSound.rewind()
        self.correctSound.play()
        game.items1.remove(self)
            
    def correct2(self):
        game.points += 20
        self.x = self.x_o
        self.y = self.y_o
        game.items2.remove(self)
        self.correctSound.rewind()
        self.correctSound.play()
            
    def wrong(self):
        if game.gameLevel ==1:
            game.points -= 5
        elif game.gameLevel ==2:
            game.points -= 10
        self.x = self.x_o
        self.y = self.y_o
        self.wrongSound.rewind()
        self.wrongSound.play()
    
    def checkWin(self):
        if len(game.items1) ==1:
            game.gameLevel =2
        
        if self.y > 250:
            if self.c == 1 and 0 <= self.x <= 270:
                self.correct1()
                
            elif self.c == 1 and self.x > 270:
                self.wrong()
                
            if self.c == 2 and 270<self.x<= 540:
                self.correct1()
                
            elif self.c == 2 and (0< self.x <= 270 or self.x>540):
                self.wrong()
                
            if self.c == 3 and 540 < self.x <=800:
                self.correct1()
                
            elif self.c == 3 and (self.x < 540):
                self.wrong()
            
            #test win for starbucks cup
            if self.img == "starbucks1" and 0 <= self.x <= 270:
                self.img = "starbucks2"
                self.correct1()
                
            elif self.img == "starbucks1" and 270<self.x<= 540:
                self.img = "starbucks3"
                self.correct1()
                
            elif self.img == "starbucks2" and 270<self.x<= 540:
                self.correct2()
            
            elif self.img == "starbucks3" and 0 <= self.x <= 270:
                self.correct2()

            #test win for pizza
            if self.img == "pizza1" and 0 <= self.x <= 270:
                self.img = "pizza2"
                self.correct1()
                
            elif self.img == "pizza1" and 540<self.x<= 800:
                self.img = "pizza3"
                self.correct1()
                
            elif self.img == "pizza2" and 540<self.x<= 800:
                self.correct2()
            
            elif self.img == "pizza3" and 0 <= self.x <= 270:
                self.correct2()

            #test win for fruits
            if self.img == "fruits1" and 0 <= self.x <= 270:
                self.img = "fruits2"
                self.correct1()
                
            elif self.img == "fruits1" and 270<self.x<= 540:
                self.img = "fruits3"
                self.correct1()
                
            elif self.img == "fruits2" and 270<self.x<= 540:
                self.correct2()
            
            elif self.img == "fruits3" and 0 <= self.x <= 270:
                self.correct2()
            # else:
            #     self.wrong()
            

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
    if game.gameLevel ==1:
        for item in game.items1:
            if mouseX > item.x and mouseY > item.y and mouseX <= item.x+item.w and mouseY <= item.y+item.h:
                game.itemClicked=item
    elif game.gameLevel ==2:
        for item in game.items2:
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
        fruits = Item(0,0,80,80,"fruits1",4)
        pizza = Item(70,0,80,80,"pizza1", 5)
        starbucks = Item(140,0,80,80,"starbucks1",4)
        styrofoam = Item(210,0,80,80,"styrofoam1",4)
        self.items1=[can,water,chopsticks,tissue,foil,paper,perrier]
        self.items2 = [fruits,pizza,starbucks]
        self.itemsClicked=None
        self.points = 0
        self.bg = loadImage(path +"/images/"+"trashcan.png")
        self.music = player.loadFile(path+"/sounds/background.mp3")
        self.music.play()
        self.gameLevel = 1
        
    def display1(self):
        image(self.bg,0,0)
        if self.gameLevel ==1:
            for item in self.items1:
                item.display()
                item.update()
    def display2(self):
        image(self.bg,0,0)
        if self.gameLevel == 2:
            for item in self.items2:
                item.display()
                item.update()

game=Game(800,600)

def setup():
    size(800,600)
    global f
    f = createFont("Helvetica",16,True)

def draw():
    background(0)
    if game.gameLevel ==1:
        game.display1()
    elif game.gameLevel ==2:
        game.display2()
    global f
    textFont(f,36)
    fill(255,0,0)
    textAlign(RIGHT)                     
    text("Score: "+str(game.points),750,50)

    
    bx = width/2
    by = height/2
