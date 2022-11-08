#khadija warraich - kwarraic
#the actual chess game logic & with the socket pass back and forth


#sets the board up completely, and puts the pieces on their starting 
#locations with colour also alloted.
class board():
    def __init__(self):
        #sets the first person to make their move as white  
        
        self.board = [
            ['blackC', 'blackN', 'blackB', 'blackQ', 'blackK', 'blackB', 'blackN', 'blackC'],
            ['blackP', 'blackP', 'blackP', 'blackP', 'blackP', 'blackP', 'blackP', 'blackP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['whiteP', 'whiteP', 'whiteP', 'whiteP', 'whiteP', 'whiteP', 'whiteP', 'whiteP'],
            ['whiteC', 'whiteN', 'whiteB', 'whiteK', 'whiteQ', 'whiteB', 'whiteN', 'whiteC']       
        ]
        
        self.whiteMoving = True
        self.gameAlive = True 
        
        
    def moveBehavior(self, start, end, board):
        self.board = board
        self.startRow = start[0]
        self.startCol = start[1]
        self.endRow = end[0]
        self.endCol = end[1]
        
        #print('this is the start row', self.startRow)
        #print('this is the start col', self.startCol)
        #print('this is the end row', self.endRow)
        #print('this is the end col', self.endCol)
        
        
        self.pcMoved = self.board[self.startRow][self.startCol]
        self.pcTaken = self.board[self.endRow][self.endCol]
        #print('this is the pc moving', self.pcMoved)
        #print('this is the pc taken', self.pcTaken)
        ##print('this is the start row', self.startRow)
        ##print('this is the start col', self.startCol)
        ##print('this is the end row', self.endRow)
        ##print('this is the end col', self.endCol)
    
    
    #helper funtion designed to check that the move a pawn makes is valid         
    def pawnMove(self):
        
        #allows for basic movements to be made in the game 
        if (((self.startRow == self.endRow - 1) or (self.startRow == self.endRow + 1)) and (self.startCol == self.endCol)):
            if self.pcTaken == '--':
                return True 
        
        #for killing other pecies
        elif (((self.startRow == self.endRow + 1) or self.startRow == self.endRow - 1)
            and ((self.startCol == self.endCol - 1) or (self.startCol == self.endCol + 1))):
            if self.pcTaken != '--':
                return True 
            else:
                return False
    
    #helper funtion designed to check that the move a castle makes is valid         
    def castleMove(self):
        
        #checks if the row remains the same 
        if (self.startRow == self.endRow):
            rng = (self.startCol - self.endCol)
            for i in range(rng):
                if (self.board[self.startRow][self.startCol+i] != '--' or 
                self.board[self.startRow][self.startCol-i] != '--'):
                    return False
            return True
                
        #checks if the collumn remain the same
        elif (self.startCol == self.endCol):
            rng = (self.startRow - self.endRow)
            for i in range(rng):
                if (self.board[self.startRow+i][self.startCol] != '--' or 
                    self.board[self.startRow-i][self.startCol] != '--'):
                    return False
            return True
            
    
    #helper funtion designed to check that the move a knight makes is valid      
    def knightMove(self):
        return True 
    
    #helper funtion designed to check that the move a bishop makes is valid  
    def bishopMove(self):
        #takes the change in x position and y position 
        self.deltaX = self.startRow - self.endRow
        self.deltaY = self.startCol - self.endCol
        
        #print('this is deltax', self.deltaX)
        #print('this is delta y', self.deltaX)
        
        #comparision of the absolute value of both to see if they match so it's truly diagonal
        if abs(self.deltaX) == abs(self.deltaY):
            
            if self.deltaX > 0 and self.deltaY > 0:
                for i in range (self.deltaX):
                    if (self.deltaX + i) != (self.deltaY + i):
                        return False
                return True 
            
            if self.deltaX < 0 and self.deltaY > 0:
                for i in range (self.deltaX):
                    if (self.deltaX - i) != (self.deltaY + i):
                        return False
                return True 
            
            if self.deltaX > 0 and self.deltaY < 0:
                for i in range (self.deltaX):
                    if (self.deltaX + i) != (self.deltaY - i):
                        return False
                return True 
            
            if self.deltaX < 0 and self.deltaY < 0:
                for i in range (self.deltaX):
                    if (self.deltaX - i) != (self.deltaY - i):
                        return False
                return True 
                

    #helper funtion designed to check that the move a queen makes is valid    
    def queenMove(self):
        #takes the change in x position and y position 
        self.deltaX = self.startRow - self.endRow
        self.deltaY = self.startCol - self.endCol
        
        
        #comparision of the absolute value of both to see if they match so it's truly diagonal
        if abs(self.deltaX) == abs(self.deltaY):
            
            if self.deltaX > 0 and self.deltaY > 0:
                for i in range (self.deltaX):
                    if (self.deltaX + i) != (self.deltaY + i):
                        return False
                return True 
            
            if self.deltaX < 0 and self.deltaY > 0:
                for i in range (self.deltaX):
                    if (self.deltaX - i) != (self.deltaY + i):
                        return False
                return True 
            
            if self.deltaX > 0 and self.deltaY < 0:
                for i in range (self.deltaX):
                    if (self.deltaX + i) != (self.deltaY - i):
                        return False
                return True 
            
            if self.deltaX < 0 and self.deltaY < 0:
                for i in range (self.deltaX):
                    if (self.deltaX - i) != (self.deltaY - i):
                        return False
                return True 
        
        #checks if the row remains the same 
        if (self.startRow == self.endRow):
            rng = (self.startCol - self.endCol)
            for i in range(rng):
                if (self.board[self.startRow][self.startCol+i] != '--' or 
                self.board[self.startRow][self.startCol-i] != '--'):
                    return False
            return True
                
        #checks if the collumn remain the same
        elif (self.startCol == self.endCol):
            rng = (self.startRow - self.endRow)
            for i in range(rng):
                if (self.board[self.startRow+i][self.startCol] != '--' or 
                    self.board[self.startRow-i][self.startCol] != '--'):
                    return False
            return True
    
    #helper funtion designed to check that the move a king makes is valid
    def kingMove(self):
        #takes the change in x position and y position 
        self.deltaX = self.startRow - self.endRow
        self.deltaY = self.startCol - self.endCol
        
        
        #comparision of the absolute value of both to see if they match so it's truly diagonal
        if abs(self.deltaX) == abs(self.deltaY):
            
            if self.deltaX > 0 and self.deltaY > 0:
                for i in range (self.deltaX):
                    if (self.deltaX + i) != (self.deltaY + i):
                        return False
                return True 
            
            if self.deltaX < 0 and self.deltaY > 0:
                for i in range (self.deltaX):
                    if (self.deltaX - i) != (self.deltaY + i):
                        return False
                return True 
            
            if self.deltaX > 0 and self.deltaY < 0:
                for i in range (self.deltaX):
                    if (self.deltaX + i) != (self.deltaY - i):
                        return False
                return True 
            
            if self.deltaX < 0 and self.deltaY < 0:
                for i in range (self.deltaX):
                    if (self.deltaX - i) != (self.deltaY - i):
                        return False
                return True 
        
        #checks if the row remains the same 
        elif (abs(self.startRow - self.endRow)) == 1:
                return True
        
        #checks if the collumn remain the same and if 
        # only one square is moved 
        elif (abs(self.startCol - self.endCo)) == 1:
            return True 
    
        pass
                
    #checks if some move that a player has made is valid or no            
    def isValidMove(self):
        #the first 5 letters are always going to be black or white, 
        #this will just get the last char which differentiates
        letter = self.pcMoved[5:]  
            
        #accounts for all the types of peices     
        if letter == 'P':
            return self.pawnMove()
        
        elif letter == 'C':
            return self.castleMove()
        
        elif letter == 'N':
            return self.knightMove()
        
        elif letter == 'B':
            return self.bishopMove()
        
        elif letter == 'Q':
            return self.queenMove()
        
        elif letter == 'K':
            return self.kingMove()
        
    def didGameEnd(self):
        if self.pcTaken[5:] ==  'K':
            self.gameAlive = False     
          
    #this funtion will only run if the correct player is can move         
    def makeMove(self):
        #checks if the move is valid and then goes about adjusting the board 
        if self.gameAlive:
            if self.isValidMove():
                self.board[self.startRow][self.startCol] = '--'
                self.board[self.endRow][self.endCol] = self.pcMoved
                return True  
        
    def checkPlayerMoving(self):
        if ((self.pcMoved[:5]) == 'white' and (self.whiteMoving == True)):
            if self.makeMove():
                self.whiteMoving = False
                self.didGameEnd()
        elif ((self.pcMoved[:5]) == 'black' and (self.whiteMoving == False)):
            if self.makeMove():
                self.whiteMoving = True
                self.didGameEnd()
    
    #debugging funtion             
    def whoPlayer(self):
        if self.whiteMoving == True:
            return 'kwarraic'
        else:
            return 'zrh'
            
            

        
    