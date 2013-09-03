BeetleMania = "BeetleMania.png"

import pygame, sys
from pygame.locals import *

x = 0
y = 200
size = [640,480]
isMoving = right = left = False
isStill = False
framesPast = 0

beetleJump = {
'One' : [443, 845, 58, 79],
'Two' : [524, 835, 80, 83],
'jumpHeight' : 30,
'cycleState' : 1,
'modifier' : .5,
'isJumping' : False
}
beetleStill = {
'One' : [16, 34, 58, 79],
'Two' : [87, 34, 58, 79],
'Three' : [159, 34, 58, 79],
'Four' : [235, 34, 60, 79],
'cycleState' : 2,
'modifier' : .5,
'isStill' : False
}
beetleWalk = {
'One' : [19, 627, 63, 79],
'Two' : [115, 627, 63, 79],
'Three' : [200,627,63,79],
'Four' : [288,627,63,79],
'Five' : [376,627,68,79],
'cycleState' : 2,
'modifier' : 1,
'isWalking' : False
}

pygame.init()

font2 = pygame.font.SysFont("arial", 40, bold=True)
screen=pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
sprite_sheet = pygame.image.load(BeetleMania).convert_alpha()

while True:
    title_text = font2.render("Mega Monster Beat Down", True, pygame.Color('black'))
    title_textrect = title_text.get_rect()
    title_textrect.top = 25
    title_textrect.left = 75

    for event in pygame.event.get():    #Keybard Input
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        keyState = pygame.key.get_pressed()
        if keyState[K_RIGHT] == True:
            isMoving = True
            right = True
            left = False
            print 'keydown right'
        if keyState[K_LEFT] == True:
            isMoving == True
            left = True
            right = False
            isStill = False
            print 'keydown left'
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                beetleJump['isJumping'] = True
                isMoving = False
                left = False
                right = False
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                print 'keyup left'
                isMoving = False
                left = False
                right = False
            if event.key == K_RIGHT:
                print 'keyup right'
                isMoving = False
                left = False
                right = False

    if isMoving == True:
        if right == True:
            beetleWalk['isWalking']=True
            beetleStill['cycleState'] = 2
        if left == True:
            #Flip Beetle .png
            beetleWalk['isWalking']=True
            beetleStill['cycleState'] = 2
    else:
        beetleWalk['cycleState'] = 2
        isStill = True
        beetleWalk['isWalking']=False

    if x > 640:
        x=-60

    if beetleWalk['cycleState'] >= 5 or beetleWalk['cycleState'] <= 1:
        beetleWalk['modifier']*=-1
    if beetleStill['cycleState'] >=4 or beetleStill['cycleState'] <= 1:
        beetleStill['modifier']*= -1

    if beetleJump['isJumping'] == True:
        if beetleJump['cycleState'] == 1:
            area = pygame.Rect(beetleJump['One'])
        if beetleJump['cycleState'] == 2:
            y-=beetleJump['jumpHeight']
            area = pygame.Rect(beetleJump['Two'])
        if beetleJump['cycleState'] == 3:
            y+=beetleJump['jumpHeight']
            area = pygame.Rect(beetleJump['One'])
        if beetleJump['cycleState'] == 4:
            beetleJump['isJumping'] = False
            beetleJump['cycleState'] = 1
    if isMoving == False and beetleJump['isJumping'] == False:
        if beetleStill['cycleState'] == 1:
            area = pygame.Rect(beetleStill['One'])
        if beetleStill['cycleState'] == 2:
            area = pygame.Rect(beetleStill['Two'])
        if beetleStill['cycleState'] == 3:
            area = pygame.Rect(beetleStill['Three'])
        if beetleStill['cycleState'] == 4:
            area = pygame.Rect(beetleStill['Four'])
    if beetleWalk['isWalking'] == True and beetleJump['isJumping'] == False:
        if beetleWalk['cycleState'] == 1:
            area = pygame.Rect(beetleWalk['One'])
        if beetleWalk['cycleState'] == 2:
            area = pygame.Rect(beetleWalk['Two'])
        if beetleWalk['cycleState'] == 3:
            area = pygame.Rect(beetleWalk['Three'])
        if beetleWalk['cycleState'] == 4:
            area = pygame.Rect(beetleWalk['Four'])
        if beetleWalk['cycleState'] == 5:
            area = pygame.Rect(beetleWalk['Five'])

    #Screen blits
    screen.fill(pygame.Color("white"))
    screen.blit(sprite_sheet, (x,y), area)
    screen.blit(sprite_sheet, (550,375), area)
    screen.blit(title_text, title_textrect)

    if beetleJump['isJumping'] == True:
        beetleJump['cycleState']+=beetleJump['modifier']
    if isMoving == True:
        print "moving "
        if right == True:
            print "right\n"
            x+=11
        if left == True:
            print "left\n"
            x-=11
        beetleWalk['isWalking'] = True
        beetleWalk['cycleState']+=beetleWalk['modifier']
    if isMoving==False:
        beetleStill['cycleState']+=beetleStill['modifier']

    pygame.time.delay(100)
    framesPast+=1

    pygame.display.update()
