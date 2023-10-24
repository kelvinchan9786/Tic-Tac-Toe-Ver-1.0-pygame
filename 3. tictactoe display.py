import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys
from itertools import product

pygame.init()
pygame.font.init()


screen = pygame.display.set_mode((300, 450))
icon = pygame.image.load(r"icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Tic Tac Toe v.1.0")
FPS = 30
running = True

CROSS_IMAGE = pygame.image.load(r"cross.png")
CROSS_STARTSCREEN = pygame.transform.scale(CROSS_IMAGE, (30, 30))
CIRCLE_IMAGE = pygame.image.load(r"circle.png")
CIRCLE_STARTSCREEN = pygame.transform.scale(CIRCLE_IMAGE, (30, 30))
CROSS = pygame.transform.scale(CROSS_IMAGE, (100, 100))
CIRCLE = pygame.transform.scale(CIRCLE_IMAGE, (100, 100))

font = pygame.font.SysFont("Arial", 20)
fontkelvin = pygame.font.SysFont("Arial", 15)
kelvin = fontkelvin.render("2022 Kelvin Chan, All rights reserved", False, (0, 0, 0))
ver = fontkelvin.render("Ver 1.0", False, (0, 0, 0))
startscreentexttrigger = True
startscreentext = font.render("Choose a symbol that starts first:", False, (0, 0, 0))
playingscreentextcross=font.render("X: What's your move?", False, (0, 0, 0))
playingscreentextcircle=font.render("O: What's your move?", False, (0, 0, 0))
playingtrigger = False
endscreen = False
lineset=[((0, 0), (300, 0)), ((0, 100), (300, 100)), ((0, 200), (300, 200)), ((0, 300), (400, 300)), ((0, 0), (0, 450)), ((100, 0), (100, 300)), ((200, 0), (200, 300)), ((300, 0), (300, 450)), ((0, 450), (300, 450))]
blocksetx = [0, 100, 200]
blocksety = [0, 100, 200]
blockset = []
blocksettemp = list(product(blocksetx, blocksety))
for x in range(0, 9):
    blocksetele = ((blocksettemp[x])[0], (blocksettemp[x])[1], x + 1)
    blockset.append(blocksetele)
blankset = blockset
crossset = set()
circleset = set()
crosswin = False
circlewin= False
winninglist = [{1, 2, 3}, {4, 5 ,6}, {7 ,8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
winner = ""
drawscreentext = font.render("It's a draw.", False, (0, 0, 0))
exitscreentext = font.render("Press this text to exit.", False, (0, 0, 0))
exitscreentextwidth, exitscreentextheight = font.size("Press this text to exit.")
exitscreentextrect = pygame.Rect(10, 350, exitscreentextwidth, exitscreentextheight)
stepnumber = 0


def background():
    screen.fill((255, 255, 255))
    

def griddrawing():
    
    for tempdrawing1 in lineset:
        pygame.draw.line(screen, (0, 0, 0), tempdrawing1[0], tempdrawing1[1], 5)
        
def checkwin(temp02):
    temp02numberonly = set()
    for x in temp02:
        temp02numberonly.add(x[2])
    if len(temp02numberonly) < 3:
        return False
    else:
        for x in winninglist:
            if x.issubset(temp02numberonly):
                return True
                break
            else:
                continue
            
while running:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background()
    griddrawing()
    screen.blit(kelvin, (85, 424))
    screen.blit(ver, (10, 424))
    if startscreentexttrigger:
        screen.blit(startscreentext, (10, 330))
        screen.blit(CROSS_STARTSCREEN, (85, 380))
        screen.blit(CIRCLE_STARTSCREEN, (185, 380))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            CROSS_STARTSCREEN_RECT = pygame.Rect(85, 380, 30, 30)
            CIRCLE_STARTSCREEN_RECT = pygame.Rect(185, 380, 30, 30)
            if CROSS_STARTSCREEN_RECT.collidepoint(mouse_pos):
                startscreentexttrigger = False
                playingtrigger = True
                currentstep = "X"
            if CIRCLE_STARTSCREEN_RECT.collidepoint(mouse_pos):
                startscreentexttrigger = False
                playingtrigger = True
                currentstep = "O"
    else:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(5, 305, 290, 120))
    if playingtrigger and stepnumber < 9:
        if currentstep == "X":
            screen.blit(playingscreentextcross, (10, 330))
        if currentstep == "O":
            screen.blit(playingscreentextcircle, (10, 330))
        for tempplay1 in blankset:
            BLANK_RECT = pygame.Rect(tempplay1[0], tempplay1[1], 100, 100)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos            
                if BLANK_RECT.collidepoint(mouse_pos):                    
                    if currentstep == "X":
                        blankset.remove(tempplay1)
                        crossset.add(tempplay1)
                        currentstep = "O"
                        crosswin = checkwin(crossset)
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(85, 830, 30, 30))
                        stepnumber += 1
                    elif currentstep == "O":
                        blankset.remove(tempplay1)
                        circleset.add(tempplay1)
                        currentstep = "X"
                        circlewin = checkwin(circleset)
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(85, 830, 30, 30))
                        stepnumber += 1
        for tempplay2 in crossset:
            screen.blit(CROSS, (tempplay2[0], tempplay2[1]))
        for tempplay3 in circleset:
            screen.blit(CIRCLE, (tempplay3[0], tempplay3[1]))
        if crosswin == True:
            winner = "X"
            playingtrigger = False
            endscreen = True
        if circlewin == True:
            winner = "O"
            playingtrigger = False
            endscreen = True
        if stepnumber >= 9 and (not crosswin and not circlewin):
            playingtrigger == False
            endscreen = True
            winner = "Draw"
    if endscreen:
        for x in crossset:
            screen.blit(CROSS, (x[0], x[1]))
        for x in circleset:
            screen.blit(CIRCLE, (x[0], x[1]))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(5, 305, 290, 120))
        winningscreentext = font.render(winner + " wins", False, (0, 0, 0))
        if winner == "X" or winner == "O":
            screen.blit(winningscreentext, (10, 330))
        else:
            screen.blit(drawscreentext, (10, 330))
        screen.blit(exitscreentext, (10, 350))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if exitscreentextrect.collidepoint(mouse_pos):
                pygame.quit()
                quit()
        
            
    pygame.display.update()
        
    
                     
    
    
pygame.quit()
