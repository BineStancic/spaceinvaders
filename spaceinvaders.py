import pygame
pygame.init()


wn_x,wn_y = (500,500)
wn = pygame.display.set_mode((wn_x,wn_y))
pygame.display.set_caption("Space Invaders")

#Sprite imports
player1 = pygame.image.load('player.PNG')
alien_1 = [pygame.image.load('alien_11.PNG'), pygame.image.load('alien_12.PNG')]
alien_2 = [pygame.image.load('alien_21.PNG'), pygame.image.load('alien_22.PNG')]
alien_3 = [pygame.image.load('alien_31.PNG'), pygame.image.load('alien_32.PNG')]

clock = pygame.time.Clock()


class player():
    def __init__(self, x, y, x_char, y_char):
        self.x = x
        self.y = y
        self.x_char = x_char
        self.y_char = y_char
        self.vel = 5
        self.isShoot = False

    def draw(self, wn):
        wn.blit(player1, (self.x, self.y))

class projectile():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8

    def draw(wn):
        pygame.draw.rectangle(win, self. colour, (self.x, self.y), (self.width, self.height))



#WALK COUNT FOR aliens change 1 fps between the two
#class npc():
#    def __init__(self,....)


#draw function
def DrawGame():
    wn.fill((0,0,0))
    buddy.draw(wn)
    pygame.display.update()

#main loop
buddy = player(50, 440, 65, 50)

lasers = []

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for lasers in lasers:
        if laser.y < 500 and laser.y > 0:
            laser.y += laser.vel
        else:
            lasers.pop(lasers.index(laser))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and buddy.x > buddy.vel:
        buddy.x -= buddy.vel
    if keys[pygame.K_d] and buddy.x < wn_x - buddy.x_char - buddy.vel:
        buddy.x += buddy.vel

    if keys[pygame.K_SPACE]:
        if len(lasers) < 5:
            lasers.append(projectile(buddy.x))




    DrawGame()

pygame.quit()
