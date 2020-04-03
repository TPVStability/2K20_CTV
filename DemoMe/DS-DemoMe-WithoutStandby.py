"""
Created on Tue Sep 10 11:30:04 2019

@author: Revanth.D
"""

import time
import random
import socket

class Client():
    def __init__(self):
        self.sock = socket.socket()
        self.socketOpen = False

	#
	# Opens the socket to RedRatHubCmd.
	#
    def OpenSocket(self, ip, port):
        self.sock.connect((ip, port))
        self.socketOpen = True

	#
	# Closes the RedRatHubCmd socket.
	#
    def CloseSocket(self):
        if self.socketOpen:
            self.sock.close()
            self.socketOpen = False
        else:
            print("Socket failed to close.")

	#
	# Sends a message to the ReadData() function
	#
    def SendMessage(self, message):
        self.ReadData(message)


	#
	# Reads data back from RedRatHub.
	#
    def ReadData(self, message):
        if not self.socketOpen:
            print("\tSocket has not been opened. Call 'OpenSocket()' first.")
            exit
            
        # Send message
        self.sock.send((message + '\n').encode())
        received = ""
		
        # Check response. This is either a single line, e.g. "OK\n", or a multi-line response with 
        # '{' and '}' start/end delimiters.
        while True:
            # Receives data
            received += self.sock.recv(64).decode()
            if self.CheckEOM(received):
                return received

                
    #
	# Checks for the end of a message
	#
    def CheckEOM(self, message):
        # Multi-line message
        if ('{' in message):
            return ('}' in message)
        
        # Single line message
        if ("\n" in message):
            return True

client = Client();
client.OpenSocket('localhost', 40000);
Counter = 1
RedRat_Device_Name = "RedRat-X 23589"
RedRat_Device_Port = "3"

def SendKey(*args):
    if len(args) == 1:
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(args[0]) + "\"" + ' output=\"' + RedRat_Device_Port+"\"\'")
    elif len(args) == 2:
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(args[0]) + "\"" + ' output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(float(args[1]))
    elif len(args) == 3:
        for j in range(args[2]):
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(args[0]) + "\"" + ' output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(float(args[1]))

Trick_List_1 = [["Forward",10.0], ["Forward",8.0] , ["Forward", 6.0] , ["Forward", 4.0] , ["Forward", 2.0]]
Trick_List_2 = [["Rewind",10.0], ["Rewind",8.0] , ["Rewind",6.0] , ["Rewind",4.0] , ["Rewind",2.0]]
Trick_List_3 = [["Pause",2.0], ["Play",3.0] , ["Pause",1.0], ["Play",4.0] ,["Pause",5.0], ["Play",2.0] ,["Pause",8.0], ["Play",3.0],["Pause",5.0], ["Play",1.0]]
Trick_List_4 = [["Rewind",2.0], ["Rewind",8.0] , ["Forward",1.0] , ["Forward",4.0] , ["Pause",3.0], ["Play",4.0], ["Rewind",1.0], ["Rewind",1.0], ["Rewind",3.0]]
Trick_List_5 = [["Pause",2.0], ["Rewind",1.0] , ["Forward",1.0 ], ["Forward",2.0] , ["Play",3.0], ["Pause",2.0], ["Forward",3.0], ["Rewind",2.0], ["Rewind",2.0], ["Play",4.0], ["Pause",4.0],
                ["Rewind",1.0], ["Rewind",2.0], ["Rewind",3.0], ["Forward",1.0], ["Forward",1.0], ["Forward",1.0], ["Play",4.0], ["Rewind",2.0], ["Rewind",2.0], ["Pause",2.0],
                ["Forward",1.0], ["Forward",2.0], ["Forward", 3.0], ["Forward", 4.0], ["Pause", 2.0], ["Rewind", 1.0], ["Rewind", 1.0], ["Rewind", 2.0], ["Rewind", 2.0],["Play", 8.0]]
Trick_List_6 = [["Rewind",0.8], ["Forward",1], ["Pause",0.7], ["Play",0.2], ["Rewind",1], ["Rewind",0.5], ["Rewind",0.3],["Forward",10.0], ["Forward",0.3] , ["Rewind", 15] ,
                ["Forward", 1],["Pause",0.5], ["Play",0.4] , ["Pause",0.3], ["Play",0.5] ,["Pause",0.6], ["Play",0.3] ,["Pause",0.4], ["Play",0.4],["Pause",0.5], ["Play",0.5],
                ["Pause",1], ["Rewind",5] , ["Forward",3 ], ["Forward",0.3] , ["Play",4], ["Pause",2.0], ["Forward",0.4], ["Rewind",0.2], ["Rewind",0.3], ["Play",3], ["Pause",0.7],
                ["Rewind",0.2], ["Rewind",0.2], ["Rewind",0.2], ["Forward",0.2], ["Forward",0.3], ["Forward",0.3], ["Play",6], ["Rewind",10], ["Rewind",0.2], ["Pause",5],
                ["Forward",0.7], ["Forward",0.4], ["Forward", 0.4], ["Forward", 0.2], ["Pause", 3], ["Rewind", 0.1], ["Rewind", 0.5], ["Rewind", 0.5], ["Rewind", 0.5],["Forward", 0.9]]

Random_Standby_Wakeup_List = ["Blue","Exit","Home","Netflix","Ambilight",0, "Channel_Up", "Channel_Down"]
Wakeup_Time_List = [[7,8],[15,4], [25,5],[3,6], [2,5],[13,6], [14,7],[1,7], [10,10],[16,8]]

def Trick_List_Navigations_Fixed(Trick_List):
    Key_1stArg = 0
    SleepTime_2ndArg = 1
    for count in range(len(Trick_List)):
        SendKey(Trick_List[count][Key_1stArg], Trick_List[count][SleepTime_2ndArg])

def Random_TrickModes(Trick_Count):   
    for count in range(0,Trick_Count):
        Trick_List = ["Pause","Play","Rewind","Forward"]
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + random.choice(Trick_List) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(3)

def Random_longpress(Nav_Count):   
    for count in range(0, Nav_Count):
        Key_List = ["Right_longpress","Up_longpress","Down_longpress","Left_longpress"]
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + random.choice(Key_List) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(0.5)

def Random_Navigation(Nav_Count):
    for count in range(0, Nav_Count):
        Key_List = ["Right","Up","Down","Left"]
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + random.choice(Key_List) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(.3)
def Random_Volume(Volume_Count):
    for count in range(Volume_Count):
        Volume_List = ["Volume_Up","Mute","Volume_Down"]
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + random.choice(Volume_List) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(0.3)
        
Apps_In_Row1 = [1,2,3,4]
Apps_In_Row2 = [5,6,7,8]
Apps_In_Row3 = [9,10,11,12]
Apps_In_Row4 = [13,14,15,16]
Apps_In_Row5 = [17,18,19,20]

def Home_Positioning_Launch_App(App_Number):
    SendKey('Home_longpress', 0.6, 1)
    
    if (App_Number in Apps_In_Row1):
        Down_Count = 1
    elif (App_Number in Apps_In_Row2):
        Down_Count = 2
    elif (App_Number in Apps_In_Row3):
        Down_Count = 3
    elif (App_Number in Apps_In_Row4):
        Down_Count = 4
    elif (App_Number in Apps_In_Row5):
        Down_Count = 5
    else:
        Down_Count = 0

    if (App_Number in Apps_In_Row1):
        Right_Count = Apps_In_Row1.index(App_Number)
    elif (App_Number in Apps_In_Row2):
        Right_Count = Apps_In_Row2.index(App_Number)
    elif (App_Number in Apps_In_Row3):
        Right_Count = Apps_In_Row3.index(App_Number)
    elif (App_Number in Apps_In_Row4):
        Right_Count = Apps_In_Row4.index(App_Number)
    elif (App_Number in Apps_In_Row5):
        Right_Count = Apps_In_Row5.index(App_Number)
        
    SendKey('Down', 0.3, Down_Count)
    SendKey('Right', 0.3, Right_Count)
    SendKey('Ok', 4, 1)
    if (Right_Count == 2):
        time.sleep(2)
    time.sleep(2)
    
def Digit_Channel_Selection(Mode,Channelnumber):
    if Mode=="Tuner":
        Switch_To_Tuner()
        if type(Channelnumber) is int:
            for x in range(0,len(str(Channelnumber))):
                sublist_temp = str(Channelnumber)
                time.sleep(0.15)
                SendKey(str(sublist_temp[x]), 0.3, 1)
            time.sleep(4)
        else:
            SendKey(str(Channelnumber), 0.3, 5)

    if Mode=="Satellite":
        Switch_To_Satellite()
        if type(Channelnumber) is int:
            for x in range(0,len(str(Channelnumber))):
                sublist_temp = str(Channelnumber)
                time.sleep(0.15)
                SendKey(str(sublist_temp[x]), 0.3, 1)
            time.sleep(4)
        else:
            SendKey(str(Channelnumber), 0.3, 5)

def Switch_To_Satellite():                   
    SendKey("Sources")
    time.sleep(3.5)
    SendKey("Up_longpress")
    time.sleep(0.5)
    for count in range(0,2):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1.5)

def Switch_To_Tuner():
    SendKey("Sources")
    time.sleep(3.5)
    SendKey("Up_longpress")
    time.sleep(0.5)
    for count in range(0,3):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1.5)



def Youtube_Row1_Demome():
    Home_Positioning_Launch_App(1)
    time.sleep(3)
    SendKey("Back",0.3,4)
    Home_Positioning_Launch_App(1)
    time.sleep(3)
    SendKey("Left_longpress",0.7, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.5, 1)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Right", 0.3, 1) #Stability Folder-1st video
    SendKey("Ok", 18, 1) #youtube video will be played and demo me+esticker will be launched
    SendKey("Back",4,1) 
    SendKey("Back",5,1) 
    SendKey("Ok", 1, 2)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Forward",2,3)
    time.sleep(20)
    SendKey("Back", 4, 2)
    SendKey("Right", 0.3, 1) 
    SendKey("Ok", 12, 1) 
    SendKey("Back",3,1) 
    SendKey("Back",2,1) 
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    SendKey("Back",4,2)
    SendKey("Rewind",3,3)
    time.sleep(16)   
    SendKey("Back", 4, 2)
    SendKey("Right", 0.3, 1) 
    SendKey("Ok", 20, 1) 
    

def Youtube_Row2_Demome():
    Home_Positioning_Launch_App(1)
    time.sleep(3)
    SendKey("Back",0.3,4)
    Home_Positioning_Launch_App(1)
    time.sleep(3)
    SendKey("Left_longpress",0.7, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.5, 1)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Right", 0.3, 1) #Stability Folder-1st video
    SendKey("Down",0.4,1) 
    SendKey("Ok", 15, 1) #youtube video will be played and demo me+esticker will be launched
    SendKey("Back",4,1) 
    SendKey("Back",3,1) 
    SendKey("Ok", 1, 2)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Forward",2,3)
    time.sleep(19)
    SendKey("Back", 4, 2)
    SendKey("Right", 0.3, 1) 
    SendKey("Ok", 22, 1) 
    SendKey("Back",3,1) 
    SendKey("Back",2,1) 
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    SendKey("Back",4,2)
    SendKey("Rewind",3,3)
    time.sleep(17)   
    SendKey("Back", 4, 2)
    SendKey("Right", 0.3, 1) 
    SendKey("Ok", 20, 1) 
    
def Guide_Demome():
    time.sleep(15)
    SendKey("Home",2,3)
    time.sleep(15)
    SendKey("TVGuide",2,1)
    SendKey("Right_longpress",0.3,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Right",0.4,4)
    SendKey("Down_longpress",0.3,1)
    SendKey("Yellow",0.7,1)
    SendKey("Down",0.5,1)
    SendKey("Ok",0.5,1)
    SendKey("Down",0.5,1)
    SendKey("Ok",0.5,1)
    SendKey("Up",0.5,2)
    SendKey("Ok",0.5,1)
    time.sleep(18)

    SendKey("TVGuide",2,1) #Launching guide on demome+esticker
    SendKey("Right",0.5,4)
    SendKey("Left_longpress",0.5,1)
    SendKey("Right",0.4,4)
    time.sleep(16)
    SendKey("Back",3,1)

    SendKey("TVGuide",2,1) #Launching guide on demome
    SendKey("Right",0.5,4)
    SendKey("Left_longpress",0.5,1)
    SendKey("Right",0.4,4)
    time.sleep(16)
    SendKey("Back",3,1)

    #guide-Launch-Exit -Demome
    
    SendKey("TVGuide",2,10)
    time.sleep(17)
    
def Netflix_Demome():
    Right_Count = [0,1,2,3,4,5,6,7]
    SendKey('Netflix',10,1)

    SendKey('Netflix',6,1)
    
    SendKey('Ok',1,3)
    SendKey('Back',1,4)
    SendKey('Left',1,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',1,3)
    SendKey('Ok',1,1)
    
    SendKey('Up',0.5,1)
    SendKey('Right',0.6,random.choice(Right_Count))
        
    SendKey('Ok',1,1)
    SendKey('Ok',20,1)
    SendKey("Netflix",8,1) #launching netflix on demome+esticker
    SendKey('Ok',1,1)
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Forward",1,2)
    time.sleep(18)
    SendKey('Back',5,1)
    SendKey("Netflix",8,1)#launching netflix on demome
    SendKey("Ok",5,1)
    SendKey("Rewind",1,2)
    time.sleep(19)

def OIB_Row1_Demome():
    #OIB_Row-1
    Home_Positioning_Launch_App(3) 
    time.sleep(3)
    SendKey("Down_longpress",0.3,1)
    SendKey("Right_longpress",0.3,1)
    SendKey("Left_longpress",0.3,1)
    SendKey("Ok",4,1)        #Page-1
    SendKey("Down_longpress",0.3,2)
    Random_longpress(20)
    time.sleep(20)
    SendKey("Back",2,1)
    Home_Positioning_Launch_App(3) #Page2
    time.sleep(2)
    SendKey("Back",0.7,1)
    SendKey("Right",0.5,1)
    SendKey("Ok",5,1)
    SendKey("Down_longpress",0.3,2)
    Random_longpress(15)
    time.sleep(21)
    
    SendKey("Back",2,3)  #Page3
    SendKey("Right",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down_longpress",0.3,2)
    Random_longpress(10)
    time.sleep(35)

    Home_Positioning_Launch_App(3) #Launching OIB on ambilight demome
    time.sleep(2)                 #Page-4
    SendKey("Back",0.7,1)
    SendKey("Right",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down_longpress",0.3,2)    
    Random_longpress(13)
    time.sleep(25)

    SendKey("Back",2,4)
    SendKey("Right",0.5,1)
    SendKey("Ok",18,1)
 
def OIB_Row2_Demome():
    #OIB_Row-1
    Home_Positioning_Launch_App(3) 
    time.sleep(3)
    SendKey("Down_longpress",0.3,1)
    SendKey("Right_longpress",0.3,1)
    SendKey("Left_longpress",0.3,1)
    SendKey("Down",0.7,1)
    SendKey("Ok",4,1)        #Page-4
    SendKey("Down_longpress",0.3,2)
    Random_longpress(20)
    time.sleep(20)
    SendKey("Back",2,1)
    Home_Positioning_Launch_App(3) #Page5
    time.sleep(2)
    SendKey("Back",0.7,1)
    SendKey("Right",0.5,1)
    SendKey("Ok",5,1)
    SendKey("Down_longpress",0.3,2)
    Random_longpress(15)
    time.sleep(21)
    
    SendKey("Back",2,3)  #Page6
    SendKey("Right",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down_longpress",0.3,2)
    Random_longpress(10)
    time.sleep(35)

    Home_Positioning_Launch_App(3) #Launching OIB on ambilight demome
    time.sleep(2)                 #Page-7
    SendKey("Back",0.7,1)
    SendKey("Right",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down_longpress",0.3,2)    
    Random_longpress(24)
    time.sleep(25)

    SendKey("Back",2,4)
    SendKey("Right",0.5,1)
    SendKey("Ok",18,1)

def App_Gallery_Demome():
    
    SendKey("Smart_Home",10,1)
    Random_longpress(4)
    Random_Navigation(10)
    time.sleep(32)

    SendKey("Smart_Home",10,1)
    SendKey("Up_longpress",0.5,2)
    SendKey("Down",1,1)
    SendKey("Right",1,1)
    SendKey("Ok",1,1)
    SendKey("Down",0.3,7)
    SendKey("Right",0.3,3)
    Random_Navigation(12)
    Random_longpress(6) 
    time.sleep(19)
    
    SendKey("Back",3,1)
    
    SendKey("Smart_Home",10,1)
    SendKey("Up_longpress",0.5,5)
    SendKey("Down",1,1)
    SendKey("Right",1,2)
    SendKey("Ok",1,1)
    SendKey("Down",0.3,4)
    SendKey("Right",0.3,2)
    Random_Navigation(12)
    Random_longpress(6) 
    time.sleep(18)

    SendKey("Back",2,2)
    SendKey("Up_longpress",0.5,4)
    SendKey("Down",1,1)
    SendKey("Right",1,3)
    SendKey("Ok",1,1)
    SendKey("Down",0.3,3)
    SendKey("Right",0.3,2)
    Random_Navigation(10)
    time.sleep(18)

def DemoMe_App_Demome():
    Home_Positioning_Launch_App(5)
    SendKey("Left",0.2,4)
    SendKey("Up",0.2,3)
    SendKey("Down",0.2,1)
    SendKey("Right",0.6,2)
    SendKey("Ok",18,1)

    Home_Positioning_Launch_App(5)
    SendKey("Down",0.2,1)
    SendKey("Ok",20,1)


    Home_Positioning_Launch_App(5)
    SendKey("Left",0.2,3)
    SendKey("Up",0.2,4)
    SendKey("Down",0.2,3)
    SendKey("Ok",28,1)

    Home_Positioning_Launch_App(5)
    SendKey("Left",0.2,3)
    SendKey("Down",0.2,4)
    SendKey("Ok",4,10)
    time.sleep(18)

def PlayStore_Demome():
    SendKey("Home_longpress",3,1)
    SendKey("Ok",5,1)
    Random_longpress(15)
    time.sleep(30)
    
def CBPlayback_Images_Demome():
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    SendKey("Left",0.3,6)
    SendKey("Down_longpress",0.2,2)
    SendKey("Up",0.3,2)
    SendKey("Right",0.3,2)
    SendKey('Down',0.4,11)
    SendKey("Ok",2,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    time.sleep(20)
    SendKey('Sources',3,1) #Launching sources on demome+esticker
    SendKey("Ok",2,2)
    Trick_List_Navigations_Fixed(Trick_List_4)
    time.sleep(18)
    SendKey("Back", 5, 1)
    SendKey('Sources',3,1) #Launching sources on demome
    SendKey("Ok",2,2)
    Trick_List_Navigations_Fixed(Trick_List_3)
    time.sleep(19)
    
def CBPlayback_Audios_Demome():
    Down_Count = [6,7,8,9,10,11]
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    SendKey("Left",0.3,6)
    SendKey("Down_longpress",0.2,2)
    SendKey("Up",0.3,2)
    SendKey("Right",0.3,2)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',0.5,2)
    SendKey("Play",7,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    time.sleep(20)
    SendKey('Sources',3,1) #Launching sources on demome+esticker
    SendKey("Ok",2,2)
    Trick_List_Navigations_Fixed(Trick_List_3)
    time.sleep(18)
    SendKey("Back", 5, 1)
    SendKey('Sources',3,1) #Launching sources on demome
    SendKey("Ok",2,2)
    Trick_List_Navigations_Fixed(Trick_List_4)
    time.sleep(19) 
    
def CBPlayback_Videos_Demome():
    Down_Count = [0,1,2,3,4,5]
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    SendKey("Left",0.3,6)
    SendKey("Down_longpress",0.2,2)
    SendKey("Up",0.3,2)
    SendKey("Right",0.3,2) 
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',0.5,2)
    SendKey("Play",7,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    time.sleep(21)
    SendKey('Sources',4,1) #Launching sources on demome+esticker
    SendKey("Ok",2,2)
    Trick_List_Navigations_Fixed(Trick_List_3)
    time.sleep(18)
    SendKey("Back", 5, 1)
    SendKey('Sources',4,1) #Launching sources on demome
    SendKey("Ok",2,2)
    Trick_List_Navigations_Fixed(Trick_List_4)
    time.sleep(19)    
    
def CBPlayback():
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    
    SendKey("Left",0.3,6)
    SendKey('Down_Longpress',1,2)
    SendKey('Up',0.7,2)
    SendKey("Right",0.4,3) 
    time.sleep(3)
    SendKey('Ok',0.9,1)
    SendKey('Ok',6,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    time.sleep(6)
    SendKey('Back',0.8,1)
    SendKey("Down",0.3,1)
    SendKey('Ok',0.8,1)
    SendKey('Ok',7,1)
    Trick_List_Navigations_Fixed(Trick_List_4)

    time.sleep(6)
    SendKey('Back',0.8,1)
    SendKey("Down",0.3,1)
    SendKey('Ok',5,2)
    Trick_List_Navigations_Fixed(Trick_List_6)

    time.sleep(6)
    SendKey('Back',0.8,1)
    SendKey("Down",0.4,1)
    SendKey('Ok',5,2)
    Trick_List_Navigations_Fixed(Trick_List_3)
    time.sleep(6)
    SendKey('Back',0.8,1)
    SendKey("Down",0.4,1)
    SendKey('Ok',5,2)
    Trick_List_Navigations_Fixed(Trick_List_5)
    

#1st video playback    
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    
    SendKey("Left",0.3,6)
    SendKey('Down_Longpress',1,2)
    SendKey('Up',0.7,2)
    SendKey("Right",0.4,3) 
    time.sleep(3)
    SendKey('Ok',0.8,1)
    SendKey('Ok',7,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
#progress bar
    SendKey('Play',6,1)
    SendKey('Down',0.4,1)
    SendKey("Right",0.4,3) 
    SendKey('Ok',2,6)
    SendKey("Left",0.4,1)
    SendKey("Right",0.4,1) 
    #audio
    SendKey('Down',0.4,6)
    SendKey('Ok',0.8,2)
    SendKey('Back',0.8,1)
    #images with audio background
    SendKey("Left",0.4,1)
    SendKey("Right",0.4,1) 
    SendKey('Down',0.4,12)
    SendKey('Ok',0.8,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    SendKey('Down',0.4,2)
    SendKey("Left",0.3,3)
    SendKey("Right",0.4,2)
    SendKey('Ok',0.8,5)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey('Down',0.3,2)
    SendKey("Left",0.3,3)
    SendKey("Right",0.4,2)
    SendKey('Ok',0.8,6)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey('Down',0.3,2)
    SendKey("Left",0.3,3)
    SendKey("Right",0.4,2)
    SendKey('Ok',0.8,6)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey('Down',0.3,2)
    SendKey("Left",0.3,3)
    SendKey("Right",0.3,2)
    SendKey('Ok',0.8,8)
    SendKey('Down',0.3,2)
    SendKey("Left",0.3,3)
    SendKey("Right",0.3,1)
    SendKey('Ok',0.8,1) 
    
#360Images
    SendKey('Back',0.8,2)
    SendKey("Left",0.2,6)
    SendKey("Right",0.4,3) 
    SendKey('Down',0.3,18)
    SendKey('Ok',0.8,1) 
    Trick_List_Navigations_Fixed(Trick_List_5)
    time.sleep(6)
    SendKey('Back',0.8,1)
    SendKey('Down',0.3,1)
    SendKey('Ok',0.8,1) 
    Trick_List_Navigations_Fixed(Trick_List_6)
    time.sleep(6)
    SendKey('Back',0.8,1)
    SendKey('Down',0.3,1)
    SendKey('Ok',0.8,1) 
    Trick_List_Navigations_Fixed(Trick_List_4)
    time.sleep(6)
#audios
    SendKey('Back',0.8,1)
    SendKey("Left",0.2,6)
    SendKey("Right",0.3,3) 
    SendKey('Down',0.3,7)
    SendKey('Ok',0.8,1) 
    Trick_List_Navigations_Fixed(Trick_List_5)
    
    SendKey('Back',0.8,1)
    SendKey('Down',0.3,1)
    SendKey('Ok',0.8,1) 
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    SendKey('Back',0.8,1)
    SendKey('Down',0.3,1)
    SendKey('Ok',0.8,1) 
    Trick_List_Navigations_Fixed(Trick_List_6)
    
    SendKey('Back',0.8,1)
    SendKey('Down',0.3,1)
    SendKey('Ok',0.8,1) 
    Trick_List_Navigations_Fixed(Trick_List_3)

def DropBox_Demome():
    Down_Count = [0,1,2,3,4,5]
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    time.sleep(3)
    SendKey('Up',0.7,1)
    SendKey('Ok',0.7,1)
    SendKey("Right",0.7,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    time.sleep(18)
    SendKey('Sources',4,1)
    SendKey('Ok',2,1)
    SendKey("Left",0.7,1)
    SendKey('Down',0.4,2)
    SendKey('Right',0.4,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_3)
    time.sleep(20)
    SendKey('Sources',4,1)
    SendKey('Ok',2,1)
    SendKey("Left",0.7,1)
    SendKey('Down',0.4,2)
    SendKey('Right',0.4,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    time.sleep(19)
    SendKey('Sources',4,1)
    SendKey('Ok',2,1)
    SendKey("Left",0.7,1)
    SendKey('Down',0.4,4)
    SendKey('Right',0.4,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_1)
    time.sleep(25)

def DropBox_StabilityFolder_Demome():
    Down_Count = [0,1,2,3,4,5]
    Down_Count1 = [6,7,8,9,10,11]
    Down_Count2 = [12,13,14,15,16,17]
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
#videos
    SendKey('Left',0.3,4)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,3)
    SendKey('Ok',1,1)
    
    SendKey("Down", 3,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    time.sleep(20)
#audio
    SendKey('Sources',4,1)
    SendKey('Ok',2,1)
    SendKey('Left',0.3,4)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,3)
    SendKey('Ok',1,1)
  
    SendKey("Down", 3,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count1))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    time.sleep(19)
 #Images   
    SendKey('Sources',4,1)
    SendKey('Ok',2,1)
    SendKey('Left',0.3,4)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,3)
    SendKey('Ok',1,1)
    
    SendKey("Down", 3,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count2))
    SendKey('Ok',3,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    time.sleep(20)
    
def SwitchingChannels_Demome():
    time.sleep(15)
    
    Digit_Channel_Selection("Tuner",5)
    time.sleep(5)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,1)
    SendKey("Volume_Down",0.1,7)
    time.sleep(25)
    
    Digit_Channel_Selection("Satellite",83)
    time.sleep(5)
    SendKey("Volume_Down",0.1,7)
    SendKey("Mute",0.3,4)
    SendKey("Volume_Up",0.1,7)
    time.sleep(20)
    
    Digit_Channel_Selection("Tuner",14)
    time.sleep(5)
    SendKey("Volume_Down",0.1,4)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,2)

    time.sleep(18)
    SendKey("Back",4,1)
    
    Digit_Channel_Selection("Satellite",147)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,1)
    SendKey("Volume_Down",0.1,5)
    time.sleep(21)


    Digit_Channel_Selection("Tuner",20)
    time.sleep(3)
    SendKey("Volume_Down",0.1,7)
    SendKey("Mute",0.3,3)
    SendKey("Volume_Up",0.1,7)
    SendKey("Volume_Down",0.1,4)
    time.sleep(19)
    
    Digit_Channel_Selection("Satellite",92)
    time.sleep(4)
    SendKey("Volume_Up",0.1,8)
    SendKey("Mute",0.3,5)
    SendKey("Volume_Down",0.1,7)
    time.sleep(22)
       
    Digit_Channel_Selection("Tuner",10)
    time.sleep(5)
    SendKey("Volume_Up",0.1,3)
    SendKey("Volume_Down",0.1,4)
    SendKey("Mute",0.3,3)
    time.sleep(18)
    
    Digit_Channel_Selection("Satellite",121)
    time.sleep(2)
    SendKey("Volume_Down",0.1,7)
    SendKey("Volume_Up",0.1,5)
    SendKey("Mute",0.3,1)
    time.sleep(22)
    
    Digit_Channel_Selection("Tuner",506)
    time.sleep(5)
    SendKey("Volume_Up",0.1,6)
    SendKey("Mute",0.3,1)
    SendKey("Volume_Down",0.1,3)

    time.sleep(18)
    
    Digit_Channel_Selection("Satellite",86)
    time.sleep(5)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,5)
    SendKey("Volume_Up",0.1,7)

    time.sleep(19)

def Switching_Satellite_Channels_Demome():
    time.sleep(15)
    
    Digit_Channel_Selection("Satellite",81) #81 - Test UHD1
    time.sleep(18)
    
    SendKey("2",0.2,1)
    SendKey("3",0.2,1)
    SendKey("9",0.2,1)
    time.sleep(5)
    SendKey("Ok",3,1)
    SendKey("Volume_Up",0.1,10)
    SendKey("Volume_Down",0.1,3)
    SendKey("Mute",0.3,11)
    time.sleep(19)
    
    SendKey("Exit",5,1)
    SendKey("1",0.2,1)
    SendKey("4",0.2,1)
    SendKey("7",0.2,1)
    
    SendKey("Ok",1,1) # Launching Channel List

    time.sleep(20)
    SendKey("Exit",5,1)
    
    SendKey("2",0.2,1)
    SendKey("2",0.2,1)
    SendKey("0",0.2,1)
    time.sleep(18)
    SendKey("Back",1,2)
    SendKey("Volume_Up",0.1,4)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,6)
    SendKey("Ok",1,1)
    
    SendKey("9",0.2,1)
    SendKey("2",0.2,1)
    time.sleep(25)
    SendKey("Back",1,2)
    SendKey("Volume_Down",0.1,10)
    
    time.sleep(19)

    SendKey("Exit",2,1)
    SendKey("1",0.2,1)
    SendKey("2",0.2,1)
    SendKey("1",0.2,1)
    time.sleep(6)
    SendKey("Volume_Up",0.1,8)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,3)

    time.sleep(18)
    SendKey("Back",2,2)
    
    SendKey("1",0.1,1)
    SendKey("7",0.1,1)
    SendKey("2",8,1)
    SendKey("Volume_Up",0.1,6)
    SendKey("Volume_Down",0.1,4)
    
    SendKey("1",0.1,1)
    SendKey("9",0.1,1)
    SendKey("9",0.2,1)
    time.sleep(18)


    SendKey("Exit",5,1)
    SendKey("2",0.1,1)
    SendKey("0",0.1,1)
    SendKey("8",4,1)
    
    SendKey("Mute",0.3,4)
    time.sleep(4)
    SendKey("Ok",0.4,1)
    SendKey("Up_longpress",0.2,1)
    time.sleep(20)
    
def Switching_Tuner_Channels_Demome():
    time.sleep(15)
    Digit_Channel_Selection("Tuner",5)
    time.sleep(1)
    SendKey("Volume_Down",0.1,3)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.3,8)
    SendKey("1",0.2,1)
    SendKey("4",0.2,1)
    time.sleep(18)
    SendKey("Exit",5,1)
    
    SendKey("Volume_Up",0.1,12)
    SendKey("Volume_Down",0.1,3)
    SendKey("Mute",0.3,3)
    SendKey("Ok",0.5,1)
    SendKey("5",0.2,1)
    SendKey("1",0.2,1)
    SendKey("3",0.2,1)
    
    time.sleep(20)
    SendKey("Exit",5,1)
    
    SendKey("Ok",3,1)
    SendKey("Volume_Down",0.1,3)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.2,1)
    SendKey("Volume_Down",0.1,9)
    SendKey("2",0.2,1)
    SendKey("0",0.2,1)
    time.sleep(4)
    SendKey("Volume_Down",0.1,3)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.2,6)
    SendKey("Volume_Down",0.1,9)
    SendKey("Volume_Up",0.1,7)
    SendKey("1",0.2,1)
    SendKey("0",0.2,1)

    time.sleep(19)

    SendKey("Exit",5,1)
    
    SendKey("Ok",0.4,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Ok",3,1)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.2,5)
    SendKey("Volume_Down",0.1,9)
    SendKey("Mute",0.3,4)
    

    
    SendKey("5",0.2,1)
    SendKey("3",0.2,1)
    SendKey("9",0.2,1)
    time.sleep(5)
    SendKey("Ok",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok",3,1)
    SendKey("5",0.2,1)
    SendKey("0",0.2,1)
    SendKey("6",0.2,1)
    time.sleep(18)
    SendKey("Back",2,2)
##    time.sleep(3)
    SendKey("Volume_Down",0.1,3)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.2,9)
    SendKey("2",0.2,1)
    SendKey("8",0.2,1)
    time.sleep(21)

    
    SendKey("Mute",0.2,4)
    SendKey("Volume_Up",0.1,4)
    SendKey("Volume_Down",0.1,3)
    time.sleep(3.5)
    SendKey("Ok",0.4,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Ok",3,1)
    time.sleep(30)

def Timeshift_Demome():
    Digit_Channel_Selection("Satellite",83)
    time.sleep(20)
    SendKey("Exit",5,1)
    SendKey("Pause",20,1)
    SendKey("Exit",5,1)
    SendKey("Pause",7,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    time.sleep(20)
    SendKey("Exit",5,1)
    SendKey("1",0.2,1)
    SendKey("6",0.2,1)
    SendKey("1",0.2,1)
    SendKey("Pause",7,1)
    Trick_List_Navigations_Fixed(Trick_List_3)
    time.sleep(25)
    SendKey("Exit",5,1)
    SendKey("8",0.2,1)
    SendKey("9",0.2,1)
    SendKey("Pause",7,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    time.sleep(19)

def OTR_Demome():
    Digit_Channel_Selection("Satellite",81)
    time.sleep(20)
    SendKey("Exit",5,1)
    SendKey("Rec",18,1)
    SendKey("Exit",5,1)
    SendKey("Stop",1,1)
    SendKey("Left",1,1)
    SendKey("Ok",1,1)
    SendKey("1",0.2,1)
    SendKey("5",0.2,1)
    SendKey("1",0.2,1)
    SendKey("Rec",25,1)
    SendKey("Exit",5,1)
    SendKey("Stop",1,1)
    SendKey("Left",1,1)
    SendKey("Ok",1,1)
    SendKey("9",0.2,1)
    SendKey("3",0.2,1)
    SendKey("Rec",25,1)
    SendKey("Exit",5,1)
    SendKey("Stop",1,1)
    SendKey("Left",1,1)
    SendKey("Ok",1,1)
    
    
    
def HDMI_Revanth():
    #hdmi-1 trickmodes & quicksettings
    SendKey("Sources",0.6,1)
    SendKey("Up_longpress",0.6,1)
    SendKey("Down",0.7,8)
    SendKey("Ok",1,2)
    time.sleep(120)
    Trick_List_Navigations_Fixed(Trick_List_5)
##    Trick_List_Navigations_Fixed(Trick_List_4)
    HDMI_QuickSettings_Revanth()
    #hdmi switching
    #1-2-3-4
    for count in range(0,3):
        SendKey("Sources",0.7,1)
        SendKey("Down",0.7,1)
        SendKey("Ok",10,1)
    #4-3-2-1
    for count in range(0,3):
        SendKey("Sources",0.7,1)
        SendKey("Up",0.7,1)
        SendKey("Ok",10,1)
    #hdmi-2 tricmodes & quicksettings
    SendKey("Sources",0.6,1)
    SendKey("Down",0.6,1)
    SendKey("Ok",60,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    HDMI_QuickSettings_Revanth()

    #2-4
    SendKey("Sources",0.6,1)
    SendKey("Down",0.6,2)
    SendKey("Ok",10,1)

    #4-1
    SendKey("Sources",0.6,1)
    SendKey("Up",0.6,3)
    SendKey("Ok",10,1)

    #1-3
    SendKey("Sources",0.6,1)
    SendKey("Up",0.6,2)
    SendKey("Ok",10,1)
     
def HDMI_QuickSettings_Revanth():
    SendKey("Settings",0.7,1)
    
    #QuickSettings-PictureStyle
    SendKey("Up_longpress",0.7,1)
    SendKey("Right",0.5,1)
    SendKey("Up_longpress",0.7,1)
    for count in range(0,7):
        SendKey("Ok",0.7,1)
        SendKey("Down",0.6,1)
    SendKey("Left",0.5,1)
    
    #QuickSettings-Picture format
    SendKey("Up_longpress",0.7,1)
    SendKey("Down",0.7,1)
    SendKey("Ok",0.5,1)
    SendKey("Up_longpress",0.7,1)
    for count in range(0,4):
        SendKey("Ok",0.7,1)
        SendKey("Down",0.5,1)
    SendKey("Down_longpress",0.5,1)
    SendKey("Ok",0.7,1)
    SendKey("Up_longpress",0.5,1)
    SendKey("Down",0.6,1)
    SendKey("Ok",0.6,1)
    for count in range(0,15):
        SendKey("Up",0.4,6)
        SendKey("Down",0.4,3)
    SendKey("Ok",0.5,1)
    SendKey("Down",0.5,1)
    SendKey("Ok",0.6,1)
    for count in range(0,20):
        SendKey("Up",0.4,6)
        SendKey("Down",0.4,3)
        SendKey("Left",0.4,7)
        SendKey("Right",0.4,5)
    
    SendKey("Ok",0.6,1)
    SendKey("Down",0.6,1)
    SendKey("Ok",0.6,1)
    SendKey("Back",0.5,1)

    #QuickSettings-Sound Style
    SendKey("Settings",0.7,1)
    SendKey("Up_longpress",0.7,1)
    SendKey("Down",0.5,2)
    SendKey("Right",0.5,1)
    SendKey("Up_longpress",0.7,1)
    for count in range(0,7):
        SendKey("Ok",0.6,1)
        SendKey("Down",0.6,1)
    SendKey("Left",0.6,1)

    #QuickSettings-AmbilightStyle
    SendKey("Down",0.5,1)
    SendKey("Ok",0.5,1)
    SendKey("Up_longpress",0.7,1)
    SendKey("Down",0.6,1)
    SendKey("Right",0.5,1)
    SendKey("Up_longpress",0.7,1)
           #video
    for count in range(0,7):
        SendKey("Ok",0.6,1)
        SendKey("Down",0.6,1)
    SendKey("Left",0.5,1)
    SendKey("Down",0.5,1)
    SendKey("Right",0.5,1)
    SendKey("Up_longpress",0.7,1)
          #audio
    for count in range(0,7):
        SendKey("Ok",0.6,1)
        SendKey("Down",0.6,1)
    SendKey("Left",0.5,1)
    SendKey("Down",0.5,1)
    SendKey("Right",0.5,1)
    SendKey("Up_longpress",0.7,1)
         #color
    for count in range(0,5):
        SendKey("Ok",0.6,1)
        SendKey("Down",0.6,1)
        #flag
    SendKey("Left",0.5,1)
    SendKey("Down",0.5,1)
    SendKey("Ok",0.5,1)
    for count in range(0,3):
        SendKey("Down_longpress",0.5,1)
        SendKey("Ok",0.5,1)
        SendKey("Left",0.2,2)
        SendKey("Ok",0.5,1)
        SendKey("Up_longpress",0.5,1)
        SendKey("Ok",0.5,1)
        SendKey("Right",0.2,2)
        SendKey("Ok",0.5,1)
    SendKey("Back",0.5,1)
    SendKey("Ok",0.5,1)
    SendKey("Left",0.5,1)
    SendKey("Back",0.5,1)

       
def Script():
    
    Digit_Channel_Selection("Satellite",83)
    time.sleep(15)
    
    Youtube_Row1_Demome()
    
    OIB_Row1_Demome()
    
    CBPlayback_Images_Demome()
    
    Switching_Satellite_Channels_Demome()
    
    Netflix_Demome()   
    
    CBPlayback_Videos_Demome()
    
    Guide_Demome()
    
    Youtube_Row2_Demome()
    
    Switching_Tuner_Channels_Demome()
    
    CBPlayback_Audios_Demome()
    
    OIB_Row2_Demome()

    OTR_Demome()

    DropBox_StabilityFolder_Demome()
    
    Netflix_Demome()
    
    App_Gallery_Demome()
    
    CBPlayback()
    
    SwitchingChannels_Demome()
    
    DemoMe_App_Demome()
    
    PlayStore_Demome()

    Timeshift_Demome()
    
    DropBox_Demome()
    
  
if __name__ == "__main__":
    for count in range(0,1000):
        Script()
