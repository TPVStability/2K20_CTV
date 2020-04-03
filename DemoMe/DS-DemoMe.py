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
RedRat_Device_Port = "2"

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
    SendKey('Home_longpress', 4, 1)
    SendKey('Up_longpress', 1, 1)
    SendKey('Left', 0.6, 1)
    
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

def Standby_Wakeup_BacktoBack_withStandbyKey():
    SendKey("Standby",5,1)
    SendKey("Standby",15,1) # After Waking up - Super Shop Demo is seen along with ESticker
    SendKey("Back",2,2) # Exit both E-Sticker and Super Shop Demo will come to Youtube Playback
    
    SendKey("Standby",15,1) # Standby on Youtube
    SendKey("Standby",17,1) # After Waking up - Super Shop Demo is seen along with ESticker

    SendKey("Standby",25,1) # Standby on SuperShopDemo+E-Sticker
    SendKey("Standby",18,1)
    SendKey("Back",2,2)  # Exit both E-Sticker and Super Shop Demo will come to Youtube Playback
    time.sleep(18) # After 18 Seconds, DemoMe will be launched

    SendKey("Standby",7,1) # Standby on DemoMe
    SendKey("Standby",16,1)
    SendKey("Back",2,1) # Only ESticker will be gone and SuperShopDemo will be still seen
    
    SendKey("Standby",8,1) # Standby on SuperShopDemo
    SendKey("Standby",5,1) # Here Youtube Content Playback will be happening in the backgroud
    
    SendKey("Standby",8,1)
    SendKey("Standby",19,1)

def Youtube_Row1_Standby_Revanth():
    time.sleep(15)
    Home_Positioning_Launch_App(1)
    SendKey("Left_longpress",0.7, 1)
    SendKey("Up_longpress", 0.5, 1)
    SendKey("Down", 0.3, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey('Up',0.3,1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video    
    SendKey("Ok", 25, 1) # Play the content for 20 Seconds
    SendKey("Back",4,2)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Pause",2,1)
    
    Standby_Wakeup_BacktoBack_withStandbyKey()

    time.sleep(15)
    SendKey("Back", 4, 2)
    SendKey("Right", 0.3, 1) # Takes you to the 2nd Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video    
    SendKey("Ok", 20, 1) # Play the content for 15 Seconds
    SendKey("Back",4,2)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Back",4,2)
    SendKey("Forward",3,1)
    Standby_Wakeup_BacktoBack_withStandbyKey()

def Youtube_Row2_Standby_Revanth():
    time.sleep(15)
    Home_Positioning_Launch_App(1)
    SendKey("Left_longpress",0.7, 1)
    SendKey("Up_longpress", 0.5, 1)
    SendKey("Down", 0.3, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey('Up',0.3,1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down", 0.3, 1)
    SendKey("Ok", 25, 1) # Play the content for 30 Seconds
    SendKey("Back",2,2)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Pause",2,1)
    Standby_Wakeup_BacktoBack_withStandbyKey()
    
    time.sleep(10)
    SendKey("Back", 2, 2)
    SendKey("Right", 0.3, 1)
    SendKey("Ok", 20, 1) # Play the content for 30 Seconds
    SendKey("Back",2,2)
    SendKey("Forward",3,1)
    Standby_Wakeup_BacktoBack_withStandbyKey()

def CBPlayback_Images_Standby_Revanth():
    time.sleep(15)
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

def CBPlayback_DemoMe_Revanth():
    time.sleep(15)
    SendKey("Home",2,3)
    
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down',0.3,7)
    SendKey('Up',0.7,2)
    SendKey('Ok',1,1)
    SendKey("Right",0.3,3)
    SendKey("Ok",0.3,3)
    SendKey("Play",18,1)
    SendKey("Back",6,1)

    SendKey('Sources',4,1) #launching sources on demome
    SendKey('Ok',0.7,1)
    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,1)
    SendKey('Up',0.7,2)
    SendKey("Right",0.2,4)
    SendKey("Down",1,1)
    SendKey("Ok",0.4,1)    
    SendKey('Play',16,1)
    
    SendKey('Sources',4,1) #launching sources on demome+Esticker
    SendKey('Ok',0.7,1)
    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,1)
    SendKey('Up',0.7,2)
    SendKey("Right",0.2,4)
    SendKey("Down",1,2)
    SendKey("Ok",0.4,1)    
    SendKey('Play',15,1)

    SendKey("Standby",10,1) #Standby on Demome+Esticker
    SendKey("Standby",21,1)

    SendKey("Standby",12,1) #Standby on supershopDemo+Esticker
    SendKey("Standby",21,1)
    
    SendKey('Sources',4,1) #launching sources on supershopdemo+Esticker
    SendKey('Ok',0.7,1)
    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,1)
    SendKey('Up',0.7,2)
    SendKey("Right",0.2,4)
    SendKey("Down",1,3)
    SendKey("Ok",0.4,1)    
    SendKey('Play',20,1)

    SendKey("Back",4,1) 
    SendKey("Standby",22,1) #Standby on Demome
    SendKey("Standby",35,1)
    SendKey("Back",7,1)

    SendKey("Standby",17,1) #Standby on supershopDemo
    SendKey("Standby",21,1)
    SendKey("Back",5,1)
    
    SendKey('Sources',4,1) #launching sources on supershopdemo
    SendKey('Ok',0.7,1)
    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,1)
    SendKey('Up',0.7,2)
    SendKey("Right",0.2,4)
    SendKey("Ok",0.4,1)    
    SendKey('Play',1,1)
    SendKey("Forward",16,1)

    SendKey("Standby",5,1) #Standby on Demome+Esticker
    SendKey("Standby",18,1)
    
    SendKey('Sources',4,1) #launching sources on supershopdemo+Esticker
    SendKey('Ok',0.7,1)
    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,1)
    SendKey('Up',0.7,2)
    SendKey("Right",0.2,4)
    SendKey("Down",1,1)
    SendKey("Ok",0.4,1)    
    SendKey('Play',8,1)
    SendKey("Rewind",16,1)

    SendKey("Back",3,1)
    SendKey("Standby",15,1) #Standby on Demome
    SendKey("Standby",16,1)
    
def Guide_Demome_Revanth():
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
    time.sleep(16)
    SendKey("Standby",15,1) #Standby on Demome+Esticker
    SendKey("Standby",12,1)

    SendKey("Standby",6,1) #Standby on Supershopdemo+Esticker
    SendKey("Standby",14,1)
    
    SendKey('Sources',4,1)  #launching guide on Supershopdemo+Esticker
    SendKey("Right",0.5,4)
    SendKey("Left_longpress",0.5,1)
    SendKey("Right",0.4,4)
    time.sleep(16)
    SendKey("Back",3,1)

    SendKey("Standby",15,1) #Standby on Demome
    SendKey("Standby",12,1)
    SendKey("Back",4,1)
    
    SendKey("Standby",15,1) #Standby on Demome
    SendKey("Standby",12,1)
    SendKey("Back",4,1)
    
    SendKey("Standby",20,1) #Standby on Supershopdemo
    SendKey("Standby",14,1)

    SendKey("Back",4,1)
    SendKey('Sources',4,1)  #launching guide on Supershopdemo
    SendKey("Right",0.5,4) 
    SendKey("Left_longpress",0.5,1)
    SendKey("Right",0.4,4)
    
    SendKey("Standby",20,1) #Standby on guide
    SendKey("Standby",16,1)

    #guide-Launch-Exit -Demome
    
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",4,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",10,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",5,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",8,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",12,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",4,1)

    SendKey("Standby",15,1) 
    SendKey("Standby",14,1)

    #guide-Launch-Exit -supershop
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",4,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",10,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",5,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",8,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",12,1)
    SendKey('Sources',4,1)  
    SendKey("Right",0.5,4)
    SendKey("Back",4,1)

def Netflix_Demome_Revanth():
    time.sleep(15)
    SendKey('Netflix',10,1)

    SendKey('Netflix',6,1)
    
    SendKey('Ok',1,3)
    SendKey('Back',1,4)
    SendKey('Left',1,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',1,2)
    SendKey('Ok',1,1)

    SendKey('Left',0.5,1)  
    SendKey('Up',0.5,1)
    SendKey('Right',1,1)
        
    SendKey('Ok',5,2)

    SendKey("Forward",15,1)

    SendKey("Standby",5,1) #Standby on Demome+Esticker
    SendKey("Netflix",14,1)
    
    SendKey("Netflix",7,1) #launching netflix on supershop+esticker
    SendKey("Ok",5,3)
    SendKey("Rewind",14,1)

    SendKey("Back",5,1)
    SendKey("Standby",16,1) #Standby on Demome
    SendKey("Netflix",14,1)

    SendKey("Back",4,1)
    SendKey("Netflix",7,1) #launching netflix on supershopdemo
    SendKey("Ok",5,1)
    SendKey("Rewind",14,1)
    
#netflix launch-exit-demome

    SendKey('Netflix',5,1)
    SendKey("Ok",1,2)
    SendKey("Forward",15,1)
    SendKey('Netflix',4,1)
    SendKey("Ok",1,2)
    SendKey("Rewind",12,1)
    SendKey('Netflix',6,1)
    SendKey("Ok",1,2)
    SendKey("Pause",10,1)
    SendKey('Netflix',7,1)
    SendKey("Ok",1,2)
    SendKey("Forward",18,1)
    SendKey('Netflix',7,1)
    SendKey("Ok",1,2)
    SendKey("Forward",20,1)

    SendKey("Back",4,1)
    SendKey('Netflix',15,1)
    SendKey("Back",3,1)
    SendKey('Netflix',12,1)
    SendKey("Back",7,1)
    SendKey('Netflix',15,1)
#netflix launch-exit-supershopdemo
    SendKey("Standby",5,1) 
    SendKey("Netflix",14,1)
    SendKey("Standby",9,1) 
    SendKey("Netflix",14,1)
    SendKey("Standby",18,1) 
    SendKey("Netflix",14,1)
    SendKey("Standby",20,1) 
    SendKey("Netflix",14,1)
    SendKey("Standby",13,1) 
    SendKey("Netflix",14,1)    
    SendKey("Standby",25,1) 
    SendKey("Netflix",14,1)

    
    SendKey("Standby",5,1) 
    SendKey("Netflix",14,1)
    SendKey("Back",4,1)
    SendKey("Standby",9,1) 
    SendKey("Netflix",14,1)
    SendKey("Back",4,1)
    SendKey("Standby",18,1) 
    SendKey("Netflix",14,1)
    SendKey("Back",4,1)
    SendKey("Standby",20,1) 
    SendKey("Netflix",14,1)
    SendKey("Back",4,1)
    SendKey("Standby",13,1) 
    SendKey("Netflix",14,1)
    SendKey("Back",4,1)    
    SendKey("Standby",25,1) 
    SendKey("Netflix",14,1)

def SwitchingChannels_Demome_Revanth():
    time.sleep(15)
    
    Digit_Channel_Selection("Tuner",5)
    time.sleep(5)
    SendKey("Up_longpress",4,1)
    SendKey("Up",0.3,6)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,1)
    SendKey("Down_longpress",3,1)
    SendKey("Down",0.3,6)
    SendKey("Volume_Down",0.1,7)
    time.sleep(15)
    
    Digit_Channel_Selection("Satellite",83)
    time.sleep(5)
    SendKey("Channel_Down_longpress",0.2,1)
    SendKey("Channel_Up",0.3,6)
    time.sleep(5)
    SendKey("Volume_Down",0.1,7)
    SendKey("Channel_Up_longpress",0.2,1)
    SendKey("Channel_Down",0.3,5)
    SendKey("Mute",0.3,4)
    SendKey("Volume_Up",0.1,7)
    time.sleep(20)
    
    Digit_Channel_Selection("Tuner",14)
    time.sleep(5)
    SendKey("Up_longpress",5,1)
    SendKey("Channel_Down",0.3,3)
    SendKey("Volume_Down",0.1,4)
    SendKey("Channel_Down_longpress",0.2,1)
    SendKey("Channel_Up",1,3)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,2)

    time.sleep(18)
    SendKey("Back",4,1)
    
    Digit_Channel_Selection("Satellite",147)
    time.sleep(5)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,1)
    SendKey("Channel_Up_longpress",0.2,1)
    SendKey("Channel_Down",0.3,4)
    time.sleep(5)
    SendKey("Volume_Down",0.1,5)
    SendKey("Channel_Up",0.3,2)
    time.sleep(4)
    SendKey("Down_longpress",5,1)

    SendKey("Standby",5,1)
    SendKey("Exit",17,1)

    Digit_Channel_Selection("Tuner",20)
    time.sleep(5)
    SendKey("Volume_Down",0.1,7)
    SendKey("Channel_Up_longpress",3,1)
    SendKey("Mute",0.3,3)
    SendKey("Up_longpress",0.2,1)
    SendKey("Volume_Up",0.1,7)
    SendKey("Channel_Down",0.2,6)
    SendKey("Volume_Down",0.1,4)
    time.sleep(10)
    
    Digit_Channel_Selection("Satellite",92)
    time.sleep(5)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down_longpress",0.2,1)
    time.sleep(5) 
    SendKey("Volume_Up",0.1,8)
    SendKey("Mute",0.3,5)
    SendKey("Volume_Down",0.1,7)
    time.sleep(15)
    SendKey("Back",4,1)
       
    Digit_Channel_Selection("Tuner",10)
    time.sleep(5)
    SendKey("Volume_Up",0.1,3)
    SendKey("Volume_Down",0.1,4)
    SendKey("Up_longpress",3,1)
    SendKey("Channel_Down",0.2,4)
    SendKey("Down_longpress",0.2,1)
    SendKey("Mute",0.3,3)
    SendKey("Channel_Up_longpress",0.5,1)
    SendKey("Standby",5,1)
    SendKey("Exit",20,1)

    SendKey("Back",4,1)
    
    Digit_Channel_Selection("Satellite",121)
    time.sleep(5)
    SendKey("Down_longpress",0.2,1)
    SendKey("Channel_Up_longpress",0.5,1)
    SendKey("Volume_Down",0.1,7)
    SendKey("Volume_Up",0.1,5)
    SendKey("Channel_Down",0.2,4)
    SendKey("Mute",0.3,1)

    time.sleep(12)
    
    Digit_Channel_Selection("Tuner",506)
    time.sleep(5)
    SendKey("Channel_Up_longpress",6,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Volume_Up",0.1,6)
    SendKey("Channel_Down_longpress",8,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Mute",0.3,1)
    SendKey("Channel_Up",1,5)
    SendKey("Volume_Down",0.1,3)

    time.sleep(18)
    
    Digit_Channel_Selection("Satellite",86)
    time.sleep(5)
    SendKey("Up_longpress",0.2,1)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,5)
    SendKey("Channel_Down_longpress",5,1)
    SendKey("Volume_Up",0.1,7)
    SendKey("Down_longpress",0.2,1)
    SendKey("Channel_Up_longpress",3,1)

    time.sleep(16)

def Switching_Satellite_Channels_Demome_Revanth():
    time.sleep(15)
    
    Digit_Channel_Selection("Satellite",81) #81 - Test UHD1
    time.sleep(1)
    
    SendKey("2",0.2,1)
    SendKey("3",0.2,1)
    SendKey("9",0.2,1)
    time.sleep(4)
    SendKey("Ok",3,1)
    SendKey("Volume_Up",0.1,10)
    SendKey("Volume_Down",0.1,3)
    SendKey("Mute",0.3,11)
    
    SendKey("Standby",5,1)
    SendKey("Exit",20,1)

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
    time.sleep(16)
    SendKey("Back",1,2)
    SendKey("Volume_Up",0.1,4)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,6)
    SendKey("Ok",1,1)
    
    SendKey("9",0.2,1)
    SendKey("2",0.2,1)
    time.sleep(20)
    SendKey("Back",1,2)
    SendKey("Volume_Down",0.1,10)
    
    SendKey("Standby",40,1)
    SendKey("Exit",22,1)

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

    SendKey("Standby",4,1)
    SendKey("Exit",22,1)
    SendKey("Exit",5,1)
    SendKey("2",0.1,1)
    SendKey("0",0.1,1)
    SendKey("8",4,1)
    
    SendKey("Mute",0.3,4)
    time.sleep(4)
    SendKey("Ok",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok",3,1)

    SendKey("Standby",5,1)
    SendKey("Exit",20,1)
    
def Switching_Tuner_Channels_Demome_Revanth():
    time.sleep(15)
    Digit_Channel_Selection("Tuner",5)
    time.sleep(1)
    SendKey("Volume_Down",0.1,3)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.3,8)
    SendKey("1",0.2,1)
    SendKey("4",0.2,1)
    time.sleep(5)
    
    SendKey("Standby",5,1)
    SendKey("Exit",20,1)

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

    time.sleep(14)

    SendKey("Standby",9,1)
    SendKey("Exit",20,1)
    SendKey("Exit",5,1)
    
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
    time.sleep(18)
    SendKey("Back",2,2)
##    time.sleep(3)
    SendKey("Volume_Down",0.1,3)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.2,9)
    SendKey("2",0.2,1)
    SendKey("8",0.2,1)
    time.sleep(18)

    SendKey("Standby",4,1)
    SendKey("Exit",22,1)
    SendKey("Exit",5,1)
    
    SendKey("Mute",0.2,4)
    SendKey("Volume_Up",0.1,4)
    SendKey("Volume_Down",0.1,3)
    time.sleep(3.5)
    SendKey("Ok",0.4,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Ok",3,1)

    SendKey("Standby",35,1)
    SendKey("Exit",5,1)

def DemoMe_App_Demome_Revanth():
    time.sleep(15)
    Home_Positioning_Launch_App(5)
    SendKey("Left",0.2,3)
    SendKey("Up",0.2,3)
    SendKey("Down",0.2,1)
    SendKey("Right",0.6,2)
    SendKey("Ok",15,1)

    SendKey("Back",1,2)
    time.sleep(12)


    Home_Positioning_Launch_App(5)
    SendKey("Left",0.2,3)
    SendKey("Up",0.2,3)
    SendKey("Down",0.2,1)
    SendKey("Right",0.6,2)
    SendKey("Down",0.2,1)
    SendKey("Ok",15,1)

    SendKey("Down",0.3,1)
    SendKey("Ok",15,1)

    SendKey("Back",1,2)
    time.sleep(12)


    Home_Positioning_Launch_App(5)
    SendKey("Left",0.2,3)
    SendKey("Up",0.2,3)
    SendKey("Down",0.2,1)
    SendKey("Right",0.6,2)
    SendKey("Down",0.2,1)
    SendKey("Ok",15,1)

    SendKey("Down",0.6,1)
    SendKey("Ok",15,1)

    SendKey("Back",1,2)
    time.sleep(12)


    SendKey("Back",1,2)

    SendKey("Standby",15,1)
    SendKey("Exit",20,1)

    Home_Positioning_Launch_App(5)
    SendKey("Left",0.2,3)
    SendKey("Up",0.2,3)
    SendKey("Down",0.2,1)
    SendKey("Right",0.5,2)
    SendKey("Ok",9,1)

    SendKey("Standby",15,1)
    SendKey("Home",15,1)

    Home_Positioning_Launch_App(5)
    SendKey("Left",0.2,3)
    SendKey("Up",0.2,3)
    SendKey("Down",0.2,1)
    SendKey("Right",0.4,2)
    SendKey("Down",0.5,1)
    SendKey("Ok",15,1)

    SendKey("Standby",25,1)
    SendKey("Standby",15,1)

    Home_Positioning_Launch_App(5)
    SendKey("Left",0.2,3)
    SendKey("Up",0.2,3)
    SendKey("Down",0.3,1)
    SendKey("Right",0.4,2)
    SendKey("Down",0.5,2)
    SendKey("Ok",15,1)

    SendKey("Standby",18,1)
    SendKey("Standby",18,1)
    
def Launcher_Demome_Revanth():
    time.sleep(15)
    SendKey("Home",2,3)
    time.sleep(20)
    SendKey("Standby",5,1)
    SendKey("Standby",120,1)

    SendKey("Home",18,1)

    SendKey("Standby",5,1)
    SendKey("Standby",30,1)

    SendKey("Home",20,1)
    SendKey("Back",4,1)
    SendKey("Home",4,1)
    Random_longpress(10)
    
    SendKey("Standby",5,1)
    SendKey("Standby",30,1)

    SendKey("Home",45,1)

    SendKey("Home",6,1)
    Random_Navigation(10)

    SendKey("Standby",5,1)
    SendKey("Home",15,1)
    SendKey("Back",4,1)
    SendKey("Home",1,1)
    Random_longpress(3)
    Random_Navigation(8)

    SendKey("Standby",5,1)
    SendKey("Standby",180,1)
    SendKey("Home",120,1)
    
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
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    time.sleep(6)
    SendKey('Back',0.8,1)
    SendKey("Down",0.3,1)
    SendKey('Ok',0.8,1)
    SendKey('Ok',10,1)
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

    SendKey("Standby",18,1)
    SendKey("Standby",6,1)

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
    SendKey('Ok',10,1)
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
    

    SendKey("Standby",22,1)
    SendKey("Standby",6,1)
    
#360Images
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    
    SendKey("Left",0.3,6)
    SendKey('Down_Longpress',1,2)
    SendKey('Up',0.7,2)
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
    time.sleep(16)
    
    
#audios
    SendKey("Standby",6,1)
    SendKey("Channel_Up",6,1)
        
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',5,1)
    
    SendKey("Left",0.3,6)
    SendKey('Down_Longpress',1,2)
    SendKey('Up',0.7,2)
    SendKey("Right",0.4,3) 
    
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
    time.sleep(16)

    
######Legacy
def App_Gallery_Nav_Revanth():
    time.sleep(15)
    SendKey("Smart_Home",10,1)
    #Featured apps category
    SendKey("Up_longpress",0.3,1)
    SendKey("Down_longpress",0.3,1)
    SendKey("Left_longpress",0.3,1)
    SendKey("Up_longpress",0.3,1)
    SendKey("Left_longpress",0.3,1)
    SendKey("Down_longpress",0.3,1)
    SendKey("Right",0.3,1)
    SendKey("Up",0.2,4)
    SendKey("Right",0.2,1)
    SendKey("Down",0.2,4)
    SendKey("Right",0.2,1)
    SendKey("Up",0.2,4)
    SendKey("Right",0.2,1)
    SendKey("Down",0.2,4)
    SendKey("Right",0.2,4)
    SendKey("Up",0.2,1)
    SendKey("Left",0.2,4)
    

    SendKey("Up_longpress",0.2,3)
    SendKey("Down",0.2,1)
    for count in range(0,5):
        SendKey("Right",0.3,1)
        SendKey("Ok",0.2,1)
    SendKey("Up",0.2,1)
    SendKey("Down",0.2,1)
    SendKey("Right",0.3,1)
    SendKey("Ok",0.3,1)
    
 #All category
    print ("AppGalleryNav-All category")

    for count in range(0,15):
        SendKey("Down",0.2,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Right",0.3,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)

    for count in range(0,10):
        SendKey("Up",0.2,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Left",0.3,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Right",0.4,2)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)

#country change
    SendKey("Green",0.8,1)
    for count in range(0,3):
        SendKey("Down_longpress",0.7,1)
        SendKey("Ok",3,1)
        SendKey("Up",0.3,3)
        SendKey("Ok",3,1)
        
    
# New Category
    print ("AppGalleryNav-New category")

    SendKey("Up_longpress",0.2,4)
    SendKey("Down",0.3,1)
    SendKey("Right",0.3,2)
    SendKey("Ok",0.3,1)

    for count in range(0,15):
        SendKey("Down",0.2,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Right",0.3,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)

    for count in range(0,10):
        SendKey("Up",0.2,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Left",0.3,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Right",0.4,2)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)

#country change
    SendKey("Green",0.8,1)
    for count in range(0,3):
        SendKey("Up_longpress",0.7,1)
        SendKey("Ok",3,1)
        SendKey("Down",0.3,3)
        SendKey("Ok",3,1)

#Video category

    print ("AppGalleryNav-Video category")
        
    SendKey("Up_longpress",0.2,4)
    SendKey("Down",0.3,1)
    SendKey("Right",0.3,3)
    SendKey("Ok",0.3,1)

    for count in range(0,5):
        SendKey("Down",0.2,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Right",0.3,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)

    for count in range(0,5):
        SendKey("Up",0.2,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Left",0.3,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Right",0.4,2)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)

#country change
    SendKey("Green",0.8,1)
    for count in range(0,3):
        SendKey("Up_longpress",0.7,1)
        SendKey("Ok",3,1)
        SendKey("Down",0.3,3)
        SendKey("Ok",3,1)
        
#Entertainment category
    print ("AppGalleryNav-Entertainment category")
        
    SendKey("Up_longpress",0.2,4)
    SendKey("Down",0.3,1)
    SendKey("Right",0.3,4)
    SendKey("Ok",0.3,1)

    for count in range(0,2):
        SendKey("Down",0.2,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Right",0.3,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)

    for count in range(0,2):
        SendKey("Up",0.2,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Left",0.3,1)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)
        SendKey("Right",0.4,2)
        SendKey("Ok",0.8,1)
        SendKey("Back",0.4,1)

#country change
    SendKey("Green",0.8,1)
    for count in range(0,3):
        SendKey("Down_longpress",0.7,1)
        SendKey("Ok",3,1)
        SendKey("Up",0.3,3)
        SendKey("Ok",3,1)

    SendKey("Exit",2,1)
  
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

def OIB():
    
    Home_Positioning_Launch_App(3)
    
    Right_Count = 0
    for count in range(0,4):
        for count1 in range(0,Right_Count):            
            SendKey("Right")
            time.sleep(1)
            
        SendKey("Ok")
        time.sleep(5)
        
        Right_Count = Right_Count+1
        SendKey("Down_longpress",0.2,2)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)

        SendKey("Home")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(1)
            
        SendKey("Back",1,2)
        SendKey("Ok")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(3)
        
    Home_Positioning_Launch_App(3)
    
    Right_Count = 0
    for count in range(0,4):
        SendKey("Down",0.5,1)
        for count1 in range(0,Right_Count):
            
            SendKey("Right")
            time.sleep(1)
            
        SendKey("Ok")
        time.sleep(15)
        
        Right_Count = Right_Count+1
        SendKey("Down_longpress",0.2,2)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)

        SendKey("Home")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(1)
            
    
        SendKey("Back",2,2)
        SendKey("Ok")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(3)



        
def How_To_App():
    ## DS-SmartTVApps - Invoke How To Application - Navigations inside it
##    print "DS-SmartTVApps - Invoke How To Application - Navigations inside it"

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
    SendKey("Exit")
    time.sleep(3)

def Test_Combinations_Legacy():
    
    Digit_Channel_Selection("Satellite",83)
    time.sleep(22) # DemoMe Playback Starts
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(20) # Super Shop Demo Me Playback Starts
    SendKey("Exit")# Satellite Channel is tuned
    time.sleep(20) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(22)# Super Shop Demo Me Playback Starts
    SendKey("Exit")# Satellite Channel is tuned
    time.sleep(2)

    Volume_Controls()
    
    Youtube_Row1_Standby_Revanth()
    Random_TrickModes(6)
    time.sleep(17) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(21)
    SendKey("Standby")
    time.sleep(16)# Super Shop Demo Me Playback Starts
    SendKey("Back") # Youtube will be launched
    time.sleep(21) # Demo Me Playback Starts
        
    OIB()
    time.sleep(17) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(19)
    SendKey("Standby")
    time.sleep(16) # Super Shop Demo Me Playback Starts
    SendKey("Back") # Internet Browser is launched
    time.sleep(4)
    Volume_Controls()

    SendKey("Home")
    time.sleep(5)
    Random_Navigation(20)
    Random_longpress(8)
    time.sleep(19) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Back")
    time.sleep(2)
    Random_Navigation(20)
    time.sleep(2)

    # HDMI 1 Selection
    SendKey("Sources")
    time.sleep(5)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,8):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(18) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(19) # Super Shop Demo Me Playback Starts
    SendKey("Back") # HDMI 1 is selected
    time.sleep(15) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Back") # HDMI 1 is selected
    time.sleep(13) # Super Shop Demo Me Playback Starts
    SendKey("Exit")# Satellite Channel is tuned
    time.sleep(17) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(19) # Super Shop Demo Me Playback Starts

    # Demo Me App
    DemoMe_App_Demome_Revanth()
    Volume_Controls()
    
    Youtube_Row2_Standby_Revanth()
    
    # HDMI 2 Selection
    SendKey("Sources")
    time.sleep(5)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,9):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(18) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(19) # Super Shop Demo Me Playback Starts
    SendKey("Back") # HDMI 2 is selected
    time.sleep(15) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Back") # HDMI 2 is selected
    time.sleep(13) # Super Shop Demo Me Playback Starts
    SendKey("Exit")# Satellite Channel is tuned
    time.sleep(17) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(19) # Super Shop Demo Me Playback Starts
    
    # HDMI 3 Selection
    SendKey("Sources")
    time.sleep(5)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,9):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(18) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(19) # Super Shop Demo Me Playback Starts
    SendKey("Back") # HDMI 3 is selected
    time.sleep(15) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Back") # HDMI 3 is selected
    time.sleep(13) # Super Shop Demo Me Playback Starts
    SendKey("Exit")# Satellite Channel is tuned
    time.sleep(17) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(19) # Super Shop Demo Me Playback Starts
    Volume_Controls()
    #USB_Playback() # Content Browser Playback
    time.sleep(18) #Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(14)# Super Shop Demo Me Playback Starts

    # HDMI 4 Selection
    SendKey("Sources")
    time.sleep(5)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,9):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(18) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(19) # Super Shop Demo Me Playback Starts
    SendKey("Back") # HDMI 4 is selected
    time.sleep(15) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Back") # HDMI 4 is selected
    time.sleep(13) # Super Shop Demo Me Playback Starts
    SendKey("Exit")# Satellite Channel is tuned
    time.sleep(17) # Demo Me Playback Starts
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(19) # Super Shop Demo Me Playback Starts
    Volume_Controls()

    App_Gallery_Nav_Revanth()
    How_To_App()

#### Legacy - End

def All_App_Launching_Demome_Revanth():
    
    Home_Positioning_Launch_App(1)
    time.sleep(4)
    SendKey("Right",0.3,1)
    SendKey("Down",0.3,1)
    SendKey("Ok",15,1)

    SendKey("Standby",5,1)
    SendKey("Standby",15,1)
    
    Home_Positioning_Launch_App(2)
    time.sleep(15)

    SendKey("Standby",15,1)
    SendKey("Standby",15,1)

    Home_Positioning_Launch_App(3)
    time.sleep(4)
    SendKey("Ok",3,1)
    Random_longpress(5)
    Random_Navigation(8)
    time.sleep(15)

    SendKey("Standby",8,1)
    SendKey("Exit",18,1)
    
    Home_Positioning_Launch_App(4)
    time.sleep(4)
    Random_longpress(5)
    Random_Navigation(10)
    time.sleep(15)

    SendKey("Standby",22,1)
    SendKey("Standby",15,1)
    
    Home_Positioning_Launch_App(5)
    time.sleep(2)
    SendKey("Down",0.2,1)
    SendKey("Right",0.2,2)
    SendKey("Ok",15,1)

    SendKey("Standby",15,1)
    SendKey("Home",15,1)

    Home_Positioning_Launch_App(6)
    time.sleep(30)

    SendKey("Standby",20,1)
    SendKey("Standby",15,1)
    
    Home_Positioning_Launch_App(7)
    time.sleep(5)
    SendKey("Ok",3,2)
    time.sleep(14)

    SendKey("Standby",7,1)
    SendKey("Standby",15,1)

    Home_Positioning_Launch_App(8)
    time.sleep(4)
    SendKey("Ok",15,1)

    SendKey("Standby",4,1)
    SendKey("Exit",20,1)

    Home_Positioning_Launch_App(9)
    time.sleep(5)
    SendKey("Ok",0.5,1)
    SendKey("Ok",15,1)

    SendKey("Standby",9,1)
    SendKey("Standby",13,1)

    Home_Positioning_Launch_App(10)
    time.sleep(5)
    SendKey("Down",0.5,1)
    SendKey("Ok",20,1)

    SendKey("Standby",12,1)
    SendKey("Home",15,1)

    Home_Positioning_Launch_App(11)
    time.sleep(17)

    SendKey("Standby",18,1)
    SendKey("Standby",15,1)

    Home_Positioning_Launch_App(12)
    time.sleep(3)
    SendKey("Ok",3,2)
    SendKey("Ok",12,1)

    SendKey("Standby",21,1)
    SendKey("Netflix",15,1)

    Home_Positioning_Launch_App(13)
    time.sleep(5)
    SendKey("Ok",17,1)

    SendKey("Standby",9,1)
    SendKey("Standby",15,1)

    Home_Positioning_Launch_App(14)
    time.sleep(6)
    SendKey("Right",0.2,7)
    SendKey("Ok",4,1)
    SendKey("Ok",15,1)

    SendKey("Standby",5,1)
    SendKey("Netflix",15,1)

    Home_Positioning_Launch_App(15)
    time.sleep(4)
    SendKey("Ok",2,2)
    time.sleep(18)
    
    SendKey("Standby",16,1)
    SendKey("Exit",12,1)
    
    Home_Positioning_Launch_App(16)
    time.sleep(6)
    SendKey("Down",0.5,1)
    SendKey("Right",0.5,1)
    SendKey("Ok",0.7,2)
    time.sleep(14)

    SendKey("Standby",13,1)
    SendKey("Home",17,1)

    Home_Positioning_Launch_App(17)
    time.sleep(5)
    SendKey("Right",0.5,1)
    SendKey("Ok",0.7,1)
    SendKey("Ok",13,1)
    SendKey("Pause",0.5,1)

    SendKey("Standby",6,1)
    SendKey("Standby",15,1)

    Home_Positioning_Launch_App(18)
    time.sleep(6)
    SendKey("Ok",12,1)

    SendKey("Standby",15,1)
    SendKey("Exit",15,1)

    Home_Positioning_Launch_App(19)
    time.sleep(5)
    SendKey("Down",0.7,2)
    SendKey("Ok",0.8,2)
    time.sleep(10)

    SendKey("Standby",11,1)
    SendKey("Home",11,1)

    Home_Positioning_Launch_App(20)
    time.sleep(15)

    SendKey("Standby",5,1)
    SendKey("Netflix",15,1)

    SendKey("Netflix",8,1)
    SendKey("Down",0.5,1)
    SendKey("Ok",3,2)
    time.sleep(15)

def OIB_Demome_Revanth():
    time.sleep(10)
    Home_Positioning_Launch_App(3)
    time.sleep(3)
    SendKey("Ok",4,1)
    Random_longpress(3)
    Random_Navigation(8)
    time.sleep(12)

    SendKey("Standby",5,1)
    SendKey("Standby",17,1)

    Home_Positioning_Launch_App(3)
    time.sleep(3)
    SendKey("Back",0.7,2)
    SendKey("Right",0.5,1)
    SendKey("Ok",4,1)
    Random_longpress(3)
    Random_Navigation(8)
    time.sleep(15)

    SendKey("Standby",21,1)
    SendKey("Standby",16,1)

    Home_Positioning_Launch_App(3)
    time.sleep(3)
    SendKey("Back",0.7,2)
    SendKey("Right",0.5,1)
    SendKey("Ok",4,1)
    Random_longpress(3)
    Random_Navigation(8)
    time.sleep(25)

    SendKey("Standby",11,1)
    SendKey("Standby",12,1)

    Home_Positioning_Launch_App(3)
    time.sleep(3)
    SendKey("Back",0.7,2)
    SendKey("Right",0.5,1)
    SendKey("Ok",4,1)
    Random_longpress(3)
    Random_Navigation(8)
    time.sleep(15)

    SendKey("Standby",16,1)
    SendKey("Standby",9,1)

    Home_Positioning_Launch_App(3)
    time.sleep(3)
    SendKey("Back",0.7,2)
    SendKey("Down",0.5,1)
    SendKey("Ok",4,1)
    Random_longpress(3)
    Random_Navigation(8)
    time.sleep(15)

    SendKey("Standby",10,1)
    SendKey("Standby",20,1)

    Home_Positioning_Launch_App(3)
    time.sleep(3)
    SendKey("Back",0.7,2)
    SendKey("Down",0.5,1)
    SendKey("Left",0.5,1)
    SendKey("Ok",4,1)
    Random_longpress(3)
    Random_Navigation(8)
    time.sleep(10)

    SendKey("Standby",4,1)
    SendKey("Standby",10,1)

    Home_Positioning_Launch_App(3)
    time.sleep(3)
    SendKey("Back",0.7,2)
    SendKey("Down",0.5,1)
    SendKey("Left",0.5,1)
    SendKey("Ok",4,1)
    Random_longpress(3)
    Random_Navigation(8)
    time.sleep(9)

    SendKey("Standby",24,1)
    SendKey("Standby",15,1)

    Home_Positioning_Launch_App(3)
    time.sleep(3)
    SendKey("Back",0.7,2)
    SendKey("Down",0.5,1)
    SendKey("Left",0.5,1)
    SendKey("Ok",4,1)
    Random_longpress(3)
    Random_Navigation(8)
    time.sleep(11)

    SendKey("Standby",6,1)
    SendKey("Standby",11,1)

def App_Gallery_Demome_Revanth():
    
    SendKey("Smart_Home",10,1)
    SendKey("Smart_Home",7,1)
    Random_longpress(4)
    Random_Navigation(10)
    time.sleep(12)

    SendKey("Standby",10,1)
    SendKey("Standby",14,1)

    SendKey("Smart_Home",10,1)
    SendKey("Up_longpress",0.5,2)
    SendKey("Down",1,1)
    SendKey("Right",1,1)
    SendKey("Ok",1,1)
    Random_longpress(6)
    Random_Navigation(12)
    time.sleep(20)

    SendKey("Standby",17,1)
    SendKey("Standby",25,1)

    SendKey("Smart_Home",10,1)
    SendKey("Up_longpress",0.5,2)
    SendKey("Down",1,1)
    SendKey("Right",1,2)
    SendKey("Ok",1,1)
    Random_longpress(6)
    Random_Navigation(12)
    time.sleep(20)

    SendKey("Standby",4,1)
    SendKey("Standby",13,1)

    SendKey("Smart_Home",10,1)
    SendKey("Up_longpress",0.5,2)
    SendKey("Down",1,1)
    SendKey("Right",1,3)
    SendKey("Ok",1,1)
    Random_longpress(6)
    Random_Navigation(12)
    time.sleep(20)

    SendKey("Standby",21,1)
    SendKey("Standby",12,1)

    SendKey("Smart_Home",10,1)
    SendKey("Up_longpress",0.5,2)
    SendKey("Down",1,1)
    SendKey("Right",1,4)
    SendKey("Ok",1,1)
    Random_longpress(6)
    Random_Navigation(12)
    time.sleep(20)

    SendKey("Standby",8,1)
    SendKey("Standby",16,1)    

def Pacman_Demome_Revanth():
    time.sleep(12)
    SendKey("Home",2,3)
    SendKey("Right",0.3,1)
    SendKey("Ok",12,1)
    SendKey("Home",3,1)
    SendKey("Ok",10,1)
    SendKey("Home",3,1)
    SendKey("Ok",5,1)
    SendKey("Ok",0.7,10)
    for count in range(0,4):
        SendKey("Up",0.5,1)
        SendKey("Right",0.4,1)
        SendKey("Up",0.4,1)
        SendKey("Left",0.4,1)
    SendKey("Ok",0.6,5)

    time.sleep(15)

    SendKey("Home",3,1)
    SendKey("Ok",5,1)

    SendKey("Standby",18,1)
    SendKey("Standby",20,1)

    SendKey("Home",3,1)
    SendKey("Ok",5,1)
    time.sleep(12)

def Skyforce_Demome_Revanth():
    time.sleep(12)
    SendKey("Home",2,3)
    SendKey("Ok",12,1)
    SendKey("Home",3,1)
    SendKey("Ok",12,1)
    SendKey("Home",3,1)
    SendKey("Ok",5,1)
    SendKey("Ok",4,2)
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

    SendKey("Standby",11,1)
    SendKey("Standby",15,1)

    SendKey("Home",2,3)
    SendKey("Ok",15,1)
    
def Badland_Demome_Revanth():
    SendKey("Home",2,3)
    SendKey("Right",0.4,2)
    SendKey("Ok",15,1)
    SendKey("Home",2,1)
    SendKey("Ok",15,1)
    SendKey("Home",2,1)
    SendKey("Ok",5,1)
    SendKey("Ok",0.5,5)
##    time.sleep(30)
    for count in range(0,9):  
        SendKey("Ok",0.3,6)
        time.sleep(1)

    SendKey("Standby",18,1)
    SendKey("Standby",15,1)

    SendKey("Home",4,1)
    SendKey("Ok",15,1)

def MXPlayer_Demome_Revanth():
    time.sleep(10)
    SendKey("Home",2,3)
    SendKey("Right",0.3,3)
    SendKey("Ok",15,1)

    SendKey("Home",4,1)
    SendKey("Ok",4,1)
    
    SendKey("Down",0.5,1)
    SendKey("Ok",0.5,2)
    SendKey("Ok",15,1)

    SendKey("Home",4,1)
    SendKey("Ok",1,2)
    
    SendKey("Standby",8,1)
    SendKey("Standby",15,1)

    SendKey("Home",4,1)
    SendKey("Ok",1,1)
    SendKey("Right",0.3,1)
    SendKey("Ok",1,2)
    time.sleep(11)

def HDMI_Demome_Revanth():
    time.sleep(12)
    SendKey("Sources",4,1)
    SendKey("Up_longpress",0.6,1)
    SendKey("Down",0.7,8)
    SendKey("Ok",1,2)
    time.sleep(15)
    SendKey("Standby",80,1)
    SendKey("Standby",20,1)

    SendKey("Sources",4,1)
    SendKey("Up_longpress",0.6,1)
    SendKey("Down",0.7,8)
    SendKey("Ok",1,2)
    
    HDMI_QuickSettings_Revanth()
    SendKey("Standby",5,1)
    SendKey("Standby",25,1)
    
    #hdmi switching
    SendKey("Sources",4,1)
    SendKey("Up_longpress",0.6,1)
    SendKey("Down",0.7,8)
    SendKey("Ok",1,2)
    
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

    SendKey("Standby",16,1)
    SendKey("Standby",12,1)
        
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

def TimeShift():
    Digit_Channel_Selection("Satellite",86)
    time.sleep(20)
    SendKey("Exit",4,1)
    SendKey("Pause",20,1)
    SendKey("Exit",4,1)
    SendKey("Pause",5,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby",15,1)
    SendKey("Standby",20,1)
    
    SendKey("Exit",4,1)
    SendKey("Pause",5,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby",25,1)
    SendKey("Standby",20,1)
    
    SendKey("Exit",4,1)
    SendKey("Pause",5,1)
    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Standby",5,1)
    SendKey("Standby",20,1)
    
    SendKey("Exit",4,1)
    SendKey("Pause",25,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby",12,1)
    SendKey("Standby",20,1)
    
def TimeShift1():
    
    Standby1 = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    Standby2 = [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    Standby3 = [4,5,7,9,12,14,18,25,27,30,38,33,35]
    
    Digit_Channel_Selection("Satellite",86)
    time.sleep(20)
    SendKey("Exit",4,1)
    SendKey("Pause",20,1)
    SendKey("Standby",12,1)
    SendKey("Standby",20,1)
    
    for x in range(0,7):    
        SendKey("Exit",4,1)
        SendKey("Pause",20,1)
        SendKey("Standby",1)
        time.sleep(random.choice(Standby1))
        SendKey("Standby",20,1)
    
    for x in range(0,7):    
        SendKey("Exit",4,1)
        SendKey("Pause",20,1)
        SendKey("Standby",1)
        time.sleep(random.choice(Standby2))
        SendKey("Standby",20,1)
        
    for x in range(0,7):    
        SendKey("Exit",4,1)
        SendKey("Pause",20,1)
        SendKey("Standby",1)
        time.sleep(random.choice(Standby3))
        SendKey("Standby",20,1)
 
def OTR_Demome():
    Digit_Channel_Selection("Satellite",83)
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

def TimeShift2():
    SendKey("Exit",4,1)
    SendKey("Pause",4,1)
    SendKey("Standby",15,1)
    SendKey("Exit",5,1)
    SendKey("Pause",5,1)
    SendKey("Standby",25,1)
    
    SendKey("Exit",4,1)
    SendKey("Pause",4,1)
    SendKey("Standby",5,1)
    SendKey("Exit",4,1)
    SendKey("Pause",4,1)
    SendKey("Standby",8,1)
    SendKey("Exit",18,1)
    SendKey("Pause",4,1)
    SendKey("Standby",5,1)
    SendKey("Exit",30,1)
    SendKey("Pause",4,1)
    SendKey("Standby",5,1)
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


def QuickMenu():
    SendKey("TVMenu",3,1)
    SendKey("Up_longpress",0.3,2)
    SendKey("Ok",0.4,1)
    SendKey("Down",0.3,1)
    SendKey("Right",0.3,1)
    for x in range(0,7):
        SendKey("Ok",0.3,1)
        SendKey("Back",0.3,1)
        SendKey("Down",0.3,1)
       
    SendKey("Left",0.3,1)
    SendKey("Down",0.3,1)

    for x in range(0,10):
        SendKey("Ok",0.4,1)
        SendKey("Back",0.3,1)
        
    SendKey("Down",0.3,1)
    SendKey("Ok",3,1)
    SendKey("Ok",0.5,1)
    
    SendKey("Down",0.3,1)
    SendKey("Ok",3,1)
    Random_Navigation(5)
    
    Switch_To_Satellite()
    Switch_To_Tuner()
    
    Home_Positioning_Launch_App(6)
    Digit_Channel_Selection("Satellite",89)
    SendKey("Ok",1,1)
    SendKey("Right",0.3,1)
    SendKey("Ok",1,1)                                  
    
    SendKey("Down",0.3,1)
    SendKey("Ok",1,2)
    
    SendKey("Down",0.3,2)
    
def QuickMenu1():
    
    SendKey("TVMenu",3,1)
    SendKey("Up_longpress",0.3,2)
    SendKey("Ok",0.4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",15,1)
    SendKey("Ok",0.8,4)
    
    SendKey("TVMenu",3,1)
    SendKey("Up_longpress",0.3,2)
    SendKey("Ok",0.4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",35,1)
    SendKey("Ok",0.8,4)
    
    SendKey("TVMenu",3,1)
    SendKey("Up_longpress",0.3,2)
    SendKey("Ok",0.4,1)
    SendKey("Down",0.3,2)    
    SendKey("Ok",0.5,1)
    
    for x in range(0,7):
        SendKey("Volume_Up",0.3, 10)
        SendKey("Mute",0.3,5)
        SendKey("Volume_Down",0.3, 10)
        SendKey("Ok",0.8, 4)
        
    time.sleep(15)
    SendKey("Ok",0.8,4)

    SendKey("TVMenu",3,1)
    SendKey("Up_longpress",0.3,2)
    SendKey("Ok",0.4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",20,1)
    for count in range(0,4):
        SendKey("Down",0.5,1)
        SendKey("Ok",0.5,1)
    SendKey("Ok",15,1)

def QuickMenu2():
    for count in range(0,5):
        SendKey("TVMenu",3,1)
        SendKey("Up_longpress",0.3,2)
        SendKey("Ok",0.4,1)
        SendKey("Down",0.3,2)
        SendKey("Ok",15,1)
        SendKey("Ok",0.8,4)
    
    for count in range(0,5):
        SendKey("TVMenu",3,1)
        SendKey("Up_longpress",0.3,2)
        SendKey("Ok",0.4,1)
        SendKey("Down",0.3,2)
        SendKey("Ok",35,1)
        SendKey("Ok",0.8,4)
    
    for count in range(0,5):
        SendKey("TVMenu",3,1)
        SendKey("Up_longpress",0.3,2)
        SendKey("Ok",0.4,1)
        SendKey("Down",0.3,2)    
        SendKey("Ok",0.5,1)
        for x in range(0,7):
            SendKey("Volume_Up",0.3,10)
            SendKey("Mute",0.3,5)
            SendKey("Volume_Down",0.3,10)
            SendKey("Ok",0.8,4)
        time.sleep(15)
        SendKey("Ok",0.8,4)

    SendKey("TVMenu",3,1)
    SendKey("Up_longpress",0.3,2)
    SendKey("Down",0.4,2)
    for x in range(0,30):
        SendKey("Ok",0.4,1)
        SendKey("Back",0.3,1)


def QuickMenu_LaunchExit():
    for x in range(0,10):
        SendKey("TVMenu",2,1)
        SendKey("Back",0.4,1)
def QuickMenu_Demome_LaunchExit():
    SendKey("TVMenu",3,1)
    SendKey("Ok",1,1)
    SendKey("Left",0.2,4)
    SendKey("Up",0.3,2)
    SendKey("Down",0.3,1)
    SendKey("Right",0.5,2)
    for x in range(0,10):
        SendKey("Ok",3,1)   
        SendKey("Back",3,1)
    
def QuickMenu_CheckTV_DemoMe():
    SendKey("TVMenu",3,1)
    SendKey("Up_longpress",0.3,2)
    SendKey("Ok",0.4,1)
    SendKey("Down",0.3,2)
    for x in range(0,5):
        SendKey("Ok",3,1)
        SendKey("TVMenu",3,1)
        SendKey("Ok",1,1)
        SendKey("Down",0.3,1)
        SendKey("Right",0.5,2)
        SendKey("Ok",3,1)
        SendKey("Back",0.7,2)
def QuickMenu_Demome():
    SendKey("TVMenu",3,1)
    SendKey("Ok",1,1)
    SendKey("Left",0.2,4)
    SendKey("Up",0.3,2)
    SendKey("Down",0.3,1)
    SendKey("Right",0.5,2)
    SendKey("Ok",10,1)
    SendKey("TVMenu",3,1)
    SendKey("Up_longpress",0.3,2)
    SendKey("Ok",0.4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",30,1)
    SendKey("Ok",0.8,4)
    
def Script():
    Netflix_Demome_Revanth()
    DropBox_StabilityFolder_Demome()
    Timeshift_Demome()
    TimeShift1()
    TimeShift()
    OTR_Demome()
    TimeShift2()
    
    Timeshift_Demome()
    TimeShift1()
    TimeShift()
    OTR_Demome()
    Netflix_Demome_Revanth()
    DropBox_StabilityFolder_Demome()
    TimeShift2()


    QuickMenu_Demome()
    QuickMenu_Demome_LaunchExit()
    QuickMenu()
    QuickMenu_CheckTV_DemoMe()
    QuickMenu1()
    
def Block1():

    Digit_Channel_Selection("Satellite",83)
    time.sleep(15)

    Launcher_Demome_Revanth()

    Youtube_Row1_Standby_Revanth()

    MXPlayer_Demome_Revanth()

    Netflix_Demome_Revanth()

    SwitchingChannels_Demome_Revanth()

    Launcher_Demome_Revanth()

    Switching_Tuner_Channels_Demome_Revanth()

    Youtube_Row2_Standby_Revanth()

    DemoMe_App_Demome_Revanth()
    
    HDMI_Demome_Revanth()

    Switching_Satellite_Channels_Demome_Revanth()

    Guide_Demome_Revanth()

    CBPlayback_DemoMe_Revanth()

    Launcher_Demome_Revanth()
    
    OIB_Demome_Revanth()

    All_App_Launching_Demome_Revanth()

def Block2():
    Script()
    
if __name__ == "__main__":
    for count in range(0,1000):
        Block1()
        Block2()
