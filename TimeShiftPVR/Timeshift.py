# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:12:46 2020

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
                    sublist_temp =str(Channelnumber)
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

def TimeShift2():
    SendKey("Exit",4,1)
    SendKey("Pause",4,1)
    SendKey("Standby",15,1)
    SendKey("Exit",5,1)
    SendKey("Pause",5,1)
    SendKey("Standby",25,1)
    
    SendKey("Exit",4,1)
    SendKey("Pause",10,1)
    SendKey("Standby",5,1)
    SendKey("Exit",4,1)
    SendKey("Pause",8,1)
    SendKey("Standby",8,1)
    SendKey("Exit",18,1)
    SendKey("Pause",4,1)
    SendKey("Standby",5,1)
    SendKey("Exit",10,1)
    SendKey("Pause",25,1)
    SendKey("Standby",5,1)
    SendKey("Exit",4,1)
    
def TimeShift3():
    SendKey("Exit",4,1)
    SendKey("Pause",0.3,1)
    SendKey("Rewind",0.3,1)
    SendKey("Pause",0.3,1)
    SendKey("Standby",3,1)
    SendKey("Exit",3,1)
    SendKey("Pause",0.3,1)
    SendKey("Forward",0.3,1)
    SendKey("Pause",0.3,1)
    SendKey("Rewind",0.3,1)
    SendKey("Pause",0.3,1)
    SendKey("Standby",2.5,1)
    SendKey("Exit",1,2)
    SendKey("Forward",0.3,1)
    SendKey("Pause",0.3,1)
    SendKey("Rewind",0.3,1)
    SendKey("Standby",2.5,1)
    SendKey("Exit",1,2)
    SendKey("Rewind",0.3,1)
    SendKey("Standby",3,1)
    SendKey("Exit",3,1)
    for x in range(0,10):
        SendKey("Pause",0.3,1)
        SendKey("Play",0.3,1)
        
    
    
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
    
def PVRRecording_Playback_Revanth():
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
    time.sleep(18)
    SendKey("Standby")
    time.sleep(5)
    
    Switch_To_Recordings()
    SendKey("Up", 0.3,2)
    SendKey("Down", 0.3,3)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Play")

    Trick_List_Navigations_Fixed(Trick_List_1) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(50)
    SendKey("Standby")
    time.sleep(8)

    Switch_To_Recordings()
    SendKey("Up", 0.3,2)
    SendKey("Down", 0.3,4)
    SendKey("Ok")

    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Play")

    SendKey("Back")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(3)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Play")
    
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(3)

    Switch_To_Recordings()
    SendKey("Down")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Play")

    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(5)
    
    Switch_To_Recordings()
    SendKey("Down")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Stop")

    Switch_To_Recordings()
    SendKey("Ok")
    time.sleep(3)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Play")
    
    SendKey("Back")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(0.6)
    SendKey("Play")

    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(25)
    SendKey("Standby")
    time.sleep(9)

    Switch_To_Recordings()
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(0.6)
    SendKey("Play")

    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(7)
    
    Switch_To_Recordings()
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(0.6)
    SendKey("Play")
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(8)

def PVR_OTR():
    SendKey("Rec")
    time.sleep(15) # Perform Recording for 15 Seconds & then Put the Set to Standby Mode
    SendKey("Standby")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Stop")
    time.sleep(1)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    
    SendKey("Rec")
    time.sleep(15) # Perform Recording for 15 Seconds
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1) # Recording is Stopped

    SendKey("Rec")
    time.sleep(5) # Perform Recording for 5 Seconds & then Put the Set to Standby Mode
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Stop")
    time.sleep(1)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    
    SendKey("Rec")
    time.sleep(25) # Perform Recording for 25 Seconds
    SendKey("Stop")
    time.sleep(1)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1) # Recording is Stopped

    SendKey("Rec")
    time.sleep(10) # Perform Recording for 10 Seconds & then Put the Set to Standby Mode
    SendKey("Standby")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Stop")
    time.sleep(1)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")

    
def Script():
#81-86, 199,200, 219,220
    Digit_Channel_Selection("Satellite", 83)
    TimeShift3()
    TimeShift2()
    TimeShift_With_StandbyOperations_Revanth()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()

    Digit_Channel_Selection("Satellite", 219)
    TimeShift2()
    TimeShift3()
    TimeShift_With_StandbyOperations_Revanth()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()
    
    Digit_Channel_Selection("Satellite", 81)
    TimeShift3()
    TimeShift2()
    TimeShift_With_StandbyOperations_Revanth()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()
    
    Digit_Channel_Selection("Satellite", 200)
    TimeShift2()
    TimeShift_With_StandbyOperations_Revanth()
    TimeShift3()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()

    Digit_Channel_Selection("Satellite", 85)
    TimeShift2()
    TimeShift3()
    TimeShift_With_StandbyOperations_Revanth()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()

    Digit_Channel_Selection("Satellite", 199)
    TimeShift3()
    TimeShift2()
    TimeShift_With_StandbyOperations_Revanth()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()

    Digit_Channel_Selection("Satellite", 82)
    TimeShift2()
    TimeShift_With_StandbyOperations_Revanth()
    TimeShift3()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()

    Digit_Channel_Selection("Satellite", 86)
    TimeShift2()
    TimeShift3()
    TimeShift_With_StandbyOperations_Revanth()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()

    Digit_Channel_Selection("Satellite", 220)
    TimeShift3()
    TimeShift2()
    TimeShift_With_StandbyOperations_Revanth()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()

    Digit_Channel_Selection("Satellite", 84)
    TimeShift2()
    TimeShift3()
    TimeShift_With_StandbyOperations_Revanth()
    PVR_OTR()    
    PVRRecording_Playback_Revanth()
    
if __name__ == "__main__":
    for count in range(0,100000):
        Script()    
