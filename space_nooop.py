import pygame as pyg
pyg.init()


wn_x,wn_y = (500,500)
wn = pyg.display.set_mode((wn_x,wn_y))
pyg.display.set_caption("Space Invaders")

#Sprite imports
player = pyg.image.load('player.PNG')
alien_1 = [pyg.image.load('alien_11.PNG'), pyg.image.load('alien_12.PNG')]
alien_2 = [pyg.image.load('alien_21.PNG'), pyg.image.load('alien_22.PNG')]
alien_3 = [pyg.image.load('alien_31.PNG'), pyg.image.load('alien_32.PNG')]

clock = pyg.time.Clock()


x,y = (50,440)
x_char, y_char = (65,50)
vel = 5
isShoot = False
walkCount = 0
step = False
#WALK COUNT FOR aliens change 1 fps between the two

#draw function
def DrawGame():
    global walkCount

    wn.fill((0,0,0))
    if walkCount +1 >= 30:
        walkCount = 0
    if step:
        wn.blit(alien_1[walkCount//15], (x,y))
        walkCount += 1


    #wn.blit(player, (x,y))
    pyg.display.update()

#main loop
run = True
while run:
    clock.tick(30)

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False

    keys = pyg.key.get_pressed()

    if keys[pyg.K_a] and x > vel:
        x -= vel
        step = True
    elif keys[pyg.K_d] and x < wn_x - x_char - vel:
        x += vel
        step = True
    else:
        step = False
        walkCount = 0

    if not(isShoot):
        if keys[pyg.K_SPACE]:
            isShoot = True


    DrawGame()

pyg.quit()
