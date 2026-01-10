import pygame
import cv2
import mediapipe as mp
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
running = True
x , y = 500 , 500
speed = 5
while running == True:
    keys = pygame.key.get_pressed()
    pygame.display.set_caption("title")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_x, mouse_y = pygame.mouse.get_pos()
    x , y = mouse_x , mouse_y
    # if keys[pygame.K_ESCAPE]:
    #     running = False
    # if keys[pygame.K_LEFT] and  0 <= x:
    #     x -= speed
    # if keys[pygame.K_RIGHT] and x <= 700:
    #     x += speed 
    # if keys[pygame.K_UP] and   0 <= y :
    #     y -= speed
    # if keys[pygame.K_DOWN] and y <= 700:
    #     y += speed 
    screen.fill((0,0,0))
    pygame.draw.rect(screen , (255 , 0 , 0) , ( x - 100 , y - 100 , 200 , 200) , 5)
    pygame.draw.rect(screen , (255 , 0 , 0) , ( x , y , 200 , 200) , 5)
    pygame.draw.line(screen , (255, 0 , 0) , (x - 100 , y - 100) , (x , y) , 5)
    pygame.draw.line(screen , (255, 0 , 0) , (x+100 , y - 100) , (x + 200 , y ) , 5)
    pygame.draw.line(screen , (255, 0 , 0) , (x - 100 , y+100) , (x , y + 200) , 5)
    pygame.draw.line(screen , (255, 0 , 0) , (x + 100 , y + 100) , (x + 200 , y + 200) , 5)
    pygame.display.flip()
