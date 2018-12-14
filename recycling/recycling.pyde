## Developers: Jude AlSharif and Tom Abi Samra
## The purpose of this game is to teach NYUAD community members how to recycle efficiently on campus.
## We used images from the internet and illustrations by the team.
## Click run in Processing 3.py to start the game


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
        self.name = img
        self.img = loadImage(path +"/images/"+self.name+".png")
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
    #win level 1    
    def correct1(self):
        game.points += 10
        self.correctSound.rewind()
        self.correctSound.play()
        game.items1.remove(self)
        if len(game.items1) == 0:
            game.gameLevel = 2
            
    #win 1 level 1        
    def correct2(self):
        game.points += 20
        self.x = self.x_o
        self.y = self.y_o
        self.correctSound.rewind()
        self.correctSound.play()
        
     #win 2 level 2   
    def correct3(self):
        game.points += 20
        self.correctSound.rewind()
        self.correctSound.play()
        game.items2.remove(self)
        if len(game.items2) == 0:
            game.gameLevel = 3

            
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
        if len(game.items1) ==0:
            game.gameLevel =2
        if len(game.items2) ==0:
            game.gameLevel =3
        
        if self.y > 250:
            if self.c == 1 and 0 <= self.x <= 270:
                self.correct1()
                
            elif self.c == 1 and self.x > 270:
                self.wrong()
                
            elif self.c == 2 and 270<self.x<= 540:
                self.correct1()
                
            elif self.c == 2 and (0< self.x <= 270 or self.x>540):
                self.wrong()
                
            elif self.c == 3 and 540 < self.x <=800:
                self.correct1()
                
            elif self.c == 3 and (self.x < 540):
                self.wrong()
            
            #test win for starbucks cup
            elif self.name == "starbucks1" and 0 <= self.x <= 270:
                self.name = "starbucks2"
                self.img = loadImage(path +"/images/"+self.name+".png")
                self.correct2()
                    
            elif self.name == "starbucks1" and 270<self.x<= 540:
                self.name = "starbucks3"
                self.img = loadImage(path +"/images/"+self.name+".png")
                self.correct2()

            elif self.name == "starbucks2" and 270<self.x<= 540:
                self.correct3()
            
            elif self.name == "starbucks3" and 0 <= self.x <= 270:
                self.correct3()

            #test win for pizza
            elif self.name == "pizza1" and 0 <= self.x <= 270:
                self.name = "pizza2"
                self.img = loadImage(path +"/images/"+self.name+".png")
                self.correct2()
                    
            elif self.name == "pizza1" and 540<self.x<= 800:
                self.name = "pizza3"
                self.img = loadImage(path +"/images/"+self.name+".png")
                self.correct2()
                
            elif self.name == "pizza2" and 540<self.x<= 800:
                self.correct3()
            
            elif self.name == "pizza3" and 0 <= self.x <= 270:
                self.correct3()

            #test win for fruits
            elif self.name == "fruits1" and 0 <= self.x <= 270:
                self.name = "fruits2"
                self.img = loadImage(path +"/images/"+self.name+".png")
                self.correct2()
                    
            elif self.name == "fruits1" and 270<self.x<= 540:
                self.name = "fruits3"
                self.img = loadImage(path +"/images/"+self.name+".png")
                self.correct2()
                
            elif self.name == "fruits2" and 270<self.x<= 540:
                self.correct3()
            
            elif self.name == "fruits3" and 0 <= self.x <= 270:
                self.correct3()
            
            #test for styrofoam
            elif self.name == "styrofoam1" and 0 <= self.x <= 270:
                self.name = "styrofoam2"
                self.img = loadImage(path +"/images/"+self.name+".png")
                self.correct2()
                    
            elif self.name == "styrofoam1" and 270<self.x<= 540:
                self.name = "styrofoam3"
                self.img = loadImage(path +"/images/"+self.name+".png")
                self.correct2()
                
            elif self.name == "styrofoam2" and 270<self.x<= 540:
                self.correct3()
            
            elif self.name == "styrofoam3" and 0 <= self.x <= 270:
                self.correct3()
            
            else:
                self.wrong()
                
 #game class            
class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        # Creating an items list for level 1
        can = Item(0,0,85,85,"can",2)
        water = Item(85,0,85,85,"alain",2)
        chopsticks=Item(170,0,85,85,"chopsticks",1)
        tissue=Item(255,0,85,85,"tissue",1)
        foil = Item(340,0,85,85,"foil",1)
        paper = Item(425,0,85,85,"paper",3)
        perrier = Item(510,0,85,85,"perrier",1)
        #creating items for level 2
        fruits = Item(0,0,100,130,"fruits1",4)
        pizza = Item(85,0,200,133,"pizza1", 5)
        starbucks = Item(270,0,100,120,"starbucks1",4)
        styrofoam = Item(400,10,85,100,"styrofoam1",4)
        self.items1=[can,water,chopsticks,tissue,foil,paper,perrier]
        self.items2 = [fruits,pizza,starbucks,styrofoam]
        self.itemsClicked=None
        self.points = 0
        self.bg = loadImage(path +"/images/"+"trashcan.png")
        self.bg3 = loadImage(path+"/images/"+"campus.png")
        self.music = player.loadFile(path+"/sounds/background.mp3")
        self.music.play()
        self.gameLevel = 0
        
     #display for level 1   
    def display1(self):
        if self.gameLevel ==1:
            image(self.bg,0,0)
            for item in self.items1:
                item.display()
                item.update()
   #display for level 2             
    def display2(self):
        if self.gameLevel == 2:
            image(self.bg,0,0)
            for item in self.items2:
                item.display()
                item.update()


overBox = False
locked = False
xOffset = 0.0
yOffset = 0.0
bx= 0 
by= 0 
objSize=0 


def mousePressed(): 
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
#dragging
def mouseDragged():
    if game.gameLevel != 0 and game.gameLevel != -1:
        if game.itemClicked is not None:
            game.itemClicked.vx=2*(mouseX-pmouseX) # previous mouseX so that it saves the change in X value
            game.itemClicked.vy=2*(mouseY-pmouseY)
    
def mouseReleased(): 
  locked = False

def mouseClicked():
    if game.gameLevel == 0:
        if 350 < mouseX < 450 and 270 < mouseY < 330:
            game.gameLevel=1
            game.music.play()
        if 320 < mouseX < 470 and 370 < mouseY < 430:
            game.gameLevel =-1
            
    if game.gameLevel == -1:
        if 20 < mouseX < 120 and 500 < mouseY < 600:
            game.gameLevel=1
            game.music.play()


game=Game(800,600)

def setup():
    size(800,600)
    global f
    f = createFont("Helvetica",16,True)

def draw():
    background(0)
    
    #menu
    if game.gameLevel == 0:
        background(0)
        global f
        textFont(f,50)
        textAlign(CENTER)
        
        fill(0,255,0)
        text("RECYCLING AT NYUAD", 400, 150)    
        
        if 350 < mouseX < 450 and 270 < mouseY < 330:
            fill(255,0,0)
            text("Play!",400,300)
        else:
            fill(255,255,255)                    
            text("Play!",400,300)
            
        if 320 < mouseX < 470 and 370 < mouseY < 430:
            fill(255,0,0)
            text("Instructions",400,400)
        else:
            fill(255,255,255) 
            text("Instructions",400,400)
            
    if game.gameLevel == -1:
        background(0)
        global f
        textFont(f,30)
        textAlign(LEFT)    
        
        text("For level 1, you will get items that you will need to drag \n and drop in the appropriate recycling bin. You will lose \n 5 points for every wrong attempt and gain 10 points for \n every correct answer! In level 2, you will need to also \n drag and drop, but the items need to be divided \n for the most efficient recycling. You will lose 10 points \n for every wrong attempt and gain 20 points \n for every correct attempt.",20,50)

        
        if 20 < mouseX < 120 and 500 < mouseY < 600:
            fill(255,0,0)
            text("Play!",50,550)
        else:
            fill(255,255,255)                    
            text("Play!",50,550)
            
      #finish screen  
    if game.gameLevel == 3:
        background(0)
        global f
        textFont(f,30)
        textAlign(LEFT)    
        
        text("CONGRATS! YOU COMPLETED THE GAME \n WITH THE SCORE OF \n "+str(game.points), 50,50)
        

        
    if game.gameLevel == 1:
        game.display1()
    elif game.gameLevel == 2:
        game.display2()
    if game.gameLevel != 0 and game.gameLevel != -1 and game.gameLevel != 3:
        global f
        textFont(f,36)
        fill(255,0,0)
        textAlign(RIGHT)                     
        text("Score: "+str(game.points),750,50)

    
    bx = width/2
    by = height/2
