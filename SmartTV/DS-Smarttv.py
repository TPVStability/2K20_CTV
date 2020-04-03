# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:45:52 2020

@author: Revanth.D
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:14:37 2020

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
RedRat_Device_Name = "No name 18758"
RedRat_Device_Port = "1"

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

def Netflix_Revanth(number, number1):
    
    SendKey('Netflix',10,1)
    SendKey('Ok',1,1)
    SendKey('Back',0.4,4)
    SendKey('Left',0.3,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',0.6,2)
    SendKey('Ok',0.6,1)
    SendKey('Up',0.6,4)
    
    if number <= 7:
        SendKey('Right',1,number-1)
    else:
        SendKey('Left',1,5)
        SendKey('Right',1,1)
        SendKey('Down',1,1)
        SendKey('Right',5,number-6)
    SendKey('Ok',5,2)
    time.sleep(20)
    Trick_List_Navigations_Fixed(Trick_List_6)
    
    
    SendKey('Back',1,4)
    SendKey('Left',1,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',1,2)
    SendKey('Ok',1,1)
    SendKey('Up',1,1)
    if number <= 7:
        SendKey('Right',1,number1-1)
    else:
        SendKey('Left',1,5)
        SendKey('Right',1,1)
        SendKey('Down',1,1)
        SendKey('Right',5,number1-6)
    SendKey('Ok',5,2)
    time.sleep(20)
    Trick_List_Navigations_Fixed(Trick_List_5)

def Youtube_Row1_New():
    Home_Positioning_Launch_App(1)
    SendKey("Left_longpress",0.7, 1)
    SendKey("Up_longpress", 0.5, 1)
    SendKey("Down", 0.3, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    
    for count in range(0,3):
        SendKey("Ok", 30.0, 1) # Play the content for 30 Seconds
        Trick_List_Navigations_Fixed(Trick_List_5)
        SendKey("Play", 1, 1)
        time.sleep(5)
        SendKey("Back", 1, 1)
        SendKey("Right", 0.5, 1)

def Youtube_Row2_New():
    Home_Positioning_Launch_App(1)
    SendKey("Left_longpress",0.7, 1)
    SendKey("Up_longpress", 0.5, 1)
    SendKey("Down", 0.3, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down", 0.3, 1)
    for count in range(0,3):
        SendKey("Ok", 30.0, 1) # Play the content for 30 Seconds
        Trick_List_Navigations_Fixed(Trick_List_5)
        SendKey("Play", 1, 1)
        time.sleep(5)
        SendKey("Back", 1, 1)
        SendKey("Right", 0.5, 1)

def HDMI_Switching():
    SendKey("Sources",4,1)
    SendKey("Down_longpress",0.3,2)
    SendKey("Ok",5,1)
    for x in range(0,4):
        SendKey("Sources",4,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",5,1)
    
    SendKey("Sources",4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",5,1)
    
    SendKey("Sources",4,1)
    SendKey("Up",0.3,1)
    SendKey("Ok",5,1)
    
    SendKey("Sources",4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",5,1)
    
    SendKey("Sources",4,1)
    SendKey("Up",0.3,3)
    SendKey("Ok",5,1)
    
    for x in range(0,4):
        SendKey("Sources",4,1)
        SendKey("Down",0.3,1)
        SendKey("Ok",5,1)

    for x in range(0,4):
        SendKey("Sources",4,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",0.5,1)
    
    SendKey("Sources",4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",0.5,1)
    
    SendKey("Sources",4,1)
    SendKey("Up",0.3,1)
    SendKey("Ok",0.5,1)
    
    SendKey("Sources",4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",0.5,1)
    
    SendKey("Sources",4,1)
    SendKey("Up",0.3,3)
    SendKey("Ok",0.5,1)
    
    for x in range(0,4):
        SendKey("Sources",4,1)
        SendKey("Down",0.3,1)
        SendKey("Ok",0.5,1)

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

def CBPlayback_Standby():
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

def DropBox():
    Down_Count = [0,1,2,3,4,5]
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    time.sleep(5)
    SendKey('Up',3,1)
    SendKey('Ok',1,1)
    SendKey("Right",2,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    
    SendKey("Back",4,2)
    SendKey("Left",0.7,1)
    SendKey('Down',0.4,2)
    SendKey('Right',0.4,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Back",4,1)
    SendKey("Left",0.7,1)
    SendKey('Down',0.4,2)
    SendKey('Right',0.4,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Back",4,1)
    SendKey("Left",0.7,1)
    SendKey('Down',0.4,4)
    SendKey('Right',0.4,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_1)


    SendKey("Back",4,1)
    SendKey("Left",0.7,1)
    SendKey('Down_longpress',0.4,2)
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    
def DropBox_StabilityFolder():
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
    time.sleep(6)
    SendKey('Ok',1,1)
    
    SendKey("Down", 3,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    SendKey("Back",4,2)
#audio
    SendKey('Left',0.3,4)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,3)
    time.sleep(5)
    SendKey('Ok',1,1)
  
    SendKey("Down", 3,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count1))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Back",4,2)
 #Images   
    SendKey('Left',0.3,4)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,3)
    time.sleep(6)
    SendKey('Ok',1,1)
    
    SendKey("Down", 3,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count2))
    SendKey('Ok',3,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Back",4,2)

def DropBox_StabilityFolder_standby():
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
    time.sleep(6)
    SendKey('Ok',1,1)
    
    SendKey("Down", 3,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    SendKey("Standby",18,1)
    SendKey("Standby",5,1)
#audio
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Left',0.3,4)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,3)
    time.sleep(5)
    SendKey('Ok',1,1)
  
    SendKey("Down", 3,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count1))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby",7,1)
    SendKey("Standby",5,1)
 #Images   
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Left',0.3,4)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,3)
    time.sleep(6)
    SendKey('Ok',1,1)
    
    SendKey("Down", 3,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count2))
    SendKey('Ok',3,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby",15,1)
    SendKey("Standby",5,1)

def Netflix2(number, number1):
    
    SendKey('Netflix',10,1)
    SendKey('Ok',1,1)
    SendKey('Back',0.4,4)
    SendKey('Left',0.3,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',0.6,2)
    SendKey('Ok',0.6,1)
    SendKey('Up',0.6,4)
    
    if number <= 7:
        SendKey('Right',1,number-1)
    else:
        SendKey('Left',1,5)
        SendKey('Right',1,1)
        SendKey('Down',1,1)
        SendKey('Right',5,number-6)
    SendKey('Ok',5,2)
    time.sleep(300)
    Trick_List_Navigations_Fixed(Trick_List_6)
    
    
    SendKey('Back',1,4)
    SendKey('Left',1,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',1,2)
    SendKey('Ok',1,1)
    SendKey('Up',1,1)
    if number <= 7:
        SendKey('Right',1,number1-1)
    else:
        SendKey('Left',1,5)
        SendKey('Right',1,1)
        SendKey('Down',1,1)
        SendKey('Right',5,number1-6)
    SendKey('Ok',5,2)
    time.sleep(300)
    Trick_List_Navigations_Fixed(Trick_List_5)

def Youtube2_Row1():
    Home_Positioning_Launch_App(1)
    SendKey("Left_longpress",0.7, 1)
    SendKey("Up_longpress", 0.5, 1)
    SendKey("Down", 0.3, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    
    for count in range(0,3):
        SendKey("Ok", 300, 1) # Play the content for 30 Seconds
        Trick_List_Navigations_Fixed(Trick_List_5)
        SendKey("Play", 1, 1)
        time.sleep(5)
        SendKey("Back", 1, 1)
        SendKey("Right", 0.5, 1)

def Youtube2_Row2():
    Home_Positioning_Launch_App(1)
    SendKey("Left_longpress",0.7, 1)
    SendKey("Up_longpress", 0.5, 1)
    SendKey("Down", 0.3, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down", 0.3, 1)
    for count in range(0,3):
        SendKey("Ok", 300, 1) # Play the content for 30 Seconds
        Trick_List_Navigations_Fixed(Trick_List_5)
        SendKey("Play", 1, 1)
        time.sleep(5)
        SendKey("Back", 1, 1)
        SendKey("Right", 0.5, 1)

def DLNA():
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Down',0.3,5)
    
    SendKey('Up_Longpress',0.5,1)
    SendKey('Down',0.4,2)
    SendKey('Right',0.3,2)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    SendKey("Back",4,2)
    
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Back",4,2)
    
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Back",4,2)
    
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Back",4,2)
    
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Back",4,2)
    
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Back",4,2)
    
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Back",4,2)
    
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    SendKey("Back",4,2)
    
def DLNA_Standby():
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Down',0.3,5)
    
    SendKey('Up_Longpress',0.5,1)
    SendKey('Down',0.4,2)
    SendKey('Right',0.3,2)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    
    SendKey("Standby",15,1)
    SendKey("Standby",5,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Down',0.3,5)
    
    SendKey('Up_Longpress',0.5,1)
    SendKey('Down',0.4,2)
    SendKey('Right',0.3,2)
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    SendKey("Standby",25,1)
    SendKey("Standby",5,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Down',0.3,5)
    
    SendKey('Up_Longpress',0.5,1)
    SendKey('Down',0.4,3)
    SendKey('Right',0.3,2)
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    SendKey("Standby",12,1)
    SendKey("Standby",5,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Down',0.3,5)
    
    SendKey('Up_Longpress',0.5,1)
    SendKey('Down',0.4,4)
    SendKey('Right',0.3,2)
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    SendKey("Standby",5,1)
    SendKey("Standby",5,1)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Down',0.3,5)
    
    SendKey('Up_Longpress',0.5,1)
    SendKey('Down',0.4,5)
    SendKey('Right',0.3,2)
    SendKey('Down',0.4,1)
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    SendKey("Standby",10,1)
    SendKey("Standby",5,1)

def OIB():
    
    Home_Positioning_Launch_App(3)
    
    for count in range(0,4):
        for count1 in range(0,4):            
            SendKey("Right",1,1)
            
        SendKey("Ok")
        time.sleep(5)
        
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

        Random_longpress(20)

        SendKey("Back",4,1)
        
    SendKey("Back",2,1)
    SendKey("Ok",2,1)
        
    Home_Positioning_Launch_App(3)
    SendKey("Down",2,1)
    
    for count in range(0,4):
        for count1 in range(0,4):            
            SendKey("Right",1,1)
            
        SendKey("Ok")
        time.sleep(5)
        
        SendKey("Down_longpress",0.2,2)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
    
        Random_longpress(20)
        
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
        SendKey("Right_longpress",0.2,2)
        SendKey("Up_longpress",0.2,2)
        
        SendKey("Up_longpress",0.2,2)
        SendKey("Down_longpress",0.2,3)
        SendKey("Left_longpress",0.2,2)
            
        SendKey("Back",4,1)
        
    SendKey("Back",2,1)
    SendKey("Ok",2,1)
        
def App_Gallery_Nav_Revanth():
    SendKey("Smart_Home",10,1)
    #Featured apps category
    for count in range(0,2):
        Random_longpress(20)  
        SendKey("Up_longpress",0.3,1)
        SendKey("Down_longpress",0.3,1)
        SendKey("Right_longpress",0.3,1)
        SendKey("Up_longpress",0.3,1)
        SendKey("Left_longpress",0.3,1)
        SendKey("Down_longpress",0.3,1)
        SendKey("Right",0.3,1)
        SendKey("Up",0.2,4)
        SendKey("Left",0.2,4)
        SendKey("Right",0.2,1)
        SendKey("Down",0.2,4)
        SendKey("Right",0.2,1)
        Random_Navigation(20)
        SendKey("Up",0.2,4)
        SendKey("Right",0.2,1)
        SendKey("Down",0.2,4)
        SendKey("Right",0.2,4)
        SendKey("Up",0.2,1)
    

    SendKey("Up_longpress",0.2,3)
    SendKey("Down",0.2,1)
    for count in range(0,5):
        SendKey("Right",0.3,1)
        SendKey("Ok",0.3,1)
    for count in range(0,5):
        SendKey("Left",0.3,1)
        SendKey("Ok",0.3,1)
        
    SendKey("Up",0.3,1)
    SendKey("Down",0.3,1)
    SendKey("Right",0.3,1)
    SendKey("Ok",0.3,1)
    
 #All category
    print ("AppGalleryNav-All category")

    for count in range(0,12):
        SendKey("Down",0.7,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.6,1)
        SendKey("Right",0.7,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)

    for count in range(0,9):
        SendKey("Up",0.6,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.6,1)
        SendKey("Left",0.6,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)
        SendKey("Right",0.6,2)
        SendKey("Ok",1,1)
        SendKey("Back",0.5,1)

#country change
    
    for count in range(0,3):
        SendKey("Green",0.8,1)
        SendKey("Down_longpress",0.7,1)
        SendKey("Ok",10,1)
        SendKey("Green",0.8,1)
        SendKey("Up",1,3)
        SendKey("Ok",10,1)
        
    
# New Category
    print ("AppGalleryNav-New category")

    SendKey("Up_longpress",0.2,4)
    SendKey("Down",0.7,1)
    SendKey("Right",0.7,2)
    SendKey("Ok",1,1)

    for count in range(0,2):
        SendKey("Down",0.7,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)
        SendKey("Right",0.7,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)

#    for count in range(0,3):
#        SendKey("Up",0.7,1)
#        SendKey("Ok",1,1)
#        SendKey("Back",0.8,1)
#        SendKey("Left",0.7,1)
#        SendKey("Ok",1,1)
#        SendKey("Back",1,1)
#        SendKey("Right",0.6,2)
#        SendKey("Ok",1,1)
#        SendKey("Back",0.8,1)

#country change
    
    for count in range(0,3):
        SendKey("Green",0.8,1)
        SendKey("Up_longpress",0.7,1)
        SendKey("Ok",8,1)
        SendKey("Green",0.8,1)
        SendKey("Down",1,3)
        SendKey("Ok",8,1)

#Video category
#    SendKey("Smart_Home",10,1)
    print ("AppGalleryNav-Video category")
        
    SendKey("Up_longpress",0.2,4)
    SendKey("Down",1,1)
    SendKey("Right",1,3)
    SendKey("Ok",1,1)

    for count in range(0,5):
        SendKey("Down",0.7,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)
        SendKey("Right",0.7,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)

    for count in range(0,4):
        SendKey("Up",0.6,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)
        SendKey("Left",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",0.7,2)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)

#country change
    
    for count in range(0,3):
        SendKey("Green",0.8,1)
        SendKey("Up_longpress",1,1)
        SendKey("Ok",8,1)
        SendKey("Green",0.8,1)
        SendKey("Down",1,3)
        SendKey("Ok",8,1)
        
#Entertainment category
    print ("AppGalleryNav-Entertainment category")
        
    SendKey("Up_longpress",0.2,4)
    SendKey("Down",0.6,1)
    SendKey("Right",0.6,4)
    SendKey("Ok",1,1)

    for count in range(0,2):
        SendKey("Down",0.6,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)
        SendKey("Right",0.7,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)

    for count in range(0,2):
        SendKey("Up",0.7,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)
        SendKey("Left",0.7,1)
        SendKey("Ok",1,1)
        SendKey("Back",0.6,1)
        SendKey("Right",0.6,2)
        SendKey("Ok",1,1)
        SendKey("Back",0.7,1)

#country change
    
    for count in range(0,3):
        SendKey("Green",0.8,1)
        SendKey("Down_longpress",0.7,1)
        SendKey("Ok",8,1)
        SendKey("Green",0.8,1)
        SendKey("Up",1,3)
        SendKey("Ok",8,1)
    
def DemoMe_App():
    Home_Positioning_Launch_App(5)
    
    SendKey("Down",0.3,1)
    SendKey("Right",0.3,2)
    SendKey("Ok",10,1)

    SendKey("Home_longpress",2,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",2,1)
    SendKey("Left",0.2,2)
    SendKey("Down",0.3,4)
    SendKey("Ok",5,1)
    SendKey("Ok",1,1)
    
    SendKey("Up",0.3,1)
    SendKey("Ok",5,1)
    
    SendKey("Home_longpress",2,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",2,1)
    SendKey("Up",0.3,2)
    SendKey("Right",0.3,2)
    SendKey("Down",0.3,1)
    SendKey("Ok",15,1)
#launch-ext
    for count in range(0,3):
        SendKey("Home_longpress",2,1)
        SendKey("Down",0.3,2)
        SendKey("Ok",2,1)
        SendKey("Down",0.3,1)
        SendKey("Right",0.3,2)
        SendKey("Ok",3,1)

    for count in range(0,3):
        SendKey("Home_longpress",2,1)
        SendKey("Down",0.3,2)
        SendKey("Ok",2,1)
        SendKey("Down",0.3,1)
        SendKey("Right",0.3,2)
        SendKey("Ok",5,1)    
 #Ambilight demo   
    SendKey("Home_longpress",2,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",2,1)
    SendKey("Left",0.2,2)
    SendKey("Up",0.3,4)
    SendKey("Down",0.3,3)
    SendKey("Ok",15,1)

        
def Start_Script():
    Digit_Channel_Selection("Satellite",86)
    
    Netflix_Revanth(6,1)
    CBPlayback()  
    App_Gallery_Nav_Revanth()
    Youtube_Row1_New()
    DemoMe_App()
    Netflix_Revanth(1,3)
    OIB()
    DropBox_StabilityFolder()
    DropBox()  

    
     
    
    

        
if __name__ == "__main__":
    for count in range(0,100):   
        Start_Script()
