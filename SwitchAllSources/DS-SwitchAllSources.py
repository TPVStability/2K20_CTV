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
RedRat_Device_Name = "No name 10401"
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

def Trick_List_Navigations_Fixed(Trick_List):
    Key_1stArg = 0
    SleepTime_2ndArg = 1
    for count in range(len(Trick_List)):
        SendKey(Trick_List[count][Key_1stArg], Trick_List[count][SleepTime_2ndArg])

Text_Zap_List = [10,11,12,13,14]
Text_Random_Standby_Wakeup_List = ["Blue","Exit","Home","Netflix","Ambilight",0, "Channel_Up", "Channel_Down"]
Wakeup_Time_List = [[7,8],[15,9], [25,9],[3,6], [2,5],[13,10], [14,12],[1,7], [10,10],[12.5,8]]

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
    SendKey('Up_longpress', 1, 1)
    SendKey('Left', 0.6, 1)
    
    if (App_Number in Apps_In_Row1):
        Down_Count = 1
    elif (App_Number in Apps_In_Row2):
        Down_Count = 2
    elif (App_Number in Apps_In_Row2):
        Down_Count = 3
    elif (App_Number in Apps_In_Row2):
        Down_Count = 4
    elif (App_Number in Apps_In_Row2):
        Down_Count = 5

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

def SwitchingChannels_Revanth(): 
    
    Digit_Channel_Selection("Tuner",5)
    time.sleep(5)
    SendKey("Up_longpress",4,1)
    SendKey("Up",0.3,6)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,1)
    SendKey("Down_longpress",3,1)
    SendKey("Down",0.3,6)
    SendKey("Volume_Down",0.1,7)
    
    Digit_Channel_Selection("Satellite",77)
    time.sleep(5)
    SendKey("Channel_Down_longpress",0.2,1)
    SendKey("Channel_Up",0.3,6)
    time.sleep(5)
    SendKey("Volume_Down",0.1,7)
    SendKey("Channel_Up_longpress",0.2,1)
    SendKey("Channel_Down",0.3,5)
    SendKey("Mute",0.3,4)
    SendKey("Volume_Up",0.1,7)
    
    Digit_Channel_Selection("Tuner",14)
    time.sleep(5)
    SendKey("Up_longpress",5,1)
    SendKey("Channel_Down",0.3,3)
    SendKey("Volume_Down",0.1,4)
    SendKey("Channel_Down_longpress",0.2,1)
    SendKey("Channel_Up",1,3)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,2)
    
    Digit_Channel_Selection("Satellite",2)
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

    Digit_Channel_Selection("Tuner",21)
    time.sleep(5)
    SendKey("Volume_Down",0.1,7)
    SendKey("Channel_Up_longpress",3,1)
    SendKey("Mute",0.3,3)
    SendKey("Up_longpress",0.2,1)
    SendKey("Volume_Up",0.1,7)
    SendKey("Channel_Down",0.2,6)
    SendKey("Volume_Down",0.1,4)
    
    Digit_Channel_Selection("Satellite",67)
    time.sleep(5)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down_longpress",0.2,1)
    time.sleep(5) 
    SendKey("Volume_Up",0.1,8)
    SendKey("Mute",0.3,5)
    SendKey("Volume_Down",0.1,7)
       
    
    Digit_Channel_Selection("Tuner",10)
    time.sleep(5)
    SendKey("Volume_Up",0.1,3)
    SendKey("Volume_Down",0.1,4)
    SendKey("Up_longpress",3,1)
    SendKey("Channel_Down",0.2,4)
    SendKey("Down_longpress",0.2,1)
    SendKey("Mute",0.3,3)
    SendKey("Channel_Up_longpress",0.5,1)
    
    Digit_Channel_Selection("Satellite",28)
    time.sleep(5)
    SendKey("Down_longpress",0.2,1)
    SendKey("Channel_Up_longpress",0.5,1)
    SendKey("Volume_Down",0.1,7)
    SendKey("Volume_Up",0.1,5)
    SendKey("Channel_Down",0.2,4)
    SendKey("Mute",0.3,1)
    
    Digit_Channel_Selection("Tuner",23)
    time.sleep(5)
    SendKey("Channel_Up_longpress",6,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Volume_Up",0.1,6)
    SendKey("Channel_Down_longpress",8,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Mute",0.3,1)
    SendKey("Channel_Up",1,5)
    SendKey("Volume_Down",0.1,3)
    
    Digit_Channel_Selection("Satellite",74)
    time.sleep(5)
    SendKey("Up_longpress",0.2,1)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,5)
    SendKey("Channel_Down_longpress",5,1)
    SendKey("Volume_Up",0.1,7)
    SendKey("Down_longpress",0.2,1)
    SendKey("Channel_Up_longpress",3,1)

def Guide_Nav():
    ## Launch Guide and perform Navigation inside it

    Switch_To_Tuner()

    SendKey("TVGuide")
    time.sleep(4)
    SendKey("Options")
    time.sleep(4)
    SendKey("Down")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Up")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Up")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Up")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Up")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Up")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Back")
    time.sleep(1)
    for count in xrange(50):
        SendKey("Right")
        time.sleep(0.1)
        
    SendKey("Exit")
    time.sleep(2)
   
    for count in range(0,1):
        SendKey("TVGuide")
        time.sleep(10)
        
    for count3 in range(0,15):
        SendKey("Left")
        time.sleep(0.23)
    time.sleep(5)

    for count in range(0,10):
        SendKey("Info")
        time.sleep(3)
        SendKey("Down")
        time.sleep(1)
        for count in range(0,5):
            SendKey("Right")
            time.sleep(0.5)
        SendKey("Back")
        time.sleep(1)
        SendKey("Left")
        time.sleep(1)
        SendKey("Left")
        time.sleep(1)
        
    SendKey("Down")
    time.sleep(1)

    for count in range(0,10):
        SendKey("Info")
        time.sleep(3)
        SendKey("Down")
        time.sleep(1)
        for count in range(0,5):
            SendKey("Right")
            time.sleep(0.5)
        SendKey("Back")
        time.sleep(1)
        SendKey("Left")
        time.sleep(1)
        SendKey("Left")
        time.sleep(1)
        
    SendKey("Down")
    time.sleep(1)
    
    for count in range(0,10):
        SendKey("Info")
        time.sleep(3)
        SendKey("Down")
        time.sleep(1)
        for count in range(0,5):
            SendKey("Right")
            time.sleep(0.5)
        SendKey("Back")
        time.sleep(1)
        SendKey("Left")
        time.sleep(1)
        SendKey("Left")
        time.sleep(1)

    SendKey("Down")
    time.sleep(1)
    
    for count in range(0,10):
        SendKey("Info")
        time.sleep(3)
        SendKey("Down")
        time.sleep(1)
        for count in range(0,5):
            SendKey("Right")
            time.sleep(0.5)
        SendKey("Back")
        time.sleep(1)
        SendKey("Left")
        time.sleep(1)
        SendKey("Left")
        time.sleep(1)  
    
    SendKey("Down")
    time.sleep(1)
    
    for count in range(0,10):
        SendKey("Info")
        time.sleep(3)
        SendKey("Down")
        time.sleep(1)
        for count in range(0,5):
            SendKey("Right")
            time.sleep(0.5)
        SendKey("Back")
        time.sleep(1)
        SendKey("Right")
        time.sleep(1)
        SendKey("Right")
        time.sleep(1)

    SendKey("Down")
    time.sleep(1)
    
    for count in range(0,10):
        SendKey("Info")
        time.sleep(3)
        SendKey("Down")
        time.sleep(1)
        for count in range(0,5):
            SendKey("Right")
            time.sleep(0.5)
        SendKey("Back")
        time.sleep(1)
        SendKey("Right")
        time.sleep(1)
        SendKey("Right")
        time.sleep(1)  
    
    Guide_Yellow()

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
    
def Random_Volume(Volume_Count):
    for count in range(Volume_Count):
        Volume_List = ["Volume_Up","Mute","Volume_Down"]
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + random.choice(Volume_List) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(0.3)

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

def Switching_Satellite_Channels_Revanth():
    
    Digit_Channel_Selection("Satellite",70)
    time.sleep(5)
    SendKey("2",0.2,1)
    SendKey("3",0.2,1)
    SendKey("9",0.2,1)
    time.sleep(4)
    SendKey("Ok",3,1)
    SendKey("Volume_Up",0.1,10)
    SendKey("Volume_Down",0.1,3)
    SendKey("Mute",0.3,11)
    
    SendKey("1",0.2,1)
    SendKey("4",0.2,1)
    SendKey("7",0.2,1)
    SendKey("Ok",1,2)
    
    
    SendKey("2",0.2,1)
    SendKey("3",0.2,1)
    SendKey("6",0.2,1)
    time.sleep(4)
    SendKey("Volume_Up",0.1,4)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,6)
    SendKey("9",0.2,1)
    SendKey("2",0.2,1)
    time.sleep(2)
    SendKey("Volume_Down",0.1,10)
    
    SendKey("1",0.2,1)
    SendKey("2",0.2,1)
    SendKey("1",0.2,1)
    time.sleep(6)
    SendKey("Volume_Up",0.1,8)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,3)
    SendKey("1",0.2,1)
    SendKey("7",0.2,1)
    SendKey("2",0.2,1)
    time.sleep(8)
    SendKey("Volume_Up",0.1,6)
    SendKey("Volume_Down",0.1,4)
    SendKey("1",0.2,1)
    SendKey("6",0.2,1)
    SendKey("7",0.2,1)
    time.sleep(5)
    SendKey("2",0.2,1)
    SendKey("0",0.2,1)
    SendKey("8",0.2,1)
    SendKey("Mute",0.3,4)
    time.sleep(4)
    SendKey("Ok",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok",3,1)
    
    SendKey("6",0.2,1)
    SendKey("7",0.2,1)
    SendKey("Mute",0.3,4)
    
    SendKey("7",0.2,1)
    SendKey("7",0.2,1)
    SendKey("Mute",0.3,4)
    
    
def Switching_Tuner_Channels_Revanth():
    Digit_Channel_Selection("Tuner",5)
    time.sleep(3)
    SendKey("Volume_Down",0.1,3)
    SendKey("Volume_Up",0.1,12)
    SendKey("Mute",0.3,8)
    SendKey("1",0.2,1)
    SendKey("4",0.2,1)
    time.sleep(5)
    
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


def Ok_List_Nav_Tuner_Legacy():
    ## Select OK to launch Tuner channel list and select different channels

    Switch_To_Tuner()
    time.sleep(3)
    
    SendKey("Ok")
    time.sleep(5)
    
    for count in range(4):    
        for count2 in range(0,32):
            SendKey("Down")
            time.sleep(0.2)
        for count2 in range(0,35):
            SendKey("Up")
            time.sleep(0.2)

    SendKey("Ok")
    time.sleep(3)

    SendKey("Ok")
    time.sleep(5)

    for count in range(7):    
        for count2 in range(5):
            SendKey("Down_longpress")
            time.sleep(0.7)
        for count2 in range(6):
            SendKey("Up_longpress")
            time.sleep(0.6)    
    
    for count in range(0,20):
        SendKey("Ok")
        time.sleep(4)
        SendKey("Down")
        time.sleep(2)
        SendKey("Ok")
        time.sleep(4)
        
    for count in range(0,5):
        SendKey("Ok")
        time.sleep(3)
        for count in range(0,3):
            SendKey("Down")
            time.sleep(2)
        SendKey("Ok")
        time.sleep(3)    


def Ok_List_Nav_Satellite_Legacy():
## Select OK to launch channel list and select different channels

    Switch_To_Satellite()
    time.sleep(3)
    
    SendKey("Ok")
    time.sleep(5)
    
    for count in range(4):    
        for count2 in range(0,32):
            SendKey("Down")
            time.sleep(0.2)
        for count2 in range(0,35):
            SendKey("Up")
            time.sleep(0.2)

    SendKey("Ok")
    time.sleep(3)

    SendKey("Ok")
    time.sleep(5)

    for count in range(7):    
        for count2 in range(5):
            SendKey("Down_longpress")
            time.sleep(0.7)
        for count2 in range(6):
            SendKey("Up_longpress")
            time.sleep(0.6)    
    
    for count in range(0,20):
        SendKey("Ok")
        time.sleep(4)
        SendKey("Down")
        time.sleep(2)
        SendKey("Ok")
        time.sleep(4)
        
    for count in range(0,5):
        SendKey("Ok")
        time.sleep(3)
        for count1 in range(0,3):
            SendKey("Down")
            time.sleep(2)
        SendKey("Ok")
        time.sleep(3)

def Teletext_Nav_Tuner():
    ## Launch Teletext and perform Navigation and increase volume on teletext page
    Digit_Channel_Selection("Tuner",5)
        
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
        Text_Zap_List = ["5", "7", "8", "9"]

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

def Zapping_Volume():
    ## Perform Zapping
    for count in range(0,10): 
        SendKey("Channel_Up")
        time.sleep(1.5)

    SendKey("Volume_Up")
    time.sleep(0.3)
    SendKey("Mute")
    time.sleep(0.3)
    SendKey("Volume_Down")
    time.sleep(0.3)
    SendKey("Mute")
    time.sleep(0.3)

    Random_Zap_3(8)
    
    for count in range(0,10): 
        SendKey("Up")
        time.sleep(1)
    
    SendKey("Volume_Up")
    time.sleep(0.3)
    SendKey("Volume_Up")
    time.sleep(0.3)
    
    Random_Zap_2(10)
     
    for count in range(6):
        SendKey("Mute")
        time.sleep(0.3)
    for count in range(5):
        SendKey("Volume_Down")
        time.sleep(0.3)
        
    SendKey("Mute")
    time.sleep(0.3)

    Random_Volume(10)
    
    for count in range(0,10): 
        SendKey("Channel_Down")
        time.sleep(2.5)
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

    Random_Zap_25(15)

    SendKey("Volume_Up")
    time.sleep(0.3)
    SendKey("Volume_Up")
    time.sleep(0.3)
    
    for count in range(6):
        SendKey("Mute")
        time.sleep(0.3)
    for count in range(5):
        SendKey("Volume_Down")
        time.sleep(0.3)

    for count in range(0,10): 
        SendKey("Down_longpress")
        time.sleep(3)
        SendKey("Mute")
        time.sleep(0.3)
        
    Random_Zap_1(15)
    
def Random_Zap_2(Zap_Count_2):
    for count in range(Zap_Count_2):
        Zap_List_2 = ["Channel_Up","Down",["2","8"],"9","Channel_Down","1","Up","4","8","2","0",["1","1"],["1","5"],["2","3"],["3","1"],["1","2"],"6", ["3","2"], "Up_longpress","Down_longpress"]

        Zap_List_Temp_2 = random.choice(Zap_List_2)
        
        if type(Zap_List_Temp_2) is list:
            for x in range(0,len(Zap_List_Temp_2)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_2[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            time.sleep(2)
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_2) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(2)

def Random_Zap_1(Zap_Count_1):
    for count in range(Zap_Count_1):
        Zap_List_1 = ["Channel_Up","Down",["2","8"],"9","Channel_Down","1","Up","4","8","2","0",["1","1"],["1","5"],["2","3"],["3","1"],["1","2"],"6", ["3","2"], "Up_longpress","Down_longpress"]

        Zap_List_Temp_1 = random.choice(Zap_List_1)
        
        if type(Zap_List_Temp_1) is list:
            for x in range(0,len(Zap_List_Temp_1)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_1[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            time.sleep(1)
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_1) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(1)
            
def Random_Zap_25(Zap_Count_25):
    for count in range(Zap_Count_25):
        Zap_List_25 = ["Channel_Up","Down",["2","8"],"9","Channel_Down","1","Up","4","8","2","0",["1","1"],["1","5"],["2","3"],["3","1"],["1","2"],"6", ["3","2"], "Up_longpress","Down_longpress"]

        Zap_List_Temp_25 = random.choice(Zap_List_25)
        
        if type(Zap_List_Temp_25) is list:
            for x in range(0,len(Zap_List_Temp_25)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_25[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            time.sleep(2.5)
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_25) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(2.5)
            
def Random_Zap_3(Zap_Count_3):
    for count in range(Zap_Count_3):
        Zap_List_3 = ["Channel_Up","Down",["2","8"],"9","Channel_Down","1","Up","4","8","2","0",["1","1"],["1","5"],["2","3"],["3","1"],["1","2"],"6", ["3","2"], "Up_longpress","Down_longpress"]
        
        Zap_List_Temp_3 = random.choice(Zap_List_3)
        
        if type(Zap_List_Temp_3) is list:
            for x in range(0,len(Zap_List_Temp_3)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_3[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            time.sleep(4)    
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_3) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(4)

def Switch_BN_HDMI_Legacy():
    ## Switch between HDMI 1/2/3/4
    
    time.sleep(5)
    SendKey("Sources")
    time.sleep(4)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,8):
        SendKey("Down")
        time.sleep(0.5)
    SendKey("Ok")
    time.sleep(4)
    
    for count in range(0,4):
        SendKey("Sources")
        time.sleep(3)
        for count1 in range(0,3):
            SendKey("Down")
            time.sleep(0.3)
        SendKey("Ok")
        time.sleep(5)

        SendKey("Sources")
        time.sleep(3)
        for count1 in range(0,1):
            SendKey("Down")
            time.sleep(0.3)
        SendKey("Ok")
        time.sleep(5)


        SendKey("Sources")
        time.sleep(3)
        for count1 in range(0,1):
            SendKey("Down")
            time.sleep(0.3)
        SendKey("Ok")
        time.sleep(5)
        
        SendKey("Sources")
        time.sleep(3)
        for count1 in range(0,3):
            SendKey("Up")
            time.sleep(0.3)
        SendKey("Ok")
        time.sleep(5)

def PiP_Without_Standby():
    Digit_Channel_Selection("Satellite",67)
    
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
        
def Switch_BN_HDMI_Tuner_Legacy():
    ## Switch between HDMI 1/4/Tuner
    
    time.sleep(5)
    SendKey("Sources")
    time.sleep(4)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.5)
    for count in range(0,8):
        SendKey("Down")
        time.sleep(0.5)
    SendKey("Ok")
    time.sleep(4)
    
    for count in range(0,4):
        SendKey("Sources")
        time.sleep(3)
        for count1 in range(0,3):
            SendKey("Down")
            time.sleep(0.3)
        SendKey("Ok")
        time.sleep(5)
        SendKey("Sources")
        time.sleep(3)
        for count1 in range(0,3):
            SendKey("Up")
            time.sleep(0.3)
        SendKey("Ok")
        time.sleep(5)

def Channel_AudioLanguage_Revanth():
    Digit_Channel_Selection("Tuner",5)
    time.sleep(5)
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
   
def Swtich_Sources_Revanth():
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
#fav-tuner
    SendKey("Sources",4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",3,1)
#tuner-network
    SendKey("Sources",4,1)
    SendKey("Down",0.3,3)
    SendKey("Ok",3,1)
#network-googleplaymovies
    SendKey("Sources",4,1)
    SendKey("Up",0.3,2)
    SendKey("Ok",3,1)
#gpm-recordings
    SendKey("Sources",4,1)
    SendKey("Down",0.3,3)
    SendKey("Ok",3,1)
#recorings-satellite
    SendKey("Sources",4,1)
    SendKey("Up",0.3,5)
    SendKey("Ok",3,1)
#satellite-hdmi3
    SendKey("Sources",4,1)
    SendKey("Down",0.3,8)
    SendKey("Ok",3,1)
#hdmi3-usb
    SendKey("Sources",4,1)
    SendKey("Up",0.3,5)
    SendKey("Ok",3,1)
#usb-hdmi4
    SendKey("Sources",4,1)
    SendKey("Down",0.3,6)
    SendKey("Ok",3,1)
#hdmi4-fav
    SendKey("Sources",4,1)
    SendKey("Up",0.3,10)
    SendKey("Ok",3,1)
#fav-recordings
    SendKey("Sources",4,1)
    SendKey("Down",0.3,6)
    SendKey("Ok",3,1)
#recordins-tuner
    SendKey("Sources",4,1)
    SendKey("Up",0.3,4)
    SendKey("Ok",3,1)
#tuner-hdmi1
    SendKey("Sources",4,1)
    SendKey("Down",0.3,5)
    SendKey("Ok",3,1)

def AudioOut_Revanth():
    SendKey("Settings",0.8,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down",0.3,6)
    SendKey("Right",0.2,1)
    
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok",0.4,1)    
    for count in range(0,5):
        SendKey("Down",0.2,1)
        SendKey("Ok",0.5,1)
        
    for count in range(0,5):
        SendKey("Up",0.2,1)
        SendKey("Ok",0.5,1)
        
    SendKey("Down",0.2,2)
    SendKey("Ok",0.5,1)

    SendKey("Up",0.2,2)
    SendKey("Ok",0.5,1)

    SendKey("Down",0.2,3)
    SendKey("Ok",0.5,1)

    SendKey("Up",0.2,2)
    SendKey("Ok",0.5,1)

    SendKey("Down",0.2,2)
    SendKey("Ok",0.5,1)

    SendKey("Up",0.2,3)
    SendKey("Ok",0.5,1)

    SendKey("Down",0.2,4)
    SendKey("Ok",0.5,1)

    SendKey("Up",0.2,2)
    SendKey("Ok",0.5,1)
def Channel_SubtitleChange_Revanth():
    Digit_Channel_Selection("Tuner",12)
    time.sleep(4)
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

def Favourites():

#1
    SendKey("Sources",4.0, 1)
    SendKey("Down_longpress",0.5, 1)
    SendKey("Up_longpress",0.5, 1)
   #SendKey("Down",0.2, 12)
   #SendKey("Up",0.2, 12)
   #SendKey("Down",1.0, 1)
   #SendKey("Ok",5.0, 1)
   #SendKey("Ok",5.0, 1)
    SendKey("Down",0.3, 2)
   #SendKey("1",0.1, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.1, 1)
    SendKey("Up_longpress",0.3, 1)  
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#2
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",0.5, 1)

#3
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    #SendKey("Down",0.2, 12)
    #SendKey("Up",0.2, 12)
    #SendKey("Down",1.0, 1)
    #SendKey("Ok",5.0, 1)
    #SendKey("Ok",5.0, 1)
    SendKey("Down",0.3, 4)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.1, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#4
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
   #SendKey("Down",0.2, 12)
   #SendKey("Up",0.2, 12)
    #SendKey("Down",1.0, 1)
    #SendKey("Ok",5.0, 1)
    #SendKey("Ok",5.0, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
   #SendKey("Up",0.2, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#5
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
   #SendKey("Down",0.2, 12)
   #SendKey("Up",0.2, 12)
   #SendKey("Down",1.0, 1)
    #SendKey("Ok",5.0, 1)
    #SendKey("Ok",5.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.2, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#6
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
   #SendKey("Down",0.2, 12)
   #SendKey("Up",0.2, 12)
   #SendKey("Down",1.0, 1)
   #SendKey("Ok",5.0, 1)
   #SendKey("Ok",5.0, 1)
    SendKey("Down",0.3, 4)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.2, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#7
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
   #SendKey("Down",0.2, 12)
   #SendKey("Up",0.2, 12)
    #SendKey("Down",1.0, 1)
    #SendKey("Ok",5.0, 1)
    #SendKey("Ok",5.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.1, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#8
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.2, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

    SendKey("Sources",4.0, 1)# Favourites switching
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)
    SendKey("Down",0.3, 1)
    SendKey("Ok",1.0, 1)

    SendKey("Sources",4.0, 1)# Favourites switching
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)

    SendKey("Sources",4.0, 1)# Favourites switching
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)
    SendKey("Down",0.3, 3)
    SendKey("Ok",1.0, 1)

    SendKey("Sources",4.0, 1)# Favourites switching
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)
    SendKey("Down",0.3, 4)
    SendKey("Ok",1.0, 1)

    SendKey("Sources",4.0, 1)# Favourites switching
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)

    SendKey("Sources",4.0, 1)# Favourites switching
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.1, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)
    SendKey("Down",0.3, 6)
    SendKey("Ok",1.0, 1)

    SendKey("Sources",4.0, 1)# Favourites switching
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)
    SendKey("Down",0.3, 7)
    SendKey("Ok",1.0, 1)


    SendKey("Sources",4.0, 1)# Favourites switching
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)
    SendKey("Down",0.3, 8)
    SendKey("Ok",1.0, 1)
    SendKey("Exit",1.0, 1)

 #1

    SendKey("Exit",1.0, 1)
       

    SendKey("Sources",4.0, 1) # Reorder channels
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 3)       
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 4) 
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Up",0.3, 4)
    
    SendKey("Down",0.3, 1)
    SendKey("Ok",1.0, 1)

    
    SendKey("Exit",1.0, 1)
    
    
#2
    SendKey("Sources",4.0, 1) # Reorder channels4
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 4)
    SendKey("Up",0.3, 1)
    SendKey("Ok",1.0, 1)

    SendKey("Up_longpress",0.1, 1)
    SendKey("Options",1.0, 1)
    #SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 3)
    #SendKey("Down",1.0, 4)       
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)
    
    SendKey("Down_longpress",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Down",0.3, 6)
    SendKey("Up",0.3, 4)
    SendKey("Ok",1.0, 1)
        
# 1
    SendKey("Sources",4.0, 1)# Favourites Rename
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    #SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 4)
    #SendKey("Down",0.1, 8)
    SendKey("Ok",1.0, 1)
    SendKey("Up",0.3, 1)
    SendKey("Right_longpress",1.0, 1)
    SendKey("Ok",0.3, 20)
    SendKey("s",0.3,1)
    SendKey("u",0.3,1)
    SendKey("d",0.3,1)
    SendKey("h",0.3,1)
    SendKey("e",0.3,1)
    SendKey("e",0.3,1)
    SendKey("r",0.3,1)
    SendKey("Back",0.3,1)
    SendKey("Down",0.3, 1)
    SendKey("Right",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Exit",1.0, 1)


#2
    SendKey("Sources",4.0, 1)# Favourites Rename
    SendKey("Up_longpress",0.5, 1)
    #SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Right",0.3, 1)
    #SendKey("Ok",1.0, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)
    SendKey("Up_longpress",0.3, 1)  
     
    SendKey("Options",1.0, 1)
        
    SendKey("Down",0.3, 4)
    SendKey("Ok",1.0, 1)
    SendKey("Up",0.1, 1)
    SendKey("Right_longpress",1.0, 1)
    SendKey("Ok",0.3, 20)
    SendKey("b",0.3,1)
    SendKey("i",0.3,1)
    SendKey("t",0.3,1)
    SendKey("r",0.3,1)
    SendKey("a",0.3,1)
    SendKey("Back",0.3,1)
    SendKey("Down",0.3, 1)
    SendKey("Right",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Exit",1.0, 1)   

#3
    SendKey("Sources",4.0, 1)# Favourites Rename
    SendKey("Up_longpress",0.5, 1)
    #SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Right",0.3, 1)
    #SendKey("Ok",1.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 3)
    SendKey("Ok",1.0, 1)
    SendKey("Up_longpress",0.5, 1)  
     
    SendKey("Options",1.0, 1)
        
    SendKey("Down",0.3, 4)
    SendKey("Ok",1.0, 1)
    SendKey("Up",0.3, 1)
    SendKey("Right_longpress",1.0, 1)
    SendKey("Ok",0.3, 20)
    SendKey("t",0.3,1)
    SendKey("p",0.3,1)
    SendKey("v",0.3,1)
    SendKey("i",0.3,1)
    SendKey("s",0.3,1)
    SendKey("i",0.3,1)
    SendKey("o",0.3,1)
    SendKey("n",0.3,1)
    SendKey("Back",0.3,1)
    SendKey("Down",0.3, 1)
    SendKey("Right",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Exit",1.0, 1)
    
#4
    SendKey("Sources",4.0, 1)# Favourites Rename
    SendKey("Up_longpress",0.5, 1)
    #SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Right",0.3, 1)
    #SendKey("Ok",1.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 4)
    SendKey("Ok",1.0, 1)
    SendKey("Up_longpress",0.5, 1)  
     
    SendKey("Options",1.0, 1)
        
    SendKey("Down",0.3, 4)
    SendKey("Ok",1.0, 1)
    SendKey("Up",0.3, 1)
    SendKey("Right_longpress",1.0, 1)
    SendKey("Ok",0.3, 20)
    SendKey("b",0.3,1)
    SendKey("r",0.3,1)
    SendKey("d",0.3,1)
    SendKey("c",0.3,1)
    SendKey("Back",0.3,1)
    SendKey("Down",0.3, 1)
    SendKey("Right",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Exit",1.0, 1)
    
    
    SendKey("Exit",1.0, 1)

#1
    SendKey("Sources",4.0, 1)# Favourites Edit
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Ok",1.0, 1) # Edit 
    SendKey("Down",0.3, 2)
    SendKey("Up",0.3, 1)
    SendKey("Ok",2.0, 1)
    SendKey("Down",0.3, 4)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Ok",2.0, 1)
    SendKey("Down",0.3, 10)#Navigations
    SendKey("Up",0.3, 2)
    SendKey("Ok",2.0, 1)
    #SendKey("Down",0.1, 10)
    SendKey("Ok",2.0, 1)
    SendKey("Back",10.0, 1)
    SendKey("Exit",1.0, 1)

#2
    SendKey("Sources",4.0, 1)# Favourites Edit
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Ok",1.0, 1) # Edit 
    SendKey("Down",0.3, 3)
    SendKey("Up",0.3, 1)
    SendKey("Ok",2.0, 1)
    SendKey("Down",0.3, 4)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Ok",2.0, 1)
    SendKey("Down",0.3, 5)#Navigations
    SendKey("Up",0.3, 1)
    SendKey("Ok",2.0, 1)
    #SendKey("Down",0.1, 10)
    SendKey("Ok",2.0, 1)
    SendKey("Back",20.0, 1)
    SendKey("Exit",1.0, 1)

#1    To Delete
    SendKey("Sources",4.0, 1) 
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.2, 1)
    SendKey("Up_longpress",0.3, 1) 
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",2.0, 1)

#2
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",2.0, 1)

#3
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#4
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#5
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#6
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#7
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

#8
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",0.5, 1)
    
    SendKey("Exit",1.0, 1)
    SendKey("Channel_Up",0.3,10)
    SendKey("Channel_Down",0.3,10)

def Filterchannels():

# To Delete
    
    SendKey("Sources",4.0, 1) 
    SendKey("Up_longpress",0.5, 1)
   #SendKey("Down",0.2, 12)
   #SendKey("Up",0.2, 12)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    #SendKey("Ok",5.0, 1)
    #SendKey("Ok",5.0, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.2, 1)
    SendKey("Up_longpress",0.3, 1) 
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",2.0, 1)

#2
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.5, 1)
   #SendKey("Down",0.2, 12)
   #SendKey("Up",0.2, 12)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)
    #SendKey("Ok",5.0, 1)
   # SendKey("Ok",5.0, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.2, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 5)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",2.0, 1)


#1 Create Favourite
    
    SendKey("Sources",4.0, 1)
    SendKey("Down_longpress",0.5, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 3)
   #SendKey("1",0.1, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",2.0, 1)
    SendKey("Up_longpress",0.3, 1)  
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

# filter Antenna Channels
    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Down",0.3, 3)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)    
    SendKey("Down_longpress",0.3, 1)  # switch to Filter Antenna Channels
    SendKey("Up_longpress",0.3, 1)
    SendKey("Down",0.3, 7)
    SendKey("Up",0.3, 10)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
     
    SendKey("Down",0.3, 2) # in options
    SendKey("Up",0.3, 2)
    SendKey("Right",0.3, 1) # in Tv/Radio
    SendKey("Down",0.3, 3)
    SendKey("Up",0.3, 3)
    SendKey("Down",0.3, 2)
    SendKey("Up",0.3, 2)
    SendKey("Down",0.3, 1)
    SendKey("Up",0.3, 3) #  Select TV
    SendKey("Ok",1.0, 1)
    
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 9)
    
        
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1) # in sources
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("Down",0.3, 1) # Radio
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 9)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1) #Sources
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("Down",0.3, 2) #Analogue
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Up",0.3, 2)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1) #Sources
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Right",0.3, 1)
    SendKey("Down",0.3, 3) #Digital
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 12)
    SendKey("Up",0.3, 10)

    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1) #Sources
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 1) #in options    
    SendKey("Right",0.3, 1) # Free/Scrambled - Free
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)

    SendKey("1",0.1, 1)
    SendKey("Up_longpress",0.3, 1) #Sources
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 2) #in options    
    SendKey("Ok",1.0, 1)
    SendKey("1",5.0, 1)  # Search channel
    SendKey("Back",1.0,1)
    SendKey("Down",0.3, 1)  
    SendKey("Right",0.3, 1)
    SendKey("Ok",1.0, 1)         
    SendKey("Down",0.3, 10)
    SendKey("Up",0.3, 10)

    SendKey("Exit",1.0, 1)

# Create Satellite favourites
    
    SendKey("Sources",4.0, 1)
    SendKey("Down_longpress",0.5, 1)
    SendKey("Up_longpress",0.5, 1)
    SendKey("Down",0.3, 2)
   #SendKey("1",0.1, 1)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    #SendKey("Up",0.1, 1)
    SendKey("Up_longpress",0.3, 1)  
    SendKey("Options",1.0, 1)
    SendKey("Down",0.3, 2)
    SendKey("Ok",1.0, 1)    
    SendKey("Ok",1.0, 1)

# filter Satellite  Channels

    SendKey("Sources",4.0, 1)
    SendKey("Up_longpress",0.1, 1)
    SendKey("Down",0.3, 2)
    SendKey("Right",0.3, 1)
    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)    
    SendKey("Down_longpress",0.3, 1)  # switch to Filter Satellite Channels
    SendKey("Up_longpress",0.3, 1)
    SendKey("Down",0.3, 7)
    SendKey("Up",0.3, 10)
    SendKey("Down_longpress",0.3, 1) # select Filter Satellite channels option
    SendKey("Ok",1.0, 1)

    SendKey("Down",0.3, 3) # in options
    SendKey("Up",0.3, 3)
    SendKey("Right",0.3, 1) # in Tv/Radio - TV
    SendKey("Ok",1.0, 1)
    SendKey("Down",0.3, 7)
    SendKey("Up",0.3, 10)
    
    SendKey("1",0.1, 1)
    SendKey("Up_longpress",0.1, 1) #Sources
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.05, 1)
    #SendKey("Ok",1.0, 1)
    SendKey("Down",0.05, 1) # Free/Scrambled - Free
    SendKey("Right",0.1, 1)
    SendKey("Ok",1.0, 1)   
    SendKey("Down",0.05, 10)
    SendKey("Up",0.05, 9)
    
    SendKey("1",0.1, 1)
    SendKey("Up_longpress",0.3, 1) #Sources
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
  
    SendKey("Down",0.3, 1) # Scrambled
    SendKey("Right",0.3, 1)
    SendKey("Down",0.3, 1)       
    SendKey("Ok",1.0, 1)
    
    SendKey("Down",0.3, 12)
    SendKey("Up",0.3, 10)


    SendKey("1",0.3, 1)
    SendKey("Up_longpress",0.3, 1) #Sources
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
  
    SendKey("Down",0.3, 2) # Satellite  select operator
    SendKey("Right",0.3, 1)          
    SendKey("Ok",1.0, 1)
    
    
    SendKey("Down",0.05, 12)
    SendKey("Up",0.05, 10)


    SendKey("1",0.1, 1)
    SendKey("Up_longpress",0.3, 1) #Sources
    SendKey("Ok",1.0, 1)
    SendKey("Down_longpress",0.3, 1)
    SendKey("Ok",1.0, 1)
  
    SendKey("Down",0.3, 3) # Satellite  Search channel
    SendKey("1",1.0, 1)
    SendKey("Back",1.0, 1)
    SendKey("Down",1.0, 1)
    SendKey("Right",0.3, 1)    
    SendKey("Ok",1.0, 1)
       
    SendKey("Down",0.3, 12)
    SendKey("Up",0.3, 10)


    SendKey("Exit",1.0, 1)
    
    
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
 
def Block1():
    
    print ("*******Block-1 - Start*******")

    Filterchannels()
    
    SwitchingChannels_Revanth()
    
    Digit_Channel_Selection("Satellite",67)
    
    Guide_Launch_Exit()
    
    Digit_Channel_Selection("Satellite",70)
    
    PiP_Without_Standby()
    
    Switching_Tuner_Channels_Revanth()
    
    Ok_List_Nav_Satellite_Legacy()
    
    Digit_Channel_Selection("Tuner",83)

    Favourites()
    
    Guide_Nav()
    
    Zapping_Volume()
    
    Digit_Channel_Selection("Tuner",8)
    
    Favourites()
    
    Switching_Satellite_Channels_Revanth()
    
    Switch_BN_HDMI_Legacy()
    
    Channel_AudioLanguage_Revanth()
    
    Swtich_Sources_Revanth()
    
    PiP_Without_Standby()
    
    Digit_Channel_Selection("Satellite",77)
    
    Digit_Channel_Selection("Tuner",14)
    
    Random_Teletext_Zap(2)
    
    Channel_SubtitleChange_Revanth()

    Filterchannels()
    
    SwitchingChannels_Revanth()
    
    Digit_Channel_Selection("Tuner",21)
    
    Test_Function_Arun_Tuner_MHEG_Navigation_PLyaback_Without_Standby()
    
    PiP_Without_Standby()
    
    Volume_Controls()
    
    Ok_List_Nav_Tuner_Legacy()
    
    Switching_Satellite_Channels_Revanth()
        
    Guide_Tuning()
    
    Switch_BN_HDMI_Tuner_Legacy()

    Favourites()
    
    Swtich_Sources_Revanth()
    
    PiP_Without_Standby()

    Filterchannels()

    Guide_Nav()

    SwitchingChannels_Revanth()
    
    print ("*******Block-1 - End*******")
        
    
def Block2():

    print ("*******Block-2 - Start*******")
    print ("Block2 - HDMI_Revanth()")
    HDMI_Revanth()

    print("Block2 - HDMI()")
    HDMI()
    print("*******Block-2 - End*******")
    
def Block3():
    print ("*******Block-3 - Start*******")
    
    SwitchingChannels_Revanth()
    Switching_Satellite_Channels_Revanth()
    Swtich_Sources_Revanth()
    Switching_Tuner_Channels_Revanth()
    Switching_Satellite_Channels_Revanth()
    Swtich_Sources_Revanth()
    SwitchingChannels_Revanth()
        
    print ("*******Block-3 - End*******")
    
def Start_Script():
    Block3()
    Block2()
    Block1()
    
if __name__ == "__main__":    
    for count in range(0,1000):
        Start_Script()
