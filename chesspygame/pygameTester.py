#khadija warraich - kwarraic - tech demo

'''' 
import pygame
import socket
from kwarraichw7 import * 

#starts the socket connection so that the information may be sent and recvd
comm = chatComm("86.36.42.136", 15112)
comm.startConnection()
comm.login('kwarraic', 'kwarraic')


#outlines the top left location of the tile
gridTotal = {'A1': (280,30), 'B1': [330,30], 'C1': [390,30], 'D1': [440,30],
            'E1': [500,30], 'F1': [560,30], 'G1': [600,30],'H1': [660,30],
            
            'A2': (280,90), 'B2': [330,90], 'C2': [390,90], 'D2': [440,90],
               'E2': [500,90], 'F2': [560,90], 'G2': [600,90],'H2': [660,90],
               
            'A3': (280,140), 'B3': [330,140], 'C3': [390,140], 'D3': [440,140],
               'E3': [500,140], 'F3': [560,140], 'G3': [600,140],'H3': [660,140],
               
            'A4': (280,200), 'B4': [330,200], 'C4': [390,200], 'D4': [440,200],
               'E4': [500,200], 'F4': [560,200], 'G4': [600,200],'H4': [660,200],
               
            'A5': (280,250), 'B5': [330,250], 'C5': [390,250], 'D5': [440,250],
               'E5': [500,250], 'F5': [560,250], 'G5': [600,250],'H5': [660,250],
               
            'A6': (280,300), 'B6': [330,300], 'C6': [390,300], 'D6': [440,300],
               'E6': [500,300], 'F6': [560,300], 'G6': [600,300],'H6': [660,300],
               
            'A7': (280,360), 'B7': [330,360], 'C7': [390,360], 'D7': [440,360],
               'E7': [500,360], 'F7': [560,360], 'G7': [600,360],'H7': [660,360],
               
            'A8': (280,410), 'B8': [330,410], 'C8': [390,410], 'D8': [440,410],
               'E8': [500,410], 'F8': [560,410], 'G8': [600,410],'H8': [660,410],}
               
               
#outlines the size of the grid + peice size         
gridLen = 50
gridWidth = 55
peiceSize = (20,25)

#initalizing pygame
pygame.init()
 
#creating the game window size and naming the window
wndSize = (960,540)
window = pygame.display.set_mode(wndSize)
pygame.display.set_caption('Chess <3')

#adding the board to the frame and scaling it
board = pygame.image.load('board.jpg').convert()
board = pygame.transform.scale(board,(wndSize))


pieces = ['brook.jpg', 'bknight.jpg', 'bbishop.jpg', 'bqueen.jpg', 'bking.jpg', 'bpawn.jpg', 'wrook.jpg', 'wknight.jpg', 'wbishop.jpg', 'wqueen.jpg', 'wking.jpg', 'wpawn.jpg']

#class to create each piece
class piece(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect(center = pos)


coors = (661,872)
#creation of sprite group
allSprites = pygame.sprite.Group()

#creating all the sprites by listing through a loop

images = 'blackrook.png'

coors = (39,59)
#brook = pygame.image.load('brook.png').convert_alpha()
#brook1 = piece(coors)
#brook1 = pygame.transform.scale(brook1,(peiceSize))



#print(type(brook1))

#blackrook1 = piece(coors,blackrook)
#print(brook)

print('--')
#p#rint(brook1)


spritex= 250
spritey = 360

g8x = 0
g8y = 0


#MAIN LOOP FOR THIS PRGRAM

gameOn = True
while gameOn:
        
    #puts the image in the background (also maybe sprites on the screen)
    window.blit(board,(0,0))

    #allows the window to close 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    #takes input from the mouse/cursor
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePress = pygame.mouse.get_pos()
            mouseX = mousePress[0]
            mouseY = mousePress[1]
            if (275 < mouseX < 710) and (30 < mouseY < 465):
                
            #print(mousePress)
                print('x', mouseX)
            print('y', mouseY)
            if g8x < mouseX < (g8x + gridWidth):
                if g8y < mouseY < g8y + gridWidth:
                    print('R1:G8')
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursorPos = pygame.mouse.get_pos()
            print(cursorPos)
            spritex = cursorPos[0]
            spritey = cursorPos[1]
            print(spritex)
            print(spritey)

        
        

    #updates the sprites and display
    allSprites.update()
    pygame.display.update()


    
pygame.quit()


'''


# import pygame module in this program
import pygame
 
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
# assigning values to X and Y variable
X = 400
Y = 400
 
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render('GeeksForGeeks', True, green, blue)
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)
 
# infinite loop
while True:
 
    # completely fill the surface object
    # with white color
    display_surface.fill(white)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()








