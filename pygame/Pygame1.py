import pygame

pygame.init()

win = pygame.display.set_mode((480, 480))  # give a new window
pygame.display.set_caption("First Game")  # name to new window

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
bulletsound = pygame.mixer.Sound ('Sound1.wav')
hitsound = pygame.mixer.Sound ('hit.wav')
music = pygame.mixer.music.load ('music.mp3')

count  = True
score = 0
pygame.mixer.music.play (-1)
class Player(object):
    def __init__(self, x, y, width, hieght):
        self.x = x
        self.y = y
        self.width = width
        self.hieght = hieght
        self.vel = 5
        self.jump = 10
        self.isjump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.count = count
        self.hitbox =  (self.x + 17, self.y + 9, self.width - 35, self.hieght - 9)
    def draw(self, win):
        global count
        
        if count :
            win.blit(char, (man.x, man.y))
            
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            '''else:
                    win.blit(char, (self.x, self.y))'''
        self.hitbox =  (self.x + 17, self.y + 9, self.width - 35, self.hieght - 9)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # creates character (window, color, parameters, fill)
    
    def hit(self):
        self.x = 10
        self.y = 410
        self.isjump = False
        self.jump = 10
        self.walkCount = 0
        font1 = pygame.font.SysFont('unispacebold', 50)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text,(250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i +=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
        
        
class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

clock = pygame.time.Clock()

class Enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'),
             pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'),
             pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'),
            pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'),
            pygame.image.load('L11E.png')]
    def __init__(self, x, y, width, hieght, end):
        self.x = x
        self.y = y
        self.width = width
        self.hieght = hieght
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 3
        self.walkcount = 0
        self.hitbox =  (self.x + 9, self.y + 0, self.width - 15, self.hieght - 8)
        self.health = 10
        self.visible = True
        
    def draw (self, win):
        self.move()
        if self.visible:
            if self.walkcount + 1 >= 33:
                self.walkcount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkcount // 3], (self.x, self.y))
                self.walkcount +=1
            else:
                win.blit(self.walkLeft[self.walkcount // 3], (self.x, self.y))
                self.walkcount +=1
            self.hitbox =  (self.x + 9, self.y + 0, self.width - 19, self.hieght - 8)
            pygame.draw.rect(win, (255, 0, 0), (self.x + 9, self.y, 50, 10), 0)
            pygame.draw.rect(win, (0, 64, 0), (self.x + 9, self.y, 50 - (5 * (10 - self.health) ) ,10 ), 0 )
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        else:
            self.hitbox =  (0,400,0,0,)
        
    def move(self):
        if self.vel > 0:
            if self.vel + self.x < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                walkcount = 0
        else:
            if self.vel + self.x > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                walkcount = 0
                
    def hit(self):
        if self.health > 1: #heallth increments
            self.health -= 1
        else:
            self.visible = False
            self.x = 0
def redrawGameWindow():
    win.blit(bg, (0, 0))  # 2nd parameter is position
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    font = pygame.font.SysFont('unispacebold', 30, True, True) #font, size, bold, italian
    text = font.render("Score: " + str(score), 1, (0,0,0)) # Arguments are: text, anti-aliasing, color
    win.blit(text, (10, 10))
    
    pygame.display.update()     # so the object is updated over screen
    

#MainLoop
run = True
man = Player(400, 400, 64, 64)
goblin = Enemy(10, 410, 64, 64, 480)
bullets = []
shootloop = 0

while run:
    # pygame.time.delay(50)
    clock.tick(27)
    
    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            man.hit()
            score -= 5 

    if shootloop > 0 :
        shootloop += 1
    if shootloop == 3:
        shootloop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitsound.play()
                goblin.hit()
                bullets.pop(bullets.index(bullet))
                score += 1 #score increments
        if bullet.x <= 500 and bullet.x > 0: # bullet boundary to delete
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] and shootloop == 0:
        if man.left:
            facing = -1
        if man.right:
            facing = 1
        if len(bullets) < 5:
            bulletsound.play()
            bullets.append(Projectile(round(man.x + (man.width//2) ), round(man.y + (man.hieght//2) ), 6, (10,10,10), facing))
        shootloop = 1
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
        count = False
    elif keys[pygame.K_RIGHT] and man.x < 430:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
        count = False
    else:
        man.standing = True
        man.walkCount = 0
    if not man.isjump:
        if keys[pygame.K_UP]:
            
            man.isjump = True
            man.walkCount = 0
            count = False
    else:
        if man.jump >= -10:
            neg = 1
            if man.jump < 0:
                neg = -1
            man.y -= (man.jump ** 2) * 0.5 * neg
            man.jump -= 1
        else:
            man.isjump = False
            man.jump = 10

    redrawGameWindow()

pygame.quit()
