import math
import random
import pygame

pygame.init()


block_size = 5
grid_size = 100

display_width = grid_size*block_size
display_height = grid_size*block_size
black = (0,0,0)
white = (255,255,255)
red =(255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
clock.tick(1)

def print_array(a):
    for i in a: print(i)

def draw_array(a,x_size,y_size, colour):
    gameDisplay.fill(black)
    for i in range(x_size):
        for j in range(y_size):
            if a[i][j]==1:
                pygame.draw.rect(gameDisplay,colour,[j*block_size,i*block_size,block_size,block_size])
    pygame.display.update()

def create_grid(a, x_size, y_size):
    for i in range(x_size):
        a.append([])
        for j in range(y_size):
            a[i].append(math.floor(random.random()+0.3))
    return a

def check_neighbours(a,x,y):
    count = 0
    for i in range(-1,2):
        u = x+i
        if u < 0 : u = len(a)-1
        if u > len(a)-1: u = 0
        #print(u)
        for j in range(-1,2):
            h = y+j
            if h < 0 : h = len(a[i])-1
            if h > len(a[i])-1: h = 0
            if a[u][h]== 1:
                if j == 0 and i == 0 and a[u][h] == 1:
                    count -= 1
                count += 1
    return count

def check_all(a,x_size,y_size):
    b = []
    for i in range(x_size):
        b.append([])
        for j in range(y_size):
            b[i].append(check_neighbours(a,i,j))
    return b

def life_step(a):
    b = check_all(a,grid_size,grid_size)
    for i in range(len(a)):
        for j in range(len(a)):
            if b[i][j] <= 1 or b[i][j] >= 4:
                a[i][j] = 0
            if b[i][j] == 3:
                a[i][j] = 1
    return a

a = []
a = create_grid(a,grid_size,grid_size)
#print_array(a)
gameDisplay.fill(black)
draw_array(a,grid_size,grid_size,white)
clock.tick(1)
gameExit = False
pause = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                a=[]
                a = create_grid(a,grid_size,grid_size)
                draw_array(a,grid_size,grid_size,white)
                clock.tick(1)
            if event.key == pygame.K_SPACE:
                pause = not pause
    colour = red        
    if not pause:
        a = life_step(a)
        colour = white
    draw_array(a,grid_size,grid_size,colour)
    clock.tick(5)


