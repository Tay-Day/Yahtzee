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
dice2 = pygame.transform.scale(dice2, (100, 100))
dice3 = pygame.image.load("dice-six-faces-three.png").convert_alpha()
dice3 = pygame.transform.scale(dice3, (100, 100))
dice4 = pygame.image.load("dice-six-faces-four.png").convert_alpha()
dice4 = pygame.transform.scale(dice4, (100, 100))
dice5 = pygame.image.load("dice-six-faces-five.png").convert_alpha()
dice5 = pygame.transform.scale(dice5, (100, 100))
dice6 = pygame.image.load("dice-six-faces-six.png").convert_alpha()
dice6 = pygame.transform.scale(dice6, (100, 100))

smallfont = pygame.font.SysFont('Corbel',35)
  
text = smallfont.render('Play Game' , True , "Dark Blue")
startButton = pygame.Surface((170, 50))
startButton.fill("white")

smallerfont = pygame.font.SysFont('Corbel', 17)
score = smallerfont.render('Score: ' , True , "Dark Blue")
scoreOutline = pygame.Surface((90, 30))
scoreOutline.fill("white")

rollsLeftText = smallerfont.render('Rolls: ' , True , "Dark Blue")
rollsLeftOutline = pygame.Surface((90, 30))
rollsLeftOutline.fill("white")

bestMoveText = smallerfont.render('Best Move' , True , "Dark Blue")
bestMoveButton = pygame.Surface((90, 30))
bestMoveButton.fill("white")

keepScoreText = smallerfont.render('Keep Score' , True , "Dark Blue")
keepScoreButton = pygame.Surface((90, 30))
keepScoreButton.fill("white")

dices = [dice1, dice2, dice3, dice4, dice5, dice6]
diceBackground = pygame.Surface((120, 120))
diceBackground.fill("white")

RedBackground = pygame.Surface((120, 120))
RedBackground.fill("red")

smallRedBackground = pygame.Surface((100, 40))
smallRedBackground.fill("red")

background = pygame.Surface((800, 400))
background.fill("light blue")

showBestMove = False
canSelectDice = True
hand = game.Dice()
numRolls = 3
score = smallerfont.render(f'Score: {hand.score_hand()}' , True , "Dark Blue")
def resetGame():
    global canSelectDice
    global hand
    global numRolls
    global showBestMove
    canSelectDice = True
    showBestMove = False
    hand.roll()
    numRolls = 3
def checkRollsLeft():
    global canSelectDice
    global numRolls
    if numRolls <= 0:
        canSelectDice = False
        return False
    return True

while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if canSelectDice and checkRollsLeft():
                if mouse[0] > 50 and mouse[0] < 150 and mouse[1] > 150 and mouse[1] < 250:
                    numRolls -= 1
                    hand.roll_keeping(0)
                    showBestMove = False
                if mouse[0] > 200 and mouse[0] < 300 and mouse[1] > 150 and mouse[1] < 250:
                    numRolls -= 1
                    hand.roll_keeping(1)
                    showBestMove = False
                if mouse[0] > 350 and mouse[0] < 450 and mouse[1] > 150 and mouse[1] < 250:
                    numRolls -= 1
                    hand.roll_keeping(2)
                    showBestMove = False
                if mouse[0] > 500 and mouse[0] < 600 and mouse[1] > 150 and mouse[1] < 250:
                    numRolls -= 1
                    hand.roll_keeping(3)
                    showBestMove = False
                if mouse[0] > 650 and mouse[0] < 750 and mouse[1] > 150 and mouse[1] < 250:
                     numRolls -= 1
                     hand.roll_keeping(4)
                     showBestMove = False
                if mouse[0] > 30 and mouse[0] < 120 and mouse[1] > 310 and mouse[1] < 340:
                    showBestMove = True
            if mouse[0] > 30 and mouse[0] < 200 and mouse[1] > 30 and mouse[1] < 80:
                resetGame()
            if mouse[0] > 670 and mouse[0] < 760 and mouse[1] > 310 and mouse[1] < 340:
                resetGame()
    
    score = smallerfont.render(f'Score: {hand.score_hand()}' , True , "Dark Blue")
    rollsLeftText = smallerfont.render(f'Rolls: {numRolls}' , True , "Dark Blue")

    diceHand = [dices[dice-1] for dice in hand.get_hand()]
    screen.blit(background, (0, 0))

    screen.blit(startButton, (30, 30))
    screen.blit(text, (40, 40)) 
    
    screen.blit(scoreOutline, (670, 30))
    screen.blit(score, (675, 37))

    
    screen.blit(rollsLeftOutline, (670, 70))
    screen.blit(rollsLeftText, (675, 77))

    screen.blit(keepScoreButton, (670, 310))
    screen.blit(keepScoreText, (677, 317))

    screen.blit(bestMoveButton, (30, 310))
    screen.blit(bestMoveText, (37, 317))
     
    if mouse[0] > 30 and mouse[0] < 200 and mouse[1] > 30 and mouse[1] < 80:
        startButton.fill("grey")
    else: 
        startButton.fill("white")

    if mouse[0] > 30 and mouse[0] < 120 and mouse[1] > 310 and mouse[1] < 340:
        bestMoveButton.fill("grey")
    else: 
        bestMoveButton.fill("white")
    
    if mouse[0] > 670 and mouse[0] < 760 and mouse[1] > 310 and mouse[1] < 340:
        keepScoreButton.fill("grey")
    else: 
        keepScoreButton.fill("white")
    d = 0
    for x in range(50, 900, 150):
        if d <= 4:
            if mouse[0] > x and mouse[0] < x + 100 and mouse[1] > 150 and mouse[1] < 250:
                screen.blit(diceBackground, (x - 10, 140))
            if showBestMove and d == expectimax.expectimax_Yhatzee(hand, 3 - numRolls):
                screen.blit(RedBackground, (x - 10, 140))
            screen.blit(diceHand[d], (x, 150))
        elif showBestMove and d == 5 and d == expectimax.expectimax_Yhatzee(hand, 3 - numRolls):
            screen.blit(smallRedBackground, (665, 305))
            screen.blit(keepScoreButton, (670, 310))
            screen.blit(keepScoreText, (677, 317))
        d += 1
    
    pygame.display.update()
    clock.tick(60)

