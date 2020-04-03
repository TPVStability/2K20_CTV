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
    
    
def Digit_Zap_Satellite_1(client,RedRat_Device_Name,RedRat_Device_Port,Digit_Zap_Count):
    for count in range(Digit_Zap_Count):
        Digit_Zap_List_Sat_1 = ["1","3",["2","8"],"9","5","1","7","4","8","2","0",["1","1"],["1","5"],["2","3"],["3","1"],["1","2"],"6", ["3","2"], ["1","4"],["1","6"],["2","0"],["2","1"],["2","2"],["2","9"]]

        Digit_Zap_List_Sat_Temp_1 = random.choice(Digit_Zap_List_Sat_1)
        
        if type(Digit_Zap_List_Sat_Temp_1) is list:
            for x in range(0,len(Digit_Zap_List_Sat_Temp_1)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Digit_Zap_List_Sat_Temp_1[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            time.sleep(1)
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Digit_Zap_List_Sat_Temp_1) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(1)
            
def Random_Zap_2(client,RedRat_Device_Name,RedRat_Device_Port,Zap_Count_2):
    for count in range(Zap_Count_2):
        Zap_List_2 = ["Channel_Up","Down",["2","8"],"9","Channel_Down","1","Up","4","8","2","0",["1","1"],["1","5"],["2","3"],["3","1"],["1","2"],"6", ["3","2"], "Up_longpress","Down_longpress"]

        Zap_List_Temp_2 = random.choice(Zap_List_2)
        
        if type(Zap_List_Temp_2) is list:
            for x in range(0,len(Zap_List_Temp_2)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_2[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            time.sleep(3)
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Zap_List_Temp_2) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(3)    


def Switch_BN_Sources(client,RedRat_Device_Name,RedRat_Device_Port):
    #Perform switching between different sources
    time.sleep(5)
    for count in range(0,5):
        SendKey("Sources")
        time.sleep(3)
        SendKey("Up_longpress")
        time.sleep(0.3)
        SendKey("Down")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(3)
        for count in range(0,10):
            SendKey("Sources")
            time.sleep(2)
            SendKey("Down")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(4)        
        time.sleep(2)
    time.sleep(5)

def Help_Nav(client,RedRat_Device_Name,RedRat_Device_Port):
## Help Navigation
    SendKey("Blue")
    time.sleep(4)
    SendKey("Right")
    
    SendKey("Down_longpress")
    time.sleep(1)
    SendKey("Right_longpress")
    time.sleep(1)
    SendKey("Down_longpress")
    time.sleep(1)
    SendKey("Right_longpress")
    time.sleep(1)
    SendKey("Back")
    time.sleep(1)

## Switch to Satellite
    SendKey("Exit")
    for count in range(3):
        SendKey("Channel_Up")
        time.sleep(3)

    for count in range(3):
        SendKey("Channel_Down")
        time.sleep(3)
        
    SendKey("TVGuide")
    time.sleep(2)
    
    for count in range(3):
        SendKey("Down_longpress")
        time.sleep(1)
        SendKey("Right_longpress")
        time.sleep(1)
        SendKey("Left_longpress")
        time.sleep(1)
        
    SendKey("Sources")
    
## Switch to Antenna    
    for count in range(5):
        SendKey("Up")
        time.sleep(.15)
        
    for count in range(3):
        SendKey("Down")
        time.sleep(.15)
        
    SendKey("Ok")
    time.sleep(3)
    SendKey("Home")
    time.sleep(4)
    

def Post_Virgin(client,RedRat_Device_Name,RedRat_Device_Port):
    Switch_To_Tuner(client,RedRat_Device_Name,RedRat_Device_Port)
    Digit_Zap_Satellite_1(client,RedRat_Device_Name,RedRat_Device_Port,10)
    Random_Zap_2(client,RedRat_Device_Name,RedRat_Device_Port,10)
    SendKey("Standby")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(15)
    Help_Nav(client,RedRat_Device_Name,RedRat_Device_Port)
    Switch_BN_Sources(client,RedRat_Device_Name,RedRat_Device_Port)
    
def Virgin_Installation(client,RedRat_Device_Name,RedRat_Device_Port):
    #Empty script
    #print time.time()
    #utils.tm = tm;
    
    #UK, Sweden, Poland, Norway, Ireland, Germany, Finland
    ##google sign,Home use,install channels
    ##Select Home
    
    virgin = 1
    country = 1
    Lang_Count = 1
    
    while (virgin < 10):
        Shop_mode = 0
        y = time.time()
        print ("Round : %d" %virgin)
        if (virgin == 11):
            Shop_mode = 1

        SendKey("Exit")
        time.sleep(4)
        SendKey("Settings")
        time.sleep(7)
        for count in range(0,15):
            SendKey("Down")
            time.sleep(.3)
        
        SendKey("Up")
        time.sleep(2)
        SendKey("Ok")
        time.sleep(3)
        for count in range(0,4):
            SendKey("Down")
            time.sleep(1)
        SendKey("Right")
        time.sleep(1)
        for count in range(0,12):
            SendKey("Down")
            time.sleep(0.4)
            
    # Factory settings reset
        print ("Factory settings reset")
        SendKey("Up")
        time.sleep(1)
        SendKey("Up")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(2)
        SendKey("Right")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(18)

        print ("Trigger Reinstall TV")
        SendKey("Down")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(3)
        SendKey("Right")
        time.sleep(2)
        SendKey("Ok")
        
        if (virgin == 1):
            print ("waiting for 200 secs virgin to begin" )
            time.sleep(200)
        else:
            print ("waiting for 180 sec virgin to begin" )
            time.sleep(180)

        SendKey("Standby")
        time.sleep(20)
        SendKey("Standby")
        time.sleep(8)

        SendKey("Standby")
        time.sleep(20)
        SendKey("Channel_Up")
        time.sleep(6)

        SendKey("Standby")
        time.sleep(10)
        SendKey("Standby")
        time.sleep(5)
        
        SendKey("Channel_Up")
        time.sleep(5)
        
    # Press OK on Ok screen
        SendKey("Ok")
        time.sleep(8)

    # Select Launguage
    # 1-UK-English, 2-Sweden-Swedish(Svenska), 3-Germany-German, 4-Spain- Espanol, 5-Italy-Italiano, 6-France-French, , 7-Poland-Eesti Lang(polish), 8-Denmark - Danish (Dansk), 9-Finland-Finnish Suomi
        print ("Select Language")
        if (Lang_Count == 2):
            for count in range(0,25):
                SendKey("Down")
                time.sleep(.7)
        elif (Lang_Count == 3):
            SendKey("Up")
            time.sleep(.7)
        elif (Lang_Count == 4):
            SendKey("Down")
            time.sleep(.7)
        elif (Lang_Count == 5):
            for count in range(0,7):
                SendKey("Up")
                time.sleep(.7)
        elif (Lang_Count == 6):
            for count in range(0,4):
                SendKey("Down")
                time.sleep(.7)
        elif (Lang_Count == 7): # Differrnt Screens after lang selection. Need to recheck
            for count in range(0,2):
                SendKey("Down")
                time.sleep(.7)
        elif (Lang_Count == 8):
            for count in range(0,2):
                SendKey("Up")
                time.sleep(.7)
        elif (Lang_Count == 9):
            for count in range(0,24):
                SendKey("Down")
                time.sleep(.7)
                
        SendKey("Ok")
        time.sleep(100)
        
##        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
##        time.sleep(5)
##        
##        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
##        time.sleep(30)
        
##        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
##        time.sleep(6)

        SendKey("Standby")
        time.sleep(20)
        SendKey("Standby")
        time.sleep(9)

        SendKey("Standby")
        time.sleep(14)
        SendKey("Channel_Down")
        time.sleep(12)


##    # Select Launguage
##        print "Select Language"
##        for i in range(0,Lang_Count):
##            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
##            time.sleep(0.5)
##        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
##        time.sleep(120)

    # Select Google account
        if (Shop_mode == 0):            
            print ("select Google account")
            SendKey("Ok")
            time.sleep(25)
            SendKey("Down")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(40)
            
            Send_Text_Keys(client,RedRat_Device_Name,RedRat_Device_Port,"stabmsafp6")
            time.sleep(8)
            SendKey("Enter")
            time.sleep(15)
            Send_Text_Keys(client,RedRat_Device_Name,RedRat_Device_Port,"abc12345@")
            time.sleep(8)
            SendKey("Enter")
            time.sleep(15)
        else:
            SendKey("Down")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(10)
            
    # Select Google Terms of Service

        SendKey("Standby")
        time.sleep(18)
        SendKey("3")
        time.sleep(8)

        SendKey("Standby")
        time.sleep(25)
        SendKey("Home")
        time.sleep(10)

        SendKey("Standby")
        time.sleep(17)
        SendKey("Standby")
        time.sleep(8)

        SendKey("Channel_Up")
        time.sleep(5)
        
        SendKey("Ok")
        time.sleep(8)
        
    # Select Location
        SendKey("Ok")
        time.sleep(6)
        
    # Select Android performance
        SendKey("Ok")
        time.sleep(10)
        
#        if (Lang_Count == 2 or Lang_Count == 3 or Lang_Count == 6): #0-English
#            for count in range(5):
#                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
#                time.sleep(3)
    # Lets Walk though features of your Device.. Screen 3 Rights and OK required
    
        for count in range(3):
            SendKey("Ok")
            time.sleep(2)
            
        for count in range(6):
            SendKey("Right")
            time.sleep(1)
##        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")    
##        time.sleep(5)
        
    #Select TV Name
##        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
##        time.sleep(8)

        SendKey("Standby")
        time.sleep(18)
        SendKey("1")
        time.sleep(7)

        SendKey("Standby")
        time.sleep(17)
        SendKey("Standby")
        time.sleep(10)

##        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
##        time.sleep(2)
        
        SendKey("Standby")
        time.sleep(5)
        SendKey("Home")
        time.sleep(4)

        SendKey("Standby")
        time.sleep(4)
        SendKey("Exit")
        time.sleep(4)

        SendKey("Standby")
        time.sleep(22)
        SendKey("Channel_Up")
        time.sleep(14)
        
    #Select Country
    #UK, Sweden, Poland, Norway, Ireland, Germany, Finland
    # UK - 0 , Sweden - 6, Poland - 15, Norway - 13, Ireland - 24, Germany -42, Finland - 29, Denmark - 35, Spain - 5
    # 1st Lang = English, UK, 2nd Lang Espanol, 3rd Lang Eesti, 4th lang - Eyynvlka, 5th Lang Francais, 6th lang  Gaeilege , 7th Lang Hrvastski , 8th lang Italinoa, 9th Lang ka3akwa

    # 1-UK-English, 2-Sweden-Swedish, 3-Germany-German(Deutsche), Spain- Espanol, Italy-Italiano, France-French, , Poland-Eesti Lang(polish), Denmark - Danish (Dansk), Finland-Finnish Suomalainen
    
#        print ("Select Country for channel installation")
#        up_count = 0
#
#        if (country == 1): # UK - UpCount=1 For English Lang, (Language0)
#            up_count = 1
#            
#        elif (country == 2): # For Espanol language (Language1) - Spanish Language, 
#            up_count = 3
#            
#        elif (country == 3):# 36 ups - Germany Country, Deutsche, DeutscheLand Country Name
#            up_count = 36
#            
#        elif (country == 4): # Poland (poola), Eesti Lang [For Google Assistant] (Language2)
#            up_count = 19
#            
#        elif (country == 5): # Eyynvlka (Greek Language),  (Language3 = Norway)
#            up_count = 13
#            
#        elif (country == 6):  # Francais, (Language4), France Country
#            up_count = 28
#            
#        elif (country == 7): # Language5, Gaelige (Language), irish Language- Eire Country - 4 Ups
#            up_count = 4
#            
#        elif (country == 8): # Language6, Hrvatski, Croatia Country, Country Name = Hrvatska
#            up_count = 27
#            
#        elif (country == 9): # Language 7 , Italiano Language, Italy country, 23 Ups
#            up_count = 23
#            
#        elif (country == 10): #Language 8 - Kazakh Launguage(ka3akwa), Kazakhstan(Kaeakctah)- 24 Ups 
#            up_count = 24
#            
#        elif (country == 11):# Language -9 - Latviesu (Latvian Language), Latvija Country
#            up_count = 0
#
#        for count in range(0,47):
#            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
#            time.sleep(0.5)

#        for count in range(0,up_count):
#            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Up" output=\"' + RedRat_Device_Port+"\"\'")
#            time.sleep(0.5)
#        time.sleep(5)    
#        if (country == 9):
#            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
#            time.sleep(10)
#        if (country == 10):
#            for k in range(3):
#                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
#                time.sleep(2)
#            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
#            time.sleep(10)
        #print "country %d:" %country
    
        SendKey("Ok")
        time.sleep(14)
        
        if (Lang_Count == 5 or Lang_Count == 6):
           for count in range(1):
               Send_Text_Keys(client,RedRat_Device_Name,RedRat_Device_Port,"11111111")
               time.sleep(3)
        
    #Select Home Use
        if (Shop_mode == 0):
            SendKey("Ok")
            time.sleep(20)
        else:
            SendKey("Down")
            time.sleep(15)
            SendKey("Ok")
            time.sleep(10)
            for count in range(9):
                SendKey("Down")
                time.sleep(2)
            SendKey("Right")
            time.sleep(13)
            SendKey("Ok")
            time.sleep(10)
            SendKey("Ok")
            time.sleep(10)

    #Select Philips Smart TV
        if (Shop_mode == 0):
            
            SendKey("Down")
            time.sleep(3)
            SendKey("Down")
            time.sleep(4)
            SendKey("Ok")
            time.sleep(10)
                    
        #Install Antenna Channels
            SendKey("Ok")
            time.sleep(5)
            print ("Select Antennal Channels Installation")
            SendKey("Ok")
            time.sleep(5)
            SendKey("Up")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(5)
            SendKey("Down")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(12)
            SendKey("Ok")
            print ("Waiting for Antenna Installation to finish")
            time.sleep(20)

            SendKey("Standby")
            time.sleep(20)
            SendKey("Home")
            time.sleep(9)

            SendKey("Standby")
            time.sleep(14)
            SendKey("Standby")
            time.sleep(7)
            
            SendKey("Standby")
            time.sleep(18)
            SendKey("Standby")
            time.sleep(9)
            
            SendKey("Up")
            time.sleep(5)
            
            SendKey("Ok")
            time.sleep(12)
            print ("Select Antennal Channels Installation")
            SendKey("Ok")
            time.sleep(5)
            SendKey("Up")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(5)
            SendKey("Down")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(10)
            SendKey("Ok")
            print ("Waiting for Antenna Installation to finish")
            time.sleep(240)
            
            SendKey("Ok")
            time.sleep(4)
            if not(country == 1):
                SendKey("Ok")
                time.sleep(6)
            
        # Install Satellite
            SendKey("Ok")
            time.sleep(8)
            SendKey("Ok")
            time.sleep(8)
            SendKey("Ok")
            print ("Search for Satellite  Channels Installation")
            time.sleep(40)
                
            SendKey("Standby")
            time.sleep(20)
            SendKey("8")
            time.sleep(8)

            SendKey("Up")
            time.sleep(4)
            
            SendKey("Ok")
            time.sleep(8)
            SendKey("Ok")
            time.sleep(10)
            SendKey("Ok")
            print ("Search for Satellite  Channels Installation")
            
            time.sleep(200)
            
            SendKey("Ok")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(5)
            
#            for count in range(15):
#                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
#                time.sleep(1)
#            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
            print ("waiting for satellite installation to complete")
            
            time.sleep(20)
                
            SendKey("Standby")
            time.sleep(20)
            SendKey("Standby")
            time.sleep(12)
            
            SendKey("Channel_Up")
            time.sleep(10)
        

            SendKey("Up")
            time.sleep(8)
            
            SendKey("Ok")
            time.sleep(13)
            SendKey("Ok")
            time.sleep(13)
            SendKey("Ok")
            print ("Search for Satellite  Channels Installation")
            time.sleep(200)
            
            SendKey("Ok")
            time.sleep(6)
            SendKey("Ok")
            time.sleep(6)
#            for count in range(15):
#                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
#                time.sleep(1)
#            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
            print ("waiting for satellite installation to complete")
            time.sleep(240)
            SendKey("Ok")
            time.sleep(10)
            SendKey("Ok")
            time.sleep(5)            

            print ("Finish quick settings")
            time.sleep(3)
            SendKey("Ok")
            time.sleep(3)
            SendKey("Down")
            time.sleep(4)
            SendKey("Down")
            time.sleep(4)
            SendKey("Down")
            time.sleep(7)
            SendKey("Down")
            time.sleep(6)
            SendKey("Ok")
            time.sleep(17)
            
        # Select 
            SendKey("Down")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(13)
            SendKey("Ok")
            time.sleep(13)
            SendKey("Ok")
            time.sleep(9)
            SendKey("Ok")
            time.sleep(13)

            time.sleep(120)
            SendKey("Ok")

        #Turn on Playprotect message is seen
        print ("Wait for Turn on Play Protect Message"    )
        time.sleep(60)
        SendKey("Down")
        time.sleep(2)
        SendKey("Down")
        time.sleep(2)
        SendKey("Right")
        time.sleep(2)
        SendKey("Ok")
        time.sleep(60)
        # Better to wait for 2 minutes atleast    
    ##    # Welcome to Android TV screen
    ##        print "Select Right keys for recommendation screen"
    ##        for count1 in range(0,15):
    ##            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Right" output=\"' + RedRat_Device_Port+"\"\'")
    ##            time.sleep(0.5)
    ##        time.sleep(5)
    ##        
    ##        if(Lang_Count == 11):
    ##            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
    ##            time.sleep(45)
    ##        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
    ##        time.sleep(20)
                
        # Exit to channels

        try:
            
            Post_Virgin(client,RedRat_Device_Name,RedRat_Device_Port)
        except:
            pass
        
        print ("Waiting for App updates")
        time.sleep(280)
        print ("exit to watch TV")
        SendKey("Exit")
        time.sleep(15)
        SendKey("Exit")
        time.sleep(10)
        virgin = virgin + 1

        print ("DS-VirginInstallation -- Time taken to complete one round of Virgin Installation is: %f" %(time.time()-y))
        
        country = country + 1
        Lang_Count = Lang_Count + 1
        
def Send_Text_Keys(client,RedRat_Device_Name,RedRat_Device_Port,URL):
    
    for x in range(0,len(URL)):
        
        if URL[x] == "\\":
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str("bslash") + "\"" ' output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(.5)
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(URL[x]) + "\"" ' output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(.5)

#Virgin_Installation_Shop_Mode(client,RedRat_Device_Name,RedRat_Device_Port):
    
def Start_RedRat_Script():
                       
    client = Client()
    client.OpenSocket('localhost', 40000)
    RedRat_Device_Name = "RedRat-X 23188"
    RedRat_Device_Port = "1"
    #Set_Date_Time_Hub.Set(client,RedRat_Device_Name,RedRat_Device_Port)
    for i in range(100):
        Virgin_Installation(client,RedRat_Device_Name,RedRat_Device_Port)
        #Virgin_Installation_Shop_Mode(client,RedRat_Device_Name,RedRat_Device_Port)
                              
if __name__ == "__main__":
    Start_RedRat_Script()
