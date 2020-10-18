import pygame as pg
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import random
from time import sleep

# screen
pg.init()
height = 500
length = 1000
screen = pg.display.set_mode((length, height))
pg.display.set_caption('Stone Paper Scissors')
game_started = False

# images
title_img = pg.image.load('Title.png')
click_text_img = pg.image.load('click.png')
win = pg.image.load('win.png')
lose = pg.image.load('lose.png')
draw = pg.image.load('draw.png')
scissor_img = pg.image.load('Scissors.png')
stone_img = pg.image.load('Stone.png')
paper_img = pg.image.load('Paper.png')
images = (scissor_img, stone_img, paper_img)
left = None
right = None

# icon
stone_icon = [pg.transform.scale(stone_img, (64, 64)), (300, 400)]
paper_icon = [pg.transform.scale(paper_img, (64, 64)), (350, 400)]
scissor_icon = [pg.transform.scale(scissor_img, (64, 64)), (400, 400)]
icon_size = 64

# mouse
mouse_clicked = False
mouse_loc = None


def display_left(img):
    img = pg.transform.rotate(img, 90)
    img = pg.transform.flip(img, True, False)
    screen.blit(img, (10, 50))


def display_right(img):
    img = pg.transform.rotate(img, 90)
    screen.blit(img, (600, 50))


def decide(comp, player):
    if player == scissor_img and comp == stone_img:
        return lose
    elif player == scissor_img and comp == paper_img:
        return win
    elif player == stone_img and comp == paper_img:
        return lose
    elif player == stone_img and comp == scissor_img:
        return win
    elif player == paper_img and comp == scissor_img:
        return lose
    elif player == paper_img and comp == stone_img:
        return win
    else:
        return draw


def check_bounds():
    global right, running, left
    if mouse_clicked:
        if stone_icon[1][0] < mouse_loc[0] < stone_icon[1][0] + icon_size:
            if stone_icon[1][1] < mouse_loc[1] < stone_icon[1][1] + icon_size:
                right = stone_img
        elif paper_icon[1][0] < mouse_loc[0] < paper_icon[1][0] + icon_size:
            if paper_icon[1][1] < mouse_loc[1] < paper_icon[1][1] + icon_size:
                right = paper_img
        elif scissor_icon[1][0] < mouse_loc[0] < scissor_icon[1][0] + icon_size:
            if scissor_icon[1][1] < mouse_loc[1] < scissor_icon[1][1] + icon_size:
                right = scissor_img
        else:
            return
        display_right(right)
        screen.blit(decide(left, right), (450, 0))
        pg.display.update()
        sleep(2)
        # running = False
        right = None


running = True
while running:
    mouse_loc = pg.mouse.get_pos()
    if pg.mouse.get_pressed()[0]:
        mouse_clicked = True

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == GAME_GLOBALS.K_SPACE:
                game_started = True

    if game_started:
        screen.fill((255, 255, 255))
        screen.blit(stone_icon[0], stone_icon[1])
        screen.blit(scissor_icon[0], scissor_icon[1])
        screen.blit(paper_icon[0], paper_icon[1])
        screen.blit(click_text_img, (470, 400))

        if mouse_clicked:
            left = random.choice(images)
            display_left(left)
            check_bounds()
            sleep(0.5)
            mouse_clicked = False
            left = None
        else:
            left = random.choice(images)
            display_left(left)
        sleep(0.2)
    else:
        screen.blit(title_img, (0, 0))
    pg.display.update()
