'''
 ==========================================================================================================
                Initial-Conditions for DS-Zap-PVR-TimeShiftBuffer-TrickModes


 -----------------------------------------------------------------------------------
 Application Order in Apps Section - App Section will be seen on Long Menu Key Press
 -----------------------------------------------------------------------------------
 
 1. Youtube            2. App Gallery              3. OIB          4. How To
 5. Demo Me            6. Amazon Prime Video       7. ARD          8.ARTE
 9. ZDF                10. NPO                     11. Puhu        12. SVT
 13.Chili              14. Megogo                  15. MX Player   16. Google Play Movies
 17.Google Play Music  18. Media                   19. Watch TV    20. Amazon Alexa

 -----------------------------------------------------------------------------------------------------
 Games in Application Favourite List in Launcher --> In the Launcher Screen below is the Games Order
 -----------------------------------------------------------------------------------------------------
 1. Sky Force 2. PAC MAN 256
 
 -----------------------------------------------------------------------------------------------------
 Addition of OIB Pages in Internet Browser - Remove the 8 Default Browser Pages & Add the below 8
 -----------------------------------------------------------------------------------------------------
 1.	www.espncricinfo.com     2.	www.flashscores.co.uk       3.	www.dangelicoguitars.com     4.www.dearestnature.com
 5.	www.cricbuzz.com         6.	www.nasaprospect.com        7.	www.www.blueacorn.com        8.www.ndtv.com

 -----------------------------------------------------------------------------------
 Other Mandatory Pre-Conditions
 -----------------------------------------------------------------------------------
 1. HDD Should be Paired to the TV
 2. Check whether Timeshift & OTR Functionalities are working properly before the test
 3. Internet Connection Should be Successful - Wired/Wireless
 4. Ensure all Logins are Successful --> Google Login
    a. Google Login
    b. Netflix Login
    c. Amazon Prime Video Login
    d. Drop Box
    e. Rakuten Login
 5. Check Youtube Playback is Happening Properly
 6. Open all the 3rd Party Applications and give all the Permissions by Selecting Allow Button
 7. Connect all Possible Devices (If Available) to the TV
 8. Connect USB with Cookie File Present in it
 9. After Succesful Pairing of HDD, Remove the HDD , Copy some contents in to Folder '1' & Connect it back to TV
 10. USB should have Folder '0' with Contents in it
 11. Add Folders 1 from HDD in to Fav List & Later Add 0 Folder from USB Drive in to the Fav List
 ==========================================================================================================
''' 

import time
import random
import threading
#print time.time()
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
RedRat_Device_Name = "No name 18229"
RedRat_Device_Port = "1"

def SendKey(*args):
    if len(args) == 1:
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(args[0]) + "\"" + ' output=\"' + RedRat_Device_Port+"\"\'")
    elif len(args) == 2:
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(args[0]) + "\"" + ' output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(float(args[1]))
    elif len(args) == 3:
        for j in range(0,args[2]):
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

Apps_In_Row1 = [1,2,3,4]
Apps_In_Row2 = [5,6,7,8]
Apps_In_Row3 = [9,10,11,12]
Apps_In_Row4 = [13,14,15,16]
Apps_In_Row5 = [17,18,19,20]

def Random_longpress(Nav_Count):   
    for count in range(0,Nav_Count):
        Key_List = ["Right_longpress","Up_longpress","Down_longpress","Left_longpress"]
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + random.choice(Key_List) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(0.5)

def Random_Navigation(Nav_Count):
    for count in range(0,Nav_Count):
        Key_List = ["Right","Up","Down","Left"]
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + random.choice(Key_List) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(.3)

def Trick_List_Navigations_Fixed(Trick_List):
    Key_1stArg = 0
    SleepTime_2ndArg = 1
    for count in range(len(Trick_List)):
        SendKey(Trick_List[count][Key_1stArg], Trick_List[count][SleepTime_2ndArg])

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

def PVR_TimeShift_Legacy():
    for Test in range(0,1):

        TimeShift_Satellite()

        ## Perform Recording
        print ("Recording")
        for count in range(0,3):
            time.sleep(2)
            SendKey("Rec")
            time.sleep(15)
            SendKey("Stop")
            time.sleep(0.4)
            SendKey("Left")
            time.sleep(0.4)
            SendKey("Ok")
            time.sleep(2)

        time.sleep(2)
        SendKey("Rec")
        time.sleep(30)
        SendKey("Stop")
        time.sleep(0.4)
        SendKey("Left")
        time.sleep(0.4)
        SendKey("Ok")
        time.sleep(2)
        SendKey("Exit")
        time.sleep(2)

        ## Perform Recording - USB Playback
        SendKey("Rec")
        time.sleep(5)
        SendKey("Sources")
        time.sleep(4)
        SendKey("Up_longpress")
        time.sleep(0.4)
        SendKey("Down",0.3,5)
        SendKey("Ok",1,1)
        SendKey("Left",0.3,4)
        SendKey("Down_longpress")
        time.sleep(1)
        for count in range(0,2):
            SendKey("Up")
            time.sleep(0.25)    
        SendKey("Ok")
        time.sleep(1)        
        SendKey("Right")
        time.sleep(0.3)
        SendKey("Right")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(5)
        for count in range(0,3):
            SendKey("Forward")
            time.sleep(2)
        for count in range(0,1):
            SendKey("Play")
            time.sleep(3)
        for count in range(0,3):
            SendKey("Forward")
            time.sleep(2)
        for count in range(0,1):
            SendKey("Pause")
            time.sleep(2.5)
        for count in range(0,3):
            SendKey("Rewind")
            time.sleep(2)
        for count in range(0,1):
            SendKey("Play")
            time.sleep(1.5)
            
        SendKey("Exit")
        time.sleep(2)
        SendKey("Stop")
        time.sleep(0.4)
        SendKey("Left")
        time.sleep(0.4)
        SendKey("Ok")
        time.sleep(3)

        ## Perform Recording - Youtube Playback
        SendKey("Rec")
        time.sleep(5)
        SendKey("Home")
        time.sleep(4)
        SendKey("Up_longpress")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Back")
        time.sleep(0.25)
        SendKey("Left")
        time.sleep(0.25)
           
        SendKey("Left")
        time.sleep(0.25)
        SendKey("Down",0.3,6)
        SendKey("Up",0.3,2)
        SendKey("Down",0.3,4)
        SendKey("Right",0.3,1)
        SendKey("Ok")
        time.sleep(9)
        for count in range(0,3):
            SendKey("Forward")
            time.sleep(2)
        for count in range(0,1):
            SendKey("Play")
            time.sleep(3)
        for count in range(0,3):
            SendKey("Forward")
            time.sleep(2)
        for count in range(0,1):
            SendKey("Pause")
            time.sleep(2.5)
        for count in range(0,3):
            SendKey("Rewind")
            time.sleep(2)
        for count in range(0,1):
            SendKey("Play")
            time.sleep(1.5)

        SendKey("Exit")
        time.sleep(3)
        SendKey("Stop")
        time.sleep(0.4)
        SendKey("Left")
        time.sleep(0.4)
        SendKey("Ok")
        time.sleep(3)

        PVR_Satellite()

        for count in range(0,2):
            ## Timeshift and Trick Modes - USB Playback
            print ("Timeshift and Trick Modes - USB Playback")

            # Check here on which channel the TV will be in
            SendKey("Pause")
            time.sleep(90)

            for count in range(0,4):
                SendKey("Rewind")
                time.sleep(3)
                SendKey("Play")
                time.sleep(2)
                for count in range(0,4):
                    SendKey("Forward")
                    time.sleep(1)

            SendKey("Sources")
            time.sleep(4)
            SendKey("Up_longpress")
            time.sleep(0.4)
            for count in range(0,5):
                SendKey("Down")
                time.sleep(0.25)
            
            SendKey("Ok") # Enter in to Content Browser
            time.sleep(1)

            SendKey("Left",0.3,4)
            SendKey("Down_longpress")
            time.sleep(1)
            for count in range(0,2):
                SendKey("Up")
                time.sleep(0.25)    
            SendKey("Ok")
            time.sleep(1)        
            SendKey("Right")
            time.sleep(0.3)
            SendKey("Right")
            time.sleep(0.3)
            SendKey("Ok")
            time.sleep(5)
            for count in range(0,3):
                SendKey("Forward")
                time.sleep(2)
            for count in range(0,1):
                SendKey("Play")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Forward")
                time.sleep(2)
            for count in range(0,1):
                SendKey("Pause")
                time.sleep(2.5)
            for count in range(0,3):
                SendKey("Rewind")
                time.sleep(2)
            for count in range(0,1):
                SendKey("Play")
                time.sleep(1.5)
                
            SendKey("Exit")
            time.sleep(2)
            for count in range(0,5): 
                SendKey("Channel_Up")
                time.sleep(1)
                
        ## Perform Recording - Google Play Movies
        
        SendKey("Rec")
        time.sleep(5)
        SendKey("Home")
        time.sleep(4)
        SendKey("Up_longpress")
        time.sleep(0.3)
        SendKey("Back")
        time.sleep(0.25)
        SendKey("Left")
        time.sleep(0.25)
        for count in range(0,3):   
            SendKey("Right")
            time.sleep(0.25)
        SendKey("Ok")
        SendKey("Back",0.3,5)
        SendKey("Left",0.25,1)
        SendKey("Right", 0.25,3)
        SendKey("Ok")
        time.sleep(4)
        SendKey("Down", 0.25,2)
        SendKey("Right", 0.25,2)
        SendKey("Ok",2,1)
        SendKey("Ok",10,1)
        for count in range(0,3):
            SendKey("Forward")
            time.sleep(2)
        for count in range(0,1):
            SendKey("Play")
            time.sleep(3)
        for count in range(0,3):
            SendKey("Forward")
            time.sleep(2)
        for count in range(0,1):
            SendKey("Pause")
            time.sleep(2.5)
        for count in range(0,3):
            SendKey("Rewind")
            time.sleep(2)
        for count in range(0,1):
            SendKey("Play")
            time.sleep(1.5)

        SendKey("Exit")
        time.sleep(3)
        SendKey("Stop")
        time.sleep(0.4)
        SendKey("Left")
        time.sleep(0.4)
        SendKey("Ok")
        time.sleep(3)        

        PVR_Tuner()

        for count in range(0,1):
            ## Timeshift and Trick Modes - Internet Browser
            print ("Timeshift and Trick Modes - Internet Browser")
            
            SendKey("Pause")
            time.sleep(150)

            SendKey("Home")
            time.sleep(4)
            SendKey("Up_longpress")
            time.sleep(0.3)
            SendKey("Down")
            time.sleep(0.25)
            SendKey("Back")
            time.sleep(0.25)
            SendKey("Left")
            time.sleep(0.25)
            for count in range(0,4):   
                SendKey("Right")
                time.sleep(0.25)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,1):
                SendKey("Down")
                time.sleep(0.25)
            for count in range(0,3):
                SendKey("Right")
                time.sleep(0.2)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Down_longpress")
            time.sleep(0.4)
            SendKey("Ok")
            time.sleep(4)

            SendKey("Exit")
            time.sleep(3)

        TimeShift_Satellite()
 
        ## Perform Recording - Internet Browser
        SendKey("Rec")
        time.sleep(5)
        SendKey("Home")
        time.sleep(4)
        SendKey("Up_longpress")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Back")
        time.sleep(0.25)
        SendKey("Left")
        time.sleep(0.25)
        for count in range(0,4):   
            SendKey("Right")
            time.sleep(0.25)
        SendKey("Ok")
        time.sleep(4)
        for count in range(0,1):
            SendKey("Down")
            time.sleep(0.25)
        for count in range(0,3):
            SendKey("Right")
            time.sleep(0.2)
        SendKey("Ok")
        time.sleep(2)
        SendKey("Down_longpress")
        time.sleep(0.4)
        SendKey("Ok")
        time.sleep(4)

        SendKey("Exit")
        time.sleep(3)
        SendKey("Stop")
        time.sleep(0.4)
        SendKey("Left")
        time.sleep(0.4)
        SendKey("Ok")
        time.sleep(3)

        PVR_Satellite()

        for count in range(0,1):
            ## Timeshift and Trick Modes - Youtube Playback
            print ("Timeshift and Trick Modes - Youtube Playback")
            
            SendKey("Pause")
            time.sleep(30)

            SendKey("Home")
            time.sleep(4)
            SendKey("Up_longpress")
            time.sleep(0.3)
            SendKey("Down")
            time.sleep(0.25)
            SendKey("Back")
            time.sleep(0.25)
            SendKey("Left")
            time.sleep(0.25)
               
            SendKey("Right")
            time.sleep(0.25)
            SendKey("Ok")
            time.sleep(9)
            SendKey("Right")
            time.sleep(0.25)
            for count in range(0,5):
                SendKey("Down")
                time.sleep(0.2)
            SendKey("Ok")
            time.sleep(12)

            for count in range(0,3):
                SendKey("Forward")
                time.sleep(2)
            for count in range(0,1):
                SendKey("Play")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Forward")
                time.sleep(2)
            for count in range(0,1):
                SendKey("Pause")
                time.sleep(2.5)
            for count in range(0,3):
                SendKey("Rewind")
                time.sleep(2)
            for count in range(0,1):
                SendKey("Play")
                time.sleep(1.5)

            SendKey("Exit")
            time.sleep(3)
            
        ## Launch Sources and select Recordings playback - Perform Trick Modes on Recorded Content
        SendKey("Sources")
        time.sleep(4)
        for count in range(0,1):
            SendKey("Up_longpress")
            time.sleep(0.4)
        for count in range(0,7):
            SendKey("Down")
            time.sleep(0.2)
        SendKey("Ok")
        time.sleep(3)
        SendKey("Down")
        time.sleep(0.5)
        SendKey("Ok")
        time.sleep(4)
        
        for count in range(0,2):
            SendKey("Forward",2,2)
            SendKey("Rewind",2,1)
            for count in range(0,3):
                SendKey("Pause")
                time.sleep(1.5)
                SendKey("Play")
                time.sleep(1)
                SendKey("Forward",2,2)
                SendKey("Rewind",2,1)
        time.sleep(3)
        SendKey("Exit")
        time.sleep(2) 
        
       ## Tuning to Satellite Channels & Perform Zapping
        SendKey("Sources")
        time.sleep(4)
        for count in range(0,1):
            SendKey("Up_longpress")
            time.sleep(0.5)
        for count in range(0,2):
            SendKey("Down")
            time.sleep(0.3)
        SendKey("Ok")
        time.sleep(3)
        for count in range(0,10): 
            SendKey("Channel_Up")
            time.sleep(2)
        for count in range(0,5): 
            SendKey("Up")
            time.sleep(2.5)
        for count in range(0,8): 
            SendKey("Channel_Up")
            time.sleep(3)
        time.sleep(5)

        PVR_Tuner()

    ## Launch Sources and select Recordings playback - Perform Trick Modes on Recorded Content - Standby and Wakeup
        SendKey("Sources")
        time.sleep(4)
        for count in range(0,1):
            SendKey("Up_longpress")
            time.sleep(0.4)
        for count in range(0,7):
            SendKey("Down")
            time.sleep(0.2)
        SendKey("Ok")
        time.sleep(3)
        SendKey("Down")
        time.sleep(4)
        SendKey("Ok")
        time.sleep(4)
        
        for count in range(0,2):
            SendKey("Forward")
            time.sleep(3)
            SendKey("Rewind")
            time.sleep(2)
            for count in range(0,3):
                SendKey("Pause")
                time.sleep(1.5)
                SendKey("Play")
                time.sleep(1)
        time.sleep(3)
        SendKey("Standby")
        time.sleep(14)
        SendKey("Standby")
        time.sleep(5)

        PVR_Satellite()

     ## Tuning to Fav List of Channels
        SendKey("Sources")
        time.sleep(4)
        SendKey("Up_longpress")
        time.sleep(0.5)
        SendKey("Down",3,1)
        SendKey("Ok")
        time.sleep(3)
        SendKey("Channel_Up",1,15)
        time.sleep(3)
        for count in range(0,10):
            SendKey("Up")
            time.sleep(2)
        time.sleep(3)

        for count in range(0,10):
            SendKey("Channel_Up")
            time.sleep(2.5)
        time.sleep(3)

        SendKey("1")
        time.sleep(5)   
        
     ## Perform zapping and start time shift on different channels-repeat 5 times
        
        for count in range(0,5): 
            SendKey("Channel_Up")
            time.sleep(5)
            SendKey("Pause")
            time.sleep(250)
            for count in range(0,2):
                SendKey("Forward")
                time.sleep(2.5)
                SendKey("Rewind")
                time.sleep(4)
                for count in range(0,3):
                    SendKey("Pause")
                    time.sleep(2)
                    SendKey("Play")
                    time.sleep(3)
                    SendKey("Exit")
                    time.sleep(4)

        TimeShift_Satellite()
                    
     ## Perform zapping and Start recording on different channels & Perform Standby/Wakeup Scenario
        for count in range(0,2):
            SendKey("Channel_Down")
            time.sleep(3)
            SendKey("Rec")
            time.sleep(10)
            SendKey("Standby")
            time.sleep(8)
            SendKey("Standby")
            time.sleep(8)
            
            SendKey("Stop")
            time.sleep(0.5)
            SendKey("Left")
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(3)

        for count in range(0,3):
            SendKey("Channel_Down")
            time.sleep(3)
            SendKey("Rec")
            time.sleep(25)
            SendKey("Standby")
            time.sleep(12)
            SendKey("Standby")
            time.sleep(10)
            
            SendKey("Stop")
            time.sleep(0.5)
            SendKey("Left")
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(3)

        PVR_Tuner()

    ## Navigating inside Recordings Manager - Play from Info
        SendKey("Sources")
        time.sleep(4)
        for count in range(0,1):
            SendKey("Up_longpress")
            time.sleep(0.5)
        for count in range(0,7):
            SendKey("Down")
            time.sleep(0.25)
        SendKey("Ok")
        time.sleep(3)
        
        for count in range(0,1): 
            SendKey("Up_longpress")
            time.sleep(0.5)
        for count in range(0,1): 
            SendKey("Left_longpress")
            time.sleep(0.5)
        SendKey("Right")
        time.sleep(0.5)    
        for count in range(0,1): 
            SendKey("Down_longpress")
            time.sleep(0.5)
        SendKey("Up_longpress")
        time.sleep(0.5)
        SendKey("Down_longpress")
        time.sleep(0.5)
        SendKey("Up_longpress")
        time.sleep(0.5)

        for count in range(0,4):
            SendKey("Down")
            time.sleep(1)
        SendKey("Info")
        time.sleep(2)
        SendKey("Green")
        time.sleep(10)
        SendKey("Stop")
        time.sleep(2)
        
        for count in range(0,7):
            SendKey("Down")
            time.sleep(1)
            SendKey("Info")
            time.sleep(3)
            SendKey("Green")
            time.sleep(10)
            SendKey("Stop")
            time.sleep(2)

        TimeShift_Satellite()

    ## Perform OTR & Perform Standby/Wakeup Scenario
        SendKey("Rec")
        time.sleep(10)
        SendKey("Standby")
        time.sleep(8)
        SendKey("Standby")
        time.sleep(8)
        SendKey("Standby")
        time.sleep(2)
        SendKey("Standby")
        time.sleep(3)
        SendKey("Standby")
        time.sleep(6)
        SendKey("Standby")
        time.sleep(15)
        SendKey("Standby")
        time.sleep(1)
        SendKey("Standby")
        time.sleep(1)
        SendKey("Standby")
        time.sleep(25)
        SendKey("Standby")
        time.sleep(8)
        
        SendKey("Stop")
        time.sleep(0.5)
        SendKey("Left")
        time.sleep(0.5)
        SendKey("Ok")
        time.sleep(3)        
        
    ## Navigating inside Recordings Manager
        SendKey("Sources")
        time.sleep(4)
        SendKey("Up_longpress",0.5,1)
        SendKey("Down",0.25,7)
        SendKey("Ok")
        time.sleep(3)
        for count in range(0,1): 
            SendKey("Up_longpress")
            time.sleep(0.5)
        for count in range(0,1): 
            SendKey("Left_longpress")
            time.sleep(0.5)
        SendKey("Right")
        time.sleep(0.5)    
        for count in range(0,1): 
            SendKey("Down_longpress")
            time.sleep(0.5)
        SendKey("Up_longpress")
        time.sleep(0.5)
        SendKey("Down_longpress")
        time.sleep(0.5)
        SendKey("Up_longpress")
        time.sleep(0.5)
        
        SendKey("Blue")
        time.sleep(5)
        SendKey("Right_longpress")
        time.sleep(0.5)
        SendKey("Down_longpress")
        time.sleep(0.5)
        SendKey("Back")
        time.sleep(0.5)
        for count in range(0,4):
            SendKey("Red")
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(0.5)
    
    ## Navigation in TV Guide - Go to Recordings Manager - Play the Recordings
        SendKey("TVGuide")
        time.sleep(5)
        for count in range(0,1):
            SendKey("Right_longpress")
            time.sleep(0.5)
        SendKey("Green")

        SendKey("Up_longpress")
        time.sleep(0.5)
        SendKey("Down_longpress")
        time.sleep(0.5)
        SendKey("Up_longpress")
        time.sleep(0.5)

        for count in range(0,3):
            SendKey("Down")
            time.sleep(1)
        SendKey("Green")
        time.sleep(10)
        SendKey("Stop")
        time.sleep(2)
        
        for count in range(0,3):
            SendKey("Down")
            time.sleep(1)
            SendKey("Info")
            time.sleep(3)
            SendKey("Green")
            time.sleep(10)
            SendKey("Stop")
            time.sleep(2)

        PVR_Satellite()

def PVR_Satellite():
    Switch_To_Satellite()
    SendKey("8")
    time.sleep(0.1)
    SendKey("3")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(6)

    SendKey("Pause")
    time.sleep(15)
    SendKey("Rewind")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(8)
    
    SendKey("Pause")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(4)
   
    SendKey("9")
    time.sleep(0.1)
    SendKey("3")
    time.sleep(5)
    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Pause")
    time.sleep(20)
    SendKey("Forward")
    time.sleep(7)
    SendKey("Standby")
    time.sleep(40)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Exit")
    time.sleep(2)

    SendKey("Pause")
    time.sleep(15)
    SendKey("Rewind")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(4)

    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(5)

    SendKey("Rec")
    time.sleep(40)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    
    SendKey("Pause")
    time.sleep(25)
    SendKey("Forward")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(7)

    SendKey("Pause")
    time.sleep(15)
    SendKey("Rewind")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(5)

    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(5)
    SendKey("Rec")
    time.sleep(30)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)

    SendKey("Pause")
    time.sleep(20)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Exit")
    time.sleep(4)

def PVR_Tuner():
    Switch_To_Tuner()
    SendKey("4")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(25)
    SendKey("Rewind")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Standby")
    time.sleep(4)
    
    SendKey("Pause")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(4)
   
    SendKey("1")
    time.sleep(0.1)
    SendKey("0")
    time.sleep(5)
    SendKey("Rec")
    time.sleep(25)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Pause")
    time.sleep(8)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(25)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Exit")
    time.sleep(2)

    SendKey("Pause")
    time.sleep(30)
    SendKey("Rewind")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(4)

    SendKey("Pause")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(12)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Exit")
    time.sleep(3)

    SendKey("2")
    time.sleep(0.1)
    SendKey("0")
    time.sleep(5)

    SendKey("Rec")
    time.sleep(40)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(7)
    SendKey("Standby")
    time.sleep(40)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(20)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Standby")
    time.sleep(7)

    SendKey("7")
    time.sleep(8)
    SendKey("Rec")
    time.sleep(15)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)

    SendKey("Pause")
    time.sleep(15)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(18)
    SendKey("Exit")
    time.sleep(4)

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

def TimeShift_With_StandbyOperations():
    print ("TimeShift_With_StandbyOperations()- Start of the Function")
    Trick_List_Navigations_Fixed(Trick_List_5) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)

    Trick_List_Navigations_Fixed(Trick_List_1) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(50)
    SendKey("Standby")
    time.sleep(6)

    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(3)

    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(3)

    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(90)
    SendKey("Standby")
    time.sleep(7)

    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(70)
    SendKey("Standby")
    time.sleep(8)

    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(5)

def TimeShift_With_StandbyOperations_Legacy():
    SendKey("Pause")
    time.sleep(8)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(5)
    SendKey("Play")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(7)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(16)
    SendKey("Standby")
    time.sleep(6)

    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward",2,4)
    SendKey("Standby")
    time.sleep(90)
    SendKey("Standby")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(5)
    SendKey("Rewind",3,3)
    SendKey("Standby")
    time.sleep(65)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(6)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(45)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    
    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(60)
    SendKey("Standby")
    time.sleep(10)

def TimeShift_With_StandbyOperations_MultipleChannels_Tuner():
    Switch_To_Tuner()

    # 213 - Test UHD 1 Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(0.1)
    SendKey("3")
    time.sleep(4)
    
    Trick_List_Navigations_Fixed(Trick_List_5) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)

    Trick_List_Navigations_Fixed(Trick_List_1) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(50)
    SendKey("Standby")
    time.sleep(6)

    # 205 - ZDF Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(0.1)
    SendKey("9")
    time.sleep(4)
    
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(16)
    SendKey("Standby")
    time.sleep(3)

    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(3)

    # 215 - Test UHD 3 Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(4)
    
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(25)
    SendKey("Standby")
    time.sleep(9)

    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(90)
    SendKey("Standby")
    time.sleep(7)

    # 228 - ITV1 HD Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("2")
    time.sleep(0.1)
    SendKey("8")
    time.sleep(4)
    
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(70)
    SendKey("Standby")
    time.sleep(8)

    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(5)

    # 206 - 1440*1080i Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(0.1)
    SendKey("6")
    time.sleep(4)
    
    SendKey("Pause")
    time.sleep(8)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(5)
    SendKey("Play")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(7)

    # 210 - H264 1920 1080i Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(0.1)
    SendKey("0")
    time.sleep(4)
    
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

    # 203 - Eins Plus Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(0.1)
    SendKey("3")
    time.sleep(4)
    
    SendKey("Pause")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(16)
    SendKey("Standby")
    time.sleep(6)

    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward",2,4)
    SendKey("Standby")
    time.sleep(90)
    SendKey("Standby")
    time.sleep(10)

    # 219 - BBC ONE HD Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(0.1)
    SendKey("9")
    time.sleep(4)
    
    SendKey("Pause")
    time.sleep(5)
    SendKey("Rewind",3,3)
    SendKey("Standby")
    time.sleep(65)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(6)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(45)
    SendKey("Standby")
    time.sleep(5)

    # 214 - Test UHD 2 Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(0.1)
    SendKey("4")
    time.sleep(4)
    
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    
    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(60)
    SendKey("Standby")
    time.sleep(10)

def TimeShift_With_StandbyOperations_MultipleChannels_Satellite():
    Switch_To_Satellite()
    
    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(60)
    
    Trick_List_Navigations_Fixed(Trick_List_5) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)

    Trick_List_Navigations_Fixed(Trick_List_1) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(50)
    SendKey("Standby")
    time.sleep(6)

    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(16)
    SendKey("Standby")
    time.sleep(3)

    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(3)

    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(25)
    SendKey("Standby")
    time.sleep(9)

    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(90)
    SendKey("Standby")
    time.sleep(7)

    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(70)
    SendKey("Standby")
    time.sleep(8)

    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(8)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(5)
    SendKey("Play")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(7)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(16)
    SendKey("Standby")
    time.sleep(6)

    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward",2,4)
    SendKey("Standby")
    time.sleep(90)
    SendKey("Standby")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(5)
    SendKey("Rewind",3,3)
    SendKey("Standby")
    time.sleep(65)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(6)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(45)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    
    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(60)
    SendKey("Standby")
    time.sleep(10)
    
def PVR_With_StandbyOperations():

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

    SendKey("9")
    time.sleep(5)
    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(14)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)


    SendKey("1")
    time.sleep(0.1)
    SendKey("9")
    time.sleep(5)

    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(15)
    SendKey("Forward")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

    SendKey("2")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(5)
    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)


##------------------------------------- REVANTH -------------------------------------


#def TimeShift_With_StandbyOperations_MultipleChannels_Satellite():
#    Switch_To_Satellite()
#
#    # 71 - Test UHD 1 Channel in Satellite - Germany
#    SendKey("7")
#    time.sleep(0.3)
#    SendKey("1")
#    time.sleep(4)
#    
#    Trick_List_Navigations_Fixed(Trick_List_5) # At the End of this Trick List, This will be in Forward Trick
#    SendKey("Standby")
#    time.sleep(5)
#    SendKey("Standby")
#    time.sleep(5)
#
#    Trick_List_Navigations_Fixed(Trick_List_1) # At the End of this Trick List, This will be in Forward Trick
#    SendKey("Standby")
#    time.sleep(18)
#    SendKey("Standby")
#    time.sleep(6)
#
#    #06 - Arte HD in Satellite - Germany
#    SendKey("0")
#    time.sleep(0.1)
#    SendKey("6")
#    time.sleep(4)
#
#    SendKey("Red")
#    time.sleep(6)
#    SendKey("Down",0.3,2)
#    time.sleep(9)
#    
#    Trick_List_Navigations_Fixed(Trick_List_2)
#    SendKey("Standby")
#    time.sleep(16)
#    SendKey("Standby")
#    time.sleep(3)
#
#    Trick_List_Navigations_Fixed(Trick_List_3)
#    SendKey("Standby")
#    time.sleep(3)
#    SendKey("Standby")
#    time.sleep(3)
#
#    # 75 - Test UHD 3 Channel in Satellite - Germany
#    SendKey("7")
#    time.sleep(0.3)
#    SendKey("5")
#    time.sleep(4)
#    
#    Trick_List_Navigations_Fixed(Trick_List_4)
#    SendKey("Standby")
#    time.sleep(25)
#    SendKey("Standby")
#    time.sleep(9)
#
#    Trick_List_Navigations_Fixed(Trick_List_5)
#    SendKey("Standby")
#    time.sleep(90)
#    SendKey("Standby")
#    time.sleep(7)
#
#    # 88 - UHD Channel in Satellite - Germany
#    SendKey("8")
#    time.sleep(0.3)
#    SendKey("8")
#    time.sleep(4)
#    
#    Trick_List_Navigations_Fixed(Trick_List_4)
#    SendKey("Standby")
#    time.sleep(70)
#    SendKey("Standby")
#    time.sleep(8)
#
#    Trick_List_Navigations_Fixed(Trick_List_1)
#    SendKey("Standby")
#    time.sleep(6)
#    SendKey("Standby")
#    time.sleep(5)
#
#    # 33 - Dolby Labs Test Stream Channel in Satellite - Germany
#    SendKey("3")
#    time.sleep(0.3)
#    SendKey("3")
#    time.sleep(4)
#    
#    SendKey("Pause")
#    time.sleep(8)
#    SendKey("Rewind")
#    time.sleep(5)
#    SendKey("Standby")
#    time.sleep(10)
#    SendKey("Standby")
#    time.sleep(5)
#
#    SendKey("Pause")
#    time.sleep(5)
#    SendKey("Play")
#    time.sleep(1)
#    SendKey("Standby")
#    time.sleep(15)
#    SendKey("Standby")
#    time.sleep(7)
#
#    # 62 - SES UHD Demo Channel in Satellite - Germany
#    SendKey("6")
#    time.sleep(0.3)
#    SendKey("2")
#    time.sleep(0.1)
#    
#    SendKey("Pause")
#    time.sleep(10)
#    SendKey("Forward")
#    time.sleep(4)
#    SendKey("Standby")
#    time.sleep(5)
#    SendKey("Standby")
#    time.sleep(4)
#
#    SendKey("Pause")
#    time.sleep(10)
#    SendKey("Rewind")
#    time.sleep(5)
#    SendKey("Standby")
#    time.sleep(10)
#    SendKey("Standby")
#    time.sleep(5)
#
#    # 68 - SWR RP HD Channel in Satellite - Germany
#    SendKey("6")
#    time.sleep(0.3)
#    SendKey("8")
#    time.sleep(4)
#    
#    SendKey("Pause")
#    time.sleep(5)
#    SendKey("Standby")
#    time.sleep(16)
#    SendKey("Standby")
#    time.sleep(6)
#
#    SendKey("Pause")
#    time.sleep(2)
#    SendKey("Forward",2,4)
#    SendKey("Standby")
#    time.sleep(90)
#    SendKey("Standby")
#    time.sleep(10)

def PVR_OTR_15():
    SendKey("Rec")
    time.sleep(15) # Perform Recording for 15 Seconds
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1) # Recording is Stopped

def PVR_OTR_25():
    SendKey("Rec")
    time.sleep(25) # Perform Recording for 25 Seconds
    SendKey("Stop")
    time.sleep(1)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1) # Recording is Stopped

def PVR_OTR_Standby_10():
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
    
def PVR_OTR_Standby_20():
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

def PVR_OTR_Standby_30():
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
       
def PVR_With_StandbyOperations_MultipleChannelesTuner():
    Switch_To_Tuner()
    # 213 - Test UHD 1 Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(0.1)
    SendKey("3")
    time.sleep(4)

    time.sleep(5)
    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(14)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

        #3
    
    SendKey("0")
    time.sleep(0.3)
    SendKey("3")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(8)

    # 205 - ZDF Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(4)

    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(15)
    SendKey("Forward")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)
     #4
    SendKey("0")
    time.sleep(0.3)
    SendKey("4")
    time.sleep(3)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(40)
    SendKey("Red")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(9)
    SendKey("Standby")
    time.sleep(7)

     # 215 - Test UHD 3 Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(4)
    
    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

     #8
    
    SendKey("0")
    time.sleep(0.3)
    SendKey("8")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(15)



 # 219 - BBC ONE HD Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(0.1)
    SendKey("9")
    time.sleep(4)
    
    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

        #11
    SendKey("1")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(3)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(30)
    SendKey("Red")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(11)
    SendKey("Standby")
    time.sleep(8)

       # 206 - 1440*1080i Channel in Tuner - Germany
    SendKey("2")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(0.1)
    SendKey("6")
    time.sleep(4)

    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

        #20
    
    SendKey("2")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(14)
    SendKey("Standby")
    time.sleep(11)


def PVR_With_StandbyOperations_Multiplechannelsstatellte():
    Switch_To_Satellite()

    # 71 - Test UHD 1 Channel in Satellite - Germany
    SendKey("9")
    time.sleep(0.3)
    SendKey("4")
    time.sleep(4)

    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(14)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

    #91
    
    SendKey("8")
    time.sleep(0.3)
    SendKey("3")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Stop")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(2)
    

       #06 - Arte HD in Satellite - Germany
    SendKey("9")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(14)

    SendKey("Red")
    time.sleep(6)
    SendKey("Down",0.3,2)
    time.sleep(9)

    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(15)
    SendKey("Forward")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

    #101
    SendKey("1")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(3)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(40)
    SendKey("Red")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(9)
    SendKey("Standby")
    time.sleep(7)

    
    # 75 - Test UHD 3 Channel in Satellite - Germany
    SendKey("8")
    time.sleep(0.3)
    SendKey("6")
    time.sleep(4)

    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)
    
    #115
    
    SendKey("1")
    time.sleep(0.3)
    SendKey("5")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(4)
    SendKey("Info")
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Stop")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(2)



    # 88 - UHD Channel in Satellite - Germany
    SendKey("8")
    time.sleep(0.3)
    SendKey("5")
    time.sleep(4)

    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

    #121
    SendKey("1")
    time.sleep(0.3)
    SendKey("2")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(3)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(30)
    SendKey("Red")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(11)
    SendKey("Standby")
    time.sleep(8)

    
    # 33 - Dolby Labs Test Stream Channel in Satellite - Germany
    SendKey("1")
    time.sleep(0.3)
    SendKey("4")
    time.sleep(0.3)
    SendKey("5")
    time.sleep(4)

    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(2)
    SendKey("Left")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Exit")
    time.sleep(5)

    #168
    
    SendKey("1")
    time.sleep(0.3)
    SendKey("5")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(14)
    SendKey("Standby")
    time.sleep(11)
    SendKey("Stop")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(2)

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

def TimeShift_With_StandbyOperations_Naveen():
    print ("TimeShift_With_StandbyOperations()- Start of the Function")
    SendKey("Pause")
    time.sleep(10)
    Trick_List_Navigations_Fixed(Trick_List_5) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(70)
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
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(3)

    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(3)

    SendKey("Pause")
    time.sleep(15)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(90)
    SendKey("Standby")
    time.sleep(10)

    SendKey("Pause")
    time.sleep(10)
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

def PVRRecording_Playback():
    Switch_To_Recordings()
    SendKey("Up", 0.3,2)
    SendKey("Down", 0.3,2)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1)
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
    time.sleep(8)
    SendKey("Standby")
    time.sleep(3)
    
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
    time.sleep(90)
    SendKey("Standby")
    time.sleep(10)

Youtube_List = [[0,0], [1,0], [2,0], [0,1], [1,1]]
## stabmsafp1 , abc12345@
## 1stArgument : Right Count, 2nd Argument : Down Count
## [0,0] - Video 1, [1,0] - Video 2, [2,0] - Video 3, [0,1] - Video 4, [1,1] - Video 5 from the Youtube Fav List Created
## 0,0 -- 1st Row, 1st Video
## 1,0 -- 1st Row, 2nd Video
## 2,0 -- 1st Row, 3rd Video
## 0,1 -- 2nd Row, 1st Video
## 1,1 -- 2nd Row, 2nd Video

def Youtube_Row1_New():
    print ("Youtube Application Launching, Playback, Trick Modes")
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
    print ("Youtube Application Launching, Playback, Trick Modes")
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

def Youtube_Row1_Standby_Wakeup_New():
    print ("Youtube Application Launching, Playback, Trick Modes")
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
        SendKey('Standby',15,1)
        SendKey('Standby',5,1)
        SendKey("Play", 1, 1)
        time.sleep(5)
        SendKey("Back", 1, 1)
        SendKey("Right", 0.5, 1)

def Youtube_Row2_Standby_Wakeup_New():
    print ("Youtube Application Launching, Playback, Trick Modes")
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
        SendKey('Standby',6,1)
        SendKey('Standby',5,1)
        SendKey("Play", 1, 1)
        time.sleep(5)
        SendKey("Back", 1, 1)
        SendKey("Right", 0.5, 1)

#NOTE: If VLC is installed in TV please make 6 down in line number 4
#            Folder can be 0 or 1
#            FileNo can be 1-5
#            FileNo1 can be 1-5
# HDD should have Folder '1' with Contents in it
# USB should have Folder '0' with Contents in it
# Add Folders 1 from HDD in to Fav List & Later Add 0 Folder from USB Drive in to the Fav List

def CBPlayback_Revanth(folder,fileNo,fileNo1):
    SendKey('Sources',3,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down',0.3,7)
    SendKey('Up',0.7,2)
    SendKey('Ok',1,1) # Select the Folders in Fav List - Focus is on the 1st Folder --> This is 0 from USB
    if folder==0:
        #print("CB_PlayBack-Favorites-0-folder")
        SendKey('Ok',1,1)
        SendKey('Down',0.5,fileNo-1)
        SendKey('Ok',0.5,2)
        SendKey("Play",10,1)
        Trick_List_Navigations_Fixed(Trick_List_5)
        Trick_List_Navigations_Fixed(Trick_List_4)
        Trick_List_Navigations_Fixed(Trick_List_1)

    if folder==1:                # Select the 2nd Folder i.e. '1' which is from HDD
        #print("CB_PlayBack-Favorites-1-folder")
##        SendKey('Back',0.4,2)
##        SendKey('Left',0.4,1)
        SendKey('Down',0.4,1)
        SendKey('Right',0.4,1)
        SendKey('Down',0.5,fileNo-1)
        SendKey('Ok',0.5,2)
        SendKey("Play",10,1)
        Trick_List_Navigations_Fixed(Trick_List_4)
        Trick_List_Navigations_Fixed(Trick_List_5)   
        Trick_List_Navigations_Fixed(Trick_List_1)
        
    #print("CB_PlayBack-USB/HDD-Videos")
    SendKey("Back",0.3,3)
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
    Trick_List_Navigations_Fixed(Trick_List_4)
    Trick_List_Navigations_Fixed(Trick_List_1)
    
def Netflix_New(number):
    SendKey('Netflix',5,1)
    SendKey('Ok',1,1)
    SendKey('Back',1,4)
    SendKey('Left',1,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',1,3)
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
    SendKey('Exit',1,2)

def HbbTV_New():
    SendKey("Sources")
    time.sleep(4)
    SendKey("Up_longpress")
    time.sleep(0.5)
    for count in range(0,2):
        SendKey("Down")
        time.sleep(2)

    SendKey("Ok")
    time.sleep(3)
    
    SendKey('Exit',3,2)
    SendKey('Channel_Up',1,4)
    Noofrights=random.choice([1,2,3,4])
    SendKey('9',0.1,1)
    SendKey('1',7,1)
    SendKey('Red',5,1)
    SendKey('Ok',5,1)
    SendKey('Up',1,1)
    SendKey('Right',1,Noofrights)
    SendKey('Ok',2,1)
    SendKey('Down',2,1)
    SendKey('Ok',20,1)
    SendKey('Standby',8,2)
    
    SendKey('Red',5,1)
    SendKey('Ok',5,1)
    SendKey('Up',1,1)
    SendKey('Right',1,Noofrights)
    
    SendKey('Ok',2,1)
    SendKey('Down',2,1)
    SendKey('Ok',20,1)
    SendKey('Back',1,2)
    
    SendKey('Right',2,Noofrights)
    SendKey('Ok',10,1)
    SendKey('Exit',3,1)
    SendKey('Red',4,1)
    
    Noofdowns=random.choice([1,2,3,4])
    
    SendKey('Down',0.5,Noofdowns)
    SendKey('Ok',10,1)
    SendKey('Exit',3,2)
    SendKey('Blue',15,1)
    SendKey('Down',1,3)
    SendKey('Ok',2,1)
    SendKey('Right',0.5,Noofrights)
    SendKey('Ok',5,3)

def Hbbtv_Text():
    SendKey("Sources")
    time.sleep(4)
    SendKey("Up_longpress")
    time.sleep(0.5)
    for count in range(2):
        SendKey("Down")
        time.sleep(2)
    SendKey("Ok")
    time.sleep(3)
    SendKey('Exit',3,2)
    SendKey('Channel_Up',1,4)
    SendKey('9',0.2,1)
    SendKey('1',7,1)
    SendKey('Text',5,1)
    Randomnumber=random.randint(1,15)
    print (Randomnumber)
    SendKey('Down',0.5,Randomnumber)
    SendKey('Ok',2,1)
    SendKey('Up',1,5)
    SendKey('Down',1,7)
    SendKey('Right',1,1)
    SendKey('Down',1,1)
    SendKey('Ok',1,10)
    SendKey('Red',2,1)
    SendKey('Text',2,10)
    SendKey('Up_longpress',1,Randomnumber)
    SendKey('Down_longpress',1,Randomnumber)
    SendKey('Exit',3,1)
    SendKey('Red',3,1)
    SendKey('Right',1,3)
    SendKey('Ok',2,2)
    SendKey('Back',1,1)
    SendKey('0',3,1)
    SendKey('Green',5,1)
    SendKey('Right',1,Randomnumber)
    SendKey('Ok',1,1)

def Amazon_New(VideoNo):
    Home_Positioning_Launch_App(12)
    time.sleep(30)

    SendKey('Right',1,5) # If we give 6 Rights, then My List will be seen. If we give 5 Right, It will take to Video Library
    SendKey('Ok',3,1)
    SendKey('Right',2,VideoNo-1)
    SendKey('Ok',7,1)
    SendKey('Ok',5,1)
    SendKey('Left',0.2,4)
    SendKey('Ok',1,1) #Playback starts
    Trick_List_Navigations_Fixed(Trick_List_5)

def How_To_App():
    ## DS-SmartTVApps - Invoke How To Application - Navigations inside it
    print ("DS-SmartTVApps - Invoke How To Application - Navigations inside it")

    Home_Positioning_Launch_App(5)
        
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

def DemoMe_App(client,RedRat_Device_Name,RedRat_Device_Port):
    print ("DS-SmartTVApps - Invoke Demo Me. Launching and Exiting")
    Home_Positioning_Launch_App(6)
    
    SendKey("Down",0.2,1)
    SendKey("Right",0.2,2)
    SendKey("Ok",5,1)

    SendKey("Exit")
    time.sleep(2)

    SendKey("Home")
    time.sleep(2)
    SendKey("Ok")
    time.sleep(2)
    
    SendKey("Down",0.2,4)
    SendKey("Ok",0.5,1)

    SendKey("Exit")
    time.sleep(2)

    for count in range(0,6):
        SendKey("Home")
        time.sleep(4)
        SendKey("Ok")
        time.sleep(1.5)
        SendKey("Down")
        time.sleep(0.2)
        SendKey("Right")
        time.sleep(0.2)
        SendKey("Right")
        time.sleep(0.2)
        SendKey("Ok")
        time.sleep(10)
        SendKey("Exit")
        time.sleep(2)

    for count in range(0,6):
        SendKey("Home")
        time.sleep(3.5)
        SendKey("Ok")
        time.sleep(2)
        SendKey("Down")
        time.sleep(0.2)
        SendKey("Down")
        time.sleep(0.2)
        SendKey("Down")
        time.sleep(0.2)
        SendKey("Down")
        time.sleep(0.2)
        SendKey("Ok")
        time.sleep(4)
        SendKey("Exit")
        time.sleep(2)
        
def OIB():
    print ("OIB")
    
    Home_Positioning_Launch_App(4)
    
    print ("OIB-1st row - Start")
    Right_Count = 0
    for count in range(0,4):
        for count1 in range(0,Right_Count):
            print (Right_Count)
            
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
        
    print ("OIB-1st row - End")
    
    print ("OIB-2nd row - Start")
    Right_Count = 0
    for count in range(0,4):
        SendKey("Down",0.5,1)
        for count1 in range(0,Right_Count):
            print (Right_Count)
            
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
        
    print ("OIB-2nd row - End")
    SendKey("Exit",0.5,1)

def Megogo_Revanth():
    Home_Positioning_Launch_App(13)
    time.sleep(60)
    SendKey("Right",0.5,2)
    SendKey("Ok",2,1)
    SendKey("Up",0.7,1)
    SendKey("Right",2,1)
    SendKey("Ok",0.8,1)
    SendKey("Down",0.8,2)
    for count in range(0,4):
        SendKey("Ok",2,1)
        SendKey("Ok",20,1)
        Trick_List_Navigations_Fixed(Trick_List_5)
        Trick_List_Navigations_Fixed(Trick_List_1)
        SendKey("Back",1.5,2)
        SendKey("Right",0.7,1)

def NPO_Revanth():
    Home_Positioning_Launch_App(14)
    time.sleep(20)
    
    SendKey("Down",1,2)
    SendKey("Ok",0.5,1)
    for count in range(0,3):
        SendKey("Ok",30,1)
        Trick_List_Navigations_Fixed(Trick_List_4)
        SendKey("Back",0.7,3)
        SendKey("Down",0.7,2)
    
def SVT_Revanth():
    Home_Positioning_Launch_App(15)
    SendKey("Ok",1,1)
    SendKey("Down",1.2,2)
    for count in range(0,3):
        SendKey("Ok",1,1)
        SendKey("Ok",30,1)
        Trick_List_Navigations_Fixed(Trick_List_5)
        SendKey("Back",0.5,2)
        SendKey("Right",0.7,1)

def Puhu_Revanth():
    Home_Positioning_Launch_App(16)
    time.sleep(30)
    SendKey("Down",0.6,2)
    SendKey("Ok",0.8,2)
    for count in range(0,3):
        SendKey("Ok",1,2)
        SendKey("Play",2,5)
        SendKey("Play",60,1)
        Trick_List_Navigations_Fixed(Trick_List_2)
        Trick_List_Navigations_Fixed(Trick_List_4)
        SendKey("Back",1,2)

def SkyForce_Revanth():
    Home_Positioning_Launch_App(17)
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

def Pacman_Revanth():
    Home_Positioning_Launch_App(18)
    time.sleep(20)
    SendKey("Ok",1,10)
    for count in range(0,4):
        SendKey("Up",0.5,1)
        SendKey("Right",0.4,1)
        SendKey("Up",0.4,1)
        SendKey("Left",0.4,1)
    SendKey("Ok",0.6,5)
    SendKey("Exit",2,1)

def Arte_Revanth():
    Home_Positioning_Launch_App(11)
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

def ARD_Revanth():
    Home_Positioning_Launch_App(16)
    time.sleep(4)
    Random_longpress(10)
    Random_Navigation(15)
    SendKey("Up_longpress",0.5,2) 

    for count in range(1,4):
        SendKey("Up",0.3,2)      
        SendKey("Right",0.8,count)
        SendKey("Ok",0.8,1)
        SendKey("Down",0.6,1)
        SendKey("Ok",0.9,3)
        time.sleep(20)
        Trick_List_Navigations_Fixed(Trick_List_5)
        SendKey("Back",0.8,2)

def Zdf_Revanth():
    Home_Positioning_Launch_App(17)
    Random_longpress(10)
    Random_Navigation(15)

    SendKey("Up_longpress",0.5,2)
    SendKey("Down",0.7,3)
    SendKey("Right",0.7,1)
    SendKey("Down",0.7,1)
    for count in range(0,2):
        SendKey("Ok",20,1)
        Trick_List_Navigations_Fixed(Trick_List_5)
        SendKey("Back",1,1)
        SendKey("Down",0.7,1)

def GoogleAssistant_Revanth():    
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.7,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",4,1)
    for count in range(0,5):
        SendKey("Down",0.6,1)
        SendKey("Ok",6,1)

    SendKey("Home",4,1)
    SendKey("Up_longpress",0.7,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down",0.5,1)
    SendKey("Right",0.6,2)
    for count in range(0,4):
        SendKey("Down",0.5,1)
        SendKey("Right",0.6,count)
        SendKey("Ok",7,1)

    # Back to Back Voice Search Operations
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.5,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down",0.5,1)
    #SendKey("Right",0.6,2)
    SendKey("Ok",1,1)
    for count in range(0,4):
        SendKey("Home",3.5,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",4,1)
        SendKey("Down",0.3,1)
        SendKey("Right",0.4,count)
        SendKey("Ok",1.5,1)

    # In Weather , Exit to TV (TV is in Background), Voice Search is in Foreground
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.5,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down",0.5,1)
    SendKey("Right",0.6,2)
    SendKey("Ok",1,1)    
    SendKey("Exit",1,1) 
    for count in range(0,3):
        SendKey("Down",5,1)
        SendKey("Right",0.6,count)
        SendKey("Ok",5,1)

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
        SendKey("Right",0.3,count)
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

def App_Gallery_Nav_Revanth_New():
    print ("App-Gallery-Nav")
    SendKey("Smart_Home",10,1)
    print ("AppGalleryNav-Feauredapps category")
    #Featured apps category
    SendKey("Up_longpress",1,1)
    SendKey("Down_longpress",1,1)
    SendKey("Left_longpress",1,1)
    SendKey("Up_longpress",1,1)
    SendKey("Left_longpress",1,1)
    SendKey("Down_longpress",1,1)
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
    
    SendKey("Up_longpress",0.5,3)
    SendKey("Down",1,1)
    for count in range(0,5):
        SendKey("Right",1,1)
        SendKey("Ok",1,1)
    SendKey("Up",1,1)
    SendKey("Down",1,1)
    SendKey("Right",1,1)
    SendKey("Ok",1,1)
    
 #All category
    print ("AppGalleryNav-All category")

    for count in range(0,15):
        SendKey("Down",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)

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
        
# New Category
    print ("AppGalleryNav-New category")

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

#Video category

    print ("AppGalleryNav-Video category")
        
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

#Entertainment category
    print ("AppGalleryNav-Entertainment category")
        
    SendKey("Up_longpress",1,4)
    SendKey("Down",1,1)
    SendKey("Right",1,4)
    SendKey("Ok",1,1)

    for count in range(0,2):
        SendKey("Down",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)

    for count in range(0,2):
        SendKey("Up",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Left",1,1)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
        SendKey("Right",1,2)
        SendKey("Ok",1,1)
        SendKey("Back",1,1)
    
def App_Gallery_Launch_Exit_Revanth():
    Home_Positioning_Launch_App(client,RedRat_Device_Name,RedRat_Device_Port,2)
    SendKey("Exit",0.7,1)
    SendKey("Home",0.7,1)
    SendKey("Ok",0.7,1)
    SendKey("Up_longpress",0.3,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",0.7,1)
    SendKey("Ok",0.7,1)
    SendKey("Down_longpress",0.3,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",0.7,1)
    SendKey("Ok",0.7,1)
    SendKey("Left_longpress",0.3,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",0.7,1)
    SendKey("Ok",0.7,1)
    SendKey("Up_longpress",0.7,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",0.7,1)
    SendKey("Ok",0.7,1)
    SendKey("Left_longpress",0.7,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",0.7,1)
    SendKey("Ok",0.7,1)
    SendKey("Down_longpress",0.3,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",0.7,1)
    SendKey("Ok",0.7,1)

    SendKey("Up_longpress",0.7,3)
    SendKey("Down",0.7,1)
    SendKey("Ok",0.7,1)
    for count in range(0,4):
        SendKey("Right",0.7,1)
        SendKey("Ok",0.7,1)
        SendKey("Exit",0.7,1)
        SendKey("Home",0.7,1)
        SendKey("Ok",0.7,1)

    SendKey("Up",0.7,1)
    SendKey("Down",0.7,1)
    SendKey("Right",0.7,1)
    for count in range(0,10):
        SendKey("Down",0.7,1)
        SendKey("Ok",0.7,1)
        SendKey("Exit",0.7,1)
        SendKey("Home",0.7,1)
        SendKey("Ok",0.7,1)
        SendKey("Right",0.7,1)
        SendKey("Ok",0.7,1)
        SendKey("Exit",0.7,1)
        SendKey("Home",0.7,1)
        SendKey("Ok",0.7,1)

def Record_Info_Tuner():
    Switch_To_Tuner()
    SendKey("5")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)

    SendKey("1")
    time.sleep(0.1)
    SendKey("4")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(7)

    SendKey("5")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(0.1)
    SendKey("6")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(4)

def Record_Info_Satellite():
    Switch_To_Satellite()
    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(0.1)
    SendKey("7")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Up")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(1)
    SendKey("Right")
    time.sleep(0.4)
    SendKey("Ok")
    time.sleep(1)

    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(0.1)
    SendKey("2")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(3.5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Up")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(11)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(1)
    SendKey("Right")
    time.sleep(0.4)
    SendKey("Ok")
    time.sleep(1)
    
def Timeshift_Record_Info_Tuner():
    Switch_To_Tuner()
    SendKey("2")
    time.sleep(0.1)
    SendKey("0")
    time.sleep(4)
    SendKey("Pause")
    time.sleep(5)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(1)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(3)

    SendKey("2")
    time.sleep(0.1)
    SendKey("8")
    time.sleep(4)
    SendKey("Pause")
    time.sleep(5)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(1)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(9)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(4)
  
def Timeshift_Record_Info_Satellite():
    Switch_To_Satellite()
    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(0.1)
    SendKey("2")
    time.sleep(5)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(1)
    SendKey("Forward")
    time.sleep(1)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(1)
    SendKey("Right")
    time.sleep(0.4)
    SendKey("Ok")
    time.sleep(1)

    SendKey("9")
    time.sleep(0.1)
    SendKey("3")
    time.sleep(5)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(1)
    SendKey("Forward")
    time.sleep(1)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(3.5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.4)
    SendKey("Red")
    time.sleep(1)
    SendKey("Right")
    time.sleep(0.4)
    SendKey("Ok")
    time.sleep(1) 

# This Function is for Sweden Country - Channel Numbers are specific to Sweden Country
def TimeShift_Satellite():
    Switch_To_Satellite()
    
    SendKey("8")
    time.sleep(0.1)
    SendKey("4")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(6)

    SendKey("Pause")
    time.sleep(5)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(8)

    SendKey("9")
    time.sleep(0.1)
    SendKey("0")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(15)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(6)

    SendKey("Pause")
    time.sleep(7)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(3)

    SendKey("9")
    time.sleep(0.1)
    SendKey("6")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(35)
    SendKey("Standby")
    time.sleep(4)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(5)
    
    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(7)
    SendKey("Pause")
    time.sleep(20)
    SendKey("Forward")
    time.sleep(3)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Exit")
    time.sleep(3)

    SendKey("9")
    time.sleep(0.1)
    SendKey("6")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)

    SendKey("9")
    time.sleep(0.1)
    SendKey("4")
    time.sleep(10)
    SendKey("Pause")
    time.sleep(6)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(6)
    
    SendKey("Pause")
    time.sleep(5)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(5)
    
    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(10)

def TimeShift_With_StandbyOperations_MultipleChannels_Satellite_Revanth():
    Switch_To_Satellite()

    # 81 - Test UHD 1 Channel in Satellite - Sweden
    SendKey("8")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(4)
    SendKey("Pause",5,1)
    
    Trick_List_Navigations_Fixed(Trick_List_5) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(40)
    SendKey("Standby")
    time.sleep(5)
    
    SendKey("Pause",8,1)
    Trick_List_Navigations_Fixed(Trick_List_1) # At the End of this Trick List, This will be in Forward Trick
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(6)

    #92 - Arte HD in Satellite - Sweden
    SendKey("9")
    time.sleep(0.1)
    SendKey("2")
    time.sleep(4)

    SendKey("Red")
    time.sleep(6)
    SendKey("Down",0.3,2)
    time.sleep(9)
    SendKey("Pause",10,1)
    
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Pause",5,1)

    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Standby")
    time.sleep(3)

    # 83 - Test UHD 3 Channel in Satellite - Sweden
    SendKey("1")
    time.sleep(0.3)
    SendKey("5")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(5)

    SendKey("Pause",15,1)
    
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(25)
    SendKey("Standby")
    time.sleep(9)

    SendKey("Pause",20,1)

    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(7)

    # 148 - UHD Channel in Satellite - Sweden
    SendKey("8")
    time.sleep(0.3)
    SendKey("7")
    time.sleep(4)

    SendKey("Pause",15,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(50)
    SendKey("Standby")
    time.sleep(8)

    SendKey("Pause",8,1)
    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(5)

    # 120 - Dolby Labs Test Stream Channel in Satellite - Sweden
    SendKey("9")
    time.sleep(0.3)
    SendKey("6")
    time.sleep(4)
    
    SendKey("Pause")
    time.sleep(20)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(12)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(5)
    SendKey("Play")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(22)
    SendKey("Standby")
    time.sleep(7)

    # 168 - UHD Channel in Satellite - Sweden
    SendKey("8")
    time.sleep(0.3)
    SendKey("5")
    time.sleep(8)
    
    SendKey("Pause")
    time.sleep(15)
    SendKey("Forward")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)

    SendKey("Pause")
    time.sleep(25)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(14)
    SendKey("Standby")
    time.sleep(5)

    # 152 - SWR RP HD Channel in Satellite - Sweden
    SendKey("9")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(6)
    
    SendKey("Pause")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(4)

    SendKey("Pause")
    time.sleep(6)
    SendKey("Forward",2,4)
    SendKey("Standby")
    time.sleep(50)
    SendKey("Standby")
    time.sleep(10)

def PVR_With_StandbyOperations_MultipleChannelesTuner_Revanth():
    Switch_To_Tuner()
    # 8 - Test UHD 1 Channel in Tuner - Sweden
    SendKey("0")
    time.sleep(0.3)
    SendKey("8")
    time.sleep(4)

    time.sleep(5)
    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(24)
    SendKey("Rewind")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(5)

    #20 - BBC One HD channel in tuner - Sweden
    SendKey("2")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(8)

    # 16 - ZDF Channel in Tuner - Sweden
    SendKey("1")
    time.sleep(0.3)
    SendKey("6")
    time.sleep(6)

    SendKey("Rec")
    time.sleep(30)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Exit")
    time.sleep(5)

    SendKey("Pause")
    time.sleep(24)
    SendKey("Rewind")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(22)
    SendKey("Standby")
    time.sleep(5)
	
    #17
    SendKey("1")
    time.sleep(0.3)
    SendKey("7")
    time.sleep(5)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(40)
    SendKey("Red")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(9)
    SendKey("Standby")
    time.sleep(4)

    # 10 - Test UHD 3 Channel in Tuner - Sweden
    SendKey("1")
    time.sleep(0.1)
    SendKey("0")
    time.sleep(4)
    
    SendKey("Rec")
    time.sleep(22)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)

    SendKey("Pause")
    time.sleep(15)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(5)

    #28
    SendKey("2")
    time.sleep(0.3)
    SendKey("8")
    time.sleep(4)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(50)
    SendKey("Standby")
    time.sleep(8)

    # 19 - BBC in Tuner - Sweden
    SendKey("1")
    time.sleep(0.1)
    SendKey("9")
    time.sleep(4)
    
    SendKey("Rec")
    time.sleep(25)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)

    SendKey("Pause")
    time.sleep(12)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Exit")
    time.sleep(4)

    #18
    SendKey("1")
    time.sleep(0.3)
    SendKey("8")
    time.sleep(5)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(35)
    SendKey("Red")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(13)
    SendKey("Standby")
    time.sleep(8)

    # 1 - 1440*1080i Channel in Tuner - Germany
    SendKey("1")
    time.sleep(4)

    SendKey("Rec")
    time.sleep(15)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(19)
    SendKey("Exit")
    time.sleep(5)

def PVR_With_StandbyOperations_Multiplechannelsstatellte_Revanth():
    Switch_To_Satellite()

    # 81 - Test UHD 1 Channel in Satellite - Sweden
    SendKey("1")
    time.sleep(0.3)
    SendKey("5")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(5)

    SendKey("Rec")
    time.sleep(20)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Pause")
    time.sleep(15)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)
    
    SendKey("Pause")
    time.sleep(26)
    SendKey("Rewind")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(15)
    SendKey("Standby")
    time.sleep(5)
    
    #93
    SendKey("9")
    time.sleep(0.3)
    SendKey("3")
    time.sleep(5)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(30)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Stop")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1)
    
    #91 - Arte HD in Satellite - Sweden
    SendKey("8")
    time.sleep(0.2)
    SendKey("8")
    time.sleep(4)

    SendKey("Red")
    time.sleep(6)
    SendKey("Down",0.4,2)
    SendKey("Ok",6,1)

    SendKey("Rec")
    time.sleep(25)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Pause")
    time.sleep(15)
    SendKey("Forward")
    time.sleep(3)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Standby")
    time.sleep(3)
    SendKey("Exit")
    time.sleep(5)

    #117
    SendKey("1")
    time.sleep(0.3)
    SendKey("5")
    time.sleep(0.3)
    SendKey("1")
    time.sleep(3)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(40)
    SendKey("Red")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Standby")
    time.sleep(9)
    SendKey("Standby")
    time.sleep(4)

    # 83 - Test UHD 3 Channel in Satellite - Sweden
    SendKey("8")
    time.sleep(0.3)
    SendKey("6")
    time.sleep(5)

    SendKey("Rec")
    time.sleep(15)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(25)
    SendKey("Standby")
    time.sleep(5)
    
    #155
    
    SendKey("1")
    time.sleep(0.3)
    SendKey("2")
    time.sleep(0.3)
    SendKey("0")
    time.sleep(5)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(32)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Exit")
    time.sleep(15)
    SendKey("Stop")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1)

# 148 - UHD Channel in Satellite - Sweden
    SendKey("1")
    time.sleep(0.3)
    SendKey("5")
    time.sleep(0.3)
    SendKey("2")
    time.sleep(5)

    SendKey("Rec")
    time.sleep(18)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)

    SendKey("Pause")
    time.sleep(10)
    SendKey("Forward")
    time.sleep(13)
    SendKey("Standby")
    time.sleep(5)
    
#168
    SendKey("1")
    time.sleep(0.3)
    SendKey("4")
    time.sleep(0.3)
    SendKey("6")
    time.sleep(5)
    SendKey("Info")
    time.sleep(0.5)
    SendKey("Red")
    time.sleep(25)
    SendKey("Red")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.4)
    SendKey("Ok")
    time.sleep(2)
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(5)
    
    # 120 - Dolby Labs Test Stream Channel in Satellite - Sweden
    SendKey("9")
    time.sleep(0.3)
    SendKey("8")
    time.sleep(6)

    SendKey("Rec")
    time.sleep(25)
    SendKey("Stop")
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.4)
    SendKey("Ok")
    time.sleep(1)

    SendKey("Pause")
    time.sleep(12)
    SendKey("Forward")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(9)
    SendKey("Exit")
    time.sleep(4)

def TimeShift_With_StandbyOperations_Revanth():
    print ("TimeShift_With_StandbyOperations()- Start of the Function")
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
 
def HDMI_Revanth():
    
    SendKey("Sources",4,1)
    SendKey("Up_longpress",0.6,1)
    SendKey("Down",0.3,8)
    SendKey("Ok",1,2)
    time.sleep(120)

    #hdmi-1 trickmodes & quicksettings
    Trick_List_Navigations_Fixed(Trick_List_5)
    HDMI_QuickSettings_Revanth()

    #hdmi switching
    #1-2-3-4
    for count in range(0,3):
        SendKey("Sources",4,1)
        SendKey("Down",0.3,1)
        SendKey("Ok",10,1)

    #4-3-2-1
    for count in range(0,3):
        SendKey("Sources",4,1)
        SendKey("Up",0.5,1)
        SendKey("Ok",10,1)

    #hdmi-2 trickmodes & quicksettings
    SendKey("Sources",4,1)
    SendKey("Down",0.3,1)
    SendKey("Ok",60,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    HDMI_QuickSettings_Revanth()

    #2-4
    SendKey("Sources",4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",8,1)

    #4-1
    SendKey("Sources",4,1)
    SendKey("Up",0.3,3)
    SendKey("Ok",6,1)

    #1-3
    SendKey("Sources",4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",7,1)

    #3-1
    SendKey("Sources",4,1)
    SendKey("Up",0.3,2)
    SendKey("Ok",9,1)

    #1-4
    SendKey("Sources",4,1)
    SendKey("Down",0.3,3)
    SendKey("Ok",5,1)
    
def HDMI_Standby_Revanth():
    #hdmi-1 trickmodes & quicksettings

    SendKey("Sources",4,1)
    SendKey("Up_longpress",0.6,1)
    SendKey("Down",0.3,8)
    SendKey("Ok",1,2)
    time.sleep(60)

    SendKey("Standby",50,1)
    SendKey("Standby",5,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Forward",2,2)
    SendKey("Standby",5,2)

    HDMI_QuickSettings_Revanth()
    SendKey("Standby",25,1)
    SendKey("Standby",5,1)

    #Random_Standby_List = [5,17,35,60]

    #hdmi switching
    #1-2-3-4
    for count in range(0,3):
        SendKey("Sources",4,1)
        SendKey("Down",0.3,1)
        SendKey("Ok",8,1)
        SendKey("Forward",3,1)
        SendKey("Standby",18,1)
        SendKey("Standby",5,1)
    
    #4-3-2-1
    for count in range(0,3):
        SendKey("Sources",4,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",10,1)
        SendKey("Pause",1,1)
        SendKey("Standby",6,1)
        SendKey("Standby",5,1)
        
    #hdmi-2 trickmodes & quicksettings
    for count in range(0,4):
        SendKey("Sources",4,1)
        SendKey("Down",0.3,1)
        SendKey("Ok",15,1)
        Trick_List_Navigations_Fixed(Trick_List_5)

        SendKey("Standby",35,1)
        SendKey("Standby",5,1)

        HDMI_QuickSettings_Revanth()
        SendKey("Standby",5,1)
        SendKey("Standby",5,1)
        
    #2-4
    SendKey("Sources",5,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",10,1)
    SendKey("Standby",20,1)
    SendKey("Standby",5,1)

    #4-1
    SendKey("Sources",4,1)
    SendKey("Up",0.3,3)
    SendKey("Ok",10,1)
    SendKey("Standby",6,1)
    SendKey("Standby",5,1)

    #1-3
    SendKey("Sources",4,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",10,1)
    SendKey("Standby",15,1)
    SendKey("Standby",5,1)

    #3-1
    SendKey("Sources",6,1)
    SendKey("Up",0.3,2)
    SendKey("Ok",10,1)
    SendKey("Standby",22,1)
    SendKey("Standby",5,1)

    #1-4
    SendKey("Sources",5,1)
    SendKey("Down",0.3,3)
    SendKey("Ok",10,1)
    SendKey("Standby",4,1)
    SendKey("Standby",4,1)




def HDMI_QuickSettings_Revanth():
    SendKey("Settings",1.5,1)
    
    #QuickSettings-PictureStyle
    SendKey("Up_longpress",0.7,1)
    SendKey("Right",0.3,1)
    SendKey("Up_longpress",0.7,1)
    for count in range(0,7):
        SendKey("Ok",0.7,1)
        SendKey("Down",0.6,1)
    SendKey("Left",0.3,1)
    
    #QuickSettings-Picture format
    SendKey("Up_longpress",0.7,1)
    SendKey("Down",0.7,1)
    SendKey("Ok",0.5,1)
    SendKey("Up_longpress",0.7,1)
    
    for count in range(0,4):
        SendKey("Ok",0.7,1)
        SendKey("Down",0.4,1)
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
    SendKey("Down",0.4,1)
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
        SendKey("Down",0.4,1)
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



def Block1():
    # This Script is for Sweden Country Installation
    #################################################################
    #Satellite - HD , Satellite - UHD, Satellite - HD
    #################################################################
    Digit_Channel_Selection("Satellite",90) # 90 - Arte HD Channel

    PVR_OTR_25()
    PVR_OTR_Standby_30()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    SendKey("8",0.1,1)
    SendKey("2",4,1)

    TimeShift_With_StandbyOperations_Naveen()
    PVR_OTR_15()
    PVR_OTR_Standby_10()
    PVRRecording_Playback()

    # Tuning to Satellite HD Channel Number 154 - SWR RP HD --> This Channel has HBBTV App. Hence Invoke HBBTV Function after this
    SendKey("9",0.1,1)
    SendKey("7",8,1)

    PVR_OTR_15()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()
    PVR_OTR_Standby_20()

    #################################################################
    #Timeshift_Record_Info_Satellite()
    #################################################################
    Timeshift_Record_Info_Satellite()
    
    #################################################################
    #Tuner - Analog , Tuner - HD, Tuner - Radio
    #################################################################

    # Tuning to Tuner Analog Channel 32 - "TELETEXT Analog Channel --> This is Analog Channel
    Digit_Channel_Selection("Tuner",32) # 32 - "TELETEXT Analog Channel

    TimeShift_With_StandbyOperations_Naveen()
    PVR_OTR_25()
    PVR_OTR_Standby_30()
    PVRRecording_Playback()

    # Tuning to Tuner HD Channel 5 - H264_1920*1080i_Live --> This Channel has Multiple Audio Languages - Change the Language and Perform Timeshift/PVR Operations after this
    SendKey("5",4,1) # Tune to Tuner Channel 5 - H264_1920*1080i_Live

    PVR_OTR_15()
    PVR_OTR_Standby_10()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    # Tuning to Tuner - Radio Channel Number 502 - BBC Asian Net --> This Channel is a Radio Channel
    SendKey("5",0.1,1)
    SendKey("0",0.1,1)
    SendKey("2",4,1)

    PVR_OTR_25()
    PVR_OTR_Standby_20()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    #################################################################
    #Record_Info_Tuner()
    #################################################################
    Record_Info_Tuner()
    
    #################################################################
    #Satellite - SD , Satellite - UHD, Satellite - UHD
    #################################################################

    # Tuning to Satellite SD Channel Number 161 - TMC 
    Digit_Channel_Selection("Satellite",158) # 161 - TMC Channel

    PVR_OTR_15()
    PVR_OTR_Standby_30()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    # Tuning to Satellite UHD Channel Number 86 - Test UHD3 --> This Channel is Test UHD3 Channel.
    SendKey("8",0.1,1)
    SendKey("1",4,1)

    PVR_OTR_25()
    PVR_OTR_Standby_10()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    # Tuning to Satellite UHD Channel Number 148 - SES UHD Demo Channel
    SendKey("8",0.1,1)
    SendKey("6",4,1)

    PVR_OTR_25()
    PVR_OTR_Standby_10()
    PVR_OTR_Standby_20()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    #################################################################
    #Record_Info_Satellite()
    #################################################################
    Record_Info_Satellite()
    
    #################################################################
    #Tuner - UHD , Tuner - SD, Tuner - HD
    #################################################################

    # Tuning to Tuner UHD Channel 9 - Test UHD2 Channel --> This is Test UHD2 Channel
    Digit_Channel_Selection("Tuner",9) # 9- Test UHD2 Channel
    PVR_OTR_15()
    PVR_OTR_Standby_30()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    # Tuning to Tuner SD Channel 14 - Eins Plus --> This Channel has Teletext - Include Teletext Navigation Function inside this
    SendKey("1",0.1,1) # Tune to Tuner Channel 5 - H264_1920*1080i_Live
    SendKey("4",4,1)

    PVR_OTR_25()
    PVR_OTR_Standby_10()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    # Tuning to Tuner - HD Channel 28 - Channel 4 HD --> AAC 5.1 English
    SendKey("2",0.1,1)
    SendKey("8",4,1)

    PVR_OTR_15()
    PVR_OTR_Standby_20()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    #################################################################
    #Timeshift_Record_Info_Tuner()
    #################################################################
    Timeshift_Record_Info_Tuner()

    #################################################################
    #Satellite - DD Channel , Satellite - UHD, Satellite - HD
    #################################################################

    # Tuning to Satellite  Channel Number 119 - Dolby Labs Test Stream
    Digit_Channel_Selection("Satellite",161) # 119 - Dolby Labs Test Stream

    PVR_OTR_25()
    PVR_OTR_Standby_30()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    # Tuning to Satellite HD Channel Number 117 - Das Erste HD --> This Channel has HBBTV App - Check the App Navigations
    SendKey("1",0.1,1)
    SendKey("5",0.1,1)
    SendKey("4",4,1)

    PVR_OTR_15()
    PVR_OTR_Standby_30()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    # Tuning to Satellite UHD Channel Number 81 - Test UHD 1 Channel
    SendKey("8",0.1,1)
    SendKey("5",4,1)
    
    PVR_OTR_15()
    PVR_OTR_Standby_20()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    #################################################################
    #Record_Info_Satellite(), Timeshift_Record_Info_Tuner()
    #################################################################
    Record_Info_Satellite()
    Timeshift_Record_Info_Tuner()
    
    #################################################################
    #Tuner - HD , Tuner - HD, Tuner - SD
    #################################################################

    # Tuning to Tuner HD Channel - 20 - BBC ONE HD- This Channel has Subtitles
    Digit_Channel_Selection("Tuner",20) # 20 - BBC ONE HD

    PVR_OTR_25()
    PVR_OTR_Standby_10()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    # Tuning to Tuner HD Channel 7 - H264_720*576p@25 --> This Channel has Multiple Audio Languages - Add the same function below this
    SendKey("7",4,1) # Tune to Tuner Channel 5 - H264_1920*1080i_Live

    PVR_OTR_15()
    PVR_OTR_Standby_20()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    # Tuning to Tuner - SD Channel 12 - Audio Description --> This has Audio Description
    SendKey("1",0.1,1)
    SendKey("2",4,1)

    PVR_OTR_25()
    PVR_OTR_Standby_30()
    TimeShift_With_StandbyOperations_Naveen()
    PVRRecording_Playback()

    #################################################################
    #Record_Info_Tuner(), Timeshift_Record_Info_Satellite()
    #################################################################
    Record_Info_Tuner()
    Timeshift_Record_Info_Satellite()

    ######################################################################
    #PVR_TimeShift_Legacy() - Legacy Script which needs to be considered
    ######################################################################
    PVR_TimeShift_Legacy()
    
    ######################################################################
    # Below is the Flow for Other Additional Functions Written w.r.t BRDC
    ######################################################################

    SendKey("Exit",4, 1)
    TimeShift_With_StandbyOperations_MultipleChannels_Satellite_Revanth()

    SendKey("Exit",4, 1)
    PVR_With_StandbyOperations_MultipleChannelesTuner_Revanth()

    SendKey("Exit",4, 1)
    PVR_With_StandbyOperations_Multiplechannelsstatellte_Revanth()
    
    SendKey("Exit",4, 1)
    TimeShift_With_StandbyOperations_Revanth()

    SendKey("Exit",4, 1)
    PVRRecording_Playback_Revanth()

    #############################################################################
    # Below is the Code for 20 Minutes TimeShift Content Playback and Trick Modes
    #############################################################################

    Digit_Channel_Selection('Satellite', 151)
    SendKey('Pause',600,1)
    Trick_List_Navigations_Fixed(Trick_List_6)


def Block2():
    
    #############################################
    # Below is the Flow for Time Shift - SmartTV
    #############################################
    Digit_Channel_Selection("Satellite",86) # Channel Number to be selected based on the Dynamic Logic. Also Decide on Satellite/Tuner based on the Loops
    SendKey("Pause",30,1)
    SendKey("Play",1,1)
    SendKey("Forward",2,3)
    Netflix_New(1) # Select the File Number to be Played from Netflix
    Trick_List_Navigations_Fixed(Trick_List_5)
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(35)
    SendKey("Standby")
    time.sleep(7)

    Digit_Channel_Selection("Satellite",161) # Channel Number to be selected based on the Dynamic Logic. Also Decide on Satellite/Tuner based on the Loops
    SendKey("Pause",30,1)
    SendKey("Play",1,1)
    SendKey("Forward",2,3)
    Youtube_Row1_New()
    #Youtube_New(2) # Select the File Number to be Played from Youtube
    Trick_List_Navigations_Fixed(Trick_List_4)
    Trick_List_Navigations_Fixed(Trick_List_3)
    SendKey("Standby")
    time.sleep(4)
    SendKey("Standby")
    time.sleep(4)

    Digit_Channel_Selection("Satellite",97) # Channel Number to be selected based on the Dynamic Logic. Also Decide on Satellite/Tuner based on the Loops
    SendKey("Pause",30,1)
    SendKey("Play",1,1)
    SendKey("Rewind",3,1)
    Amazon_New() # Select the File Number to be Played from Amazon
    Trick_List_Navigations_Fixed(Trick_List_1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(7)

    ########################################
    # Below is the Flow for PVR - Smart TV
    ########################################
    Digit_Channel_Selection("Tuner",10) # Channel Number to be selected based on the Dynamic Logic. Also Decide on Satellite/Tuner based on the Loops
    SendKey("Rec",5,1) # Perform OTR Record for 30 Sec
    OIB()
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)

    App_Gallery_Nav_Revanth_New()
    SendKey("Standby")
    time.sleep(23)
    SendKey("Standby")
    time.sleep(5)

    Netflix_New(2) # Select the File Number to be Played from Netflix
    Trick_List_Navigations_Fixed(Trick_List_5)
    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Standby")
    time.sleep(21)
    SendKey("Standby")
    time.sleep(9)

    Youtube_Row2_New()
    #Youtube_New(1) # Select the File Number to be Played from Youtube
    Trick_List_Navigations_Fixed(Trick_List_4)
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(5)

    Amazon_New() # Select the File Number to be Played from Amazon
    Trick_List_Navigations_Fixed(Trick_List_3)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(9)
    SendKey("Standby")
    time.sleep(6)

    HbbTV_New()
    Trick_List_Navigations_Fixed(Trick_List_4)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(17.5)
    SendKey("Standby")
    time.sleep(7)

    SendKey("Exit")
    time.sleep(2)
    SendKey("Stop") # Stopping the OTR Recording which was started before
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(2)

    ###########################################
    # Below is the Flow for PVR - Connectivity
    ############################################

    #Include Content Browser Playbacks here
    Digit_Channel_Selection("Satellite",161) # Channel Number to be selected based on the Dynamic Logic. Also Decide on Satellite/Tuner based on the Loops
    SendKey("Rec",5,1) # Perform OTR Record for 30 Sec
    #CBPlayback_New(1,video) # Select 1st Video File Playback
    Trick_List_Navigations_Fixed(Trick_List_5)
    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)

    CBPlayback_Revanth(0,1,3) # Select 2nd Video File Playback
    Trick_List_Navigations_Fixed(Trick_List_4)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(15.5)
    SendKey("Standby")
    time.sleep(9)

    CBPlayback_Revanth(0,7,2) # Select 1st Audio File Playback
    Trick_List_Navigations_Fixed(Trick_List_3)
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(5)

    CBPlayback_Revanth(1,3,4) # Select Image Files and Navigate Inside the Same using some Slide Show Options
    Trick_List_Navigations_Fixed(Trick_List_1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    SendKey("Standby")
    time.sleep(9)
    SendKey("Standby")
    time.sleep(6)

    CBPlayback_Revanth(0,2,3) # Select 3rd Video File Playback
    Trick_List_Navigations_Fixed(Trick_List_3)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(7)
    SendKey("Standby")
    time.sleep(6)

    CBPlayback_Revanth(0,4,5) # Select 4th Video Playback
    Trick_List_Navigations_Fixed(Trick_List_4)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(18.5)
    SendKey("Standby")
    time.sleep(10)

    CBPlayback_Revanth(1,3,4) # Select 4th Video Playback
    Trick_List_Navigations_Fixed(Trick_List_5)
    Trick_List_Navigations_Fixed(Trick_List_2)
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Exit",1,1)
    SendKey("Stop") # Stopping the OTR Recording
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(2)

    ####################################################
    # Below is the Flow for PVR - Applications and Games
    ####################################################
  
    Digit_Channel_Selection("Satellite",151) # Channel Number to be selected based on the Dynamic Logic. Also Decide on Satellite/Tuner based on the Loops
    SendKey("Rec",5,1) # Perform OTR Record for 30 Sec
    #CBPlayback_New(1,video) # Select 1st Video File Playback
    Trick_List_Navigations_Fixed(Trick_List_5)
    Trick_List_Navigations_Fixed(Trick_List_1)
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(5)

#    Megogo_Revanth(13)
    SendKey("Standby")
    time.sleep(16)
    SendKey("Standby")
    time.sleep(10)

#    NPO_Revanth(14)
    SendKey("Standby")
    time.sleep(19)
    SendKey("Standby")
    time.sleep(10)

#    SVT_Revanth(15)
    SendKey("Standby")
    time.sleep(21)
    SendKey("Standby")
    time.sleep(6)

#   Puhu_Revanth(16)
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(4)

#    SkyForce_Revanth(17)
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(6)

#    Pacman_Revanth(18)
    SendKey("Standby")
    time.sleep(8)
    SendKey("Standby")
    time.sleep(4)

    SendKey("Exit",1,1)
    SendKey("Stop") # Stopping the OTR Recording
    time.sleep(0.5)
    SendKey("Left")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(2)

    ######################################################
    # Below is the Flow for Recording Playback - SmartTV
    ######################################################

    PVRRecording_Playback()
    Netflix_New(3)
    Trick_List_Navigations_Fixed(Trick_List_4)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(45)
    SendKey("Standby")
    time.sleep(5)

    PVRRecording_Playback()

    App_Gallery_Nav_Revanth_New()
    
    Trick_List_Navigations_Fixed(Trick_List_4)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(5)

    SendKey("Exit",4, 1)
    

def Start_RedRat_Script():
    for i in range(0,1000):
        y = time.time()
        try:
            Block1()
        except:
            pass
        z = time.time()
        print ("Time taken to Complete Block1() is : %f" %(z-y))

        y = time.time()
        try:
            Block2()
        except:
            pass
        z = time.time()
        print ("Time taken to Complete Block2() is : %f" %(z-y))
        
if __name__ == "__main__":
    Start_RedRat_Script()






    
    
