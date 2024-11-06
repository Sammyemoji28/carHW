
import pygame
import time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Spaceship Homework")
screen = pygame.display.set_mode((800,800))

width = 800
height = 800

bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg,(width,height))
car = pygame.image.load("car.png")
carX = 400
carY = 400
angle = 0

keysL = [False,False,False,False]

while carY < 800:
    screen.blit(bg, (0,0))
    screen.blit(car, (carX, carY))
    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keysL[0] = True
                if angle != 270:
                    car = pygame.transform.rotate(car, 270)
                    angle = 270
            elif event.key == pygame.K_DOWN:
                keysL[1] = True
                if angle != 90:
                    car = pygame.transform.rotate(car, 90)
                    angle = 90
            elif event.key == pygame.K_LEFT:
                keysL[2] = True
                if angle != 0:
                    car = pygame.transform.rotate(car, 0)
                    angle = 0
            elif event.key == pygame.K_RIGHT:
                keysL[3] = True
                if angle != 180:
                    car = pygame.transform.rotate(car, 180)
                    angle = 180
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keysL[0] = False
            elif event.key == pygame.K_DOWN:
                keysL[1] = False
            elif event.key == pygame.K_LEFT:
                keysL[2] = False
            elif event.key == pygame.K_RIGHT:
                keysL[3] = False

    if keysL[0]:
        if carY > 0:
            carY -= 5
    if keysL[1]:
        if carY < 700:
            carY += 5
    if keysL[2]:
        if carX > 0:
            carX -= 5
    if keysL[3]:
        if carX < 700:
            carX += 5
    time.sleep(0.1)
    pygame.display.update()