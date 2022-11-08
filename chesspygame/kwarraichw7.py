#khadija warraich - kwarraic: homework 7

#    15-112: Principles of Programming and Computer Science
#    HW07 Programming: Implementing a Chat Client
#    Name      : khadija warraic
#    AndrewID  : kwarraic

#    File Created: 
#    Modification History:
#    Start Oct 1           End Oct 4 
#    
#    
#    
import socket
import math

########## FILL IN THE FUNCTIONS TO IMPLEMENT THE CHATCOMM CLASS ##########
class chatComm:
    def __init__(self,ipaddress,portnum):
        #variable initalization
        self.ipadress = ipaddress
        self.portnum = portnum
        
        
    
    def startConnection(self):
        #creation of socket, then connection to the server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ipadress, self.portnum))

    def leftRotate (self, x, c):
        return ((x << c) & 0xFFFFFFFF) | ((x >> (32-c)&0x7FFFFFFF>>(32-c)))


    def login(self,username, password):
        #initalization of username and password
        self.username = username
        self.password = password
        self.result = []

        #sending the encoded username to the server + reciving the information
        self.socket.send((b"LOGIN " + self.username.encode("utf-8") + b"\n"))
        data = self.socket.recv(1024)
        #print(data.decode())
        challenge = data.decode().split()[2]


        #getting the 512 large str
        message = self.password + challenge
        block = message + str(1)
        msglen = str(len(message))

        while len(block)  < 509 - len(message):
            block += message

        remainingChars = 512 - len(block)
        extraZeros = '0' * (remainingChars-3)

        block += extraZeros

        if len(msglen) == 2:
            block += ('0' + str(len(message)))
        else:
            block += str(len(message))


        #splitting of the chunks
        lst= []
        temptr = ""
        counter = 0 
        for i in range(16):
            lst.append(block[counter:counter+32])
            counter += 32

        #finding the ascii val of each chunk
        asciiTemp = 0
        M = []
        for item in lst:
            for char in item:
                asciiTemp += ord(char)
            M.append(asciiTemp)
            asciiTemp = 0

        #hashing algorithim - taken from the handout and adjusted it to python 
        
        s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 5,
             9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 4, 11, 16,
            23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6, 10, 15, 21,
             6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21 ]

        K = [0] *64
        for i in range(64):
            K[i] = math.floor(2**32 * abs(math.sin(i + 1)))

        

        a0 = 0x67452301 
        b0 = 0xefcdab89 
        c0 = 0x98badcfe 
        d0 = 0x10325476 
        A = a0
        B = b0
        C = c0
        D = d0


        #main loop:
        for i in range(64):
            if 0 <= i <= 15: 
                F = (B & C) | ((~ B) & D)
                F = F & 0xFFFFFFFF
                g = i
            
            elif 16 <= i<= 31:
                F = (D & B) | ((~ D) & C)
                F = F & 0xFFFFFFFF
                g = (5*i + 1) % 16
                
            elif 32 <= i <= 47:
                F = B ^ C ^ D
                F = F & 0xFFFFFFFF
                g = (3*i + 5) % 16
                
            elif 48 <= i <= 63:
                F = C ^ (B | (~ D))
                F = F & 0xFFFFFFFF
                g = (7*i) % 16

            dTemp = D
            D = C
            C = B
            B = B + self.leftRotate((A + F + K[i] + M[g]), s[i])
            B = B & 0xFFFFFFFF


            A = dTemp


        #Add this chunk's hash to result so far:
        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

        self.result = str(a0) + str(b0) + str(c0) + str(d0)

        #sends the login request with the username, and the hashed pw 
        self.socket.send(b'Login '+self.username.encode('utf-8') +b" "+(self.result +"\n").encode('utf-8'))
        info = self.socket.recv(512)
        info = info.decode()


        if 'Successful' in info:
            return True
        else:
            return False


    #sends request to the server for the names of the users and then removes
    #the extra information so only the lst of names are returned 
    def getUsers(self):
        self.socket.send('@users'.encode('utf-8'))
        firstSix = self.socket.recv(6).decode()
        firstSix = int(firstSix[1:])
        totalBits = firstSix - 6
        userss = ""
        while totalBits > 0:
            total = (self.socket.recv(512)).decode()
            userss += total
            totalBits -= 512
            
            
        
        #inittotal = inttotal.decode()
        #total = int(inittotal[1:])
        #data = (self.socket.recv(total)).decode()
        #lstUsers = data.split('@')
        lstUsers = userss.split('@')
        return lstUsers[4:]

    #send a request to the server for the list of freinds, then removes the
    #extra information
    def getFriends(self):
        self.socket.send('@friends'.encode('utf-8'))
        info = self.socket.recv(9000000)
        info = info.decode()
        #print(info)
        #total = int(info[1:])
        #fri = (self.socket.recv(total)).decode()
        #lstFriends = fri.split('@')
        lstFriends = info.split('@')
        return lstFriends[4:]

    #send a request to the server for the list of friend requests, then removes the
    #extra information    
    def getRequests(self):
        self.socket.send('@rxrqst'.encode('utf-8'))
        info = (self.socket.recv(9000000)).decode()
        #info = info.decode()
        #total = int(info[1:])
        #rqst = (self.socket.recv(total)).decode()
        dataa = info.split('@')
        return dataa[3:]

    
    def sendFriendRequest(self, friend):
        #initalises variables 
        self.friend = friend

        #gets the size of the whole request and then adds the appropriate 0s
        request = ("@request@friend@" + self.friend)  #.encode('utf-8')
        lenReq = len(request) +6

        digStr = len(str(lenReq))
        while (digStr < 5):
            lenReq = '0' + str(lenReq)
            digStr += 1

        #completes the request string
        request = "@" + str(lenReq) + request

        #sends the request and recives the information back from the server
        self.socket.send(request.encode('utf-8'))
        info = self.socket.recv(1024)
        info = info.decode()

        #checks to see if the request is executed properly 

        if "@ok" in info:
            return True
        else:
            return False
        

    
    def acceptFriendRequest(self,friend):
        self.friend = friend
        #gets the size of the whole request and then adds the appropriate 0s
        request = ("@accept@friend@" + self.friend)  #.encode('utf-8')
        lenReq = len(request) +6

        digStr = len(str(lenReq))
        while (digStr < 5):
            lenReq = '0' + str(lenReq)
            digStr += 1

        request = "@" + str(lenReq) + request

        #sends the request to the server 
        self.socket.send(request.encode('utf-8'))
        info = self.socket.recv(1024)
        info = info.decode()


        #checks to see if the request had been successful
        if ("@ok" or "@no such friend request")in info:
            return True
        else:
            return False
        

    
    def sendMessage(self, friend, message):
        #initalises the variables 
        self.msg = message
        self.friend = friend 

        #gets the size of the whole request and then adds the appropriate 0s
        request = ("@sendmsg@" + self.friend +"@" + str(self.msg))
        lenReq = len(request) +6

        digStr = len(str(lenReq))
        while (digStr < 5):
            lenReq = '0' + str(lenReq)
            digStr += 1

        request = "@" + str(lenReq) + request

        
        #sends the request to server and recives the information back 
        self.socket.send(request.encode('utf-8'))
        info = self.socket.recv(1024)
        info = info.decode()

        #checks to see if the request was successful 
        if "@ok" in info:
            return True
        else:
            return False

    
    def sendFile(self,friend, filename):
        #intialses variables 
        self.file = filename
        self.friend = friend
        
        #gets the file that is wanting to be transfered and reads its contents
        fhin = open(self.file)
        line = fhin.read()

        # gets the size of the whole request and then adds the 0s
        request = ("@sendfile@" + self.friend +"@" + self.file + "@" + line )  
        lenReq = len(request) +6


        digStr = len(str(lenReq))
        while (digStr < 5):
            lenReq = '0' + str(lenReq)
            digStr += 1

        request = "@" + str(lenReq) + request

        #sends the request to the server and decodes the response
        self.socket.send(request.encode('utf-8'))
        info = self.socket.recv(1024)
        info = info.decode()

        #checks to see if it was sucessful 
        if "@ok" in info:
            return True
        else:
            return False
        
    
    def getMail(self):
        #intialses variables 
        self.msgLst = []
        self.fileLst = []
        tempHold = ()

        #sends the request to the server and decodes the response
        self.socket.send('@rxmsg'.encode('utf-8'))
        info = self.socket.recv(1024)
        info = info.decode()

        #removes all @ symbols 
        splittedVers = info.split('@')

        #takes care if there are no messages
        if len(splittedVers) == 3:
            return [[],[]]

        #for the final return lists 
        for i in range(len(splittedVers)):
            if splittedVers[i] == 'msg':
                tempHold = (splittedVers[i+1], splittedVers[i+2])
                self.msgLst.append(tempHold)
            elif splittedVers[i] == 'file':
                tempHold = (splittedVers[i+1], splittedVers[i+2])
                self.fileLst.append(tempHold)

        #takes care of any files sent and saves them       
        for i in range(len(splittedVers)):
            if splittedVers[i] == 'file':
                fhout = open(splittedVers[i+1], 'w')
                fhout.write(info[i+2])
                fhout.close()
                
        
        return [self.msgLst, self.fileLst]


''''
comm = chatComm("86.36.42.136", 15112)
comm.startConnection()
comm.login('zrh', 'zrh')
print(comm.getMail())


comm = chatComm("86.36.42.136", 15112)
comm.startConnection()
comm.login('kwarraic', 'kwarraic')
print(comm.getMail())
'''