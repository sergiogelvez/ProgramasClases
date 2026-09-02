import pygame, sys
from pygame.locals import *

# configurar pygame
pygame.init()
# configurar la ventana
superficieVentana = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('¡Hola mundo!')

# estructura similar a TkInter
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO  = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
TURQ = (0, 128, 128)
fuenteBásica = pygame.font.SysFont(None, 48)
texto = fuenteBásica.render('¡Hola mundo!', True, BLANCO, AZUL)
textRect = texto.get_rect()

textRect.centerx = superficieVentana.get_rect().centerx
textRect.centery = superficieVentana.get_rect().centery

superficieVentana.fill(BLANCO)

pygame.draw.polygon(superficieVentana, VERDE, ((130, 23), (291, 106), (236, 277), (56, 277), (0, 106)))

pygame.draw.line(superficieVentana, AZUL, (60, 60), (10, 60), 4)
pygame.draw.line(superficieVentana, AZUL, (120, 60), (60, 100), 10)
pygame.draw.line(superficieVentana, AZUL, (60, 120), (120, 120), 4)

pygame.draw.line(superficieVentana, AZUL, (130, 23), (291, 106), 4)

pygame.draw.circle(superficieVentana, AZUL, (300, 50), 20, 0)

pygame.draw.circle(superficieVentana, TURQ, (100, 50), 10, 3)

pygame.draw.ellipse(superficieVentana, ROJO, (300, 250, 40, 80), 1)
pygame.draw.ellipse(superficieVentana, ROJO, (150, 250, 120, 20), 0)

pygame.draw.line(superficieVentana, NEGRO, (150, 250), (270, 250), 1)
pygame.draw.line(superficieVentana, NEGRO, (150, 270), (270, 270), 1)
pygame.draw.line(superficieVentana, NEGRO, (150, 250), (150, 270), 1)
pygame.draw.line(superficieVentana, NEGRO, (270, 250), (270, 270), 1)

pygame.draw.rect(superficieVentana, ROJO, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

arregloDePíxeles = pygame.PixelArray(superficieVentana)
arregloDePíxeles[480][380] = NEGRO
arregloDePíxeles[480][381] = NEGRO
arregloDePíxeles[481][380] = NEGRO

arregloDePíxeles[480][380] = NEGRO
del arregloDePíxeles

superficieVentana.blit(texto, textRect)

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
