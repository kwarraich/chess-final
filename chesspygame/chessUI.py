#khadija warraich - kwarraic
#the actual chess logic 

#sets the board up completely, and puts the pieces on their starting 
#locations with colour also alloted. This view puts the white on the
#bottom half of the screen

class chessUI():
    def __init__(self):
        #the board consists of 8 lists one for each row. The -- is meant to signal the unavalible 
        #spaces on the board. 
        self.board = [
            ["blackC", "blackPN", "blackB", "blackQ", "blackK", "blackB", "blackN", "blackR"],
            ["blackP", "blackP", "blackP", "blackP", "blackP", "blackP", "blackP", "blackP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["whiteP", "whiteP", "whiteP", "whiteP", "whiteP", "whiteP", "whiteP", "whiteP"],
            ["whiteC", "whiteN", "whiteB", "whiteQ", "whiteQ", "whiteB", "whiteN", "whiteC"]]
        
        self.whiteToMove = True
        self.checkMate = False
        self.check = False
        
                   
                          
#parent class for all the peices - each child class takes care of if the move 
#is something that peice may perform and the peice name
class peice:
    def __init__(self, colour):
        self.colour = colour
        
    
    def isValidMove(self, start, to):
        return False
    
    def pcsColour(self):
        return self.colour
    

#child classes for each of the unique peices 
class rook(peice, ):
    def __init__(self):
        super().__init__(colour)
        self.type = 'rook'
        
    
    def isValidMove(self,start,to):
        pass
    
class knight(peice):
    def __init__(self):
        super().__init__(colour)
        self.type = 'knight'
    
    def isValidMove(self):
        pass
    
class bishop(peice):
    def __init__(self):
        super().__init__(colour)
        self.type = 'bishop'
    
    def isValidMove(self):
        pass
        
    
class queen(peice):
    def __init__(self):
        super().__init__(colour)
        self.type = 'queen'
    
    def isValidMove(self,start,end):
        
    
class king(peice):
    def __init__(self):
        super().__init__(colour)
        self.type = 'king'
    
    def isValidMove(self):
        pass
    
    def canCastle(self):
        pass

class pawn(peice):
    def __init__(self):
        super().__init__(colour)
        self.type = 'pawn'
    
    def isValidMove(self):
        pass

        
#chess class which will take care of most of the funtionality 
class chess():
    # constructor method
    def __init__(self):
        self.player = 'white'
        
    def makeMove(self):
        print(self.player)
        pass
        
         
   
    def checkValidMove(self):
        pass 
        



    
