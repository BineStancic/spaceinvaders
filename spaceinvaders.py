import pygame
import random
pygame.init()


wn_x,wn_y = (600,600)
wn = pygame.display.set_mode((wn_x,wn_y))
pygame.display.set_caption("Space Invaders")

#Sprite imports
player1 = pygame.image.load('player.PNG')
alien_1 = [pygame.image.load('alien_11.PNG'), pygame.image.load('alien_12.PNG')]
alien_2 = [pygame.image.load('alien_21.PNG'), pygame.image.load('alien_22.PNG')]
alien_3 = [pygame.image.load('alien_31.PNG'), pygame.image.load('alien_32.PNG')]
menu = pygame.image.load('menu_image.png')

#sounds
lasersound = pygame.mixer.Sound('shoot.wav')
hitsound = pygame.mixer.Sound('invaderkilled.wav')
gameoversound = pygame.mixer.Sound('Roblox_Death.wav')


#music = pygame.mixer.music.load('')
#pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

score = 0

class player():
    def __init__(self, x, y, x_char, y_char):
        self.x = x
        self.y = y
        self.x_char = x_char
        self.y_char = y_char
        self.vel = 5
        self.hitbox = (self.x, self.y + 10, 70, 50)

    def draw(self, wn):
        wn.blit(player1, (self.x, self.y))
        self.hitbox = (self.x, self.y + 10, 70, 50)
        #pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)

    def hit(self):
        wn.fill((0,0,0))
        pygame.display.update()
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('OOOOOF', 1, (255, 0, 0))
        wn.blit(text, (wn_x/2 - (text.get_width()/2),(wn_y/2 - (text.get_height()/2))))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #keys = pygame.key.get_pressed()
            #if keys[pygame.K_SPACE]:
            #    break




class projectile():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.radius = radius
        self.colour = colour
        self.vel = 8

    def draw(self, wn):
        pygame.draw.rect(wn, self.colour, (self.x, self.y, self.width, self.height))



#WALK COUNT FOR aliens change 1 fps between the two
class npc():
    #alien_1 = [pygame.image.load('alien_11.PNG'), pygame.image.load('alien_12.PNG')]
    #alien_2 = [pygame.image.load('alien_21.PNG'), pygame.image.load('alien_22.PNG')]
    #alien_3 = [pygame.image.load('alien_31.PNG'), pygame.image.load('alien_32.PNG')]

    def __init__(self, x, y, width, height, end, alien_type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.step = 0
        self.vel = 3
        self.hitbox = (self.x, self.y, 50, 45)
        self.life = 0
        self.visible = True
        self.alien_type = alien_type


    def draw(self, wn):
        self.move()
        if self.visible:
            if self.step +1 >= 30:
                self.step = 0
            if self.vel != 0:
                wn.blit(self.alien_type[self.step//15], (self.x,self.y))
                self.step += 1
            self.hitbox = (self.x, self.y, 50, 45)
            #pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel *-1.1
                self.y+=40
                self.step = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel *-1.1
                self.y+=40
                self.step = 0

    def hit(self):
        if self.life > 0:
            self.life -=1
        else:
            self.visible = False
        print('oof')

#draw function
def DrawGame():
    wn.fill((0,0,0))
    buddy.draw(wn)
    for aliens in alienzzz:
        aliens.draw(wn)
    #alienns2.draw(wn)
    for laser in lasers:
        laser.draw(wn)
    text = font.render('Score: ' +str(score), 1, (255,0,0))
    wn.blit(text, (390, 10))
    pygame.display.update()

#main loop
buddy = player(50, wn_y - 60, 65, 50)

alienzzz = [npc(50, 50, 60, 60, 300, alien_1), npc(110, 50, 60, 60, 360, alien_1), npc(170, 50, 60, 60, 420, alien_1), npc(230, 50, 60, 60, 480, alien_1), \
npc(50, 110, 60, 60, 300, alien_2), npc(110, 110, 60, 60, 360, alien_2), npc(170, 110, 60, 60, 420, alien_2), npc(230, 110, 60, 60, 480, alien_2), \
npc(50, 170, 60, 60, 300, alien_3), npc(110, 170, 60, 60, 360, alien_3), npc(170, 170, 60, 60, 420, alien_3), npc(230, 170, 60, 60, 480, alien_3)]
#alienns2 = npc(50, 100, 60, 60, 400)

#fonts
font = pygame.font.SysFont('comicsans', 30, True)

lasers = []
lasertime = 0

alien_lasers = []
alien_lasertime = 0

def game_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        wn.blit(menu,(50,50))
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('SPACE INVADERS', 1, (255, 0, 0))
        wn.blit(text, (wn_x/2 - (text.get_width()/2),(wn_y/6 - (text.get_height()/2))))

        font2 = pygame.font.SysFont('comicsans', 50)
        text2 = font2.render('By Bine Stancic', 1, (255, 0, 0))
        wn.blit(text2, (wn_x/2 - (text2.get_width()/2),(wn_y/1.3 - (text2.get_height()/2))))

        font2 = pygame.font.SysFont('comicsans', 50)
        text2 = font2.render('Hit SPACE to start', 1, (255, 0, 0))
        wn.blit(text2, (wn_x/2 - (text2.get_width()/2),(wn_y/1.2 - (text2.get_height()/2))))

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            break

game_menu()

run = True
while run:
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if lasertime > 0:
        lasertime += 1
    if lasertime > 15:
        lasertime = 0

    for aliens in alienzzz:
        if buddy.hitbox[1] < aliens.hitbox[1] + aliens.hitbox[3] and buddy.hitbox[1] + buddy.hitbox[3]  > aliens.hitbox[1]:
            if buddy.hitbox[0] + buddy.hitbox[2] > aliens.hitbox[0]  and buddy.hitbox[0] < aliens.hitbox[0] + aliens.hitbox[2]:
                #hitsound.play()
                gameoversound.play()
                buddy.hit()

    for laser in lasers:
        for aliens in alienzzz:
            if aliens.visible == True:
                if laser.y - laser.height < aliens.hitbox[1] + aliens.hitbox[3] and laser.y + laser.height > aliens.hitbox[1]:
                    if laser.x + laser.width > aliens.hitbox[0] and laser.x - laser.width < aliens.hitbox[0] + aliens.hitbox[2]:
                        hitsound.play()
                        aliens.hit()
                        #syntax laser hits 2 aliends
                        lasers.pop(lasers.index(laser))
                        score += 1

        if laser.y < wn_y and laser.y > 0:
            laser.y -= laser.vel
        else:
            lasers.pop(lasers.index(laser))

    ###ALIENS Shooting projectiles back
    '''
    if alien_lasertime > 0:
        alien_lasertime += 1
    if alien_lasertime > 15:
        alien_lasertime = 0

    for alien_laser in alien_lasers:
        if aliens.visible == True:

            if alien_laser.y - alien_laser.height < buddy.hitbox[1] + buddy.hitbox[3] and alien_laser.y + alien_laser.height > buddy.hitbox[1]:
                if alien_laser.x + alien_laser.width > buddy.hitbox[0] and alien_laser.x - alien_laser.width < buddy.hitbox[0] + buddy.hitbox[2]:
                    hitsound.play()
                    aliens.hit()
                    #syntax laser hits 2 aliends
                    lasers.pop(lasers.index(laser))
                    score += 1

        if alien_laser.y < wn_y and alien_laser.y > 0:
            alien_laser.y -= alien_laser.vel
        else:
            alien_lasers.pop(alien_lasers.index(alien_laser))
    '''

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and buddy.x > buddy.vel:
        buddy.x -= buddy.vel
    if keys[pygame.K_d] and buddy.x < wn_x - buddy.x_char - buddy.vel:
        buddy.x += buddy.vel


    if keys[pygame.K_SPACE] and lasertime == 0:
        if len(lasers) < 5:
            lasersound.play()
            lasers.append(projectile((buddy.x + buddy.x_char //2), (buddy.y-10), 7, 20, (220,220,220)))
            #print(round(buddy.x + buddy.x_char //2))
        lasertime = 1


    DrawGame()

pygame.quit()
