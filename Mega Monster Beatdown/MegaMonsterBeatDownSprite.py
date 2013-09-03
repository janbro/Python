import os, sys
import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', message
    return sound

class beetle(pygame.sprite.Sprite):
    """beetle sprite, main character"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #Call sprite initializer
        self.image, self.rect = load_image('beetleMania(2).png', None)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos


pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Mega Monster Beat Down')
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250,250,250))
beetle = beetle()
allsprites = pygame.sprite.RenderPlain((beetle))
clock = pygame.time.Clock()

screen.blit(background, (0,0))
pygame.display.flip()

while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    allsprites.update()

    screen.blit(background, (0,0))
    allsprites.draw(screen)
    pygame.display.flip()