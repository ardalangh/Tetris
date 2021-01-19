import random
import pygame


col = 10
row = 20
screenWidth = 800
screenHeight = 750
gameWidth = 300
gameHeight = 600
blockSize = 30

top_left_x = (screenWidth - gameWidth) // 2
top_left_y = screenHeight - gameHeight

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3


def create_grid(locked_position = {}):
    grid = []
    for x in range(20):
        lst = []
        for i in range(10):
            lst.append((0,0,0))
        grid.append(lst)


def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False 
    return True

def draw_grid(surface, row , col):
    sx = top_left_x
    sy = top_left_y

    for i in range(row):
        # horizontal
        pygame.draw.line(surface, (0,0,0), (sx,  sy + i * 30), (sx + gameWidth, sy + i * 30)) 
        for j in range(col):
            # vertical 
            pygame.draw.line(surface, (0,0,0), (sx + j * 30, sy), (sx + j * 30, sy + gameHeight))  

            
def get_shape():
    global shape
    global shape_color
    return Piece(5,0,random.choice(shapes))

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]



    for i , line in enumerate(format):
        row - list(line)
        for j, col in enumerate(row):
            if col == "0": 
                positions.append((shape.x + j, shape.y + i))

    
    for i , pos in  enumerate(positions):
        positions[i] = (pos[0] - 1, pos[1] - 4)

    return positions


def clear_rows(grid, locked_position):

    inc = 0 

    for i in range(len(grid)-1,-1,-1):
        row = grid[i]

        if (0, 0, 0) not in row:
            inc += 1


            ind = i

            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue


        if inc > 0:
            for key in sorted(list(locked), key = lambda x : x[1])[::-1]:
                x , y = keyif y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)


def draw_window(surface):
    surface.fil((0,0,0))

    font = pygame.font.SysFont('sans', 60)
    label = font.render("Tetris", 1, (255,255,255))

    surface.blit(label, (top_left_x + gameWidth / 2 - (label.get_width() / 2), 30), 0)



    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)


    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0 ,0), (top_left_x, top_left_y, gameWidth, gameHeight), 5)


def draw_next_shape(next_piece, win):
    font = pygame.font.SysFont('snans', 30)
    label = font.render("Next Shape", 1, (255,255,255))


    sx = top_left_x + gameWidth + 50
    sy = top_left_y + gameHeight / 2 - 100

    fomrat = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, col in enumerate(row):
            if col == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * 30, sy + i* 30, 30, 30), 0)


    surface.blit(label, (sx + 10, sy - 30))















def main():
    global grid
    locked_positions= {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True 
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock
    falltime = 0
    leveltime = 0
    fallspeed = 0.27
    score = 0
    while run:
        grid = create_grid(locked_position)
        falltime+=clock.get_rawtime()
        leveltime +=clock.get_rawtime()
        clock.tick()
        if(leveltime / 1000 > 4):
            leveltime = 0
            if(fallspeed > .15):
                fallspeed -=0.0005
        if falltime / 1000 >= fallspeed:
            falltime = 0
            current_piece.y +=1
            change_piece = True

            
        for event in pygame.event.get():


                        
            if event.type == pygame.QUIT:      #if user wants to quit
                run = False                     #stop while loop
                pygame.quit()                  #quit/exit pygame



            # if the type of my event relates to keyboard stuff
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT  or pygame.K_A: # if user presses a or left arrow key
                    current_piece.x -= 1                      #  move left
                    if not valid_space(current_piece,grid):  # if after the piece moves left, it is not in a valid space, undo all actions.
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT or pygame.K_D:  # if user presses d or right arrow key 
                    current_piece.x +=1                        #moves right
                    if not valid_space(current_piece,grid):
                        current_piece.x -= 1                        # if after the piece moves right, it is not in a valid space, undo all actions by doing reverse of it.
                if event.key == pygame.K_UP or pygame.K_W:      # if user presses either w or up arrow
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)         # rotate piece       
                    if not valid_space(current_piece,grid):                                                  # if after rotation piece is not in a valid space on grid
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)   #undo rotation by doing exact opposite as before
                if event.key == pygame.K_DOWN or pygame.K_S:    #if pressing down s or down arrow
                    current_piece.y += 1      #move piece down
                    if not valid_space(current_piece,grid): # if not in valid pos
                        current_piece.y -= 1    #undo actions 
        shape_pos = convert_shape_format(current_piece)


        for i in range(len(shape_pos)):
            x,y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
                
        if change_piece:
            for pos in shape_pos:
               p = (pos[0], pos[1])
               locked_positions[p] = current_piece.color
            current_piece = next_piece
            change_piece = False


            if clear_rows(grid, locked_positions): 
                score += 10

        draw_window(win)
        draw_next_shape(next_piece, win)
        pygame.display.update()


        # Function not done Until next week
        
        


    
def main_menu():
    run = True

    while run:
        win.fill((0,0,0))
        draw_text_middle("Press any key ro begin.", 60, (255,255,255), win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:     
                run = False                     
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                main()

    pygame.quit()
            
#start main menu

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tetris with pygame")



main_menu()


#comment main func code
