import pygame
pygame.init()


wn_x,wn_y = (500,500)
wn = pygame.display.set_mode((wn_x,wn_y))
pygame.display.set_caption("Space Invaders")

#Sprite imports
player1 = pygame.image.load('player.PNG')

clock = pygame.time.Clock()


class player():
    def __init__(self, x, y, x_char, y_char):
        self.x = x
        self.y = y
        self.x_char = x_char
        self.y_char = y_char
        self.vel = 5
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, wn):
        wn.blit(player1, (self.x, self.y))
        self.hitbox = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)

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
    alien_1 = [pygame.image.load('alien_11.PNG'), pygame.image.load('alien_12.PNG')]
    alien_2 = [pygame.image.load('alien_21.PNG'), pygame.image.load('alien_22.PNG')]
    alien_3 = [pygame.image.load('alien_31.PNG'), pygame.image.load('alien_32.PNG')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.step = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)


    def draw(self, wn):
        self.move()
        if self.step +1 >= 30:
            self.step = 0
        if self.vel != 0:
            wn.blit(self.alien_1[self.step//15], (self.x,self.y))
            self.step += 1
        self.hitbox = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel *-1
                self.step = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel *-1
                self.step = 0

    def hit(self):
        print('oof')

#draw function
def DrawGame():
    wn.fill((0,0,0))
    buddy.draw(wn)
    aliens.draw(wn)
    alienns2.draw(wn)
    for laser in lasers:
        laser.draw(wn)
    pygame.display.update()

#main loop
buddy = player(50, 440, 65, 50)
aliens = npc(50, 50, 60, 60, 300)
alienns2 = npc(50, 100, 60, 60, 400)

lasers = []
lasertime = 0

run = True
while run:
    clock.tick(30)

    if lasertime > 0:
        lasertime += 1
    if lasertime > 15:
        lasertime = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for laser in lasers:
        if laser.y - laser.height < aliens.hitbox[1] + aliens.hitbox[3] and laser.y + laser.height > aliens.hitbox[1]:
            if laser.x + laser.width > aliens.hitbox[0] and laser.x - laser.width < aliens.hitbox[0] + aliens.hitbox[2]:
                aliens.hit()
                lasers.pop(lasers.index(laser))

        if laser.y < wn_y and laser.y > 0:
            laser.y -= laser.vel
        else:
            lasers.pop(lasers.index(laser))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and buddy.x > buddy.vel:
        buddy.x -= buddy.vel
    if keys[pygame.K_d] and buddy.x < wn_x - buddy.x_char - buddy.vel:
        buddy.x += buddy.vel


    if keys[pygame.K_SPACE] and lasertime == 0:
        if len(lasers) < 5:
            lasers.append(projectile((buddy.x + buddy.x_char //2), (buddy.y-10), 7, 20, (220,220,220)))
            #print(round(buddy.x + buddy.x_char //2))
        lasertime = 1


    DrawGame()

pygame.quit()
