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
        print ("Socket Connection")
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
client.OpenSocket('172.27.197.141', 40000);
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

Trick_List_1 = [["Forward",10.0], ["Forward",8.0] , ["Forward", 6.0] , ["Forward", 4.0] , ["Forward", 2.0],["Play",1.0]]
Trick_List_2 = [["Rewind",10.0], ["Rewind",8.0] , ["Rewind",6.0] , ["Rewind",4.0] , ["Rewind",2.0],["Play",1.0]]
Trick_List_3 = [["Pause",2.0], ["Play",3.0] , ["Pause",1.0], ["Play",4.0] ,["Pause",5.0], ["Play",2.0] ,["Pause",8.0], ["Play",3.0],["Pause",5.0], ["Play",1.0]]
Trick_List_4 = [["Rewind",2.0], ["Rewind",8.0] , ["Forward",1.0] , ["Forward",4.0] , ["Pause",3.0], ["Play",4.0], ["Rewind",1.0], ["Rewind",1.0], ["Rewind",3.0],["Play",1.0]]
Trick_List_5 = [["Pause",2.0], ["Rewind",1.0] , ["Forward",1.0 ], ["Forward",2.0] , ["Play",3.0], ["Pause",2.0], ["Forward",3.0], ["Rewind",2.0], ["Rewind",2.0], ["Play",4.0], ["Pause",4.0],
                ["Rewind",1.0], ["Rewind",2.0], ["Rewind",3.0], ["Forward",1.0], ["Forward",1.0], ["Forward",1.0], ["Play",4.0], ["Rewind",2.0], ["Rewind",2.0], ["Pause",2.0],
                ["Forward",1.0], ["Forward",2.0], ["Forward", 3.0], ["Forward", 4.0], ["Pause", 2.0], ["Rewind", 1.0], ["Rewind", 1.0], ["Rewind", 2.0], ["Rewind", 2.0],["Play", 8.0]]
Trick_List_6 = [["Rewind",0.8], ["Forward",1], ["Pause",0.7], ["Play",0.2], ["Rewind",1], ["Rewind",0.5], ["Rewind",0.3],["Forward",10.0], ["Forward",0.3] , ["Rewind", 15] ,
                ["Forward", 1],["Pause",0.5], ["Play",0.4] , ["Pause",0.3], ["Play",0.5] ,["Pause",0.6], ["Play",0.3] ,["Pause",0.4], ["Play",0.4],["Pause",0.5], ["Play",0.5],
                ["Pause",1], ["Rewind",5] , ["Forward",3 ], ["Forward",0.3] , ["Play",4], ["Pause",2.0], ["Forward",0.4], ["Rewind",0.2], ["Rewind",0.3], ["Play",3], ["Pause",0.7],
                ["Rewind",0.2], ["Rewind",0.2], ["Rewind",0.2], ["Forward",0.2], ["Forward",0.3], ["Forward",0.3], ["Play",6], ["Rewind",10], ["Rewind",0.2], ["Pause",5],
                ["Forward",0.7], ["Forward",0.4], ["Forward", 0.4], ["Forward", 0.2], ["Pause", 3], ["Rewind", 0.1], ["Rewind", 0.5], ["Rewind", 0.5], ["Rewind", 0.5],["Forward", 0.9],["Play",1.0]]

#Text_Zap_List = [10,11,12,13,14]

Random_Standby_Wakeup_List = ["Blue","Exit","Home","Netflix","Ambilight",0, "Channel_Up", "Channel_Down"]
Wakeup_Time_List = [[7,8],[15,9], [25,9],[3,6], [2,5],[13,10], [14,12],[1,7], [10,10],[12.5,8]]

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

Apps_In_Row1 = [1,2,3,4]
Apps_In_Row2 = [5,6,7,8]
Apps_In_Row3 = [9,10,11,12]
Apps_In_Row4 = [13,14,15,16]
Apps_In_Row5 = [17,18,19,20]

def Home_Positioning_Launch_App(App_Number):
    SendKey('Home_longpress', 4, 1)
    
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
        time.sleep(7)
    time.sleep(8)
    
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
    time.sleep(2)

def Switch_To_Tuner():
    SendKey("Sources")
    time.sleep(3.5)
    SendKey("Up_longpress")
    time.sleep(0.5)
    for count in range(0,3):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(3)

def Netflix_Standby_Revanth(number, number1):
    SendKey('Netflix',5,1)
    SendKey('Ok',1,1)
    SendKey('Back',1,4)
    SendKey('Left',1,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',1,2)
    SendKey('Ok',1,1)
    SendKey('Up',1,1)
    if number <= 5:
        SendKey('Right',1,number-1)
    else:
        SendKey('Left',1,5)
        SendKey('Right',1,1)
        SendKey('Down',1,1)
        SendKey('Right',5,number-6)
    SendKey('Ok',5,2)
    time.sleep(20)
    Trick_List_Navigations_Fixed(Trick_List_5)
    
    SendKey("Standby",20,1)
    SendKey("Netflix",7,1)
    SendKey('Ok',10,1)
    SendKey("Forward",2,1)
    SendKey('Ok',2,1)
    
    SendKey("Standby",5,2)
    SendKey('Ok',10,1)
    SendKey("Rewind",2,1)
    SendKey('Ok',2,1)

    SendKey("Standby",14,1)
    SendKey("Standby",6,1)
    SendKey('Ok',10,1)
    SendKey("Pause",3,1)

    SendKey("Standby",18,1)
    SendKey("Netflix",7,1)
    
    SendKey('Ok',1,1)
    SendKey('Back',1,4)
    SendKey('Left',1,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',1,2)
    SendKey('Ok',1,1)
    SendKey('Up',1,1)
    
    if number <= 5:
        SendKey('Right',1,number1-1)
    else:
        SendKey('Left',1,5)
        SendKey('Right',1,1)
        SendKey('Down',1,1)
        SendKey('Right',5,number1-6)
    SendKey('Ok',5,2)
    time.sleep(20)
    Trick_List_Navigations_Fixed(Trick_List_5)

    SendKey("Standby",16,1)
    SendKey("Standby",6,1)
    SendKey('Ok',10,1)
    SendKey("Pause",3,1)

    SendKey("Standby",12,1)
    SendKey("Netflix",7,1)

    SendKey("Standby",25,1)
    SendKey("Netflix",7,1)
    SendKey('Ok',10,1)
    SendKey("Forward",2,1)
    SendKey('Ok',2,1)
    
    SendKey("Standby",5,2)
    SendKey('Ok',10,1)
    SendKey("Rewind",2,1)
    SendKey('Ok',2,1)
    
def App_Gallery_Nav_Standby_Revanth():
    SendKey("Smart_Home",10,1)
    #Featured apps category
    SendKey("Up_longpress",1,1)
    SendKey("Down_longpress",1,1)
    SendKey("Left_longpress",1,1)
    SendKey("Up_longpress",1,1)
    SendKey("Left_longpress",1,1)
    SendKey("Down_longpress",1,1)
    SendKey("Standby",4,2)
    SendKey("Right",1,1)
    SendKey("Up",1,4)
    SendKey("Right",1,1)
    SendKey("Down",1,4)
    SendKey("Right",1,1)
    SendKey("Up",1,4)
    SendKey("Right",1,1)
    SendKey("Down",1,4)
    SendKey("Right",1,4)
    SendKey("Up",1,1)
    SendKey("Left",1,4)

    SendKey("Standby",45,1)
    SendKey("Exit",5,1)

 #All category
    SendKey("Smart_Home",10,1)
    SendKey("Smart_Home",10,1)
    SendKey("Up_longpress",1,1)
    SendKey("Down",1,1)
    SendKey("Right",1,1)
    SendKey("Ok",1,1)

    for count in range(0,15):
        SendKey("Down",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
    SendKey("Standby",8,1)
    SendKey("Standby",4,1)
    for count in range(0,10):
        SendKey("Up",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Left",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",1,2)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        
    SendKey("Standby",5,1)
    SendKey("Netflix",15,1)
    
# New Category
    SendKey("Smart_Home",10,1)
    SendKey("Up_longpress",1,4)
    SendKey("Down",1,1)
    SendKey("Right",1,2)
    SendKey("Ok",1,1)

    for count in range(0,15):
        SendKey("Down",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
    SendKey("Standby",6,1)
    SendKey("Standby",4,1)
    for count in range(0,10):
        SendKey("Up",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Left",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",1,2)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        
    SendKey("Standby",60,1)
    SendKey("Channel_Up",5,1)
    
#Video category
    SendKey("Smart_Home",10,1)        
    SendKey("Up_longpress",1,4)
    SendKey("Down",1,1)
    SendKey("Right",1,3)
    SendKey("Ok",1,1)

    for count in range(0,5):
        SendKey("Down",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
    SendKey("Standby",4,1)
    SendKey("Standby",4,1)
    for count in range(0,5):
        SendKey("Up",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Left",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",1,2)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        
    SendKey("Standby",25,1)
    SendKey("7",5,1)     

def Standby_Wakeup_BacktoBack_withStandbyKey():
    SendKey("Standby",15,1)
    SendKey("Standby",5,1)
    
    SendKey("Standby",22,1)
    SendKey("Standby",5,1)
    
    for x in range(0,4):
        SendKey("Standby",4,1)
        SendKey("Standby",4,1)
        
    SendKey("Standby",14,1)
    SendKey("Standby",6,1)
    
    SendKey("Standby",33,1)
    SendKey("Standby",7,1)
    
    SendKey("Standby",4,4)
    
    SendKey("Standby",18,1)
    SendKey("Standby",6,1)
    
    for x in range(0,4):
        SendKey("Standby",5,1)
        SendKey("Standby",5,1)

def Standby_Wakeup_BacktoBack(): 
        SendKey("Standby",5,1)
        SendKey("Netflix",10,1)
        SendKey('Ok',3,3)
        
        SendKey("Standby",22,1)
        SendKey("Standby",5,1)
        
        SendKey("Standby",4,1)
        SendKey("Exit",6,1)
        
        for x in range(0,4):
            SendKey("Standby",5,1)
            SendKey("Standby",5,1)
        
        SendKey("Standby",33,1)
        SendKey("Home",7,1)
        
        SendKey("Standby",4,1)
        SendKey("Ambilight",1,8)
        SendKey("8",4,1)
        
        SendKey("Standby",14,1)
        SendKey("Netflix",5,1)
        
        for x in range(0,4):
            SendKey("Standby",5,1)
            SendKey("Exit",5,1)
        
        SendKey("Standby",16,1)
        SendKey("Channel_Up",5,1)

        SendKey("Standby",10,1)
        SendKey("Standby",3,1)
        
        SendKey("Standby",15,1)
        SendKey("Standby",3,1)    
        
        for x in range(0,4):
            SendKey("Standby",5,1)
            SendKey("Netflix",8,1)
            
# Channel 139 - Satellite
def HBBTV_Monkey():
    SendKey('Red',5,1)
    SendKey('Right',1,2)
    SendKey('Ok',5,1)
    SendKey('Down',2,1)
    SendKey('Ok',1,1)
    for k in range(1,8):
        SendKey('Ok',20,1)
        SendKey('Down',1,1)
        SendKey('Right',1,2)
        SendKey('Ok',0.4,3)
        SendKey('Left',0.5,3)
        SendKey('Ok',0.4,3)
        SendKey('Down',1,1)
        SendKey('Ok',2,1)
        SendKey('Right',2,1)
    SendKey('Down',3,1)
    for j in range(1,7):
        SendKey('Ok',20,1)
        SendKey('Down',1,1)
        SendKey('Right',1,2)
        SendKey('Ok',0.4,3)
        SendKey('Left',0.5,3)
        SendKey('Ok',0.4,3)
        SendKey('Down',1,1)
        SendKey('Ok',2,1)
        SendKey('Right',2,1)

def OIB_Standby_Revanth():
    
    Home_Positioning_Launch_App(3)
    SendKey("Down_longpress",0.3,2)
    SendKey("Left_longpress",0.3,2)
    
    for count in range(0,4):
        SendKey("Right",0.3,count)
        SendKey("Ok",5,1)
        
        SendKey("Down_longpress",0.2,2)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        
        SendKey("Standby",20,1)
        SendKey("Standby",6,1)
        
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        
        SendKey("Standby",5,1)
        SendKey("Standby",5,1)
        
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        
        Random_longpress(20)
        
        SendKey("Standby",18,1)
        SendKey("Standby",4,1)
        
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)

        SendKey("Standby",16,1)
        SendKey("Standby",8,1)

        Random_longpress(20)

        SendKey("Standby",17.5,1)
        SendKey("Standby",6,1)

#        SendKey("Standby",1,1)
#        SendKey("Standby",2,1)
#        SendKey("Standby",1,1)
#        SendKey("Standby",2,1)
#        SendKey("Standby",1,1)
#        SendKey("Standby",2,1)
#        SendKey("Standby",2,1)
        
        SendKey("Back",4,1)
        
    SendKey("Back",2,1)
    SendKey("Ok",2,1)
            
    Standby_Wakeup_BacktoBack()
    SendKey("Exit",5,1)

# 2nd Row of OIB
    Home_Positioning_Launch_App(3)
    SendKey("Down",2,1)
    
    for count in range(0,4):
        SendKey("Right",0.3,count)
        SendKey("Ok",5,1)
            
        SendKey("Ok",5,1)
        
        SendKey("Down_longpress",0.2,2)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        
        SendKey("Standby",4,1)
        SendKey("Standby",8,1)
        
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
    
        Random_longpress(20)
        
        SendKey("Standby",15.5,1)
        SendKey("Standby",4,1)
        
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
    
        SendKey("Standby",21,1)
        SendKey("Standby",8,1)
        
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        
        SendKey("Standby",25,1)
        SendKey("Standby",8,1)
        
        SendKey("Back",4,1)
        
    SendKey("Back",2,1)
    SendKey("Ok",2,1)
               
    Standby_Wakeup_BacktoBack_withStandbyKey()
    SendKey("Exit",2,1)

def Amazon_Standby_Revanth(VideoNo,VideoNo1):
    Home_Positioning_Launch_App(6)
    time.sleep(30)    
    SendKey('Right',1,5) # If we give 6 Rights, then My List will be seen. If we give 5 Right, It will take to Video Library
    SendKey('Ok',3,1)
    SendKey('Right',2,VideoNo-1)
    SendKey('Ok',7,1)
    SendKey('Ok',5,1)
    SendKey('Left',0.2,4)
    SendKey('Ok',1,1) #Playback starts
    Trick_List_Navigations_Fixed(Trick_List_5)

    SendKey("Standby",70,1)
    SendKey("Standby",5,1)
    SendKey('Ok',15,1)
    
    SendKey('Right',1,5) # If we give 6 Rights, then My List will be seen. If we give 5 Right, It will take to Video Library
    SendKey('Ok',3,1)
    SendKey('Right',2,VideoNo1-1)
    SendKey('Ok',7,1)
    SendKey('Ok',5,1)
    SendKey('Left',0.2,4)
    SendKey('Ok',1,1) #Playback starts
    Trick_List_Navigations_Fixed(Trick_List_5)

    SendKey("Standby",5,1)
    SendKey("3",10,1)

def GoogleAssistant_With_Standby_Revanth():    
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.7,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",2,1)
    SendKey("Standby",7,1)
    SendKey("Standby",4,1)
    
    SendKey("Down",0.3,1)
    SendKey("Ok",2,1) # Searching the 1st Result of Voice Search - 
    SendKey("Standby",10,1)
    SendKey("Standby",6,1)

    SendKey("Down",0.3,1)
    SendKey("Right",0.3,1)
    SendKey("Ok",3,1)
    SendKey("Standby",4,1)
    SendKey("Standby",4,1)

    SendKey("Down",0.3,1)
    SendKey("Right",0.3,1)
    SendKey("Ok",3.5,1)
    SendKey("Standby",17,1)
    SendKey("Standby",5,1)

    SendKey("Down",0.5,1)
    SendKey("Right",0.6,1)
    SendKey("Ok",7,1)
    SendKey("Standby",100,1) # Full Standby Case
    SendKey("Standby",10,1)

    # This is for Weather Option in Voice Search
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.5,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down",0.5,1)
    SendKey("Right",0.6,2)
    SendKey("Ok",3,1)
    SendKey("Standby",5,1) # Semi Standby Case
    SendKey("Standby",5,1)
    
    for count in range(0,3):
        SendKey("Down",0.4,1)
        SendKey("Right",0.3,1)
        SendKey("Ok",4,1)
        SendKey("Standby",6,1) # Semi Standby Case
        SendKey("Standby",4,1)

    SendKey("Down",0.3,1)
    SendKey("Right",0.3,2)
    SendKey("Ok",4,1)
    SendKey("Standby",60,1) # Full Standby Case
    SendKey("Standby",4,1)    

    # Back to Back Voice Search Operations with Standby Operations
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.5,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",4,1)

    SendKey("Down",0.5,1)
    SendKey("Ok",3,1)

    for count in range(0,4):
        SendKey("Home",3.5,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",4,1)
        SendKey("Down",0.3,1)
        SendKey("Right",0.4,count)
        SendKey("Ok",2,1)
        SendKey("Standby",6,1) # Semi Standby Case
        SendKey("Standby",5,1)

    # In Weather , Exit to TV (TV is in Background), Voice Search is in Foreground
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.5,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down",0.5,1)
    SendKey("Right",0.6,2)
    SendKey("Ok",1,1)    
    SendKey("Exit",1,1) 
    SendKey("Standby",6,2)
    
    for count in range(0,3):
        SendKey("Down",5,1)
        SendKey("Right",0.6,count)
        SendKey("Ok",5,1)
        SendKey("Standby",5,2)
        
def SkyForce_Revanth():
    SendKey("Home",5,2)
    SendKey("Left",0.7,1)
    SendKey("Right",1,1)
    SendKey("Ok",1,1)
    time.sleep(30)
    SendKey("Ok",5,2)
    SendKey("Right",0.7,1)
    SendKey("Ok",1,2)
    SendKey("Ok",10,1)
    SendKey("Ok",1,3)
    SendKey("Down",0.2,6)
    for count in range(0,4):
        SendKey("Right",0.3,5)
        SendKey("Left_longpress",0.2,1)
        SendKey("Right_longpress",0.2,1)
        SendKey("Left",0.2,5)
    SendKey("Ok",0.5,4)

    SendKey("Standby",60,1)
    SendKey("0",5,1)
    
def Arte_Revanth():
    Home_Positioning_Launch_App(8)
    time.sleep(4)
    Random_longpress(15)
    Random_Navigation(15)
    SendKey("Up_longpress",0.4,2)
    SendKey("Left_longpress",0.4,1)
    SendKey("Right",0.3,2)
    SendKey("Ok",1,1)
    for count in range(0,3):
        SendKey("Right",0.8,1)
        SendKey("Ok",20,1)
        Trick_List_Navigations_Fixed(Trick_List_5)
        time.sleep(5)
        SendKey("Back",0.8,2)
        SendKey("Down",0.7,1)
        
    SendKey("Standby",4,1)
    SendKey("Home",5,1)

def Pacman_Revanth():
    SendKey("Home",5,2)
    SendKey("Left",0.7,1)
    SendKey("Right",1,2)
    SendKey("Ok",1,1)
    time.sleep(20)
    SendKey("Ok",1,10)
    for count in range(0,4):
        SendKey("Up",0.5,1)
        SendKey("Right",0.4,1)
        SendKey("Up",0.4,1)
        SendKey("Left",0.4,1)
    SendKey("Ok",0.6,5)
    SendKey("Exit",2,1)

    SendKey("Standby",22,1)
    SendKey("Netflix",15,1)

def CBPlayback_Standby_Revanth(folder,fileNo,fileNo1):
    
    ''' 1-5 = Video
        6-11 = Audio
        12-47 = Images '''
    
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down',0.3,7)
    SendKey('Up',0.7,2)
    SendKey('Ok',1,1) # Select the Folders in Fav List - Focus is on the 1st Folder --> This is 0 from USB
    if folder==0:
        SendKey('Ok',1,1)
        SendKey('Down',0.5,fileNo-1)
        SendKey('Ok',0.5,2)
        SendKey("Play",10,1)
        Trick_List_Navigations_Fixed(Trick_List_5)
        
    if folder==1:                # Select the 2nd Folder i.e. '1' which is from HDD
##        SendKey('Back',0.4,2)
##        SendKey('Left',0.4,1)
        SendKey('Down',0.4,1)
        SendKey('Right',0.4,1)
        SendKey('Down',0.5,fileNo-1)
        SendKey('Ok',0.5,2)
        SendKey("Play",10,1)
        Trick_List_Navigations_Fixed(Trick_List_5) 

    SendKey("Forward",2,1)
    SendKey("Standby",19,1)
    SendKey("Channel_Up",5,1)  
        
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey("Left",0.2,4)
    SendKey('Up_Longpress',1,1)
    SendKey("Ok",0.3,1)
    SendKey("Right",0.3,1)
    SendKey("Down",0.3,1)
    SendKey("Right",0.3,1)
    SendKey('Right',0.5,fileNo1-1)
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)

    SendKey("Rewind",2,1)
    SendKey("Standby",9,1)
    SendKey("Home",5,1)
    
def CBPlayback_Images_Standby_Revanth():
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    SendKey("Left",0.2,6)
    SendKey("Right",0.2,1)
    SendKey("Down",0.2,2)
    SendKey("Right",0.2,2)
    SendKey("Ok",2,1)
    SendKey("Forward",0.5,9)
    SendKey("Pause",0.5,1)
    SendKey("Rewind",0.5,1)
    SendKey("Stop",0.5,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Ok",5,1)
    SendKey("Down",0.4,2)
    SendKey("Right",0.2,5)
    SendKey("Left",0.2,2)
    SendKey("Ok",5,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    
    SendKey("Standby",6,1)
    SendKey("Channel_Down",5,1)

def CBPlayback():
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    SendKey("Left",0.2,6)
    SendKey("Right",0.2,3)
    SendKey('Ok',5,2)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Pause",2,1)
    SendKey("Standby",5,1)
    SendKey("Home",5,1)

    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    SendKey("Left",0.2,6)
    SendKey("Right",0.2,3)
    SendKey("Down",0.3,1)
    SendKey('Ok',5,2)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Forward",2,1)
    SendKey("Standby",15,1)
    SendKey("Exit",5,1)

    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    SendKey("Left",0.2,6)
    SendKey("Right",0.2,3)
    SendKey("Down",0.3,2)
    SendKey('Ok',5,2)
    Trick_List_Navigations_Fixed(Trick_List_6)
    SendKey("Rewind",2,1)
    SendKey("Standby",22,1)
    SendKey("Netflix",10,1)

    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    SendKey("Left",0.2,6)
    SendKey("Right",0.2,3)
    SendKey("Down",0.3,3)
    SendKey('Ok',5,2)
    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Forward",2,2)
    SendKey("Standby",18,1)
    SendKey("Standby",5,1)

    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    SendKey("Left",0.2,6)
    SendKey("Right",0.2,3)
    SendKey("Down",0.3,4)
    SendKey('Ok',5,2)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Rewind",2,2)
    SendKey("Standby",4,1)
    SendKey("Home",5,1)


def CBPlayback_Favorites():
    ''' 1-5 = Video
        6-11 = Audio
        12-47 = Images '''
    
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    
    SendKey('Right',0.5,2)
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Pause",2,1)
    
    SendKey("Standby",5,1)
    SendKey("Home",5,1)


    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    
    SendKey('Right',0.5,2)
    SendKey('Down',0.5,1)
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Forward",2,1)
    
    SendKey("Standby",15,1)
    SendKey("Exit",5,1)

    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    
    SendKey('Right',0.5,2)
    SendKey('Down',0.5,2)
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    SendKey("Rewind",2,1)
    
    SendKey("Standby",22,1)
    SendKey("Netflix",12,1)

    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    
    SendKey('Right',0.5,2)
    SendKey('Down',0.5,3)
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Forward",2,2)
    
    SendKey("Standby",18,1)
    SendKey("Standby",5,1)
        
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    
    SendKey('Right',0.5,2)
    SendKey('Down',0.5,4)
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Rewind",2,2)
    
    SendKey("Standby",4,1)
    SendKey("Home",5,1)
    
    
def Youtube_Row1_New():
    Home_Positioning_Launch_App(1)
    SendKey("Back",0.4, 4)
    Home_Positioning_Launch_App(1)
    #SendKey("Left_longpress",0.7, 1)
    #SendKey("Up_longpress", 0.5, 1)
    #SendKey("Down", 0.3, 3)
    #SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.3, 1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down_longpress", 0.4, 3)
    SendKey("Right", 0.3, 1)
# 1st Video    
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Play", 1, 1)
    Standby_Wakeup_BacktoBack_withStandbyKey()
    SendKey("Back", 1, 1)
    SendKey("Right", 0.5, 1)
    
# 2nd Video    
    SendKey("Ok", 15.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Play", 1, 1)
    SendKey("Standby",15,1)    
    SendKey("Standby",5,1)
    SendKey("Back", 1, 1)
    SendKey("Right", 0.5, 1)

#3rd Video
    SendKey("Ok", 25.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_4)
    Standby_Wakeup_BacktoBack_withStandbyKey()

def Youtube_Row2_New():
    Home_Positioning_Launch_App(1)
    SendKey("Back",0.4, 4)
    Home_Positioning_Launch_App(1)
    #SendKey("Left_longpress",0.7, 1)
    #SendKey("Up_longpress", 0.5, 1)
    #SendKey("Down", 0.3, 3)
    #SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.3, 1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down_longpress", 0.4, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down", 0.3, 1)
    
# 1st Video    
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_6)
    SendKey("Play", 1, 1)
    SendKey("Back", 1, 1)
    SendKey("Right", 0.5, 1)
    SendKey("Forward",2,4)
    Standby_Wakeup_BacktoBack_withStandbyKey()

# 2nd Video    
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Play", 1, 1)
    SendKey("Standby",18,1)    
    SendKey("Standby",5,1)
    SendKey("Back", 1, 1)
    SendKey("Right", 0.5, 1)
    
#3rd Video    
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Rewind",3,3)
    Standby_Wakeup_BacktoBack_withStandbyKey()

def Channel_AudioLanguage_Standby_Revanth():
    Digit_Channel_Selection("Tuner",5)
    time.sleep(1)
    SendKey("Options",1,1)
    SendKey("Up_longpress",0.3,1)
    SendKey("Down",0.3,3)
    SendKey("Right",0.3,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok",0.2,1)
    
    for count in range(0,10):
        for x in range(0,6):
            SendKey("Down",0.2,1)
            SendKey("Ok",0.3,1)
        for y in range(0,6):
            SendKey("Up",0.2,1)
            SendKey("Ok",0.3,1)
    
    SendKey("Options",0.5,1)
    SendKey("Channel_Up",3,1)
    SendKey("Options",0.5,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down",0.3,3)
    SendKey("Right",0.2,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok",0.2,1)
    
    for count in range(0,10):
        for x in range(0,6):
            SendKey("Down",0.2,1)
            SendKey("Ok",0.3,1)
        for y in range(0,6):
            SendKey("Up",0.2,1)
            SendKey("Ok",0.3,1)
    
    SendKey("Options",0.4,1)
    SendKey("Channel_Up",3,1)
    SendKey("Options",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down",0.3,3)
    SendKey("Right",0.2,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok",0.2,1)
    
    for count in range(0,10):
        for x in range(0,6):
            SendKey("Down",0.2,1)
            SendKey("Ok",0.3,1)
        for y in range(0,6):
            SendKey("Up",0.2,1)
            SendKey("Ok",0.3,1)
    
    SendKey("Standby",22,1)
    SendKey("Netflix",15,1)
    
def SwitchingChannels_Standby_Revanth(): 
    
    Digit_Channel_Selection("Tuner",5)
    time.sleep(1)
    SendKey("Up_longpress",4,1)
    SendKey("Up",0.3,6)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,1)
    SendKey("Down_longpress",3,1)
    SendKey("Down",0.3,6)
    SendKey("Volume_Down",0.1,7)
    
    Digit_Channel_Selection("Satellite",83)
    time.sleep(1)
    SendKey("Channel_Down_longpress",0.2,1)
    SendKey("Channel_Up",0.3,6)
    time.sleep(5)
    SendKey("Volume_Down",0.1,7)
    SendKey("Channel_Up_longpress",0.2,1)
    SendKey("Channel_Down",0.3,5)
    SendKey("Mute",0.3,4)
    SendKey("Volume_Up",0.1,7)
    
    Digit_Channel_Selection("Tuner",14)
    time.sleep(1)
    SendKey("Up_longpress",0.5,1)
    SendKey("Channel_Down",0.3,3)
    SendKey("Volume_Down",0.1,4)
    SendKey("Channel_Down_longpress",0.2,1)
    SendKey("Channel_Up",1,3)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,2)
    
    Digit_Channel_Selection("Satellite",163)
    time.sleep(1)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,1)
    SendKey("Channel_Up_longpress",0.2,1)
    SendKey("Channel_Down",0.3,4)
    SendKey("Volume_Down",0.1,5)
    SendKey("Channel_Up",0.3,2)
    time.sleep(4)
    SendKey("Down_longpress",5,1)
    
    SendKey("Standby",20,1)
    SendKey("9",5,1)

    Digit_Channel_Selection("Tuner",20)
    time.sleep(1)
    SendKey("Volume_Down",0.1,7)
    SendKey("Channel_Up_longpress",0.3,1)
    SendKey("Mute",0.3,3)
    SendKey("Up_longpress",0.2,1)
    SendKey("Volume_Up",0.1,7)
    SendKey("Channel_Down",0.2,6)
    SendKey("Volume_Down",0.1,4)
    
    Digit_Channel_Selection("Satellite",87)
    time.sleep(1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Volume_Up",0.1,8)
    SendKey("Mute",0.3,5)
    SendKey("Volume_Down",0.1,7)
    time.sleep(5)
    
    SendKey("Standby",20,1)
    SendKey("Channel_Up",5,1)
    
    Digit_Channel_Selection("Tuner",10)
    time.sleep(1)
    SendKey("Volume_Up",0.1,3)
    SendKey("Volume_Down",0.1,4)
    SendKey("Up_longpress",3,1)
    SendKey("Channel_Down",0.2,4)
    SendKey("Down_longpress",0.2,1)
    SendKey("Mute",0.3,3)
    SendKey("Channel_Up_longpress",0.5,1)
    
    Digit_Channel_Selection("Satellite",151)
    time.sleep(1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Channel_Up_longpress",0.5,1)
    SendKey("Volume_Down",0.1,7)
    SendKey("Volume_Up",0.1,5)
    SendKey("Channel_Down",0.2,4)
    SendKey("Mute",0.3,1)
    
    SendKey("Standby",12,1)
    SendKey("Exit",5,1)
    
    Digit_Channel_Selection("Tuner",506)
    time.sleep(1)
    SendKey("Channel_Up_longpress",6,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Volume_Up",0.1,6)
    SendKey("Channel_Down_longpress",8,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Mute",0.3,1)
    SendKey("Channel_Up",1,5)
    SendKey("Volume_Down",0.1,3)
    
    Digit_Channel_Selection("Satellite",96)
    time.sleep(1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,5)
    SendKey("Channel_Down_longpress",5,1)
    SendKey("Volume_Up",0.1,7)
    SendKey("Down_longpress",0.2,1)
    SendKey("Channel_Up_longpress",3,1)
    
    SendKey("Standby",12,1)
    SendKey("Home",5,1)
    
def Switching_Satellite_Channels_Revanth():
    
    Digit_Channel_Selection("Satellite",83)
    time.sleep(1)
    
    SendKey("1",0.2,1)
    SendKey("6",0.2,1)
    SendKey("4",0.2,1)
    time.sleep(4)
    SendKey("Ok",3,1)
    SendKey("Volume_Up",0.1,10)
    SendKey("Volume_Down",0.1,3)
    SendKey("Mute",0.3,11)
    
    SendKey("Standby",5,2)
    
    SendKey("1",0.2,1)
    SendKey("5",0.2,1)
    SendKey("1",0.2,1)
    
    SendKey("Ok",1,1) # Launching Channel List
    
    SendKey("1",0.2,1)
    SendKey("5",0.2,1)
    SendKey("7",0.2,1)
    time.sleep(4)
    SendKey("Volume_Up",0.1,4)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,6)
    SendKey("Ok",1,1)
    
    SendKey("9",0.2,1)
    SendKey("2",0.2,1)
    time.sleep(2)
    SendKey("Volume_Down",0.1,10)
    
    SendKey("Standby",40,1)
    SendKey("Exit",5,1)
    
    SendKey("1",0.2,1)
    SendKey("2",0.2,1)
    SendKey("1",0.2,1)
    time.sleep(6)
    SendKey("Volume_Up",0.1,8)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,3)
    
    SendKey("1",0.2,1)
    SendKey("6",0.2,1)
    SendKey("0",0.2,1)
    time.sleep(8)
    SendKey("Volume_Up",0.1,6)
    SendKey("Volume_Down",0.1,4)
    
    SendKey("1",0.2,1)
    SendKey("5",0.2,1)
    SendKey("5",0.2,1)
    time.sleep(5)
    
    SendKey("1",0.2,1)
    SendKey("3",0.2,1)
    SendKey("5",0.2,1)
    SendKey("Mute",0.3,4)
    time.sleep(4)
    SendKey("Ok",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok",3,1)

    SendKey("Standby",5,1)
    SendKey("Exit",5,1)
    
def Switching_Tuner_Channels_Revanth():
    Digit_Channel_Selection("Tuner",5)
    time.sleep(1)
    SendKey("Volume_Down",0.1,3)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.3,8)
    SendKey("1",0.2,1)
    SendKey("4",0.2,1)
    time.sleep(5)
    
    SendKey("Standby",5,2)
    
    SendKey("Volume_Up",0.1,12)
    SendKey("Volume_Down",0.1,3)
    SendKey("Mute",0.3,3)
    SendKey("Ok",0.5,1)
    SendKey("5",0.2,1)
    SendKey("1",0.2,1)
    SendKey("3",0.2,1)
    time.sleep(1)
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
    time.sleep(3)
    SendKey("Ok",0.4,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Ok",3,1)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.2,5)
    SendKey("Volume_Down",0.1,9)
    SendKey("Mute",0.3,4)
    
    SendKey("Standby",28,1)
    SendKey("Exit",5,1)
    
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
    time.sleep(3)
    SendKey("Volume_Down",0.1,3)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.2,9)
    SendKey("2",0.2,1)
    SendKey("8",0.2,1)
    time.sleep(5)
    SendKey("Mute",0.2,4)
    SendKey("Volume_Up",0.1,4)
    SendKey("Volume_Down",0.1,3)
    time.sleep(3.5)
    SendKey("Ok",0.4,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Ok",3,1)

    SendKey("Standby",35,1)
    SendKey("Exit",5,1)

def Switch_Sources_Standby():
    SendKey("Sources",4,1)
    SendKey("Up_longpress",0.3,1)
    SendKey("Down",0.3,1)
    SendKey("Ok",4,1)
    
    for count in range(0,14):
        SendKey("Sources",4,1)
        SendKey("Down",0.3,1)
        SendKey("Ok",4,1)
#ypbpr-fav
    SendKey("Sources",4,1)
    SendKey("Up",0.3,11)
    SendKey("Ok",3,1)
    
    SendKey("Standby",16,1)
    SendKey("Exit",5,1)
    
#fav-tuner
    SendKey("Sources",4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",3,1)
    
    SendKey("Standby",5,2)
    
#tuner-network
    SendKey("Sources",4,1)
    SendKey("Down",0.3,3)
    SendKey("Ok",3,1)
    
    SendKey("Standby",14,1)
    SendKey("Exit",5,1)
    
#network-googleplaymovies
    SendKey("Sources",4,1)
    SendKey("Up",0.3,6)
    SendKey("Down",0.3,4)
    SendKey("Ok",3,1)
    
    SendKey("Standby",18,1)
    SendKey("Netflix",5,1)
    
#gpm-recordings
    SendKey("Sources",4,1)
    SendKey("Down",0.3,3)
    SendKey("Ok",3,1)
    
    SendKey("Standby",8,1)
    SendKey("Standby",5,1)
    
#recorings-satellite
    SendKey("Sources",4,1)
    SendKey("Up",0.3,5)
    SendKey("Ok",3,1)
    
    SendKey("Standby",22,1)
    SendKey("Home",5,1)
    
#satellite-hdmi3
    SendKey("Sources",4,1)
    SendKey("Down",0.3,8)
    SendKey("Ok",3,1)
    
    SendKey("Standby",13,1)
    SendKey("0",5,1)
    
#hdmi3-usb
    SendKey("Sources",4,1)
    SendKey("Up",0.3,5)
    SendKey("Ok",3,1)
    
    SendKey("Standby",21,1)
    SendKey("Standby",5,1)
    
#usb-hdmi4
    SendKey("Sources",4,1)
    SendKey("Down",0.3,6)
    SendKey("Ok",3,1)
    
    SendKey("Standby",11,1)
    SendKey("Channel_Up",5,1)
    
#hdmi4-fav
    SendKey("Sources",4,1)
    SendKey("Up",0.3,10)
    SendKey("Ok",3,1)
    
    SendKey("Standby",5,1)
    SendKey("Channel_Down",5,1)
    
#fav-recordings
    SendKey("Sources",4,1)
    SendKey("Down",0.3,6)
    SendKey("Ok",3,1)
    
    SendKey("Standby",17,1)
    SendKey("7",5,1)
    
#recordins-tuner
    SendKey("Sources",4,1)
    SendKey("Up",0.3,4)
    SendKey("Ok",3,1)
    
    SendKey("Standby",6,1)
    SendKey("Netflix",5,1)
    
#tuner-hdmi1
    SendKey("Sources",4,1)
    SendKey("Down",0.3,5)
    SendKey("Ok",3,1)

    SendKey("Standby",16,1)
    SendKey("Home",5,1)


#### Arun Additional Scripts Start
        
def Test_Function_Arun_Satellite_OTR_Standby_Mains_wakeup():
    
    Digit_Channel_Selection('Satellite', 85)
    time.sleep(1)
    SendKey("Rec")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(1)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    
    Digit_Channel_Selection('Satellite', 83)
    time.sleep(1)
    SendKey("Rec")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    
    Digit_Channel_Selection('Satellite', 91)
    time.sleep(1)
    SendKey("Rec")
    time.sleep(9)
    SendKey("Standby")
    time.sleep(8)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    
    Digit_Channel_Selection('Satellite', 126)
    time.sleep(1)
    SendKey("Rec")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(6)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    
    Digit_Channel_Selection('Satellite', 176)
    SendKey("Rec")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(9)
    SendKey(random.choice(Random_Standby_Wakeup_List))      
    
def Test_Function_Arun_Satellite_Timeshift_Standby_Mains_wakeup():
    Digit_Channel_Selection('Satellite', 152)
    time.sleep(1)
    SendKey("Pause")
    time.sleep(10)
    Random_TrickModes(5)
    SendKey("Standby")
    time.sleep(9)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    
    SendKey("Exit")
    time.sleep(0.5)
    SendKey("Channel_Up")
    time.sleep(0.1)
    SendKey("8")
    time.sleep(0.1)
    SendKey("3")
    time.sleep(3)
    SendKey("Pause")
    time.sleep(15)
    Random_TrickModes(10)
    SendKey("Standby")
    time.sleep(22)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    
    Switch_To_Satellite()
    SendKey("Channel_Up")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(0.1)
    SendKey("8")
    time.sleep(3)
    SendKey("Pause")
    time.sleep(20)
    Random_TrickModes(7)
    SendKey("Standby")
    SendKey(random.choice(Random_Standby_Wakeup_List))
    
    SendKey("Exit")
    time.sleep(0.5)
    SendKey("Channel_Up")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(3)
    SendKey("Pause")
    time.sleep(30)
    Random_TrickModes(9)
    SendKey("Standby")
    time.sleep(30)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    
    Switch_To_Satellite()
    SendKey("Channel_Up")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(3)
    SendKey("Pause")
    time.sleep(30)
    Random_TrickModes(4)
    SendKey("Standby")
    time.sleep(3)
    SendKey(random.choice(Random_Standby_Wakeup_List))

     
def Test_Function_Arun_Tuner_MHEG_Navigation_PLyaback_Without_Standby():
    Switch_To_Tuner()
    for count in range(0,10):
        SendKey("Channel_Up")
        time.sleep(0.1)
    SendKey("2")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(15)
    
    for count in range(0,3):
        SendKey("Red")
        time.sleep(10)
        SendKey("Down_longpress")
        time.sleep(0.1)
        SendKey("Up_longpress")
        time.sleep(0.1)
        for count in range(0,6):
            SendKey("Right")
            time.sleep(0.1)
        for count in range(0,6):
            SendKey("Left")
            time.sleep(0.1)
        Random_Navigation(10)
        SendKey("Exit")
        time.sleep(10)
        
    SendKey("Red")
    time.sleep(5)
    SendKey("Up_longpress")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(2)
    Random_Navigation(10)
    SendKey("Right")
    time.sleep(0.5)
    SendKey("Up_longpress")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(2)
    for count in range(0,5):
        SendKey("Ok")
        time.sleep(0.1)
        SendKey("Right")
        time.sleep(0.2)
        SendKey("Left")
        time.sleep(0.2)
    SendKey("Back")
    time.sleep(0.1)
    SendKey("Back")
    time.sleep(0.1)
    
    SendKey("Down")
    time.sleep(0.1)
    for count in range(0,6):
        SendKey("Right")
        time.sleep(0.1)
    for count in range(0,6):
        SendKey("Left")
        time.sleep(0.1)
    SendKey("Ok")
    time.sleep(5)
    Random_TrickModes(15)
    SendKey("Back")
    time.sleep(0.5)
    SendKey("Back")
    time.sleep(0.5)
    
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(5)
    Random_TrickModes(5)
    SendKey("Back")
    time.sleep(0.5)
    SendKey("Back")
    time.sleep(0.5)
    
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(5)
    Random_TrickModes(5)
    SendKey("Back")
    time.sleep(0.5)
    SendKey("Back")
    time.sleep(0.5)
    
    SendKey("Exit")
    time.sleep(0.1)
    
    for count in range(0,10):
        SendKey("Channel_Up")
        time.sleep(0.1)
        
def Test_Function_Arun_Tuner_MHEG_Navigation_PLyaback_With_Standby():
    Switch_To_Tuner()
    for count in range(0,10):
        SendKey("Channel_Up")
        time.sleep(0.1)
    SendKey("2")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(15)
    
    for count in range(0,3):
        SendKey("Red")
        time.sleep(10)
        SendKey("Down_longpress")
        time.sleep(0.1)
        SendKey("Up_longpress")
        time.sleep(0.1)
        for count in range(0,6):
            SendKey("Right")
            time.sleep(0.1)
        for count in range(0,6):
            SendKey("Left")
            time.sleep(0.1)
        Random_Navigation(15)
        SendKey("Standby")
        time.sleep(4)
        SendKey(random.choice(Random_Standby_Wakeup_List))
        time.sleep(2)

    time.sleep(15)
    SendKey("Red")
    time.sleep(5)
    SendKey("Up_longpress")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(2)
    Random_Navigation(10)
    SendKey("Right")
    time.sleep(0.5)
    SendKey("Up_longpress")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(2)
    for count in range(0,5):
        SendKey("Ok")
        time.sleep(0.1)
        SendKey("Right")
        time.sleep(0.2)
        SendKey("Left")
        time.sleep(0.2)
    SendKey("Back")
    time.sleep(0.1)
    SendKey("Back")
    time.sleep(0.1)
    SendKey("Standby")
    time.sleep(4)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(2)
    
    time.sleep(15)
    SendKey("Red")
    time.sleep(5)
    SendKey("Up_longpress")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Down")
    time.sleep(0.1) 
    SendKey("Down")
    time.sleep(0.1)
    for count in range(0,6):
        SendKey("Right")
        time.sleep(0.1)
    for count in range(0,6):
        SendKey("Left")
        time.sleep(0.1)
    SendKey("Ok")
    time.sleep(5)
    Random_TrickModes(15)
    SendKey("Back")
    time.sleep(0.5)
    SendKey("Back")
    time.sleep(0.5)
    SendKey("Standby")
    time.sleep(4)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(2)
    
    time.sleep(15)
    SendKey("Red")
    time.sleep(5)
    SendKey("Up_longpress")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(5)
    Random_TrickModes(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(2)

    time.sleep(15)
    SendKey("Red")
    time.sleep(5)
    SendKey("Up_longpress")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(5)
    Random_TrickModes(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(2)
    
    time.sleep(15)
    SendKey("Red")
    time.sleep(5)
    SendKey("Up_longpress")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(5)
    Random_TrickModes(5)
    SendKey("Back")
    time.sleep(0.5)
    SendKey("Back")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(5)
    Random_TrickModes(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(2)
    
    SendKey("Exit")
    time.sleep(0.1)
    
    for count in range(0,10):
        SendKey("Channel_Up")
        time.sleep(0.1)
    
#### Arun Script End    

def TimeShift_With_StandbyOperations_Revanth():

    SendKey("Pause")
    time.sleep(10)
    Trick_List_Navigations_Fixed(Trick_List_5) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(15)
    Trick_List_Navigations_Fixed(Trick_List_1) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(50)
    SendKey("Standby")
    time.sleep(6)

    SendKey("Pause")
    time.sleep(20)
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(4)

    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Standby")
    time.sleep(3.5)
    SendKey("Standby")
    time.sleep(3.5)

    SendKey("Pause")
    time.sleep(10)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(15)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(90)
    SendKey("Standby")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(20)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(70)
    SendKey("Standby")
    time.sleep(15)

    SendKey("Pause")
    time.sleep(10)
    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(5)

def Channel_SubtitleChange_Standby_Revanth():
    Digit_Channel_Selection("Tuner",12)
    time.sleep(1)
    SendKey("Options",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down",0.2,2)
    SendKey("Right",0.2,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down",0.2,1)
    SendKey("Ok",0.3,1)
    SendKey("Left",0.2,1)
    SendKey("Down",0.2,1)
    SendKey("Right",0.2,1)
    SendKey("Ok",0.3,1)
    for count in range(6):
        SendKey("Down",0.3,1)
        SendKey("Ok",4,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",4,1)
    
    SendKey("Standby",5,1)
    SendKey("Channel_Up",5,1)
     
    SendKey("1",0.1,1)
    SendKey("8",0.1,1)
    time.sleep(4)
    SendKey("Options",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down",0.2,3)
    SendKey("Right",0.2,1)
    SendKey("Ok",0.3,1)
    for count in range(6):
        SendKey("Down",0.3,1)
        SendKey("Ok",4,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",4,1)

    SendKey("Standby",22,1)
    SendKey("0",5,1)  
    
    SendKey("2",0.1,1)
    SendKey("0",0.1,1)
    time.sleep(4)
    SendKey("Options",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down",0.2,3)
    SendKey("Right",0.2,1)
    SendKey("Ok",0.3,1)
    for count in range(6):
        SendKey("Down",0.3,1)
        SendKey("Ok",4,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",4,1)
    
    SendKey("2",0.1,1)
    SendKey("8",0.1,1)
    time.sleep(4)
    SendKey("Options",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down",0.2,3)
    SendKey("Right",0.2,1)
    SendKey("Ok",0.3,1)
    for count in range(6):
        SendKey("Down",0.3,1)
        SendKey("Ok",4,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",4,1)
    
    SendKey("Standby",30,1)
    SendKey("Home",10,1) 
    SendKey("Exit",1,1) 

def Guide_Nav():
    ## Launch Guide and perform Navigation inside it

    Switch_To_Tuner()
    
    for count in range(0,2):
        SendKey("TVGuide")
        time.sleep(5)

        Guide_Yellow()

        for count1 in range(0,25):
            SendKey("Right")
            time.sleep(0.2)

        Random_Navigation(20)

        for count2 in range(0,24):
            SendKey("Down")
            time.sleep(0.15)

        Guide_Yellow()
                   
        Random_longpress(15)
            
        for count3 in range(0,23):
            SendKey("Left")
            time.sleep(0.23)

        Random_Navigation(20)
        
        for count4 in range(0,23):
            SendKey("Up")
            time.sleep(0.2)
        
        Random_longpress(15)
        Guide_Yellow()
        SendKey("Exit")
        time.sleep(4)

def Guide_Yellow():
    SendKey("Yellow")
    time.sleep(0.8)
    SendKey("Up_longpress")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    for count in range(8):
        SendKey("Yellow")
        time.sleep(0.8)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(1)        
        
def Guide_Launch_Exit():
    ## Perform Guide Launching and Exiting
    for count in range(2):
        SendKey("TVGuide")
        time.sleep(3)
        SendKey("TVGuide")
        time.sleep(3)
        
    for count in range(3):
        SendKey("TVGuide")
        time.sleep(3)
        SendKey("Right_longpress")
        time.sleep(0.5)
        SendKey("Exit")
        time.sleep(3)
        
    SendKey("TVGuide")
    time.sleep(2)
    SendKey("Exit")
    time.sleep(2)
    
    SendKey("TVGuide")
    time.sleep(4)
    SendKey("TVGuide")
    time.sleep(1)

    for count in range(2):
        SendKey("TVGuide")
        time.sleep(4)
        SendKey("Down_longpress")
        time.sleep(0.6)
        SendKey("Exit")
        time.sleep(3)

    for count in range(4):
        SendKey("TVGuide")
        time.sleep(3)
        SendKey("Right_longpress")
        time.sleep(0.7)
        SendKey("Ok")
        time.sleep(4)
    
    SendKey("TVGuide")
    time.sleep(5)
    SendKey("TVGuide")
    time.sleep(5)

    Guide_Yellow()
    
    SendKey("TVGuide")
    time.sleep(4)
    SendKey("Exit")
    time.sleep(4)
    
    for count in range(0,2):
        for count1 in range(0,5):
            SendKey("Volume_Up")
            time.sleep(0.1)
        for count1 in range(0,5):
            SendKey("Volume_Down")
            time.sleep(0.1)
        for count1 in range(0,4):
            SendKey("Mute")
            time.sleep(0.3)
            SendKey("Mute")
            time.sleep(0.3)
    time.sleep(2)
    
def Volume_Controls():
    ## Perform Volume Control Operations
        
    for count in range(0,3): 
        SendKey("Volume_Up")
        time.sleep(0.2)
        
    SendKey("Mute")
    time.sleep(0.3)

    for count in range(3):
        SendKey("Volume_Down")
        time.sleep(0.3)

    for count in range(3):
        SendKey("Mute")
        time.sleep(0.3)
        
    Random_Volume(10)
    
    for count in range(0,12): 
        SendKey("Volume_Up")
        time.sleep(0.2)

    for count in range(0,12):        
        SendKey("Volume_Down")
        time.sleep(0.2)

    Random_Volume(10)
    
def Random_Volume(Volume_Count):
    for count in range(Volume_Count):
        Volume_List = ["Volume_Up","Mute","Volume_Down"]
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + random.choice(Volume_List) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(0.3)
        
def HDMI_Standby_Revanth():
    SendKey("Sources",0.6,1)
    SendKey("Up_longpress",0.6,1)
    SendKey("Down",0.7,8)
    SendKey("Ok",1,2)
    time.sleep(120)
    SendKey("Standby",80,1)
    SendKey("Standby",5,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby",5,2)
##    Trick_List_Navigations_Fixed(Trick_List_4)
    HDMI_QuickSettings_Revanth()
    SendKey("Standby",25,1)
    SendKey("Standby",5,1)
    #hdmi switching
    for count in range(0,3):
        SendKey("Sources",0.7,1)
        SendKey("Down",0.7,1)
        SendKey("Ok",10,1)
        SendKey("Standby",18,1)
        SendKey("Standby",5,1)

    for count in range(0,3):
        SendKey("Sources",0.7,1)
        SendKey("Up",0.7,1)
        SendKey("Ok",10,1)
        SendKey("Standby",6,1)
        SendKey("Standby",5,1)

    for count in range(0,4):
        SendKey("Sources",0.6,1)
        SendKey("Down",0.6,1)
        SendKey("Ok",1,1)
        Trick_List_Navigations_Fixed(Trick_List_5)
        SendKey("Standby",35,1)
        SendKey("Standby",5,1)
        HDMI_QuickSettings_Revanth()
        SendKey("Standby",5,1)
        SendKey("Standby",5,1)
        
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
    
def Guide_Tuning():
    ## Perform Guide, Tuning to different Channels from Guide
    
    Guide_Down_Counter = 0
    
    for count in range(15):
        SendKey("TVGuide")
        time.sleep(3)

        for count in range(0,Guide_Down_Counter):
            SendKey("Down")
            time.sleep(0.3)
        SendKey("Ok")
        time.sleep(3.5)

        if (Guide_Down_Counter%3 == 0):
            Volume_Controls()
                
        Guide_Down_Counter = Guide_Down_Counter + 1
        
    SendKey("TVGuide")
    time.sleep(4)
    
def Teletext_Nav_Tuner():
    ## Launch Teletext and perform Navigation and increase volume on teletext page
    Digit_Channel_Selection("Tuner",32)
        
    SendKey("Text")
    time.sleep(2)
    for count in range(0,12):
        SendKey("Channel_Up")
        time.sleep(0.3)
        SendKey("Mute")
        time.sleep(0.3)
        SendKey("Volume_Down")
        time.sleep(0.3)
        SendKey("Volume_Down")
        time.sleep(0.3)
        SendKey("Mute")
        time.sleep(0.3)

    SendKey("Volume_Up")
    time.sleep(0.3)
    SendKey("Mute")
    time.sleep(0.3)
    SendKey("Volume_Down")
    time.sleep(0.3)
    SendKey("Volume_Down")
    time.sleep(0.3)
    SendKey("Mute")
    time.sleep(0.3)
    SendKey("Mute")
    time.sleep(0.3)    

    for count in range(0,13):
        SendKey("Up")
        time.sleep(0.3)
        SendKey("Volume_Up")
        time.sleep(0.3)
        
    SendKey("Mute")
    time.sleep(0.3)
    SendKey("Volume_Down")
    time.sleep(0.3)
    SendKey("Volume_Down")
    time.sleep(0.3)
    SendKey("Mute")
    time.sleep(0.3)

    for count in range(0,15):
        SendKey("Down")
        time.sleep(0.2)
    SendKey("Mute")
    time.sleep(0.3)
    SendKey("Volume_Down")
    time.sleep(0.3)
    SendKey("Volume_Down")
    time.sleep(0.3)
    SendKey("Mute")
    time.sleep(0.3)

    SendKey("Text")

    Random_Teletext_Zap(3)

def Random_Teletext_Zap(Text_Zap_Count):
    SendKey("Exit")
    time.sleep(2)
    for count in range(Text_Zap_Count):
        Text_Zap_List = [["1","0"],["1","5"],["1","2"],["1","3"],["1","4"]]

        Text_List_Temp = random.choice(Text_Zap_List)
        if type(Text_List_Temp) is list:
            for x in range(0,len(Text_List_Temp)):
                SendKey(str(Text_List_Temp[x]))
                time.sleep(.1)
            #time.sleep(.3)
        else:
            client.SendMessage(str(Text_List_Temp))
            #time.sleep(.3)
        time.sleep(4)
        Random_Text(40)
                                      
def Random_Text(Text_Count):
    SendKey("Text")
    time.sleep(4)
                   
    for count in range(3):
        SendKey("8")
    time.sleep(10)
                   
    for count in range(Text_Count):
        Text_List = ["Channel_Up","Down",["8","8","8"],["1","1","1"],"Channel_Down",["3","3","3"],"Up","Up_longpress","Down_longpress",["2","2","2"],["7","7","7"],["9","9","9"],["5","5","6"],
                     ["5","5","5"],["7","5","6"],["1","2","5"],["2","7","0"],["3","0","2"],"Yellow","Red","Green",["3","2","5"],["3","8","2"],["4","1","2"],["4","3","5"],["5","1","2"],["6","2","2"],["7","5","0"]]
        Text_List_Temp = random.choice(Text_List)
        if type(Text_List_Temp) is list:
            for x in range(0,len(Text_List_Temp)):
                SendKey(str(Text_List_Temp[x]))
                time.sleep(.1)
            time.sleep(.5)    
        else:
            SendKey(str(Text_List_Temp))

        time.sleep(0.4)
        
        if (count%5 == 0):
            Random_Volume(5)
        if (count%4 == 0)    :
            Text_Yellow_Green_Red_Nav(25)

    SendKey("Text")
    time.sleep(2)
    SendKey("Exit")
    time.sleep(2)
    Text_Yellow_Green_Red_Nav(35)

def Text_Yellow_Green_Red_Nav(Text_Count):
                  
    for count in range(Text_Count):
        Text_List = ["Yellow","Red","Green"]
        Text_List_Temp = random.choice(Text_List)
        if type(Text_List_Temp) is list:
            for x in range(0,len(Text_List_Temp)):
                SendKey(str(Text_List_Temp[x]))
                time.sleep(0.1)
            time.sleep(0.2)    
        else:
            SendKey(str(Text_List_Temp))
        time.sleep(0.2)    

def Switch_To_Recordings():
    SendKey("Sources")
    time.sleep(3.5)
    SendKey("Up_longpress")
    time.sleep(0.5)
    for count in range(0,7):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(2)

def PVRRecording_Playback_Standby_Revanth():
    Switch_To_Recordings()
    SendKey("Up", 0.3,2)
    SendKey("Down", 0.3,2)
    SendKey("Ok")
    time.sleep(0.8)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(0.6)
    SendKey("Play")
    Trick_List_Navigations_Fixed(Trick_List_5) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(16)

    SendKey("5",5,1)
    
    
    Switch_To_Recordings()
    SendKey("Up", 0.3,2)
    SendKey("Down", 0.3,3)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Play")

    Trick_List_Navigations_Fixed(Trick_List_4) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(50)
    SendKey("Exit",5,1)

def DemoMe_App():
    Home_Positioning_Launch_App(5)
    
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Right")
    time.sleep(0.2)
    SendKey("Right")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(5)

    SendKey("Standby",10,1)
    SendKey("Standby")
    time.sleep(5)

    Home_Positioning_Launch_App(5)

    SendKey("Down")
    time.sleep(0.2)
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(5)

    SendKey("Standby",22,1)
    SendKey("Home")
    time.sleep(5)

    Home_Positioning_Launch_App(5)
    
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(5)

    SendKey("Standby",15,1)
    SendKey("Netflix")
    time.sleep(15)
    
def Megogo_Revanth_Standby_Wakeup():
    Home_Positioning_Launch_App(14)
    time.sleep(60)
    SendKey("Right",0.5,2)
    SendKey("Ok",2,1)
    SendKey("Up",0.7,1)
    SendKey("Right",2,1)
    SendKey("Ok",0.8,1)
    SendKey("Down",0.8,2)
    
    SendKey("Ok",2,1)
    SendKey("Ok",20,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Standby",7,1)
    SendKey("8",5,1)
    
    Home_Positioning_Launch_App(14)
    time.sleep(60)
    SendKey("Right",0.3,2)
    SendKey("Ok",2,1)
    SendKey("Up",0.5,1)
    SendKey("Right",2,1)
    SendKey("Ok",0.8,1)
    SendKey("Down",0.8,2)
    
    SendKey("Ok",2,1)
    SendKey("Ok",20,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    SendKey("Standby",22,1)
    SendKey("Netflix",15,1)

def How_To_App():
    ## DS-SmartTVApps - Invoke How To Application - Navigations inside it

    Home_Positioning_Launch_App(4)
        
    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(1.5)
    SendKey("Play")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(1.8)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(3)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2.5)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Play")
    time.sleep(4)
    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(0.1)
    
    SendKey("Standby",13,1)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Down")
    time.sleep(0.2)
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Right")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(1.5)
    SendKey("Play")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(1.8)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(3)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2.5)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Play")
    time.sleep(4)
    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(0.1) 
    SendKey("Standby",20,1)
    SendKey("Exit")
    time.sleep(5)

def MXPlayer_Standby_Revanth():
    
    Home_Positioning_Launch_App(15)
    
    SendKey("Down",0.4,1)
    SendKey("Ok",0.5,2)
    SendKey("Ok",5,1)    
    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Forward",2,1)
    SendKey("Standby",8,1)
    SendKey("Standby",5,1)
    time.sleep(4)
    
    SendKey("Back",0.2,1)
    SendKey("Right",0.3,1)
    SendKey("Ok",0.5,2)
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Rewind",2,1)
    SendKey("Standby",18,1)
    SendKey("Standby",5,1)
    time.sleep(4)
    
def HDMI():
    
    SendKey("Sources")
    time.sleep(5)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,8):
        SendKey("Down")
        time.sleep(0.4)
    SendKey("Ok") # HDMI 1
    time.sleep(4)
    for count in range(0,4):
        SendKey("Sources")
        time.sleep(3)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(3)
        SendKey("Sources")
        time.sleep(3)
        SendKey("Up")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(3)
    Volume_Controls()
    time.sleep(3)
    SendKey("Netflix")
    time.sleep(5)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Ok")
    time.sleep(3)
    SendKey("Ok")
    time.sleep(5)
    SendKey("Right_longpress")
    time.sleep(7)
    SendKey("OK")
    time.sleep(3)
    
    SendKey("Sources")
    time.sleep(4)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,8):
        SendKey("Down")
        time.sleep(0.5)
    SendKey("Ok") # HDMI 1
    time.sleep(4)
    for count in range(0,3):
        SendKey("Sources")
        time.sleep(2)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(3)
        for count in range(0,3):
            SendKey("Standby")
            time.sleep(5)
            SendKey("Standby")
            time.sleep(5)
        Volume_Controls()
        time.sleep(4)
        SendKey("Sources")
        time.sleep(4)
        for count in range(0,1):
            SendKey("Up_longpress")
            time.sleep(0.5)
        for count in range(0,9):
            SendKey("Down")
            time.sleep(0.5)
            SendKey("Ok")
        time.sleep(3)
        SendKey("Sources")
        time.sleep(3)
        SendKey("Up")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(3)
        for count in range(0,3):
            SendKey("Standby")
            time.sleep(5)
            SendKey("Standby")
            time.sleep(5)
        for count in range(0,4):
            SendKey("Pause")
            time.sleep(0.3)
            SendKey("Play")
            time.sleep(0.3)
            SendKey("Forward")
            time.sleep(3)
            SendKey("Rewind")
            time.sleep(3)
        Quick_Settings()
        time.sleep(4)
        #Youtube()
        time.sleep(3)
        SendKey("Netflix")
        time.sleep(5)
        SendKey("Ok")
        time.sleep(2)
        SendKey("Ok")
        time.sleep(2)
        SendKey("Ok")
        time.sleep(5)
        SendKey("Right_longpress")
        time.sleep(7)
        SendKey("OK")
        time.sleep(3)
        Volume_Controls()
        time.sleep(2)
    SendKey("Sources")
    time.sleep(3)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,8):
        SendKey("Down")
        time.sleep(0.5)
    SendKey("Ok") # HDMI 1
    time.sleep(4)
    for count in range(0,4):
        SendKey("Pause")
        time.sleep(0.3)
        SendKey("Play")
        time.sleep(0.3)
        SendKey("Forward")
        time.sleep(1)
        SendKey("Rewind")
        time.sleep(2)
    SendKey("Standby")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(8)
    Volume_Controls()
    time.sleep(2)
    
#    App_Gallery_Nav_Standby_Revanth()
#    time.sleep(4)
#    OIB()
#    time.sleep(4)
    
    SendKey("Sources")
    time.sleep(4)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,9):
        SendKey("Down")
        time.sleep(0.5)
    SendKey("Ok") # HDMI 2
    time.sleep(4)
    for count in range(0,6):
        SendKey("Standby")
        time.sleep(20)
        SendKey("Standby")
        time.sleep(8)
    Volume_Controls()
    time.sleep(2)
    for count in range(0,4):
        SendKey("Pause")
        time.sleep(0.3)
        SendKey("Play")
        time.sleep(0.3)
        SendKey("Forward")
        time.sleep(3)
        SendKey("Rewind")
        time.sleep(3)
        for count in range(0,5):
            SendKey("Standby")
            time.sleep(5)
            SendKey("Standby")
            time.sleep(5)
    Quick_Settings()
    time.sleep(5)
    SendKey("Sources")
    time.sleep(4)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,9):
        SendKey("Down")
        time.sleep(0.5)
    SendKey("Ok")
    time.sleep(4)
    #USB_Playback()
    #time.sleep(4)
    Volume_Controls()
    time.sleep(1)
    SendKey("Sources")
    time.sleep(5)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,8):
        SendKey("Down")
        time.sleep(0.4)
    SendKey("Ok") # HDMI 1
    time.sleep(4)
    for count in range(0,4):
        SendKey("Sources")
        time.sleep(3)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(3)
        SendKey("Sources")
        time.sleep(3)
        SendKey("Up")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(3)
        for count in range(0,6):
            SendKey("Standby")
            time.sleep(20)
            SendKey("Standby")
            time.sleep(8)
        SendKey("Netflix")
        time.sleep(5)
        SendKey("Ok")
        time.sleep(2)
        SendKey("Ok")
        time.sleep(2)
        SendKey("Ok")
        time.sleep(5)
        SendKey("Right_longpress")
        time.sleep(7)
        SendKey("OK")
        time.sleep(3)
    #USB_Playback()
    #time.sleep(5)
    
def Quick_Settings():
    
        SendKey("Settings")
        time.sleep(5)
        SendKey("Up_longpress")
        time.sleep(0.5)
        for count in range(2):
            SendKey("Right")
            time.sleep(0.4)
        
        #print " Checking the Picture Sytle"
        for count4 in range(1):
            SendKey("Up_longpress")
            time.sleep(1.5)
        SendKey("Ok")
        time.sleep(0.8)
        SendKey("Down")
        time.sleep(0.5)
        SendKey("Ok")
        time.sleep(0.6)
        SendKey("Down")
        time.sleep(0.5)
        SendKey("Ok")
        time.sleep(0.8)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.6)
        SendKey("Down")
        time.sleep(0.4)
        SendKey("Ok")
        time.sleep(0.7)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.7)
        SendKey("Down")
        time.sleep(0.5)
        SendKey("Ok")
        time.sleep(0.8)

      ## Checking the Sound --> Sound Styles
        #print "Checking the Sound --> Sound Style"
        
        for count in range(1):
            SendKey("Left")
            time.sleep(0.25)
        for count in range(2):
            SendKey("Down")
            time.sleep(0.3)
        for count in range(2):    
            SendKey("Right")
            time.sleep(0.2)
        SendKey("Up_longpress")
        time.sleep(0.5)
        SendKey("Ok")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.25)
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Ok")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.4)
        SendKey("Ok")
        time.sleep(0.4)
        SendKey("Down")
        time.sleep(0.2)
        SendKey("Ok")
        time.sleep(0.3)    
    
   ## Checking the Ambilight
        #print "Quick Settings - Checking the Ambilight"
        
        for count in range(1):
            SendKey("Left")
            time.sleep(0.3)
        for count in range(1):
            SendKey("Down")
            time.sleep(0.3)
        
        for count in range(1):    
            SendKey("Right")
            time.sleep(0.3)
                    
        SendKey("Up_longpress")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.5)
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Ok")
        time.sleep(0.5)
        SendKey("Up_longpress")
        time.sleep(0.3)
        for count in range(6):
            SendKey("Down")
            time.sleep(0.3)
            SendKey("Ok")
            time.sleep(0.3)
            
    ## Ambilight Style - Follow Audio
        #print "Ambilight Style - Follow Audio"
        
        for count in range(1):
            SendKey("Left")
            time.sleep(0.3)
        for count in range(1):
            SendKey("Down")
            time.sleep(0.3)
        for count in range(1):    
            SendKey("Ok")
            time.sleep(0.6)
            
        SendKey("Up_longpress")
        time.sleep(0.3)
        
        for count in range(7):
            SendKey("Down")
            time.sleep(0.25)
            SendKey("Ok")
            time.sleep(0.25)

    ## Ambilight Style - Follow Colour
        #print "Ambilight Style - Follow Colour"
        for count in range(1):
            SendKey("Left")
            time.sleep(0.3)
        for count in range(1):
            SendKey("Down")
            time.sleep(0.3)
        for count in range(1):    
            SendKey("Ok")
            time.sleep(0.6)
            
        SendKey("Up_longpress")
        time.sleep(0.3)
        
        for count in range(5):
            SendKey("Down")
            time.sleep(0.25)
            SendKey("Ok")
            time.sleep(0.25)
        for count in range(1):
            SendKey("Left")
            time.sleep(0.3)
        for count in range(3):
            SendKey("Down")
            time.sleep(0.3)
        for count in range(1):    
            SendKey("Ok")
            time.sleep(0.6)
            
        SendKey("Down_longpress")
        time.sleep(0.3)
        for count in range(2):
            SendKey("Up")
            time.sleep(0.25)
            SendKey("Ok")
            time.sleep(0.25)

        ## Screen Off
        #print "Screen Off"
        for count in range(1):
            SendKey("Left")
            time.sleep(0.3)
        for count in range(2):
            SendKey("Down")
            time.sleep(0.3)
        for count in range(1):    
            SendKey("Ok")
            time.sleep(9)
            
        SendKey("Ok")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(9)
            
        SendKey("Ok")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(9)
            
        SendKey("Ok")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(9)
            
        SendKey("Ok")
        time.sleep(0.3)

        SendKey("Blue")
        time.sleep(4)
        SendKey("Right_longpress")
        time.sleep(0.3)
        SendKey("Down_longpress")
        time.sleep(0.3)
        SendKey("Left_longpress")
        time.sleep(0.3)

def Standby_Wakeup_3():
    for count in range(0,5):
        SendKey("Standby",3,1)
        SendKey("Standby",2.5,1)
    time.sleep(5)
    SendKey("Exit",5,1)
def Standby_Wakeup_Keys_Semi_Full():
    # 3 Seconds delay between Standby/Wakeups
    for count in range(0,7):
        SendKey("Standby",4,1)
        SendKey("Standby",3,1)
        SendKey("Standby",3,1)
    time.sleep(4)
    SendKey("Exit",3,1)
    # Different Keys to Wakeup - Semi Standby
    for count in range(0,3):
        SendKey("Standby",4,1)
        SendKey("Up",0.5,1)
        SendKey("Down",0.5,1)
        SendKey("Ok",0.5,1)
        SendKey("Left",0.5,1)
        SendKey("Right",0.5,1)
        SendKey("Sources",0.5,1)
        SendKey("Up",0.5,1)
        SendKey("Down",0.5,1)
        SendKey("Ok",0.5,1)
        SendKey("Left",0.5,1)
        SendKey("Right",0.5,1)
        
        SendKey("Standby",3.5,1)
        
    # Different Keys to Wakeup - Full Standby
    for count in range(0,3):
        SendKey("Standby",4,1)
        SendKey("Up",0.5,1)
        SendKey("Down",0.5,1)
        SendKey("Ok",0.5,1)
        SendKey("Left",0.5,1)
        SendKey("Right",0.5,1)
        SendKey("Sources",0.5,1)
        SendKey("Up",0.5,1)
        SendKey("Down",0.5,1)
        SendKey("Ok",0.5,1)
        SendKey("Left",0.5,1)
        SendKey("Right",0.5,1)
        time.sleep(22)
        SendKey("Sources",0.5,1)
        SendKey("Up",0.5,1)
        SendKey("Down",0.5,1)
        SendKey("Ok",0.5,1)
        SendKey("Left",0.5,1)
        SendKey("Right",0.5,1)
        SendKey("Sources",0.5,1)
        SendKey("Up",0.5,1)
        SendKey("Down",0.5,1)
        SendKey("Ok",0.5,1)
        SendKey("Left",0.5,1)
        SendKey("Right",0.5,1)
        
        SendKey("Standby",3.5,1)
    
    # Semi + Full Standby
    for count in range(0,3):
        SendKey("Standby",19,1)
        SendKey("Standby",4.2,1)
        SendKey("Standby",18,1)
        SendKey("Standby",4,1)
        SendKey("Standby",17,1)
        SendKey("Standby",3.5,1)
        SendKey("Standby",5,1)
        SendKey("Standby",4,1)
        SendKey("Standby",3.5,1)
        SendKey("Standby",3.5,1)
        SendKey("Standby",4,1)
        SendKey("Standby",4,1)
        time.sleep(4)
        SendKey("Exit",4,1)
    

def Standby_Wakeup_BorderCase():
    # Border Case - 14,15,16 Seconds
    # Selecting Satellite Channels
    Digit_Channel_Selection("Satellite",219)
    for count in range(0,2):
        SendKey("Standby",14,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)

        SendKey("Standby",15,1)
        SendKey("Standby",2,1)
        SendKey("Standby",4,1)

        SendKey("Standby",16,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)

        SendKey("Standby",14.5,1)
        SendKey("Standby",3,1)
        SendKey("Standby",4,1)

        SendKey("Standby",15.5,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)
        
    # Selecting Channel 120
    SendKey("1",0.1,1)
    SendKey("2",0.1,1)
    SendKey("0",4,1)
    for count in range(0,2):
        SendKey("Standby",14,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)

        SendKey("Standby",15,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)

        SendKey("Standby",16,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)

        SendKey("Standby",14.5,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)

        SendKey("Standby",15.5,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)
        
        SendKey("Standby",17,1)
        SendKey("Standby",2,1)
        SendKey("Standby",4,1)
        
        SendKey("Standby",18,1)
        SendKey("Standby",2.5,1)
        SendKey("Standby",4,1)
        
    # Launching Netflix
    SendKey("Netflix",9,1)
    
    for count in range(0,2):
        SendKey("Standby",14,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)
        SendKey("Ok",1,3)

        SendKey("Standby",15,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)
        SendKey("Ok",1,3)

        SendKey("Standby",16,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)
        SendKey("Ok",1,3)

        SendKey("Standby",14.5,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)
        SendKey("Ok",1,3)

        SendKey("Standby",15.5,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)
        SendKey("Ok",1,3)
        
        SendKey("Standby",17,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)
        SendKey("Ok",1,3)
        
        SendKey("Standby",18,1)
        SendKey("Standby",1,1)
        SendKey("Standby",4,1)
        SendKey("Ok",1,3)

def PiP_Standby():
    Digit_Channel_Selection("Satellite",81)
    
    for x in range(0,5):
        SendKey('Netflix',5,1)
        SendKey('Ok',1,1)
        SendKey('Back',1,4)
        SendKey('Left',1,5)     
        SendKey('Down',0.3,8)
        SendKey('Up',1,2)
        SendKey('Ok',1,3)
        time.sleep(10)
#Opening PiP    
        Switch_To_Satellite()
        SendKey("Options",1,1)
        SendKey('Ok',3,1)
        SendKey("Play",10,1)
        SendKey("Exit",2,1)
        SendKey("Options",1,1)
        SendKey('Ok',3,1)
        SendKey('Ok',5,1)
        Switch_To_Tuner()
        SendKey("Options",1,1)
        SendKey('Ok',5,1)
    
    SendKey("Standby",16,1)
    SendKey("Standby",6,1)
        
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down',0.3,7)
    SendKey('Up',0.7,2)
    SendKey('Right',0.8,2) 
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    SendKey("Standby",6,1)
    SendKey("Standby",5,1)
        
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,7)
    SendKey('Ok',1,3)
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',3,1)
    SendKey("Exit",2,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,4)
    SendKey('Ok',1,3)
    SendKey("Options",1,1)
    SendKey('Ok',3,1)
    
    SendKey("Standby",13,1)
    SendKey("Standby",5,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,8)
    SendKey('Ok',1,3)
    
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    SendKey("Exit",2,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,2)
    SendKey('Ok',5,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,7)
    SendKey('Ok',1,3)
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    SendKey("Standby",20,1)
    SendKey("Exit",5,1)
    
    SendKey("Home",4,1)
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    SendKey('Up',0.3,3)
    SendKey('Down',0.4,1)
    SendKey('Ok',5,1)
    SendKey('Ok',2,1)
    
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    SendKey('Down',0.4,1)
    SendKey('Ok',5,1)
    
    SendKey("Standby",9,1)
    SendKey("Home",5,1)
    for x in range(0,5):
        SendKey("Home_longpress",2,1)
        SendKey('Down',0.4,1)
        SendKey('Ok',5,1)
        SendKey('Right',0.3,1)
        SendKey('Ok',0.5,2)
    
        SendKey("Exit",2,1)
        SendKey("Options",1,1)
        SendKey('Ok',5,1)
    
        SendKey("Standby",15,1)
        SendKey("Exit",5,1) 
   
def PiP_Without_Standby():
    Digit_Channel_Selection("Satellite",81)
    
    for x in range(0,5):
        SendKey('Netflix',5,1)
        SendKey('Ok',1,1)
        SendKey('Back',1,4)
        SendKey('Left',1,5)     
        SendKey('Down',0.3,8)
        SendKey('Up',1,2)
        SendKey('Ok',1,3)
        time.sleep(10)
#Opening PiP    
        Switch_To_Satellite()
        SendKey("Options",1,1)
        SendKey('Ok',3,1)
        SendKey("Play",10,1)
        SendKey("Exit",2,1)
        SendKey("Options",1,1)
        SendKey('Ok',3,1)
        SendKey('Ok',5,1)
        Switch_To_Tuner()
        SendKey("Options",1,1)
        SendKey('Ok',3,1)
        
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down',0.3,7)
    SendKey('Up',0.7,2)
    SendKey('Right',0.8,2) 
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,7)
    SendKey('Ok',1,3)
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',3,1)
    SendKey("Exit",2,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,4)
    SendKey('Ok',1,3)
    SendKey("Options",1,1)
    SendKey('Ok',3,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,8)
    SendKey('Ok',1,3)
    
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    SendKey("Exit",2,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,2)
    SendKey('Ok',5,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,7)
    SendKey('Ok',1,3)
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    SendKey("Exit",2,1)
    
    SendKey("Home",4,1)
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    SendKey('Up',0.3,3)
    SendKey('Down',0.4,1)
    SendKey('Ok',5,1)
    SendKey('Ok',2,1)
    
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    SendKey('Down',0.4,1)
    SendKey('Ok',5,1)
    
    for x in range(0,5):
        SendKey("Home_longpress",2,1)
        SendKey('Down',0.4,1)
        SendKey('Ok',5,1)
        SendKey('Right',0.3,1)
        SendKey('Ok',0.5,2)
    
        SendKey("Exit",2,1)
        SendKey("Options",1,1)
        SendKey('Ok',5,1)

        
def Block1():
    print("*******Block-1 - Start*******")
    
    
    Digit_Channel_Selection("Satellite",83)
    time.sleep(1)
    SendKey("Standby",50,1)
    SendKey("Standby",5,1)

    
    SendKey("1",0.2,1)
    SendKey("5",0.2,1)
    SendKey("1",0.2,1)
    time.sleep(5)
    SendKey("Pause",15,1)
    SendKey("Forward",2,3)
    SendKey("Standby",5,1)
    SendKey("Netflix",10,1)

    print ("Block-1 - Standby_Wakeup_BacktoBack")
    Standby_Wakeup_BacktoBack()

    
    SendKey("1",0.2,1)
    SendKey("6",0.2,1)
    SendKey("3",0.2,1)
    time.sleep(5)
    SendKey("Pause",10,1)
    SendKey("Standby",32,1)
    SendKey("Exit",7,1)
    
    Standby_Wakeup_3()

    print ("Block-1 - Swtich_Sources_Standby")
    Switch_Sources_Standby()

    print ("Block-1 - Standby_Wakeup_BacktoBack")
    Standby_Wakeup_BacktoBack()

    
    Digit_Channel_Selection("Satellite",95)
    time.sleep(1)
    SendKey("Rec",20,1)
    SendKey("Standby",5,1)
    SendKey("Channel_Up",5,1)

    print ("Block-1 - Tuner-9")
    Digit_Channel_Selection("Tuner",9)
    time.sleep(1)
    SendKey("Pause",20,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Forward",3,3)
    SendKey("Standby",40,1)
    SendKey("Channel_Down",6,1)

    Standby_Wakeup_Keys_Semi_Full()

    print ("Block-1 - Standby_Wakeup_BacktoBack")
    Standby_Wakeup_BacktoBack()
  
    print ("Block-1 - Test_Function_Satellite_OTR_Standby")
    Test_Function_Arun_Satellite_OTR_Standby_Mains_wakeup()
    
    print ("Block-1 - Tuner-28")
    Digit_Channel_Selection("Tuner",28)
    time.sleep(1)
    SendKey("Rec",25,1)
    SendKey("Standby",3,1)
    SendKey("Home",7,1)

    print ("Block-1 - Channel_AudioLanguage_Standby")
    Channel_AudioLanguage_Standby_Revanth()
    
    print ("Block-1 - Tuner-31")
    Digit_Channel_Selection("Tuner",31)
    SendKey("Standby",7,1)
    SendKey("Exit",5,1)

    Standby_Wakeup_BorderCase()
    
    print ("Block-1 - Sat-207")
    Digit_Channel_Selection("Satellite",164)
    time.sleep(1)
    SendKey("Standby",40,1)
    SendKey("Channel_Down",6,1)

    print ("Block-1 - TimeShift_With_StandbyOperations")
    TimeShift_With_StandbyOperations_Revanth()
    
    SendKey("Standby",8,1)
    SendKey("Netflix",15,1)

    print ("Block-1 - Standby_Wakeup_BacktoBack")
    Standby_Wakeup_BacktoBack()
    
    print ("Block-1 - Sat-118")
    Digit_Channel_Selection("Satellite",152)
    time.sleep(1)
    SendKey("Red",4,1)
    SendKey("Ok",1,1)
    SendKey("Down",0.5,1)
    SendKey("Ok",15,1)
    SendKey("Standby",60,1)
    SendKey("Channel_Down",5,1)

    Standby_Wakeup_Keys_Semi_Full()

    print ("Block-1 - SwitchingChannels_Standby")
    SwitchingChannels_Standby_Revanth()

    print ("Block-1 - Test_Function_Tuner_MHEG_Navigation_PLyaback_With_Standby")
    Test_Function_Arun_Tuner_MHEG_Navigation_PLyaback_With_Standby()

    print ("Block-1 - Tuner-1")
    Digit_Channel_Selection("Tuner",1)
    SendKey("Standby",7,1)
    SendKey("Ambilight",0.4,8)    
    SendKey("1",5,1)    

    print ("Block-1 - Guide_Nav")
    Guide_Nav()
    
    print ("Block-1 - Standby_Wakeup_BacktoBack")
    Standby_Wakeup_BacktoBack()
    
    print ("Block-1 - SwitchingChannels_Standby")
    SwitchingChannels_Standby_Revanth()

    print ("Block-1 - Tuner-512")
    Digit_Channel_Selection("Tuner",512)
    SendKey("Standby",24,1)
    SendKey("Netflix",15,1)   

    Standby_Wakeup_BorderCase()

    print ("Block-1 - Switching_Tuner_Channels")
    Switching_Tuner_Channels_Revanth()

    print ("Block-1 - Teletext_Nav_Tuner")
    Teletext_Nav_Tuner()
    
    print ("Block-1 - Standby_Wakeup_BacktoBack")
    Standby_Wakeup_BacktoBack()
    
    print ("Block-1 - Switching_Satellite_Channels")
    Switching_Satellite_Channels_Revanth()

    print ("Block-1 - Guide_Launch_Exit")
    Guide_Launch_Exit()

    print ("Block-1 - PVRRecording_Playback_Standby")
    PVRRecording_Playback_Standby_Revanth()
    
    SendKey("Standby",10,1)
    SendKey("Netflix",15,1)
    
    print ("Block-1 - Channel_SubtitleChange_Standby")
    Channel_SubtitleChange_Standby_Revanth()
    
    Standby_Wakeup_Keys_Semi_Full()
    
    print ("Block-1 - Test_Function_Satellite_Timeshift_Standby")
    Test_Function_Arun_Satellite_Timeshift_Standby_Mains_wakeup()

    Standby_Wakeup_BacktoBack()
    
    print("*******Block-1 - End*******")
    
def Block2():
    print("*******Block-2 - Start*******")
    PiP_Standby()
    
    print ("Block-2 - Sat-120")
    Digit_Channel_Selection("Satellite",81)
    
    print ("Block-2 - DemoMe_App")
    DemoMe_App()

    print ("Block-2 - Netflix_Standby-1,2")
    Netflix_Standby_Revanth(1,2)
    
    PiP_Without_Standby()

    print ("Block-2 - App_Gallery_Nav_Standby")
    App_Gallery_Nav_Standby_Revanth()

    print ("Block-2 - Youtube_Row1_Standby")
    Youtube_Row1_New()

    print ("Block-2 - CBPlayback_Standby_0,7,2")
    #CBPlayback_Standby_Revanth(0,7,2)
    CBPlayback()

    print ("Block-2 - OIB_Standby")
    OIB_Standby_Revanth()

    print ("Block-2 - Netflix_Standby-3,4")
    Netflix_Standby_Revanth(3,4)

    print ("Block-2 - Standby_Wakeup_BacktoBack")
    Standby_Wakeup_BacktoBack()

    print ("Block-2 - Amazon_Standby-1,2")
    Amazon_Standby_Revanth(1,2)

    print ("Block-2 - hbbtv")
    ###hbbtv

    print ("Block-2 - GoogleAssistant_With_Standby")
    GoogleAssistant_With_Standby_Revanth()

#    print ("Block-2 - SkyForce")
#    SkyForce_Revanth()
    
    PiP_Without_Standby()

    print ("Block-2 - Standby_Wakeup_BacktoBack")
    Standby_Wakeup_BacktoBack()

##    print ("Block-2 - hbbtv_text")
    ###hbbtv_text

##    print ("Block-2 - Arte_Revanth") 
##    Arte_Revanth()

    print ("Block-2 - DemoMe_App")
    DemoMe_App()

##    print ("Block-2 - Pacman_Revanth")
    #Pacman_Revanth()
    
    print ("Block-2 - CBPlayback_Standby-0,1,3")
    CBPlayback_Standby_Revanth(0,1,3)

    print ("Block-2 - Youtube_Row2_Standby")
    Youtube_Row2_New()

    print ("Block-2 - Standby_Wakeup_BacktoBack")
    Standby_Wakeup_BacktoBack()

    print ("Block-2 - CBPlayback_Images_Standby")
    #CBPlayback_Images_Standby_Revanth()
    CBPlayback_Favorites()

    PiP_Standby()
    
    print ("Block-2 -  Netflix_Standby-5,6")
    Netflix_Standby_Revanth(5,6)

    print ("Block-2 - CBPlayback_Standby-1,3,4")
    #CBPlayback_Standby_Revanth(1,3,4)
    CBPlayback_Favorites()

    print ("Block-2 - Amazon_Standby-3,4")
    Amazon_Standby_Revanth(3,4)

    print ("Block-2 - GoogleAssistant_With_Standby")
    GoogleAssistant_With_Standby_Revanth()

##    print ("Block-2 - Megogo_Revanth_Standby_Wakeup")
##    Megogo_Revanth_Standby_Wakeup()
    
    PiP_Standby()

    print ("Block-2 - How_To_App")
    How_To_App()

    print ("Block-2 - MXPlayer_Standby")
    MXPlayer_Standby_Revanth()
    
    CBPlayback()

    print("*******Block-2 - End*******")

def Block3():
    print("*******Block-3 - Start*******")

    print("Block-3 - HDMI_Standby_Revanth()")
    HDMI_Standby_Revanth()

##    print("Block-3 - HDMI")
##    HDMI()

    print("*******Block-3 - End*******")
    
def Start_Script():
    Block1()
    Block2()
    Block3()
        
if __name__ == "__main__":
    for count in range(0,100):    
        Start_Script()
