"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (255, 255)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

# --- Define the size of a square
WIDTH = 60
HEIGHT = 60
MARGIN = 20

ROW_NUM = 3
COL_NUM = 3

def check_win(grid, row_pos, col_pos, player):

    print(grid)
    win_con = [player, player, player]
    check_row = grid[row_pos]
    check_column = []


    check_diag_1 = []
    check_diag_2 = []

    for i in range(3):
        check_column.append(grid[i][col_pos])
        check_diag_1.append(grid[i][i])
        check_diag_1.append(grid[i][2-i])
    print("Row = ", check_row, "column = ", check_column)
    
    if check_row == win_con or check_column == win_con or check_diag_1 == win_con or check_diag_2 == win_con:
        return True
    else:
        return False
# --- Create grid of numbers
# Create an empty list
grid = []
grid_weight = []
# Loop for each row
for row in range(ROW_NUM):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    grid_weight.append([])
    # Loop for each column
    for column in range(COL_NUM):
        # Add a the number zero to the current row and identify the "weight" of the cell
        grid[row].append(0)
        grid_weight[row].append((column) + 3 * row)
player = 1
background = RED
board_score = 0
# Loop until the user clicks the close button.
done = False
win = False 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not win:
            
            pos = pygame.mouse.get_pos()
            row_pos = pos[1] // (HEIGHT + MARGIN)
            col_pos = pos[0] // (WIDTH + MARGIN)

            if player == 1:
                if grid[row_pos][col_pos] == 0:
                    grid[row_pos][col_pos] = 1
                    board_score += 3 ** grid_weight[row_pos][col_pos]
                    win = check_win(grid, row_pos, col_pos, player)
                    
                    background = BLUE
                    
                    
                    if win:
                        background = GREEN

                    player = 2
            else:
                if grid[row_pos][col_pos] == 0:
                    grid[row_pos][col_pos] = 2
                    board_score += 2 * 3 ** grid_weight[row_pos][col_pos]

                    win = check_win(grid, row_pos, col_pos, player)

                    if win:
                        background = BLACK
                            
                    player = 1
                    background = RED
                            
            #print("Row: ", row_pos, " Column: ", col_pos, " Weight: ", grid_weight[row_pos][col_pos])
            #print("Board Score: ", board_score, " mod14: ", board_score % 3)
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(background)
 
    # --- Drawing code should go here
    color = WHITE
    for row in range (ROW_NUM):
        y_pos = (row)* (HEIGHT + MARGIN)+ MARGIN
        for column in range(COL_NUM):
            x_pos = (column)* (WIDTH + MARGIN)+ MARGIN
            color = WHITE
            if grid[row][column]==1:
                color = GREEN
            elif grid[row][column]==2:
                color = PURPLE
            pygame.draw.rect(screen,color,[x_pos, y_pos, WIDTH, HEIGHT])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
