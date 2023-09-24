import game
import expectimax
import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Mini Yhatzee')
clock = pygame.time.Clock()

dice1 = pygame.image.load("dice-six-faces-one.png").convert_alpha()
dice1 = pygame.transform.scale(dice1, (100, 100))

dice2 = pygame.image.load("dice-six-faces-two.png").convert_alpha()
dice3 = pygame.image.load("dice-six-faces-three.png").convert_alpha()
dice4 = pygame.image.load("dice-six-faces-four.png").convert_alpha()
dice5 = pygame.image.load("dice-six-faces-five.png").convert_alpha()
dice6 = pygame.image.load("dice-six-faces-six.png").convert_alpha()

dices = [dice1, dice2, dice3, dice4, dice5, dice6]

background = pygame.Surface((800, 400))
background.fill("light blue")
canSelectDice = True
hand = game.Dice()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if canSelectDice:
                d = 0
                for x in range(50, 770, 120):
                    if mouse[0] > x and mouse[0] < x+50 and mouse[1] > 150 and mouse[1] < 200:
                        hand.roll_keeping(d)
                        d += 1
                
    dices = [dices[dice-1] for dice in hand.get_hand()]
    mouse = pygame.mouse.get_pos()
    screen.blit(background, (0, 0)) 
    d = 0
    for x in range(50, 770, 120):
        if d <= 4:
            screen.blit(dices[d], (x, 150))
        d += 1
    
    pygame.display.update()
    clock.tick(60)

