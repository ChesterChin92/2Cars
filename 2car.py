__author__ = 'John Choo , Chester Chin '

import pygame
pygame.init()
pygame.font.init()
import time
import random
import os

# # # # DISPLAY # # # #
# original 1080, 1920
# TODO design a function for different resolution

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# colour selection list
black = (0, 0, 0)
white = (255, 254, 255)
grey = (102, 102, 102)
whiteGrey = (204, 204, 204)
backgroundBlue = (35, 52, 122)
dividerBlue = (129, 151, 236)
red = (229, 54, 88)
blue = (79, 187, 235)


pygame.display.set_caption('2 Car')
clock = pygame.time.Clock()

# # # # CAR # # # #


carImageRed = pygame.image.load(os.path.join(os.path.join(os.curdir, 'Graphics'), "red-car.png"))
carImageRed = pygame.transform.scale(carImageRed, (54, 96))

carImageBlue = pygame.image.load(os.path.join(os.path.join(os.curdir, 'Graphics'), "blue-car.png"))
carImageBlue = pygame.transform.scale(carImageBlue, (54, 96))

SquareImageRed = pygame.image.load(os.path.join(os.path.join(os.curdir, 'Graphics'), "en-red.jpg"))
SquareImageRed = pygame.transform.scale(SquareImageRed, (54, 54))

SquareImageBlue = pygame.image.load(os.path.join(os.path.join(os.curdir, 'Graphics'), "en-blue.jpg"))
SquareImageBlue = pygame.transform.scale(SquareImageBlue, (54, 54))


ft = pygame.font.Font('fonts/BOOKOS.ttf',60)

running = 1
running_main = 0
while running:
    pygame.event.pump()
    mx, my = pygame.mouse.get_pos()
    lc = pygame.mouse.get_pressed()[0]

    screen.fill((255, 255, 255))

    normal_i = ft.render('Start Game', 1, (0, 0, 0)), ft.size('Normal Mode')

    screen.blit(normal_i[0], (400-normal_i[1][0]/2, 150-normal_i[1][1]/2))
    if 400-normal_i[1][0]/2 < mx < 400+normal_i[1][0]/2 and 150-normal_i[1][1]/2 < my < 150+normal_i[1][1]/2:
        pygame.draw.rect(screen, (255, 0, 0), (400-normal_i[1][0]/2-10, 150-normal_i[1][1]/2-5,normal_i[1][0]+20,normal_i[1][1]+10),4)
        if lc:
            running = 0
            running_main = 1
            # screen.fill((255, 255, 255))

    pygame.display.flip()
    pygame.time.wait(20)


# # # # MAIN # # # #
red_x_pos = 100
red_y_pos = 100
blue_x_pos = 200
blue_y_pos = 200
x = 0
y = 0

def move_circle():
    global x
    global y
    global red_x_pos
    global blue_x_pos
    for counter in range(0,50):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    red_x_pos = red_x_pos - 25

                elif event.key == pygame.K_x:
                    red_x_pos = red_x_pos + 25

                elif event.key == pygame.K_m:
                    blue_x_pos = blue_x_pos - 25

                elif event.key == pygame.K_n:
                    blue_x_pos = blue_x_pos + 25

        x = x + counter
        y = y + counter
        screen.fill((255, 255, 255))
        screen.blit(SquareImageBlue,(x,y))
        screen.blit(carImageRed, (red_x_pos, red_y_pos))
        screen.blit(carImageBlue, (blue_x_pos, blue_y_pos))
        pygame.display.flip()
        pygame.time.wait(20)
        print(x)
        print(y)
        x = 0
        y = 0


while running_main:
    global x
    global y
    screen.fill((255, 255, 255))
    screen.blit(carImageRed, (red_x_pos, red_y_pos))
    screen.blit(carImageBlue, (blue_x_pos, blue_y_pos))
    screen.blit(SquareImageBlue,(x,y))



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                red_x_pos = red_x_pos - 25

            elif event.key == pygame.K_x:
                red_x_pos = red_x_pos + 25

            elif event.key == pygame.K_m:
                blue_x_pos = blue_x_pos - 25

            elif event.key == pygame.K_n:
                blue_x_pos = blue_x_pos + 25

            elif event.key == pygame.K_SPACE:
                print ("Space Key")
                move_circle()




    pygame.display.flip()
    # print(red_x_pos, blue_y_pos)
    pygame.time.wait(20)


# Function


