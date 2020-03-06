add_library('sound')
from random import choice
class Bullet:
    def __init__(self,gun):
        self.x=gun.x + 0.5
        self.y=gun.y + 3
        self.w=15
        self.h=5
        self.img=loadImage("Dart 2.png")
        
    def draw(self):
        stroke(255,255,0)
        strokeWeight(self.h)
        line(self.x, self.y, self.x + self.w, self.y)
        #image(self.img,self.x,self.y,self.w,self.h)
        self.x += 150
        if self.x > width:
            bullet.remove(self)        
class badbullet:
    def __init__(self, enemy):
        self.x=enemy.x 
        self.y=enemy.y + enemy.h/2
        self.w=15
        self.h=5
        
    def draw(self):
        stroke(255,255,0)
        strokeWeight(self.h)
        line(self.x, self.y, self.x + self.w, self.y)
        self.x -= 145
        if self.x < 0:
            badbullets.remove(self)
        


class Gun:
    def __init__(self,gun,x,y,w,h,spc,a,p):
        self.img = gun
        self.gun=loadImage(gun)
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.spc=spc
        self.a=a
        self.p=p
        self.reloadA = a
        
    def update(self):
        if self.img== "Light pistol.png" or self.img== "Heavy Pistol.png":
            self.x=Marcus.x+107
            self.y=Marcus.y+35
        elif self.img== "Starter Pistol.png":
            self.x=Marcus.x+75
            self.y=Marcus.y+35
        elif self.img== "Heavy assault gun.png":
            self.x=Marcus.x+50
            self.y=Marcus.y+10
        elif self.img== "Light assault gun.png":
            self.x=Marcus.x+50
            self.y=Marcus.y+10
        elif self.img=="Heavy Shotgun.png":
           self.x=Marcus.x+50
           self.y=Marcus.y+10
            
    def draw(self):
        image(self.gun,self.x,self.y,self.width,self.height)
        fill(252, 202, 3)
        if start:
            textSize(30)
            text("Ammo Count: " + str(self.a),239,675)
        


class Guy:
    def __init__(self):
        self.imgs=[loadImage("Assault Marcus.png"),loadImage("Pistol Marcus.png")]
        self.x=6 
        self.y=height/2-100
        self.width=150
        self.length=150
        self.guns=[Gun("Starter Pistol.png",width/2,height/2, 75, 35,1, 7, .5),
                   Gun("Light pistol.png",width/2,height/2, 65, 35,1, 7, .5),
                   Gun("Heavy Pistol.png",width/2,height/2, 64, 35,1, 7, .5),
                   Gun("Heavy assault gun.png",width/2,height/2, 90, 50, 1, 7, .5),
                   Gun("Light assault gun.png",width/2,height/2, 90, 50, 1, 7, .5),
                   Gun("Heavy Shotgun.png",width/2,height/2, 90, 55, 1, 7, .5)]
        self.gunindex=0            
        self.currentgun=self.guns[self.gunindex]
        self.enemiesKilled = 0
        self.health=100
    
    def Detect(self):
        global start
        for f in badbullets:
            if f.x + f.w > self.x and f.x < self.x + self.width:
                if f.y + f.h > self.y and f.y < self.y + self.length:
                    badbullets.remove(f)
                    self.health -= 25
                    if self.health <= 0:
                        start=False
                        self.currentgun.x = width/2
                        self.currentgun.y = height/2
             
    def draw(self):
        if self.currentgun == self.guns[0] or self.currentgun == self.guns[1] or  self.currentgun == self.guns[2]:
            self.img=self.imgs[0]
        else:
            self.img=self.imgs[1]
        image(self.img,self.x,self.y,self.width,self.length)
        self.currentgun.update()
        self.currentgun.draw()
        fill(0,255,0)
        rect (99,641,self.health,50)
        fill(255,0,0)
        rect (99+self.health,641,100-self.health,50)
        fill(0, 255, 0)
        textSize(30)
        text("Killed: " + str(self.enemiesKilled),499,675)
        
        
class Badguy:
    def __init__(self):
        self.x=width 
        self.y=choice([252.5,62.5,442.5])
        self.img = loadImage("Enemy.png")
        self.w = 100
        self.h = 100
    
    def draw(self):
        image(self.img,self.x,self.y,self.w,self.h)
        if self.x > width - 300:
            self.x -= 5
            
    def Detect(self):
        for f in bullet:
            if f.x + f.w > self.x:
                if f.y + f.h > self.y and f.y < self.y + self.h:
                
                    Marcus.enemiesKilled+=1
                    
                   
                    if Marcus.enemiesKilled %7==0:
                        Marcus.currentgun.a=Marcus.currentgun.reloadA
                    badguys.remove(self)
                    bullet.remove(f)
                    badguys.append(Badguy())
                    if Marcus.enemiesKilled%10 == 0: #Doubling people
                        badguys.append(Badguy())
                    break
                    
                
        
def setup():
    global Marcus,bg,bullet,startbg,start, badguys, badbullets, totalBadguys, Help, help, Game, prompt, Music
    size (1366, 705)
    guns = ["Heavy assault gun.png", "Light assault gun.png", "Heavy Shotgun.png", "Light Shotgun.png", "Starter Pistol.png", "Heavy Pistol.png", "Light pistol.png", "Heavy Shotgun.png"]
    Marcus=Guy()
    bg=loadImage('Ground.png')
    startbg=loadImage('Startup screen.png')
    bullet=[]
    start=False
    badguys = [Badguy()]
    badbullets = []
    totalBadguys=0
    Help=loadImage("Help.png")
    help=False
    Game=True
    prompt= loadImage("Prompt Screen.png")
    Music = SoundFile(this, "8 Bit Win! Happy Victorious Game Music By HeatleyBros (1).mp3")
    if Music.isPlaying:
        Music.stop()
    Music.loop()
               
                
def draw():
    if start==True:
        if Game:
            image(bg,0,0,width,height)
            Marcus.draw()
            for B in bullet:
                B.draw()
            for badguy in badguys:
                badguy.draw()
                badguy.Detect()
            for b in badbullets:
                b.draw()
            Marcus.Detect()
            if frameCount % 30 == 0:
                badbullets.append(badbullet(badguys[int(random(len(badguys)))]))
        else:
            image(prompt, 0, 0, width, height) 
    elif help:
        image(Help, 0, 0, width, height)
    else:
        image(startbg,0,0,width,height)
        Marcus.currentgun.draw()
        
        

    
def keyPressed():
    if start == True:
        if key=='w'or key =='W'or keyCode==UP:
            if Marcus.y > 73.5:
                Marcus.y+=-190
        if key=='s'or key =='S'or keyCode==DOWN:
            if Marcus.y  < 442:
                Marcus.y+=190
            
def mouseClicked():
    global start, Marcus, totalBadguys,badguys,badbullets, help, Game
    if mouseButton==LEFT:
        if start == True and Game == True:
            if Marcus.currentgun.a > 0 and not(1324<=mouseX<=1354 and 0<=mouseY<=36):
                for i in range(Marcus.currentgun.spc): 
                    bullet.append(Bullet(Marcus.currentgun))
                    Marcus.currentgun.a -= 1
            if 1324<=mouseX<=1354: # x button
                if 0<=mouseY<=36:
                    Game=False
        elif 338<=mouseX<=542: #back button
            if 319<=mouseY<=379:
                Game=True
        elif 714<=mouseX<=961: #quit button
            if 320<=mouseY<=379:
                start=False
                Marcus.guns=[Gun("Starter Pistol.png",width/2,height/2, 75, 35,1, 7, .5),
                Gun("Light pistol.png",width/2,height/2, 65, 35,1, 7, .5),
                Gun("Heavy Pistol.png",width/2,height/2, 64, 35,1, 7, .5),
                Gun("Heavy assault gun.png",width/2,height/2, 90, 50, 1, 7, .5),
                Gun("Light assault gun.png",width/2,height/2, 90, 50, 1, 7, .5),
                Gun("Heavy Shotgun.png",width/2,height/2, 90, 55, 1, 7, .5)]
                Marcus.currentgun=Marcus.guns[Marcus.gunindex]                  
        else:
            Marcus.guns=[Gun("Starter Pistol.png",width/2,height/2, 75, 35,1, 7, .5),
                Gun("Light pistol.png",width/2,height/2, 65, 35,1, 7, .5),
                Gun("Heavy Pistol.png",width/2,height/2, 64, 35,1, 7, .5),
                Gun("Heavy assault gun.png",width/2,height/2, 90, 50, 1, 7, .5),
                Gun("Light assault gun.png",width/2,height/2, 90, 50, 1, 7, .5),
                Gun("Heavy Shotgun.png",width/2,height/2, 90, 55, 1, 7, .5)]
            Marcus.currentgun=Marcus.guns[Marcus.gunindex]
            if 451<mouseX<896 and 564<mouseY<646: #start button
                start=True
                Game=True 
                Marcus.x = 6
                Marcus.y = height/2 - 100
                Marcus.health = 100
                Marcus.enemiesKilled = 0
                totalBadguys = 0
                badguys=[Badguy()]
                badbullets=[]
            if 33<=mouseX<=203:#Left Button in loading screen
                if 302<=mouseY<=400:
                    if Marcus.gunindex!=0:
                        Marcus.gunindex-=1
                    else:
                        Marcus .gunindex=len(Marcus.guns)-1
                    Marcus.currentgun=Marcus.guns[Marcus.gunindex]#Choosing guns
            if 1169<=mouseX<=1330: #Right Button in loading screen
                if 307<=mouseY<=401:
                    if Marcus.gunindex!=len(Marcus.guns)-1:
                        Marcus.gunindex+=1
                    else:
                        Marcus.gunindex=0
                    Marcus.currentgun=Marcus.guns[Marcus.gunindex]
            if 992<=mouseX<=1266: #help button
                if 35<=mouseY<=113:
                    help=True
                    
            if 1201<=mouseX<=1357: #Back Button in help
                if 0<=mouseY<=108:
                    help=False
                    
                    

#YAAAAAAY!
    
