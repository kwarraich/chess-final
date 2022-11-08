#main file for project

#imports of extra moduels  
import pygame
import os
import kwarraichw7 as chat
import chess

#initalizisng pygame
pygame.init() 

#setting RGB Values up:
whiteCol = (255,255,255)
bgcol = (97, 0, 31)
darkGrey = (100,100,100)
blackCol = (0,0,0)

names = ['whiteC', 'whiteN', 'whiteB', 'whiteK', 'whiteQ', 'whiteP', 
         'blackC', 'blackN', 'blackB', 'blackK', 'blackQ', 'blackP']

#dictionary for the peices:
pcs = {}


#helper funtion which loads all the peices from the file 
def loadPieces():
    #collects all peices from the folder 
    peices = ['blackC', 'blackN', 'blackB', 'blackQ', 'blackK', 'blackP', 
              'whiteC', 'whiteN','whiteB', 'whiteQ', 'whiteK', 'whiteP']
    #loops through all the peices 
    for peice in peices:
        pcs[peice] = pygame.image.load(peice + '.png')
   
                      
#helper funtion which draws a 64 rectangles to create the board 
def drawBoard(window):
    colours = [pygame.Color('White'), pygame.Color('Black')]   
    
    for i in range (8):
        for j in range (8):
            colour = colours[(i+j)%2]
            pygame.draw.rect(window, colour, (i*100,j*100,100,100))
  
            
#puts all the peices onto the board       
def drawPcs(window,brd):
    print(len(brd))
    for i in range (8):
        for j in range (8):
            insertingpc = brd[j][i]
            #checks to see if it's a blank spot or not 
            if (insertingpc == 'blackC' or insertingpc == 'blackN' or insertingpc == 'blackB' or 
            insertingpc == 'blackK' or insertingpc == 'blackQ' or insertingpc == 'blackP' or
            insertingpc == 'whiteC' or insertingpc == 'whiteN' or insertingpc == 'whiteB' or
            insertingpc == 'whiteK' or insertingpc == 'whiteQ' or insertingpc == 'whiteP'):
                
                window.blit(pcs[insertingpc], ((j*100)+20,(i*100)))
 
 
def connection(colour):
    print("we moved to connectin now") 
    comm = chat.chatComm("86.36.42.136", 15112)
    comm.startConnection()
    if colour == 'white':
        comm.login('kwarraic', 'kwarraic')
        mainlp('white')
    elif colour == 'black':
        comm.login('zrh', 'zrh')
        mainlp('black')
    
              
#logs the user into the client file for online funtionality 
def setUp():
    #sets up the basic window and captions it
    scrnSize = (500,700)
    scrn = pygame.display.set_mode(scrnSize)
    pygame.display.set_caption('Starting Up Chess yo')
     
    #intializes the font and gets it set up for multiple use 
    fnt = pygame.font.Font(None, 20)
    
    #sets the messages that the font should display 
    welcomeMsg = fnt.render('Welcome to Multiplayer Chess', False, 'White' )
    welcomeMsgRct = welcomeMsg.get_rect()
    welcomeMsgRct.center = (500//2, 700//4)
    
    playerChoiceMsg = fnt.render('Click on the colour that you will be playing as', False, 'White' )
    playerChoiceMsgRect = playerChoiceMsg.get_rect()
    playerChoiceMsgRect.center = (500//2, 700//3)
     
    gameOn = True
    while gameOn:
        #setting the background up with the colour and placing the messages on there 
        scrn.fill(bgcol)
        scrn.blit(welcomeMsg, welcomeMsgRct)
        scrn.blit(playerChoiceMsg, playerChoiceMsgRect)
        whiteOpt = pygame.draw.rect(scrn, whiteCol, (100,350,100,100))
        blkOpt = pygame.draw.rect(scrn, blackCol, (300,350,100,100))
        
        chosenColour = None
        
        
        for event in pygame.event.get():
            #allows the window to close 
            if event.type == pygame.QUIT:
                gameOn = False
            
            #determines what colour the usermade 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePress = pygame.mouse.get_pos()
                
                #individual xy information    
                x = mousePress[0]
                y = mousePress[1]
                
                if (x >100 and x < 200) and (y>350 and y<450):
                    chosenColour = 'white'
                
                elif (x >300 and x < 400) and (y>350 and y<450):
                    chosenColour = 'black'
                    
                if chosenColour:
                    mainlp(chosenColour)
                    pygame.quit()
                        
        #updates the view of the player            
        pygame.display.update()
    pygame.quit()



    
#funtion which drives all the chess aspects       
def mainlp(activePlayer): 
    
    #sets the connection to the server 
    comm = chat.chatComm("86.36.42.136", 15112)
    comm.startConnection()
    if activePlayer == 'white':
        comm.login('kwarraic', 'kwarraic')
        print('player is khadija')
    elif activePlayer == 'black':
        comm.login('zrh', 'zrh')
        print('player is zeina')
    
     
    #sets a screen up
    wndSize = (800,800)
    window = pygame.display.set_mode(wndSize)
    pygame.display.set_caption('Chess <3')
  
    #creates the chess board from the chess class 
    logic = chess.board()
    gameBoard = logic.board
    
    #loads the peices and displays the board graphics and players graphics 
    loadPieces()
    drawBoard(window)
    pcsSprites = pygame.sprite.Group()
    drawPcs(window, gameBoard)
    
    chosenSqr = ()
    playerMoves = []
    
    #dead code to be removed 
    for line in gameBoard:
        print(line)
        
    #main while loop, this loop is action driven, meaning depends on the user 
    #input it will go for something different 
    gameOn = True
    while gameOn:
        #chatCliMsg = comm.getMail() [0][0][1]
        chatCliMsg = 'h'
        if len(chatCliMsg[0]) > 0:
            if "CHESS:" in chatCliMsg:
                gameBoard = chatCliMsg[0][0][1][7:-1]
                
                x = len(gameBoard)
                i = 0
                tempGBoard = []
                tempHolderStr = ""
                while x > 0:
                    if gameBoard[i] == '[' :
                        while gameBoard[i] != ']':
                            tempHolderStr += gameBoard
                            i+=1
                            x-=1
                        tempGBoard.append(tempHolderStr+']')
            
            #gameBoard = tempGBoard
                
                
                
                
            drawBoard(window)
            drawPcs(window, gameBoard)
            
    
    #allows the window to close 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False

        #takes input from the mouse/cursor
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('in mouse down')
                if logic.gameAlive:
                    print('in game alive')
                    #collects the xy location and then simplfies the row and the
                    #column from 0-9 (top left 00 - bottom right 99) 
                    mousePress = pygame.mouse.get_pos()
                    
                    
                    #collects the box information     
                    x = mousePress[0]//100
                    y = mousePress[1]//100
                    
                    print('x is this ', x)
                    print('y is this ', y)
                    
                    #checks to see if the same square was pressed or if two
                    #different squares are pressed
                    if chosenSqr == (x,y):
                        chosenSqr = ()
                    else:
                        print('adding a move')
                        chosenSqr = (x,y)
                        playerMoves.append(chosenSqr)
                    
                    #checks to see if two moves are made, and then makes 
                    #the move and then updates the board
                    if len(playerMoves) == 2:
                        #print('2 moves yo')
                        logic.moveBehavior(playerMoves[0], playerMoves[1],gameBoard)
                        #print('post behavior for move ')
                        logic.checkPlayerMoving()
                        #print('ok it checked yo')
                        sendTo = logic.whoPlayer()
                        #print(sendTo)
                        #print('yo we have a sending player ')
                        comm.sendMessage(sendTo, ('CHESS: ' +  str(gameBoard)))
                        #print('yo we sent bro')
                        playerMoves = []
                        #print('the player moves array', playerMoves)
                        
                        #dead code
                        for line in gameBoard:
                            print(line)
                        
                        drawBoard(window)
                        drawPcs(window, gameBoard)
                else:
                    pygame.quit()
                
        pygame.display.update()
    
    pygame.quit()
   
   
   
setUp()


'''chatCliMsg = [[('kwarraic', "CHESS: [['blackC', 'blackN', 'blackB', 'blackQ', 'blackK', 'blackB', 'blackN', 'blackC'], ['blackP', 'blackP', '--', 'blackP', 'blackP', 'blackP', 'blackP', 'blackP'], ['--', '--', 'blackP', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', 'whiteP', '--', '--', '--', '--'], ['whiteP', 'whiteP', 'whiteP', '--', 'whiteP', 'whiteP', 'whiteP', 'whiteP'], ['whiteC', 'whiteN', 'whiteB', 'whiteK', 'whiteQ', 'whiteB', 'whiteN', 'whiteC']]"), ('kwarraic', "CHESS: [['blackC', 'blackN', 'blackB', 'blackQ', 'blackK', 'blackB', 'blackN', 'blackC'], ['blackP', 'blackP', '--', 'blackP', 'blackP', 'blackP', 'blackP', 'blackP'], ['--', '--', 'blackP', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', 'whiteP', '--', '--', '--', '--'], ['whiteP', 'whiteP', 'whiteP', '--', 'whiteP', 'whiteP', 'whiteP', 'whiteP']")], []]
print(chatCliMsg[0][0][1])
if len(chatCliMsg[0][0][1]) > 6:
    print('tgis if')
    if "CHESS:" in chatCliMsg[0][0][1]:
        chatCliMsg = chatCliMsg[0]
        print(22)'''
