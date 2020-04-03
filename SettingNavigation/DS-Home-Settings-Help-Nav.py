'''
 ==========================================================================================================
                Initial-Conditions for DS-Home-Settings-Help-Nav

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
 OIB Pages in Internet Browser
 -----------------------------------------------------------------------------------------------------
 1.	www.espncricinfo.com     2.	www.flashscores.co.uk       3.	www.dangelicoguitars.com     4.www.dearestnature.com
 5.	www.cricbuzz.com         6.	www.nasaprospect.com        7.	www.www.blueacorn.com        8.www.ndtv.com

 -----------------------------------------------------------------------------------
 Other Mandatory Pre-Conditions
 -----------------------------------------------------------------------------------
 1. HDD Should be Paired to the TV
 2. Check whether Timeshift & OTR Functionalities are working properly before the test
 3. Internet Connection Should be Successful - Wired/Wireless
 4. Ensure all Logins are Successful 
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
#import Set_Date_Time_Hub
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

global Lang_Counter

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
        
def Trick_List_Navigations_Fixed(Trick_List):
    Key_1stArg = 0
    SleepTime_2ndArg = 1
    for count in range(len(Trick_List)):
        SendKey(Trick_List[count][Key_1stArg], Trick_List[count][SleepTime_2ndArg])
        
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

def Youtube_Row1_New():
    Home_Positioning_Launch_App(1)
    
    SendKey("Left_longpress",0.7, 1)
    SendKey("Up_longpress", 0.5, 1)
    SendKey("Down", 0.3, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_5)
    Picture()
    Picture_Advanced()
    Ambilight()
    Ambilight_Advanced()
    
    SendKey("Back", 1, 2)
    SendKey("Right", 0.5, 1)
    SendKey("Ok", 10, 1)
    Trick_List_Navigations_Fixed(Trick_List_4)

    Sound()
    Sound_Advanced()
    Eco_Settings()
    Universal_Access()
    
def Youtube_Row2_New():
    Home_Positioning_Launch_App(1)
    SendKey("Left_longpress",0.7, 1)
    SendKey("Up_longpress", 0.5, 1)
    SendKey("Down", 0.3, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down", 0.3, 1)
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_6)
    Quick_Settings()

    SendKey("Back", 1, 2)
    SendKey("Right", 0.5, 1)
    SendKey("Ok", 10, 1)
    Help_Navigation(21)
    Blue_Book_Read()
    Blue_Book_Nav()
    Blue_Back()

def App_Gallery_Nav_Revanth_New():
    SendKey("Smart_Home",10,1)
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
    SendKey("Smart_Home",10,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",0.7,1)
    SendKey("Ok",0.7,1)
    SendKey("Up_longpress",0.3,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",1,1)
    SendKey("Ok",0.7,1)
    SendKey("Down_longpress",0.3,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",1,1)
    SendKey("Ok",0.7,1)
    SendKey("Left_longpress",0.3,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",1,1)
    SendKey("Ok",0.7,1)
    SendKey("Up_longpress",0.7,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",1,1)
    SendKey("Ok",0.7,1)
    SendKey("Left_longpress",0.7,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",1,1)
    SendKey("Ok",0.7,1)
    SendKey("Down_longpress",0.3,1)
    SendKey("Exit",0.7,1)
    SendKey("Home",1,1)
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
        SendKey("Home",1,1)
        SendKey("Ok",0.7,1)
        SendKey("Right",0.7,1)
        SendKey("Ok",0.7,1)
        SendKey("Exit",0.7,1)
        SendKey("Home",1,1)
        SendKey("Ok",0.7,1)

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
        
    SendKey("Exit",0.5,1)

def CBPlayback_Videos():
    Down_Count = [0,1,2,3,4,5]
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down',0.3,7)
    SendKey('Up',0.7,2)
    SendKey('Right',0.8,2) 
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    time.sleep(4)
    Sound()
    Ambilight()
    Sound_Advanced()
    Eco_Settings()
    
    SendKey("Back",0.3,2)
    SendKey("Left",0.2,4)
    SendKey('Down_Longpress',0.4,2)
    SendKey('Up',0.7,2)
    SendKey('Right',0.8,2) 
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    Quick_Settings()
    Picture()
    Ambilight_Advanced()
    Picture_Advanced()
    Help_Navigation(16)

def CBPlayback_Audios():
    Down_Count = [6,7,8,9,10,11]
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down',0.3,7)
    SendKey('Up',0.7,2)
    SendKey('Right',0.8,2) 
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    time.sleep(4)
    Sound()
    Sound_Advanced()
    
    SendKey("Back",0.3,2)
    SendKey("Left",0.2,4)
    SendKey('Down_Longpress',0.4,2)
    SendKey('Up',0.7,2)
    SendKey('Right',0.8,2) 
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    Universal_Access()
    Sound_Advanced()
    
def CBPlayback_Images():
    Down_Count = [12,13,14,15,16,17]
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down',0.3,7)
    SendKey('Up',0.7,2)
    SendKey('Right',0.8,2) 
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',0.5,2)
    SendKey("Play",10,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    Picture()
    Ambilight_Advanced()
    Picture_Advanced()
    Blue_Book_Read()
    Ambilight()
    Help_Navigation(12)
    
def Netflix(number, number1):
    
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
    Quick_Settings()
    Sound()
    Ambilight_Advanced()
    Help_Navigation(20)
    Blue_Back()
    Picture()
    Picture_Advanced()
    
    
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
    Blue_Book_Read()
    Blue_Book_Nav()
    Sound_Advanced()
    Ambilight()
    Eco_Settings()
    Universal_Access()

    
def HbbTV_New():
    Switch_To_Satellite()
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
    SendKey('Exit',3,1)

def Amazon_New(VideoNo):
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

def Megogo_Revanth():
    Home_Positioning_Launch_App(14)
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
    Home_Positioning_Launch_App(10)
    time.sleep(20)
    
    SendKey("Down",1,2)
    SendKey("Ok",0.5,1)
    for count in range(0,3):
        SendKey("Ok",30,1)
        Trick_List_Navigations_Fixed(Trick_List_3)
        Trick_List_Navigations_Fixed(Trick_List_2)
        SendKey("Back",0.7,3)
        SendKey("Down",0.7,2)
    
def SVT_Revanth():
    Home_Positioning_Launch_App(12)
    SendKey("Ok",1,1)
    SendKey("Down",1.2,2)
    for count in range(0,4):
        SendKey("Ok",1,1)
        SendKey("Ok",30,1)
        Trick_List_Navigations_Fixed(Trick_List_4)
        Trick_List_Navigations_Fixed(Trick_List_5)
        SendKey("Back",0.5,2)
        SendKey("Right",0.7,1)

def Puhu_Revanth():
    Home_Positioning_Launch_App(11)
    time.sleep(30)
    SendKey("Down",0.8,2)
    SendKey("Ok",0.8,2)
    for count in range(0,3):
        SendKey("Ok",1,2)
        SendKey("Play",2,5)
        SendKey("Play",60,1)
        Trick_List_Navigations_Fixed(Trick_List_2)
        Trick_List_Navigations_Fixed(Trick_List_4)
        SendKey("Back",1,2)

def SkyForce_Revanth():
    SendKey("Home",4,2)
    SendKey("Ok",5,1)
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
    SendKey("Home",4,2)
    SendKey("Right",1,1)
    SendKey("Ok",5,1)
    time.sleep(20)
    SendKey("Ok",1,10)
    for count in range(0,4):
        SendKey("Up",0.5,1)
        SendKey("Right",0.4,1)
        SendKey("Up",0.4,1)
        SendKey("Left",0.4,1)
    SendKey("Ok",0.6,5)
    SendKey("Exit",2,1)
    
def Help_Navigation(letter):
    SendKey("Blue")
    time.sleep(6.0)
    for k in range(0,7):
        SendKey("Left")
        time.sleep(0.3)
    SendKey("Up")
    time.sleep(0.2)
    SendKey("Right")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(1.0)
    SendKey("Up_longpress")
    time.sleep(1.0)
    SendKey("Up_longpress")
    time.sleep(1.0)
    for j in range(0,letter):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Right")
    time.sleep(1)
    SendKey("Down_longpress")
    time.sleep(0.5)
    SendKey("Up_longpress")
    time.sleep(0.4)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Blue")
    time.sleep(1.0)

def Launch_Settings_App():
        SendKey("Settings")
        time.sleep(3.0)
        SendKey("Down_longpress")
        time.sleep(1.5)
        SendKey("Up")
        time.sleep(0.4)
        SendKey("Ok")
        time.sleep(2.0)    

def Navigation_in_Settings():
        Launch_Settings_App()
        for count in range(3):
            SendKey("Down_longpress")
            time.sleep(1.5)
            SendKey("Up_longpress")
            time.sleep(1.5)
        SendKey("Up")
        for count in range(5):
            time.sleep(0.25)
            SendKey("Right")
        time.sleep(1.0)
        SendKey("Ok")
        time.sleep(2.0)
    ## Checking the Picture Style
        
def Picture():
    Launch_Settings_App()

    SendKey("Ok",0.6,1)
    SendKey("Ok",0.6,1)
    SendKey("Up_longpress",0.6,1)
    
    SendKey("Ok",0.6,1)
    SendKey("Down",0.3,1)
    
    SendKey("Ok",0.6,1)
    SendKey("Down",0.3,1)
    
    SendKey("Ok",0.6,1)
    SendKey("Down",0.3,1)
    
    SendKey("Ok",0.6,1)
    SendKey("Down",0.3,1)
        
    SendKey("Ok")
    time.sleep(0.6)
    SendKey("Down")
    time.sleep(0.3)
    
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.6)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.6)
       
## Checking the Colour
    print ("Checking the Colour")
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    for count in range(3):
        SendKey("Down_longpress")
        time.sleep(0.2)
        SendKey("Up_longpress")
        time.sleep(0.2)

## Checking the Contrast
    print (" Checking the Contrast")
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    for count in range(3):
        SendKey("Down_longpress")
        time.sleep(0.4)
        SendKey("Up_longpress")
        time.sleep(0.4)

## Checking the Sharpness
    print ("Checking the Sharpness")
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    for count in range(3):
        SendKey("Down_longpress")
        time.sleep(0.3)
        SendKey("Up_longpress")
        time.sleep(0.3)

## Checking the Brightness
    print ("Checking the Brightness")
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    for count in range(4):
        SendKey("Down_longpress")
        time.sleep(0.3)        
        SendKey("Up_longpress")
        time.sleep(0.3)
    
def Picture_Advanced():
    Launch_Settings_App()
    
    print ("Starting Picture Advance --> Colour Enhancement")
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    
    SendKey("Up_longpress")
    time.sleep(0.3)
    
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    #Blue_Book_Read(client,RedRat_Device_Name,RedRat_Device_Port)
    
#    #Checking Colour Gamut in Advanced
#    print ("Checking the Advanced --> Colour Gamut")
#    SendKey("Left")
#    time.sleep(0.5)
#    SendKey("Down")
#    time.sleep(0.5)
#    SendKey("Right")
#    time.sleep(0.2)
#    SendKey("Up_longpress")
#    time.sleep(0.2)
#    SendKey("Ok")
#    time.sleep(0.5)
#    SendKey("Down")
#    time.sleep(0.5)
#    SendKey("Ok")
#    time.sleep(0.5)    
    
## Checking the Advanced --> Colour Temperature
    print ("Checking the Advanced --> Colour Temperature")
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.6)
    Blue_Book_Nav()
    
## Checking the Advanced --> Contrast 
    print ("Checking the Advanced --> Contrast" )
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.25)
    SendKey("Up_longpress")
    time.sleep(0.3)
    Blue_Back()
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.6)

## Checking the Advanced --> Contrast --> Dynamic Contrast
    print ("Checking the Advanced --> Dynamic Contrast" )
    SendKey("Left")
    time.sleep(0.3)
    for count in range(3):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5) 

    Help_Navigation(16) ##Navigations in letter = 16 i.e. "S"
    SendKey("Back")
    time.sleep(0.8)
    Blue_Book_Read()

## Checking the Advanced --> Contrast --> Video Contrast
    print ("Checking the Advanced --> Video Contrast" )
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.2)
    Blue_Back()
    
## Checking the Advanced --> Contrast --> Gamma
    print ("Checking the Advanced --> Gamma" )
    SendKey("Left")
    time.sleep(0.3)
    for count in range(2):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.2)
    Blue_Book_Read()
    SendKey("Down_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.2)

## Checking the Advanced --> Picture Clean
    print ("Checking the Advanced --> Picture Clean" )
    for count in range(2):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(2):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)

## Checking the Advanced --> Picture Clean --> MPEG Artefact Reduction
    print ("Checking the Advanced --> Picture Clean --> MPEG Artefact Reduction" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Right")
        time.sleep(0.2)
    Blue_Book_Read()
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    Blue_Book_Nav()

## Checking the Advanced --> Motion --> Motion Styles
    print ("Checking the Advanced --> Motion --> Motion Styles" )
    for count in range(2):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)

def Sound():
    print ("Sound()- Start of the Function")
    print ("STARTED - Sound Style")
    Launch_Settings_App()
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    
 ## Checking the Sound --> Headphones
    print ("Checking the Sound --> Headphones Volume" )
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
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.2)
    Blue_Book_Read()

 ## Checking the Sound --> Personal Mode Settings --> ATMOS
    print ("Checking the Sound --> Personal Mode Settings --> ATMOS" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)

## Checking the Sound --> Expert Mode Settings --> Clear Dialogue
    print ("Checking the Sound --> Expert Mode Settings --> Clear Dialogue" )
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
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    Blue_Back()

## Checking the Sound --> Expert Mode Settings --> Equalizer
    print ("Checking the Sound --> Expert Mode Settings --> Equalizer" )
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
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.3)
    
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)

    SendKey("Left")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)

    SendKey("Left")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)

    SendKey("Left")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.5)

    print ("STOPPED - Sound")
    ## Checking the Sound --> Advanced
    
def Sound_Advanced():
    Launch_Settings_App()
    print ("Sound_Advanced()- Start of the Function")
       
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Down",0.3,5)
    SendKey("Right")
    time.sleep(0.5)
    SendKey("Right")
    time.sleep(0.4)
    SendKey("Up_longpress",0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)

## Checking the Sound --> Advanced
    print ("Checking the Sound --> Advanced" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(2):
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
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)

    # Checking the Advanced Sound --> Digital out levelling
    print ("Checking the Advanced Sound --> Digital out levelling" )
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)

    # Checking the Advanced Sound --> Digital out delay
    print ("Checking the Advanced Sound --> Digital out Delay" )
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(0.5)
    
    # Checking the Advanced Sound --> Digital out Offset
    print ("Checking the Advanced Sound --> Digital out Offset" )
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down_longpress",0.2,1)
    print ("STOPPED - Sound Advanced")
    
def Ambilight():
    print ("Ambilight()- Start of the Function")
    Launch_Settings_App()
    print ("Ambilight Style - Follow Video")
    for count in range(2):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Up_longpress")
    time.sleep(0.3)
    for count in range(6):
        SendKey("Down")
        time.sleep(0.5)
        SendKey("Ok")
        time.sleep(0.5)
## Ambilight Style - Follow Audio
    print ("Ambilight Style - Follow Audio")
    
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Ok")
        time.sleep(0.5)
    SendKey("Up_longpress")
    time.sleep(0.3)
    for count in range(6):
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.5)
    
## Ambilight Style - Follow Colour
    print ("Ambilight Style - Follow Colour")
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Ok")
        time.sleep(0.5)
    SendKey("Up_longpress")
    time.sleep(0.3)
    for count in range(4):
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.5)

## Ambilight Style - Follow Flag
    print ("Ambilight Style - Follow Flag")
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Ok")
        time.sleep(0.5)
        
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    
    SendKey("Back")
    time.sleep(0.5)
    
## Checking the Ambilight --> Brightness
    print ("Checking the Ambilight -- Brightness" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.25)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)

## Checking the Ambilight --> Saturation
    print ("Checking the Ambilight -- Saturation" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Right")
        time.sleep(0.25)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    print ("STOPPED - Ambilight")

def Ambilight_Advanced():
    Launch_Settings_App()
    print ("Ambilight_Advanced()- Start of the Function")
    for count in range(2):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    for count in range(4):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):   
        SendKey("Right")
        time.sleep(0.3)

    for count in range(3):
        SendKey("Right")
        time.sleep(0.3)
        SendKey("Right")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.5)
    
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)

    SendKey("Ok")
    time.sleep(0.5)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Left")
    time.sleep(0.3)
    for count in range(7):
        SendKey("Ok")
        time.sleep(0.5)
        SendKey("Right")
        time.sleep(0.3)
        SendKey("Left")
        time.sleep(0.3)
            
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.5)
    print ("STOPPING - Ambilight Advanced")
    Blue_Book_Read()
    
def Eco_Settings():
    print ("Eco_Settings()- Start of the Function")
    Launch_Settings_App()
    for count in range(4):
        SendKey("Up")
        time.sleep(0.3)            
    for count in range(3):
        SendKey("Down")
        time.sleep(0.4)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(0.25)
    SendKey("Down")
    time.sleep(0.25)
    SendKey("Ok")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(0.3)

## Checking the Eco Settings - Switch Off Timer
    print ("Checking Eco Settings - Switch Off Timer")
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(3):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    
    SendKey("Down_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.2)
    print ("STOPPING - Eco Setting")
  ## Checking the Region and Language - Languages - Menu Language
    
def Region_Language():
    print ("Region_Language()- Start of the Function")
    
    global Lang_counter
    print ("Language Counter %d" %Lang_counter)
    
    Launch_Settings_App()
    for count in range(5):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(3):    
        SendKey("Right")
        time.sleep(0.3)
    for count in range(2):
        SendKey("Down_longpress")
        time.sleep(.3)
        SendKey("Down_longpress")
        time.sleep(.3)
        SendKey("Up_longpress")
        time.sleep(.2)
        SendKey("Up_longpress")
        time.sleep(.2)
        SendKey("Up_longpress")
        time.sleep(.2)
    SendKey("Ok")
    time.sleep(0.6)
    
    for count in range(25):
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Ok")
        time.sleep(2)

    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    for count in range(Lang_counter):
        SendKey("Down")
        time.sleep(0.5)
    
    time.sleep(3)

##    Help_Navigation(client,16,RedRat_Device_Name,RedRat_Device_Port) ##Navigations in letter = 16 i.e. "S"
    SendKey("Back")
    time.sleep(0.23)
    
## Checking the Region and Language - Languages - Primary Audio
    print ("Region and Language - Languages - Primary Audio" )
    #Launch_Settings_App(client,RedRat_Device_Name,RedRat_Device_Port)
    
        
    for count in range(1):    
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Right")
        time.sleep(0.3)
        
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)

    SendKey("Ok")
    time.sleep(0.7)
    
    for count in range(25):
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Ok")
        time.sleep(0.8)

    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1)

##    Help_Navigation(client,2,RedRat_Device_Name,RedRat_Device_Port) ##Navigations in letter = 2 i.e. "C"
    SendKey("Back")
    time.sleep(0.8)
    #Blue_Book_Nav(client,RedRat_Device_Name,RedRat_Device_Port)

## Checking the Region and Language - Languages - Secondary Audio
    print ("Region and Language - Languages - Secondary Audio" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    #Blue_Book_Read(client,RedRat_Device_Name,RedRat_Device_Port)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)

    SendKey("Ok")
    time.sleep(0.8)
    
    for count in range(25):
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Ok")
        time.sleep(0.8)

    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(1)

##    Help_Navigation(client,4,RedRat_Device_Name,RedRat_Device_Port) ##Navigations in letter = 4 i.e. "E"
    SendKey("Back")
    time.sleep(0.8)
    
## Checking the Region and Language - Languages - Primary Subtitles
    print ("Region and Language - Languages - Primary Subtitles" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    #Blue_Back(client,RedRat_Device_Name,RedRat_Device_Port)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    #Blue_Book_Nav(client,RedRat_Device_Name,RedRat_Device_Port)
    SendKey("Ok")
    time.sleep(0.8)
    
    for count in range(25):
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Ok")
        time.sleep(0.8)

    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    
    SendKey("Ok")
    time.sleep(3)

##    Help_Navigation(client,7,RedRat_Device_Name,RedRat_Device_Port) ##Navigations in letter = 7 i.e. "H"
    SendKey("Back")
    time.sleep(0.8)

## Checking the Region and Language - Languages - Secondary Subtitles
    print ("Region and Language - Languages - Secondary Subtitles" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    #Blue_Back(client,RedRat_Device_Name,RedRat_Device_Port)
    SendKey("Ok")
    time.sleep(0.7)
    
    for count in range(25):
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Ok")
        time.sleep(0.8)

    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(3)

##    Help_Navigation(client,3,RedRat_Device_Name,RedRat_Device_Port) ##Navigations in letter = 3 i.e. D"
    SendKey("Back")
    time.sleep(0.8)
    

## Checking the Region and Language - Languages - Primary Text
    print ("Region and Language - Languages - Primary Text" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)

    SendKey("Ok")
    time.sleep(0.8)
    #Blue_Book_Nav(client,RedRat_Device_Name,RedRat_Device_Port)
    #for count in range(25):
    #    SendKey("Down")
    #    time.sleep(0.25)
    #    SendKey("Ok")
    #    time.sleep(0.8)

    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(3)
    
##    Help_Navigation(client,16,RedRat_Device_Name,RedRat_Device_Port) ##Navigations in letter = 16 i.e. "S"
    SendKey("Back")
    time.sleep(0.8)
        

  ## Checking the Region and Language - Languages - Secondary Text
    print ("Region and Language - Languages - Secondary Text" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(1):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Up_longpress")
    time.sleep(0.2)

    SendKey("Ok")
    time.sleep(0.3)
    
    for count in range(25):
        SendKey("Down")
        time.sleep(0.25)
        SendKey("Ok")
        time.sleep(0.8)

    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(2)

##    Help_Navigation(client,18,RedRat_Device_Name,RedRat_Device_Port) ##Navigations in letter = 18 i.e. "U"
    SendKey("Back")
    time.sleep(0.8)
    Blue_Book_Read(client,RedRat_Device_Name,RedRat_Device_Port)
    print ("STOPPED - Region and Language")
    
def Universal_Access():
    ## Checking the Universal Access
    print ("Universal_Access()- Start of the Function")
    Launch_Settings_App()
    for count in range(7):
        SendKey("Up")
        time.sleep(0.3)            
    for count in range(7):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(3):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.25)
    SendKey("Down")
    time.sleep(0.25)
    SendKey("Ok")
    time.sleep(0.7)

## Checking the Universal Access - Hearing Impaired
    print ("Checking the Universal Access - Hearing Impaired" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.25)
    SendKey("Down")
    time.sleep(0.25)
    SendKey("Ok")
    time.sleep(0.5)

    Help_Navigation(14) ##Navigations in letter = 14 i.e. "P"
    SendKey("Back")
    time.sleep(0.8)

            
## Checking the Universal Access - Audio Description
    print ("Checking the Universal Access - Audio Description" )
    for count in range(1):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.25)
                
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.25)
    SendKey("Down")
    time.sleep(0.25)
    SendKey("Ok")
    time.sleep(0.5)
    
    SendKey("Left")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    Blue_Back()
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)

    Help_Navigation(17) ##Navigations in letter = 17 i.e. "T"
    SendKey("Back")
    time.sleep(0.8)
    print ("STOPPING - Universal Access" )
    ## Checking the Wireless and Networks - Wired or Wifi
    
def Wireless_Networks():
    print ("Wireless_Networks()- Start of the Function")
    Launch_Settings_App()
    for count in range(9):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(2):    
        SendKey("Right")
        time.sleep(0.3)
                
    SendKey("Up_longpress")
    time.sleep(0.3)
    for count in range(4):
        SendKey("Down")
        time.sleep(0.3)
    
    SendKey("Right")
    time.sleep(0.3)
    print ("STARTING - WOWLAN")
    for count in range(5):
        SendKey("Up")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.3)

    SendKey("Left")
    time.sleep(0.3)
    for count in range(2):
        SendKey("Down")
        time.sleep(0.3)
    
    SendKey("Right")
    time.sleep(0.3)
    print ("STARTING - DMR")
    for count in range(5):
        SendKey("Up")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.3)
        SendKey("Ok")
        time.sleep(0.3)

    SendKey("Left")
    time.sleep(0.3)
    for count in range(1):
        SendKey("Down")
        time.sleep(0.3)
    
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Up_longpress")
    time.sleep(0.3)
    print ("STARTING - Wifi ON/OFF")
    for count in range(5):
        SendKey("Up")
        time.sleep(.3)
        SendKey("Ok")
        time.sleep(2)
        SendKey("Down")
        time.sleep(.3)
        SendKey("Ok")
        time.sleep(2)
    print ("STOPPING - Networks")

def Source_selection(Source_Count):
    print ("Source_selection()- Start of the Function")
    print ("Source Selection number : %d" %Source_Count)
    SendKey("Sources")
    time.sleep(5)
    SendKey("Up_longpress")
    time.sleep(1.5)
    for count in range(0,Source_Count):
        SendKey("Down")
        time.sleep(0.5)
    SendKey("Ok")
    time.sleep(4)
    if (Source_Count == 5):
        SendKey("Up_longpress")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.4)
        for count6 in range(4):
            SendKey("Ok")
            time.sleep(2)
        time.sleep(4)
        SendKey("Ok")
        time.sleep(2)

def Language_Selection(counter):
    print ("Language_Selection()- Start of the Function")
    global Lang_counter
    #Lang_counter = random.randrange(0,25,1)
    Lang_counter = counter + 0
    print ("Language Counter value is : %d" %Lang_counter)
    Launch_Settings_App()
    for count in range(6):
        SendKey("Left")
        time.sleep(0.3)
    for count in range(2):
        SendKey("Up_longpress")
        time.sleep(0.3)
    for count in range(5):
        SendKey("Down")
        time.sleep(0.3)
    for count in range(4):
        SendKey("Right")
        time.sleep(0.3)
    
    SendKey("Up_longpress")
    time.sleep(0.5)
    SendKey("Up_longpress")
    time.sleep(0.5)
    
    for count111 in range(0,Lang_counter):
        SendKey("Down")
        time.sleep(0.4)
        
    SendKey("Ok")
    time.sleep(4)

##def Language_Selection_New(Language):
##    #25
##    global Language_List
##    Language_List = ["English","German","Hindi","Tamil","Telugu"]
##    global Lang_Counter
##    Lang_counter = random.choice(Language_List)
##    Launch_Settings_App()
##    for count in range(6):
##        SendKey("Left")
##        time.sleep(0.3)
##    for count in range(2):
##        SendKey("Up_longpress")
##        time.sleep(0.3)
##    for count in range(5):
##        SendKey("Down")
##        time.sleep(0.3)
##    for count in range(4):
##        SendKey("Right")
##        time.sleep(0.3)
##    
##    SendKey("Up_longpress")
##    time.sleep(0.5)
##    SendKey("Up_longpress")
##    time.sleep(0.5)
##    
##    for count111 in range(0,Lang_coun):
##        SendKey("Down")
##        time.sleep(0.4)
##        
##    SendKey("Ok")
##    time.sleep(4)
##    

def Google_Play_Movies():
    print ("Google_Play_Movies()- Start of the Function")
    Home_Positioning_Launch_App(16)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Down")
    time.sleep(0.1)
    SendKey("Right")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(6)

    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(0.4)
  
def How_To_App():
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
    
def Quick_Settings():
        print ("Quick_Settings()- Start of the Function")
    
        SendKey("Settings")
        time.sleep(5)
        SendKey("Up_longpress")
        time.sleep(0.5)
        for count in range(2):
            SendKey("Right")
            time.sleep(0.4)
        
        print (" Checking the Picture Sytle")
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
        print ("Checking the Sound --> Sound Style")
        
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
        print ("Quick Settings - Checking the Ambilight")
        
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
        print ("Ambilight Style - Follow Audio")
        
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
        print ("Ambilight Style - Follow Colour")
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

                        
    ## Ambilight Style - Follow Flag
        print ("Ambilight Style - Follow Flag")
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
        SendKey("Down_longpress")
        time.sleep(0.3)
        SendKey("Right")
        time.sleep(0.3)
        SendKey("Up_longpress")
        time.sleep(0.3)
        SendKey("Down_longpress")
        time.sleep(0.3)
        SendKey("Right")
        time.sleep(0.3)
        SendKey("Up_longpress")
        time.sleep(0.3)
        SendKey("Down_longpress")
        time.sleep(0.3)
        SendKey("Up_longpress")
        time.sleep(0.3)
        SendKey("Right")
        time.sleep(0.3)
        SendKey("Down_longpress")
        time.sleep(0.3)
        
        SendKey("Back")
        time.sleep(1)    

       ## Audio Out
        print ("Audio Out")
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
        print ("Screen Off")
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

        Random_longpress(15)
        
def Blue_Book_Read():
    print ("Blue_Book_Read()- Start of the Function")
    SendKey("Blue")
    time.sleep(4)
    SendKey("Right_longpress")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(1)
    SendKey("Blue")
    time.sleep(1)   

def Blue_Book_Nav():
    print ("Blue_Book_Nav()- Start of the Function")
    SendKey("Blue")
    time.sleep(4)
    SendKey("Left_longpress")
    time.sleep(0.3)
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Right")
    time.sleep(0.3)
    SendKey("Down_longpress")
    time.sleep(0.4)
    SendKey("Down_longpress")
    time.sleep(0.5)
    SendKey("Up_longpress")
    time.sleep(0.4)
    SendKey("Up_longpress")
    time.sleep(0.5)

    for count in range(10):
        SendKey("Right_longpress")
        time.sleep(0.4)
        SendKey("Down_longpress")
        time.sleep(0.5)
        SendKey("Left_longpress")
        time.sleep(0.4)
        SendKey("Right")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(0.3)
    
    Random_longpress(15)
    
    SendKey("Back")
    time.sleep(3)
    
def Rakuten_TV():
    print ("Rakuten_TV()- Start of the Function")        
    SendKey("Rakuten_TV")
    time.sleep(35)
    SendKey("Left")
    time.sleep(3)
    
    for count in range(0,4):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(5)
    
    SendKey("Right")
    time.sleep(2)
    SendKey("Right")
    time.sleep(2)
    SendKey("Ok")
    time.sleep(3)
    for count in range(4):
        SendKey("Down")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(15)
    
    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Rewind")
    time.sleep(2)
    SendKey("Forward")
    time.sleep(2)
    SendKey("Play")
    time.sleep(2)
    SendKey("Pause")
    time.sleep(2)
    SendKey("Forward")
               
def Blue_Back():
    print ("Blue_Back()- Start of the Function")
    SendKey("Blue")
    time.sleep(4)
    SendKey("Back")
    time.sleep(1)
    
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

def ARD_Revanth():
    Home_Positioning_Launch_App(7)
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
    Home_Positioning_Launch_App(9)
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
    SendKey("Sources",1,1)
    SendKey("Down",0.6,2)
    SendKey("Ok",10,1)
    HDMI_QuickSettings_Revanth()

    #4-1
    SendKey("Sources",2,1)
    SendKey("Up",0.6,3)
    SendKey("Ok",10,1)

    #1-3
    SendKey("Sources",3,1)
    SendKey("Up",0.6,2)
    SendKey("Ok",10,1)
    HDMI_QuickSettings_Revanth()
    
    
    
def HDMI_Standby_Revanth():
    #hdmi-1 trickmodes & quicksettings
    SendKey("Sources",3,1)
    SendKey("Up_longpress",0.6,1)
    SendKey("Down",0.3,8)
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
    #1-2-3-4
    for count in range(0,3):
        SendKey("Sources",0.7,1)
        SendKey("Down",0.7,1)
        SendKey("Ok",10,1)
        SendKey("Standby",18,1)
        SendKey("Standby",5,1)
    #4-3-2-1
    for count in range(0,3):
        SendKey("Sources",0.7,1)
        SendKey("Up",0.7,1)
        SendKey("Ok",10,1)
        SendKey("Standby",6,1)
        SendKey("Standby",5,1)
        
    #hdmi-2 trickmodes & quicksettings
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
        
    #2-4
    SendKey("Sources",0.6,1)
    SendKey("Down",0.6,2)
    SendKey("Ok",10,1)
    SendKey("Standby",20,1)
    SendKey("Standby",5,1)

    #4-1
    SendKey("Sources",0.6,1)
    SendKey("Up",0.6,3)
    SendKey("Ok",10,1)
    SendKey("Standby",6,1)
    SendKey("Standby",5,1)

    #1-3
    SendKey("Sources",0.6,1)
    SendKey("Up",0.6,2)
    SendKey("Ok",10,1)
    SendKey("Standby",40,1)
    SendKey("Standby",5,1)



                                          
def Block1():
    
    Digit_Channel_Selection("Tuner",5)
    SendKey("Home",4,1)
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
        
    Sound()
    Sound_Advanced()
    Picture()
    Picture_Advanced()
    Sound()
    Sound_Advanced()
    Ambilight()
    Ambilight_Advanced()
##    Eco_Settings()
##    Universal_Access()
##    Quick_Settings()
##    Help_Navigation(16)
##    Blue_Book_Read()
##    Blue_Book_Nav()
##    Blue_Back() 

    Digit_Channel_Selection("Satellite",83)
    Picture()
    Picture_Advanced()
    Blue_Back()
    Ambilight()
    Ambilight_Advanced()
    Help_Navigation(19)
    Sound()
    Sound_Advanced()
    Blue_Book_Read()
    Universal_Access()
    Eco_Settings()
    Quick_Settings()
    Blue_Book_Nav() 
    
    Digit_Channel_Selection("Tuner",14)
##    Picture()
##    Picture_Advanced()
##    Quick_Settings()
##    Ambilight()
##    Ambilight_Advanced()
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)

    Blue_Book_Nav()
    Sound()
    Sound_Advanced()
    Blue_Book_Read()
    Universal_Access()
    Blue_Back()
    Eco_Settings()
    Help_Navigation(14)

    Digit_Channel_Selection("Satellite",109)
    Blue_Book_Read()
    Picture()
    Picture_Advanced()
##    Blue_Book_Nav()
##    Quick_Settings()
##    Eco_Settings()
##    Universal_Access()
##    Blue_Back()
    Ambilight()
    Ambilight_Advanced()
##    Wireless_Networks()
    Sound()
    Sound_Advanced()
    Help_Navigation(9)
  
    Digit_Channel_Selection("Tuner",20)
    Help_Navigation(10)
    Picture()
    Picture_Advanced()
    Blue_Book_Nav()
    Quick_Settings()
    Universal_Access()
    Sound()
    Sound_Advanced()
    Eco_Settings()
    Blue_Book_Read()
    Ambilight()
    Ambilight_Advanced()
    Blue_Back()

    Digit_Channel_Selection("Satellite",105)
    Universal_Access()
##    Picture()
##    Picture_Advanced()
    Quick_Settings()
    Blue_Book_Nav()
##    Sound()
##    Sound_Advanced()
    Blue_Book_Read()
    Eco_Settings()
    Help_Navigation(5)
##    Ambilight()
##    Ambilight_Advanced()
    Blue_Back()

    Digit_Channel_Selection("Tuner",10)

    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    Quick_Settings()
    Picture()
    Picture_Advanced()
    Sound()
    Sound_Advanced()
    Blue_Book_Read()
    Blue_Back()
    Blue_Book_Nav()
    Eco_Settings()
    Universal_Access()
    Help_Navigation(3)
    Ambilight()
    Ambilight_Advanced()

    Digit_Channel_Selection("Satellite",92)
    Quick_Settings()
    Picture()
    Picture_Advanced()
    Sound()
    Sound_Advanced()
##    Blue_Book_Read()
##    Blue_Back()
##    Blue_Book_Nav()
##    Eco_Settings()
##    Universal_Access()
    Help_Navigation(18)
    Ambilight()
    Ambilight_Advanced()

    Digit_Channel_Selection("Tuner",506)

    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    Sound()
    Sound_Advanced()
##    Blue_Book_Nav()
##    Quick_Settings()
##    Picture()
##    Picture_Advanced()
##    Eco_Settings()
##    Ambilight()
##    Ambilight_Advanced()
##    Blue_Book_Read()
##    Blue_Back()
##    Universal_Access()
##    Help_Navigation(16)
    
    Digit_Channel_Selection("Satellite",86)

    Picture()
    Picture_Advanced()
    Ambilight()
    Ambilight_Advanced()
    Sound()
    Sound_Advanced()
    Blue_Book_Read()
    Blue_Back()
    Quick_Settings()
    Eco_Settings()
    Help_Navigation(13)
    Blue_Book_Nav()
    Universal_Access()

    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    


def Block4():
    Digit_Channel_Selection("Tuner",5)
##    Sound()
##    Sound_Advanced()
##    Picture()
##    Picture_Advanced()
##    Sound()
##    Sound_Advanced()
##    Ambilight()
##    Ambilight_Advanced()
    Eco_Settings()
    Universal_Access()
    Quick_Settings()
    Help_Navigation(16)
    Blue_Book_Read()
    Blue_Book_Nav()
    Blue_Back() 

    Digit_Channel_Selection("Satellite",83)

    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    Picture()
    Picture_Advanced()
    Blue_Back()
    Ambilight()
    Ambilight_Advanced()
    Help_Navigation(19)
    Sound()
    Sound_Advanced()
    Blue_Book_Read()
    Universal_Access()
    Eco_Settings()
    Quick_Settings()
    Blue_Book_Nav() 
    
    Digit_Channel_Selection("Tuner",14)

    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    Picture()
    Picture_Advanced()
    Quick_Settings()
    Ambilight()
    Ambilight_Advanced()
##    Blue_Book_Nav()
##    Sound()
##    Sound_Advanced()
##    Blue_Book_Read()
##    Universal_Access()
##    Blue_Back()
##    Eco_Settings()
##    Help_Navigation(14)

    Digit_Channel_Selection("Satellite",120)
##    Blue_Book_Read()
##    Picture()
##    Picture_Advanced()
    Blue_Book_Nav()
    Quick_Settings()
    Eco_Settings()
    Universal_Access()
    Blue_Back()
##    Ambilight()
##    Ambilight_Advanced()
##    Sound()
##    Sound_Advanced()
##    Help_Navigation(9)
  
    Digit_Channel_Selection("Tuner",20)
    Help_Navigation(10)
    Picture()
    Picture_Advanced()
    Blue_Book_Nav()
    Quick_Settings()
    Universal_Access()
    Sound()
    Sound_Advanced()
    Eco_Settings()
    Blue_Book_Read()
    Ambilight()
    Ambilight_Advanced()
    Blue_Back()

    Digit_Channel_Selection("Satellite",105)
##    Universal_Access()
    Picture()
    Picture_Advanced()
##    Quick_Settings()
##    Blue_Book_Nav()
    Sound()
    Sound_Advanced()
##    Blue_Book_Read()
##    Eco_Settings()
##    Help_Navigation(5)
    Ambilight()
    Ambilight_Advanced()
##    Blue_Back()

    Digit_Channel_Selection("Tuner",10)

    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    Quick_Settings()
    Picture()
    Picture_Advanced()
    Sound()
    Sound_Advanced()
    Blue_Book_Read()
    Blue_Back()
    Blue_Book_Nav()
    Eco_Settings()
    Universal_Access()
    Help_Navigation(3)
    Ambilight()
    Ambilight_Advanced()

    Digit_Channel_Selection("Satellite",182)
##    Quick_Settings()
##    Picture()
##    Picture_Advanced()
##    Sound()
##    Sound_Advanced()
    Blue_Book_Read()
    Blue_Back()
    Blue_Book_Nav()
    Eco_Settings()
    Universal_Access()
##    Help_Navigation(18)
##    Ambilight()
##    Ambilight_Advanced()

    Digit_Channel_Selection("Satellite",120)

    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    Picture()
    Picture_Advanced()
    Ambilight()
    Ambilight_Advanced()
    Sound()
    Sound_Advanced()
    Blue_Book_Read()
    Blue_Back()
    Quick_Settings()
    Eco_Settings()
    Help_Navigation(13)
    Blue_Book_Nav()
    Universal_Access()
    
def Block2():
    
    print ("***** BLOCK - 2 -  Start *****")

    PiP_Without_Standby()
   
    Youtube_Row1_New()

    CBPlayback_Videos()
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    Quick_Settings()
    Help_Navigation(21)
    Blue_Book_Read()
    Blue_Book_Nav()
    Blue_Back()
    Picture()
    Picture_Advanced()
    Sound()
    Sound_Advanced()
    Ambilight()
    Ambilight_Advanced()
    Eco_Settings()
    Universal_Access()

    Netflix(3,4)
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    HbbTV_New()
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    Ambilight()
    Ambilight_Advanced()
    Quick_Settings()
    Sound()
    Sound_Advanced()
    Blue_Back()
    Help_Navigation(11)
    Blue_Book_Read()
    Eco_Settings()
    Universal_Access()
    Picture()
    Picture_Advanced()
    Blue_Book_Nav()

    PiP_Without_Standby()

    Amazon_New(1)
    Eco_Settings()
    Universal_Access()
    Ambilight()
    Ambilight_Advanced()
    Quick_Settings()
    Blue_Back()
    Picture()
    Picture_Advanced()
    Help_Navigation(6)
    Sound()
    Sound_Advanced()
    Blue_Book_Read()
    Blue_Book_Nav()

    CBPlayback_Audios()
    
    How_To_App()

    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)
    
    Blue_Book_Read()
    Blue_Book_Nav()
    Universal_Access()
    Ambilight()
    Ambilight_Advanced()
    Eco_Settings()
    Sound()
    Sound_Advanced()
    Quick_Settings()
    Picture()
    Picture_Advanced()
    Blue_Back()
    Help_Navigation(22)

    Netflix(1,2)
    
    OIB()
    
    SendKey("Exit",2,1)
    SendKey("Options",1,1)
    SendKey('Ok',5,1)

    Quick_Settings()
    Blue_Book_Read()
    Universal_Access()
    Picture()
    Picture_Advanced()
    Eco_Settings()
    Blue_Back()
    Sound()
    Sound_Advanced()
    Ambilight()
    Ambilight_Advanced()
    Blue_Book_Nav()
    Help_Navigation(14)

    CBPlayback_Images()
    
    Youtube_Row2_New()

    PiP_Without_Standby()

    CBPlayback_Videos() 
    
    
    print ("***** BLOCK - 2 -  End *****")

def Block3():
    HDMI_Revanth()
    HDMI()
    
if __name__ == "__main__":
    client = Client();
    client.OpenSocket('localhost', 40000);
    Counter = 1
    RedRat_Device_Name = "No name 15484"
    RedRat_Device_Port = "1"

    for i in range(1000):
        Count = 0
        Language_Selection(Count + i)
        
        try:
            y = time.time()
            Block1()
            z = time.time()
            print ("****************** Block-1 - End - Time taken to Complete Block 1 ()is : %f" %(z-y))
        except:
            pass

        try:
            y = time.time()
            Block2()
            z = time.time()
            print ("****************** Block-2 - End - Time taken to Complete Block 2()is : %f" %(z-y))
        except:
            pass

        try:
            y = time.time()
            Block3()
            z = time.time()
            print ("****************** Block-3 - End - Time taken to Complete Block 3()is : %f" %(z-y))
        except:
            pass

        try:
            y = time.time()
            Block4()
            z = time.time()
            print ("****************** Block-4 - End - Time taken to Complete Block 4()is : %f" %(z-y))
        except:
            pass





