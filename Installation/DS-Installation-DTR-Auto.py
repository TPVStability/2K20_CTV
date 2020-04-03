import time
import socket
import random

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

Random_Standby_Wakeup_List = ["Exit","Home","Netflix","Ambilight",0, "Channel_Up", "Channel_Down", "7"]

def Freq_Installation_610():
    y = time.time()
    print ("Start of the Function Freq_Installation_610()")    
    SendKey("Home")
    time.sleep(5)
    for count in range(0,6):
        SendKey("Up")
        time.sleep(0.15)
    time.sleep(3)
    for count in range(0,5):
        SendKey("Right")
        time.sleep(0.2)
    time.sleep(3)
    SendKey("Ok")
    time.sleep(4)
    for count in range(0,15):
        SendKey("Down")
        time.sleep(0.15)
    SendKey("Up")
    time.sleep(2)
    for count in range(0,2):
        SendKey("Ok")
        time.sleep(3)
    for count in range(0,3):
        SendKey("Down")
        time.sleep(0.5)
    for count in range(0,1):
        SendKey("Ok")
        time.sleep(0.3)    
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.3)                
    SendKey("6")
    time.sleep(0.2)
    SendKey("1")
    time.sleep(0.1)
    SendKey("0")
    time.sleep(0.1)
    SendKey("0")
    time.sleep(0.1)
    SendKey("0")
    time.sleep(0.1)
    SendKey("Ok")
    time.sleep(15)
    SendKey("Ok")
    time.sleep(3)
    SendKey("Ok")
    time.sleep(3)
    SendKey("Exit")
    time.sleep(5)    
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(12)
    print ("End of the Function Freq_Installation_610()")

    z = time.time()

    print ("Time taken to Complete Freq_Installation_610() is : %f" %(z-y))
    
def Freq_Installation(Inputfrequecy):
    y = time.time()
    ##Perform Frequency installation - 602 Frequency
    SendKey("Home",5,1)
    SendKey("Up",0.15,6)
    SendKey("Right",3,5)
    SendKey("Ok",4,1)
    SendKey("Down_longpress",1,2)
    SendKey("Up",2,1)
    SendKey("Ok",3,2)
    SendKey("Down",0.3,6)
    SendKey("Up",0.5,1)
    
    SendKey("Ok",2,1)    
    SendKey("Down",0.7,1)
    SendKey("Ok",2,1)
    if Inputfrequecy == 602:        
        SendKey("6",0.2,1)
        SendKey("0",0.1,1)
        SendKey("2",0.1,1)
        SendKey("0",0.1,2)
    elif Inputfrequecy == 178:
        SendKey("1",0.2,1)
        SendKey("7",0.1,1)
        SendKey("8",0.1,1)
        SendKey("0",0.1,2)
    elif Inputfrequecy == 666:
        SendKey("6",0.2,1)
        SendKey("6",0.1,2)
        SendKey("0",0.1,2)
    elif Inputfrequecy == 594:
        SendKey("5",0.2,1)
        SendKey("9",0.1,1)
        SendKey("4",0.1,1)
        SendKey("0",0.1,2)
    elif Inputfrequecy== 474:
        SendKey("4",0.2,1)
        SendKey("7",0.1,1)
        SendKey("4",0.1,1)
        SendKey("0",0.1,2)
    else:
        SendKey("6",0.2,1)
        SendKey("1",0.1,1)
        SendKey("2",0.1,1)
        SendKey("0",0.1,2)
    SendKey("Ok",15,1)
    SendKey("Ok",3,1)
    SendKey("Ok",2,1)
    SendKey("Exit",3,1)
    SendKey("Standby",10,1)
    SendKey("Standby",6,1)

    z = time.time()

    print ("Time taken to Complete Freq_Installation_602() is : %f" %(z-y))
        
            
def Satellite_Installation():
    y = time.time()
    print ("Start of the Function Satellite_Installation()")            
    SendKey("Exit")
    time.sleep(2)
    SendKey("Exit")
    time.sleep(1)    
    SendKey("Home")
    time.sleep(5)
    for count in range(0,1):
        SendKey("Up_longpress")
        time.sleep(0.15)
    time.sleep(0.5)            
    for count in range(0,1):
        SendKey("Right_longpress")
        time.sleep(0.2)
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(4)            
    for count in range(0,1):
        SendKey("Down_longpress")
        time.sleep(0.15)
    SendKey("Up")
    time.sleep(2.5)    
    for count in range(0,1):
        SendKey("Ok")
        time.sleep(2.5)                
    for count in range(0,1):
        SendKey("Down")
        time.sleep(1)                
    for count in range(0,1):
        SendKey("Ok")
        time.sleep(6) # Selecting Satellite Channel
        

##            if (flag == 1):
##                SendKey("Ok",2,3)
##                time.sleep(100)
##                SendKey("Ok")
##                time.sleep(1)
##                SendKey("Ok")
##                time.sleep(240)
##                SendKey("Ok")
##                time.sleep(3)
##                SendKey("Ok")
##                time.sleep(3)
##            else:
        SendKey("Ok")
        time.sleep(1)
        SendKey("Up")
        time.sleep(1)
        SendKey("Up")
        time.sleep(1)
        SendKey("Down")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(1)
        SendKey("Right")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(140)
        SendKey("Ok")
        time.sleep(1)
        SendKey("Ok")
        time.sleep(240)
        SendKey("Ok")
        time.sleep(3)
        SendKey("Ok")
        time.sleep(3)
    print ("End of the Function Satellite_Installation()")

    z = time.time()

    print ("Time taken to Complete Satellite_Installation() is : %f" %(z-y))

global lastcountry
lastcountry=""

def Auto_Installation(Country,Installtype,Installation): # Country='Sweden', Installtype: DVBC/DVBT, Installation : Advanced/Update
    y = time.time()
    global lastcountry

    Country1=['Germany','Netherlands','UK','Sweden','Poland','Norway','Czech','Slovakia','Slovenia','Finland','Belarus','Ukraine','Estonia','Luxembourg']
    Country1_Keys=[28,4,2,6,14,15,34,9,8,31,39,1,32,18]
    Country2=['Turkey','Albania','Khazakistan','Georgia','Other']
    Country2_Keys=[3,44,21,29,0]
    Country3=['Spain','Russia']
    Country3_Keys=[7,11]

    print ("Country %f" ,Country)
    SendKey('Home',5,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Right_longpress",0.2,1)
    SendKey("Ok",4,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Up",0.2,1)
    SendKey("Ok",2,4)
    
    print ("lastcountry %f" ,lastcountry)
    if lastcountry in Country2:
        print ("Entered in to If Loop")
        if Country == 'Belarus':
            SendKey('Down',1,3)
            SendKey('Ok',2,1)
            SendKey('Down_longpress',1,6)# Country Selection - Focus is on Others
        SendKey('Down_longpress',1,6)
        if Country in Country1:
            SendKey('Up',1,Country1_Keys[Country1.index(Country)])
            SendKey("Ok",2,1)
        elif Country in Country2:
            SendKey('Up',1,Country2_Keys[Country2.index(Country)])
            SendKey("Ok",2,1)
            if Country == 'Khazakistan':
                SendKey("Ok",2,1)
        elif Country in Country3:
            SendKey('Up',1,Country3_Keys[Country3.index(Country)])
            SendKey("Ok",2,1)
        print ("Country in Country2 List")
        
        if Installtype=='DVBC':
            SendKey('Down',1,1)
            SendKey('Ok',2,2)
            if Country =='Czech':
                SendKey('Ok',3,1)
                SendKey('Left',1,1)
                SendKey('Ok',240,1)
                
            elif Country =='Slovakia':
                print("Entered Slovakia in if Condition")
                SendKey('Left',2,1)
                SendKey('Ok',240,1)

            elif Country =='Ukraine':
                SendKey('Ok',240,1)                

            elif Country =='Luxembourg':
                SendKey('Ok',2,1)
                SendKey('Left',2,1)
                SendKey('Ok',240,1)
                
            elif Country =='Slovenia':
                SendKey('Down_longpress',1,1)
                SendKey('Ok',2,1)
                SendKey("Up",1,1)
                SendKey("Ok",2,1)
                
            elif Country =='Poland':
                SendKey("Up",1,1)
        if (Country in {'Czech', 'Luxembourg' ,'Slovakia','Ukraine'}):
            pass
        else:
            for count in range(0,2):
                SendKey('Up',1,1)
                SendKey('Ok',2,1)

            # Configure for Full Installation
            SendKey('Down',1,1)
            SendKey('Ok',2,1)
            SendKey('Right',1,1)
            SendKey('Down',1,1)
            SendKey('Ok',2,1)
            SendKey('Back',1,1)
            SendKey('Up',1,1)
            
    elif (lastcountry not in Country2) and (lastcountry not in Country1):
        print ("Entered in to Elif Loop")
        SendKey('Down_longpress',2,4)# Country Selection - Focus is on Others
        if Country in Country1:
            SendKey('Up',1,Country1_Keys[Country1.index(Country)])
            SendKey("Ok",2,1)
        elif Country in Country2:
            SendKey('Up',1,Country2_Keys[Country2.index(Country)])
            SendKey("Ok",2,1)
        elif Country in Country3:
            SendKey('Up',1,Country3_Keys[Country3.index(Country)])
            SendKey("Ok",2,2)

        if (Country in {'Czech', 'Luxembourg' ,'Slovakia','Ukraine'}):
            pass
        else:
            for k in range(0,2):
                SendKey("Ok",2,1)
                SendKey("Up",1,1)
                         
            # Configure for Full Installation
            SendKey('Down',1,1)
            SendKey('Ok',2,1)
            SendKey('Right',1,1)
            SendKey('Down',1,1)
            SendKey('Ok',2,1)
            SendKey('Back',1,1)
            SendKey('Up',1,1)
                
    else:
        print ("Entered in to Else Loop")
        if Installation=="Advanced":
            SendKey('Down',1,3)
            SendKey('Ok',2,1)
            SendKey('Down_longpress',2,4)# Country Selection - Focus is on Others
            if Country in Country1:
                SendKey('Up',1,Country1_Keys[Country1.index(Country)])
                SendKey("Ok",2,1)
            elif Country in Country2:
                SendKey('Up',1,Country2_Keys[Country2.index(Country)])
                SendKey("Ok",2,1)
            elif Country in Country3:
                SendKey('Up',1,Country3_Keys[Country3.index(Country)])
                SendKey("Ok",2,2)

            if Installtype=='DVBC':
                SendKey('Down',1,1)
                SendKey('Ok',2,2)
                if Country =='Slovenia':
                    SendKey('Down_longpress',1,1)
                    SendKey('Ok',2,1)
                    SendKey("Up",1,1)
                    SendKey("Ok",2,1)
                    
                elif Country =='Poland':
                    SendKey("Up",1,1)
                    
                elif Country =='Czech':
                    SendKey('Ok',3,1)
                    SendKey('Left',1,1)
                    SendKey('Ok',240,1)
                    
                elif Country =='Slovakia':
                    SendKey('Ok',2,1)
                    SendKey('Left',2,1)
                    SendKey('Ok',240,1)

                elif Country =='Ukraine':
                    SendKey('Ok',240,1)

                elif Country =='Luxembourg':
                    SendKey('Ok',2,1)
                    SendKey('Left',2,1)
                    SendKey('Ok',240,1)
        
                elif (Country in {'Czech', 'Luxembourg' ,'Slovakia','Ukraine'}):
                    pass

            else:
                for k in range(0,2):
                    SendKey("Up",1,1)
                    SendKey("Ok",2,1)
                    SendKey("Up",1,1)
                         
                # Configure for Full Installation
                SendKey('Down',1,1)
                SendKey('Ok',2,1)
                SendKey('Right',1,1)
                SendKey('Down',1,1)
                SendKey('Ok',2,1)
                SendKey('Back',1,1)
                SendKey('Up',1,1)
        else:
            SendKey('Up',1,3)
            SendKey('Ok',2,2)
            
    if (Country in {'Slovakia', 'Ukraine'}):
        pass
    else:
        SendKey('Ok',240,1)# install time
        
    SendKey('Ok',2,2)
    SendKey('Exit',5,1)
    
    lastcountry=Country

    z = time.time()

    print ("Time taken to Complete Auto_Installation() is : %f" %(z-y))

def PostConditionchecks():
    y = time.time()
    print ("Start of the Function PostConditionchecks()")
    SendKey('Exit',1,2)
    SendKey('TvGuide',5,1)
    SendKey('Right_longpress',0.3,5)
    SendKey('Left_longpress',0.3,1)
    SendKey('Down_longpress',0.3,5)
    SendKey('Up_longpress',0.3,4)
    SendKey('Exit',2,1)
    SendKey('Channel_Up',1,10)
    SendKey('Text',1,10)
    SendKey('Home',5,1)
    SendKey('Up_longpress',1,2)
    SendKey('Down',1,1)
    SendKey('Left_longpress',1,2)
    SendKey('Right',1,1)
    SendKey('Ok',5,1)
    SendKey('Ok',10,1)
    SendKey('Exit',2,1)
    SendKey('Record',30,1)
    SendKey('Stop',1,1)
    SendKey('Right',1,1)
    SendKey('Ok',2,1)
    SendKey('Channel_Up',1,3)
    SendKey('Pause',30,1)
    SendKey('Play',1,1)
    SendKey('Exit',1,1)
    print ("End of the Function PostConditionchecks()")

    z = time.time()

    print ("Time taken to Complete PostConditionchecks() is : %f" %(z-y))

def DTR_Installation():
    #global flag
    y = time.time()
    # Perform DTR Installation
    print ("Start of the Function DTR_Installation()")    
    SendKey("1")
    time.sleep(5)
    SendKey("Home")
    time.sleep(5)
    for count in range(0,6):
        SendKey("Up_longpress")
        time.sleep(1)
    time.sleep(3)
    for count in range(0,5):
        SendKey("Right")
        time.sleep(0.2)
    time.sleep(3)
    SendKey("Ok")
    time.sleep(4)
    for count in range(0,2):
        SendKey("Down_longpress")
        time.sleep(1)
    SendKey("Up")
    time.sleep(2)
    for count in range(0,2):
        SendKey("Ok")
        time.sleep(2)
    for count in range(0,3):
        SendKey("Down")
        time.sleep(1)
    for count in range(0,1):
        SendKey("Ok")
        time.sleep(1)
    time.sleep(3)
    SendKey("Down")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(16)
    SendKey("Ok")
    time.sleep(3)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Exit")
    time.sleep(3)
    print ("End of the Function DTR_Installation()")

    z = time.time()

    print ("Time taken to Complete DTR_Installation() is : %f" %(z-y))
    #flag = 1
            
def Test_Scenarios(client,RedRat_Device_Name,RedRat_Device_Port):
    y = time.time()
    print (time.time())
    
    ## CRFL 1 Line Should be used for testing
    ## CRFL 6 Line Should be used for testing
    ## Auto Installation for the Following Countries - UK, Sweden, Poland, Norway, Ireland, Germany, Finland
    ## DTR Installation
    ## Manual Frequency Installation - 177.5, 602, 610, 722  Frequencies
    ## Be on Watch TV before starting the test
    ## Analog Manual Installtion - 535, 224, 133
    
    for Installation in range(0,1000):
        print (time.time())
        for Auto in range(0,1):
         ## DVB-S Installation

    
            # Perform Zapping
            for count in range (0,10):
                SendKey("Channel_Up")
                time.sleep(2)
            for count in range (0,5):
                SendKey("Up")
                time.sleep(3)
            for count in range (0,15):
                SendKey("Up")
                time.sleep(1.5)    
            SendKey("Standby")
            time.sleep(12)
            SendKey("Standby")
            time.sleep(8)   
            
    
          ## Selecting WatchTV   
            SendKey("Exit")
            time.sleep(2)
            SendKey("Exit")
            time.sleep(1)
            SendKey("Sources")
            time.sleep(5)
            SendKey("Up")
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.15)
            SendKey("Down")
            time.sleep(0.2)
            SendKey("Down")
            time.sleep(0.2)
            SendKey("Down")
            time.sleep(0.2)
            SendKey("Ok")
            time.sleep(2)
    
         ##Perform auto installation - Dig+Analog Installation - UK Country
            print ("Perform auto installation - Dig+Analog Installation - UK Country")
            SendKey("Home")
            time.sleep(5)
            for count in range(0,5):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(0.5)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.3)
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)            
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Left_longpress")
            time.sleep(1)
            SendKey("Up_longpress")
            time.sleep(1)            
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(1.5)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(1)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(4)
            for count in range(0,45):
                SendKey("Down")
                time.sleep(0.15)
            for count in range(0,2):
                SendKey("Up")
                time.sleep(0.15)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(180)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(2)
            
            # Perform Zapping
            for count in range (0,10):
                SendKey("Channel_Up")
                time.sleep(2)
            for count in range (0,5):
                SendKey("Up")
                time.sleep(3)
            for count in range (0,15):
                SendKey("Up")
                time.sleep(1.5)    
            SendKey("Standby")
            time.sleep(12)
            SendKey("Standby")
            time.sleep(8)   
    
    
        # From Settings - Select Channel Installation Screen
            print ("From Settings - Select Channel Installation Screen")
            SendKey("Settings")
            time.sleep(5)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.15)
            time.sleep(0.5)
            for count in range(0,1):
                SendKey("Up")
                time.sleep(0.2)
            time.sleep(0.1)
            SendKey("Ok")
            time.sleep(4)
                    
        ##Perform auto installation - Dig+Analog Installation - Sweden Country
            print ("Perform auto installation - Dig+Analog Installation - Sweden Country")
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.15)
            time.sleep(0.5)
            for count in range(0,1):
                SendKey("Up")
                time.sleep(0.2)
            time.sleep(0.1)
            SendKey("Ok")
            time.sleep(4)
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Left_longpress")
            time.sleep(1)
            SendKey("Up_longpress")
            time.sleep(1)            
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(1.5)                
            for count in range(0,3):
                SendKey("Down")
                time.sleep(1)
            SendKey("Ok")
            for count in range(0,47):
                SendKey("Down")
                time.sleep(0.15)                
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.1)            
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")

            time.sleep(320)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(3)
                
            # Perform Zapping
            for count in range (0,10):
                SendKey("Channel_Up")
                time.sleep(2)
            for count in range (0,5):
                SendKey("Up")
                time.sleep(3)
            for count in range (0,15):
                SendKey("Up")
                time.sleep(1.5)    
            SendKey("Standby")
            time.sleep(10)
            SendKey("Standby")
            time.sleep(10)   
    
        ##Perform Frequency installation - 602 Frequency
            print ("Perform Frequency installation - 602 Frequency")
            SendKey("Home")
            time.sleep(5)
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(3)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.2)
            time.sleep(3)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,15):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.5)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(0.3)
    
            SendKey("Down")
            time.sleep(0.3)
            SendKey("Ok")
            time.sleep(0.3)                
            SendKey("6")
            time.sleep(0.2)
            SendKey("0")
            time.sleep(0.01)
            SendKey("2")
            time.sleep(0.01)
            SendKey("0")
            time.sleep(0.01)
            SendKey("0")
            time.sleep(0.01)
            SendKey("Ok")
            time.sleep(15)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Exit")
            time.sleep(5)    
            SendKey("Standby")
            time.sleep(10)
            SendKey("Standby")
            time.sleep(12)
            
        # From Settings - Perform auto installation - Dig+Analog Installation - Poland Country
            print ("From Settings - Perform auto installation - Dig+Analog Installation - Poland Country")
            SendKey("Settings")
            time.sleep(5)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.1)
            time.sleep(0.5)
            for count in range(0,1):
                SendKey("Up")
                time.sleep(0.2)
            time.sleep(0.1)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Ok")
            time.sleep(2.5)
            SendKey("Left_longpress")
            time.sleep(1)
            SendKey("Up_longpress")
            time.sleep(1)
            
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(1.5)    
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.3)    
            SendKey("Ok")
            time.sleep(1)
            for count in range(0,45):
                SendKey("Down")
                time.sleep(0.15)                
            for count in range(0,14):
                SendKey("Up")
                time.sleep(0.15)            
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(255)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(3)
                
        # Perform Zapping
            for count in range (0,10):
                SendKey("Channel_Up")
                time.sleep(2)
            for count in range (0,5):
                SendKey("Up")
                time.sleep(3)
            for count in range (0,15):
                SendKey("Up")
                time.sleep(1.5)    
            SendKey("Standby")
            time.sleep(5)
            SendKey("Standby")
            time.sleep(5)   
    
        # Perform DTR Installation
            print ("Perform DTR Installation")    
            SendKey("1")
            time.sleep(5)
            SendKey("Home")
            time.sleep(5)
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(3)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.2)
            time.sleep(3)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,15):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(1)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(1)
            time.sleep(4)
            SendKey("Down")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(16)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Exit")
            time.sleep(3)
            
                
        # From Settings - Perform auto installation - Dig+Analog Installation - Norway  Country
            print ("From Settings - Perform auto installation - Dig+Analog Installation - Norway  Country")
            SendKey("Settings")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.1)
            SendKey("Up")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Left_longpress")
            time.sleep(1)
            SendKey("Up_longpress")
            time.sleep(1)            
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(1.5)        
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.3)    
            SendKey("Ok")
            time.sleep(1)                
            for count in range(0,1):
                SendKey("Up")
                time.sleep(0.1)            
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(270)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(3)
                
            # Perform Zapping
            for count in range (0,10):
                SendKey("Channel_Up")
                time.sleep(2)
            for count in range (0,5):
                SendKey("Up")
                time.sleep(3)
            for count in range (0,15):
                SendKey("Up")
                time.sleep(1.5)    
            SendKey("Standby")
            time.sleep(7)
            SendKey("Standby")
            time.sleep(7)   
    
        ##Perform Frequency installation - 722 Frequency
            print ("Perform Frequency installation - 722 Frequency")
            SendKey("Home")
            time.sleep(5)
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(3)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.2)
            time.sleep(3)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,15):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.5)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(0.3)    
            SendKey("Down")
            time.sleep(0.3)
            SendKey("Ok")
            time.sleep(0.3)                
            SendKey("7")
            time.sleep(0.2)
            SendKey("2")
            time.sleep(0.01)
            SendKey("2")
            time.sleep(0.01)
            SendKey("0")
            time.sleep(0.01)
            SendKey("0")
            time.sleep(0.01)
            SendKey("Ok")
            time.sleep(15)
            SendKey("Ok")
            time.sleep(3)
            SendKey("Ok")
            time.sleep(3)
            SendKey("Exit")
            time.sleep(5)    
            SendKey("Standby")
            time.sleep(10)
            SendKey("Standby")
            time.sleep(12)
            
        # From Settings - Perform auto installation - Dig+Analog Installation - Ireland  Country
            print ("From Settings - Perform auto installation - Dig+Analog Installation - Ireland  Country")
            SendKey("Settings")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Left_longpress")
            time.sleep(1)
            SendKey("Up_longpress")
            time.sleep(1)            
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(1.5)        
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.3)    
            SendKey("Ok")
            time.sleep(1)
            for count in range(0,48):
                SendKey("Down")
                time.sleep(0.15)                
            for count in range(0,24):
                SendKey("Up")
                time.sleep(0.3)
            time.sleep(5)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(280)
            SendKey("Ok")
            time.sleep(1)
            time.sleep(3)
                
            # Perform Zapping
            for count in range (0,10):
                SendKey("Channel_Up")
                time.sleep(2)
            for count in range (0,5):
                SendKey("Up")
                time.sleep(3)
            for count in range (0,15):
                SendKey("Up")
                time.sleep(1.5)    
            SendKey("Standby")
            time.sleep(15)
            SendKey("Standby")
            time.sleep(15)   
    
    
        # From Settings - Perform auto installation - Dig+Analog Installation - Germany  Country
            print ("From Settings - Perform auto installation - Dig+Analog Installation - Germany  Country")
            SendKey("Settings")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Ok")
            time.sleep(2.5)
            SendKey("Left_longpress")
            time.sleep(1)
            SendKey("Up_longpress")
            time.sleep(1)            
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(1.5)    
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.3)    
            SendKey("Ok")
            time.sleep(1)
            for count in range(0,48):
                SendKey("Down")
                time.sleep(0.15)            
            for count in range(0,28):
                SendKey("Up")
                time.sleep(0.3)
            time.sleep(5)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(280)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(5)    
            SendKey("Standby")
            time.sleep(10)
            SendKey("Standby")
            time.sleep(10)
    
        ##Perform Frequency installation - 610 Frequency
            print ("Perform Frequency installation - 610 Frequency")        
            SendKey("Home")
            time.sleep(5)
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(3)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.2)
            time.sleep(3)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,15):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.5)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(0.3)    
            SendKey("Down")
            time.sleep(0.3)
            SendKey("Ok")
            time.sleep(0.3)                
            SendKey("6")
            time.sleep(0.2)
            SendKey("1")
            time.sleep(0.1)
            SendKey("0")
            time.sleep(0.1)
            SendKey("0")
            time.sleep(0.1)
            SendKey("0")
            time.sleep(0.1)
            SendKey("Ok")
            time.sleep(15)
            SendKey("Ok")
            time.sleep(3)
            SendKey("Ok")
            time.sleep(3)
            SendKey("Exit")
            time.sleep(5)    
            SendKey("Standby")
            time.sleep(10)
            SendKey("Standby")
            time.sleep(12)
    
        # Perform DTR Installation
            print ("Perform DTR Installation")
            SendKey("1")
            time.sleep(5)
            SendKey("Home")
            time.sleep(5)
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(3)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.2)
            time.sleep(3)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,15):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(1)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(1)
            time.sleep(4)
            SendKey("Down")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(16)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Exit")
            time.sleep(3)    
            SendKey("Standby")
            time.sleep(8)
            SendKey("Standby")
            time.sleep(8) 
            
        # From Settings - Perform auto installation - Dig+Analog Installation - Finland  Country
            print ("From Settings - Perform auto installation - Dig+Analog Installation - Finland  Country")
            SendKey("Settings")
            time.sleep(5)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Ok")
            time.sleep(2.5)
            SendKey("Left_longpress")
            time.sleep(1)
            SendKey("Up_longpress")
            time.sleep(1)            
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(1.5)    
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.3)    
            SendKey("Ok")
            time.sleep(1)
            for count in range(0,47):
                SendKey("Down")
                time.sleep(0.3)                
            for count in range(0,31):
                SendKey("Up")
                time.sleep(0.3)            
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(270)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(5)
            
                
            # Perform Zapping
            for count in range (0,10):
                SendKey("Channel_Up")
                time.sleep(2)
            for count in range (0,5):
                SendKey("Up")
                time.sleep(3)
            for count in range (0,15):
                SendKey("Up")
                time.sleep(1.5)    
            SendKey("Standby")
            time.sleep(8)
            SendKey("Standby")
            time.sleep(8)
        
        ##Perform DTR installation - 602 Frequency
        print ("Perform DTR installation - 602 Frequency")   
        for DTR_Freq in range(0,2):    
            SendKey("Home")
            time.sleep(5)
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(3)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.2)
            time.sleep(3)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,15):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.5)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(0.5)
            SendKey("Down")
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(0.8)                
            SendKey("6")
            time.sleep(0.2)
            SendKey("0")
            time.sleep(0.01)
            SendKey("2")
            time.sleep(0.01)
            SendKey("0")
            time.sleep(0.01)
            SendKey("0")
            time.sleep(0.01)
            SendKey("Ok")
            time.sleep(15)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Exit")
            time.sleep(5)    
            SendKey("Standby")
            time.sleep(10)
            SendKey("Standby")
            time.sleep(12)
    
                
        Zapping_Count = 0    
        for DTR in range(0,2):
        ##Perform DTR installation
            print ("Perform DTR installation")
            SendKey("1")
            time.sleep(5)
            SendKey("Home")
            time.sleep(5)
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(3)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.2)
            time.sleep(3)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,15):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(1)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(1)
            time.sleep(4)
            SendKey("Down")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(16)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Exit")
            time.sleep(3)
            
            Zapping_Count = Zapping_Count+5
            ##Zap 2 times
            for count in range (0,Zapping_Count):
                SendKey("Channel_Up")
                time.sleep(2)
            time.sleep(15)
    
        ##Perform DTR installation - 177.5 Frequency
        print ("Perform DTR installation - 177.5 Frequency")   
        for DTR_Freq in range(0,2):    
            SendKey("Home")
            time.sleep(5)
            for count in range(0,6):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(3)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.2)
            time.sleep(3)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,15):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(3)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(0.5)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(0.5)
                SendKey("Down")
                time.sleep(0.5)
                SendKey("Ok")
                time.sleep(0.5)                
            SendKey("1")
            time.sleep(0.2)
            SendKey("7")
            time.sleep(0.01)
            SendKey("7")
            time.sleep(0.01)
            SendKey("5")
            time.sleep(0.01)
            SendKey("0")
            time.sleep(0.01)
            SendKey("Ok")
            time.sleep(15)
            SendKey("Ok")
            time.sleep(3)
            SendKey("Ok")
            time.sleep(3)
            SendKey("Exit")
            time.sleep(5)
            print (time.time())



         ##Perform auto installation - Dig+Analog Installation - Spain Country
            print ("Perform auto installation - Dig+Analog Installation - Spain Country")
            SendKey("Home")
            time.sleep(5)
            for count in range(0,5):
                SendKey("Up")
                time.sleep(0.15)
            time.sleep(0.5)
            for count in range(0,5):
                SendKey("Right")
                time.sleep(0.3)
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Ok")
            time.sleep(2.5)
            SendKey("Left_longpress")
            time.sleep(1)
            SendKey("Up_longpress")
            time.sleep(1)            
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(1.5)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(1)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(4)
            for count in range(0,48):
                SendKey("Down")
                time.sleep(0.15)
            for count in range(0,7):
                SendKey("Up")
                time.sleep(0.3)
            SendKey("Ok")
            time.sleep(1.25)
            SendKey("Ok")
            time.sleep(1.25)    
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(180)
            SendKey("Ok")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(2)
            
            # Perform Zapping
            for count in range (0,10):
                SendKey("Channel_Up")
                time.sleep(2)
            for count in range (0,5):
                SendKey("Up")
                time.sleep(3)
            for count in range (0,15):
                SendKey("Up")
                time.sleep(1.5)    
            SendKey("Standby")
            time.sleep(12)
            SendKey("Standby")
            time.sleep(8)

        ##Perform auto installation - Dig+Analog Installation - Russia Country
            print ("Perform auto installation - Dig+Analog Installation - Russia Country")
            SendKey("Home")
            time.sleep(5)
            for count in range(0,1):
                SendKey("Up_longpress")
                time.sleep(0.15)
            time.sleep(0.5)
            for count in range(0,1):
                SendKey("Right_longpress")
                time.sleep(0.3)
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(4)
            for count in range(0,14):
                SendKey("Down")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(1.5)
            SendKey("Ok")
            time.sleep(2.5)
            SendKey("Left_longpress")
            time.sleep(1)
            SendKey("Up_longpress")
            time.sleep(1)            
            for count in range(0,2):
                SendKey("Ok")
                time.sleep(1.5)
            for count in range(0,3):
                SendKey("Down")
                time.sleep(1)
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(4)
            for count in range(0,3):
                SendKey("Down_longpress")
                time.sleep(0.15)
            for count in range(0,11):
                SendKey("Up")
                time.sleep(0.3)
            SendKey("Ok")
            time.sleep(1.25)
            SendKey("Up_longpress")
            time.sleep(0.5)
            SendKey("Down")
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(1.5)            
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(200)            
            SendKey("Ok")
            time.sleep(2)
            SendKey("Ok")
            time.sleep(2)            
            # Perform Zapping
            for count in range (0,10):
                SendKey("Channel_Up")
                time.sleep(2)
            for count in range (0,5):
                SendKey("Up")
                time.sleep(3)
            for count in range (0,15):
                SendKey("Up")
                time.sleep(1.5)    
            SendKey("Standby")
            time.sleep(12)
            SendKey("Standby")
            time.sleep(8)            
            print ("DVB-S Installation")
            SendKey("Exit")
            time.sleep(2)
            SendKey("Exit")
            time.sleep(1)    
            SendKey("Home")
            time.sleep(5)
            for count in range(0,1):
                SendKey("Up_longpress")
                time.sleep(0.15)
            time.sleep(0.5)            
            for count in range(0,1):
                SendKey("Right_longpress")
                time.sleep(0.2)
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(4)            
            for count in range(0,1):
                SendKey("Down_longpress")
                time.sleep(0.15)
            SendKey("Up")
            time.sleep(2.5)    
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(2.5)                
            for count in range(0,1):
                SendKey("Down")
                time.sleep(1)                
            for count in range(0,1):
                SendKey("Ok")
                time.sleep(4)                
            SendKey("Ok")
            time.sleep(1)
            SendKey("Up")
            time.sleep(0.5)
            SendKey("Up")
            time.sleep(0.5)
            SendKey("Up")
            time.sleep(0.5)
            SendKey("Up")
            time.sleep(0.5)
            SendKey("Down")
            time.sleep(0.5)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Right")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(240)
            SendKey("Ok")
            time.sleep(1)
            SendKey("Ok")
            time.sleep(240)
            SendKey("Ok")
            time.sleep(3)
            SendKey("Ok")
            time.sleep(3)
            
    z = time.time()

    print ("Time taken to Complete Test_Scenarios() is : %f" %(z-y))
    
## Manual Frequency Installation - 177.5, 602, 610, 722  Frequencies
def DTR_Installation_Tuner(client,RedRat_Device_Name,RedRat_Device_Port,DTR_Freq):
    y = time.time()
    print ("Perform DTR installation")  
    for count in range(0,2):
        SendKey("Home")
        time.sleep(5)
        SendKey("Up_longpress")
        time.sleep(0.5)
        SendKey("Right_longpress")
        time.sleep(0.5)
        SendKey("Ok")
        time.sleep(4)
        SendKey("Down_longpress")
        time.sleep(0.3)
        SendKey("Up")
        time.sleep(1.5)
        for count in range(0,2):
            SendKey("Ok")
            time.sleep(2.5)                
        for count in range(0,1):
            SendKey("Left_longpress")
            time.sleep(1.5)            
        SendKey("Down_longpress")
        time.sleep(1)            
        SendKey("Up")
        time.sleep(0.5)
        for count in range(0,2):
            SendKey("Ok")
            time.sleep(1)                
        DTR_Freq_Temp = str(DTR_Freq)
        for x in range(0,len(DTR_Freq_Temp)):
            print (DTR_Freq_Temp[x])
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(DTR_Freq_Temp[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
            time.sleep(0.5)
        SendKey("Ok")
        time.sleep(17)
        SendKey("Ok")
        time.sleep(1.5)
        SendKey("Ok")
        time.sleep(3)
        
        SendKey("Exit")
        time.sleep(2)
    z = time.time()

    print ("Time taken to Complete DTR_Installation_Tuner() is : %f" %(z-y))
        
            
def Manual_Analog_Installation_Tuner(Analog_Freq):
    y = time.time()
    SendKey("Home")
    time.sleep(5)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Right_longpress")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(4)
    SendKey("Down_longpress")
    time.sleep(0.2)
    SendKey("Up")
    time.sleep(2)
    for count in range(0,2):
        SendKey("Ok")
        time.sleep(2)
    SendKey("Left_longpress")
    time.sleep(0.4)
    for count in range(0,6):
        SendKey("Down")
        time.sleep(0.4)
    SendKey("Right")
    time.sleep(0.3)
    for count in range(3):
        SendKey("Up")
        time.sleep(0.2)    
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(2)

    Analog_Freq_Temp = str(Analog_Freq)
    
    for x in range(0,len(Analog_Freq_Temp)):
        print (Analog_Freq_Temp[x])
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Analog_Freq_Temp[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(0.3)
    SendKey("Ok")
    time.sleep(15)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Exit")
    time.sleep(1)

    z = time.time()

    print ("Time taken to Complete Manual_Analog_Installation_Tuner() is : %f" %(z-y))

def Manual_Installation_Satellite(client,RedRat_Device_Name,RedRat_Device_Port):
    y = time.time()
    SendKey("Home")
    time.sleep(5)
    SendKey("Up_longpress")
    time.sleep(0.2)
    SendKey("Right_longpress")
    time.sleep(0.2)
    SendKey("Ok")
    time.sleep(4)
    SendKey("Down_longpress")
    time.sleep(0.2)
    SendKey("Up")
    time.sleep(2)
    for count in range(0,1):
        SendKey("Ok")
        time.sleep(2)
    SendKey("Down_longpress")
    time.sleep(0.5)
    SendKey("Up")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1.5)
    SendKey("Down_longpress")
    time.sleep(0.5)
    SendKey("Up")
    time.sleep(0.5)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Down_longpress")
    time.sleep(0.5)
    for count in range(2):
        SendKey("Ok")
        time.sleep(1.5)
    SendKey("Ok")
    time.sleep(15)
    SendKey("Ok")
    time.sleep(15)
    SendKey("Ok")
    time.sleep(3)  
    SendKey("Exit")
    time.sleep(1)

    z = time.time()

    print ("Time taken to Complete Manual_Installation_Satellite() is : %f" %(z-y))

def Freq_Installation_722():
    y = time.time()
    print ("Start of the Function Freq_Installation_722()")
    SendKey("Home")
    time.sleep(5)
    for count in range(0,6):
        SendKey("Up")
        time.sleep(0.15)
    time.sleep(3)
    for count in range(0,5):
        SendKey("Right")
        time.sleep(0.2)
    time.sleep(3)
    SendKey("Ok")
    time.sleep(4)
    for count in range(0,15):
        SendKey("Down")
        time.sleep(0.15)
    SendKey("Up")
    time.sleep(2)
    for count in range(0,2):
        SendKey("Ok")
        time.sleep(3)
    for count in range(0,3):
        SendKey("Down")
        time.sleep(0.5)
    for count in range(0,1):
        SendKey("Ok")
        time.sleep(0.3)    
    SendKey("Down")
    time.sleep(0.3)
    SendKey("Ok")
    time.sleep(0.3)                
    SendKey("7")
    time.sleep(0.2)
    SendKey("2")
    time.sleep(0.01)
    SendKey("2")
    time.sleep(0.01)
    SendKey("0")
    time.sleep(0.01)
    SendKey("0")
    time.sleep(0.01)
    SendKey("Ok")
    time.sleep(15)
    SendKey("Ok")
    time.sleep(3)
    SendKey("Ok")
    time.sleep(3)
    SendKey("Exit")
    time.sleep(5)    
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(12)
    print ("End of the Function Freq_Installation_722()")

    z = time.time()

    print ("Time taken to Complete Freq_Installation_722() is : %f" %(z-y))

def Block1():
    #Satellite_Installation()
    SendKey("Standby")
    time.sleep(9)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)
    
    #PostConditionchecks()
    
    Manual_Analog_Installation_Tuner(535)
    SendKey("Standby")
    time.sleep(25)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)    

    #PostConditionchecks()

    Auto_Installation('UK','DVBT','Advanced')
    
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(6)    
    
    DTR_Installation()
    
    SendKey("Standby")
    time.sleep(18)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)    
        
    Auto_Installation('Sweden','DVBT','Advanced')
    
    SendKey("Standby",600,1)
    SendKey("Standby",60,1)
         
    Freq_Installation(602)

    #PostConditionchecks()
    Auto_Installation('Poland','DVBT','Advanced')
    
    SendKey("Standby",16,1)    
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)
    
    #PostConditionchecks()

    Auto_Installation('UK','DVBT','Advanced')
    
    SendKey("Standby")
    time.sleep(22)
    SendKey("Standby")
    time.sleep(8)  
    
    DTR_Installation()

    Auto_Installation('Czech','DVBC','Advanced')

    #PostConditionchecks()
          
    SendKey("Standby",300,1)
    SendKey("Standby",60,1)
          
    Auto_Installation('Norway','DVBT','Advanced')
          
    #PostConditionchecks()
          
    Freq_Installation(602)
    SendKey("Standby")
    time.sleep(5)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)    
    
    #PostConditionchecks()

    Auto_Installation('Germany','DVBT','Advanced')
    SendKey("Standby")
    time.sleep(7)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)    

    Auto_Installation('Turkey','DVBT','Advanced')

    SendKey("Standby")
    time.sleep(16.5)
    SendKey("Standby")
    time.sleep(8)  
    
    Auto_Installation('Other','DVBT','Advanced')
    
    SendKey("Standby")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(8)  
    
    Auto_Installation('UK','DVBT','Advanced')
        
    SendKey("Standby")
    time.sleep(14)
    SendKey("Standby")
    time.sleep(8)  
    
    SendKey("Standby")
    time.sleep(18.5)
    SendKey("Standby")
    time.sleep(6)  
    
    #PostConditionchecks()

    DTR_Installation()
    SendKey("Standby")
    time.sleep(17.5)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)    

   # PostConditionchecks()

    Freq_Installation(594)

    Auto_Installation('Finland','DVBT','Advanced')
    SendKey("Standby")
    time.sleep(25)
    SendKey("Standby")
    time.sleep(6)    
    
    PostConditionchecks()

    Freq_Installation(666)
    
    Auto_Installation('UK','DVBT','Advanced')
    
    SendKey("Standby")
    time.sleep(22)
    SendKey("Standby")
    time.sleep(6) 
    
    SendKey("Standby")
    time.sleep(18)
    SendKey("Standby")
    time.sleep(6)  

    DTR_Installation()

    Auto_Installation('Spain','DVBT','Advanced')

#    PostConditionchecks()

    Auto_Installation('Russia','DVBT','Advanced')
    SendKey("Standby")
    time.sleep(16)
    SendKey("Standby")
    time.sleep(6)    
    
    PostConditionchecks()

    Auto_Installation('Albania','DVBT','Advanced')

#    PostConditionchecks()
    
    Auto_Installation('UK','DVBT','Advanced')
    
    SendKey("Standby")
    time.sleep(17)
    SendKey("Standby")
    time.sleep(6) 
    

def Block2():
    print("Block 2 - Start of Auto_Installation('UK','DVBT','Advanced') Function")
    Auto_Installation('UK','DVBT','Advanced')
    SendKey("Standby")
    time.sleep(17.5)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)   
    
    Freq_Installation(178)
    Auto_Installation('Khazakistan','DVBT','Advanced')
    
    SendKey("Standby")
    time.sleep(5)
    SendKey("Standby")
    time.sleep(5)   
    
    SendKey("Standby")
    time.sleep(19)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(7)   
    
#    PostConditionchecks()
    Auto_Installation('Slovakia','DVBC','Advanced')
    
    SendKey("Standby")
    time.sleep(18.5)
    SendKey("Standby")
    time.sleep(8)   
    
#   PostConditionchecks()
    Auto_Installation('Other','DVBT','Advanced')
    SendKey("Standby")
    time.sleep(25)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(8)   
    
    Satellite_Installation()
    Auto_Installation('Belarus','DVBT','Advanced')
#   PostConditionchecks()
    Auto_Installation('Ukraine','DVBC','Advanced')
        
#    PostConditionchecks()
    
    SendKey("Standby",300,1)
    SendKey("Standby",60,1)
    
    DTR_Installation()
    Auto_Installation('UK','DVBT','Advanced')
#    Satellite_Installation()
    Auto_Installation('Estonia','DVBT','Advanced')

    SendKey("Standby")
    time.sleep(22)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)  
    
#    PostConditionchecks()
    Auto_Installation('Luxembourg','DVBC','Advanced')    
    SendKey("Standby")
    time.sleep(15.5)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)  
    
#    PostConditionchecks()
#    Satellite_Installation()

    Auto_Installation('Georgia','DVBT','Advanced')
#    PostConditionchecks()
    SendKey("Standby",300,1)
    SendKey("Standby",60,1)
    
    Auto_Installation('Other','DVBT','Advanced')
    
    DTR_Installation()
    SendKey("Standby")
    time.sleep(10)
    SendKey("Standby")
    time.sleep(6)  

    Freq_Installation(594)

    SendKey("Standby")
    time.sleep(20)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)  
        
def Block3():
    print("Block 1 - Start of Auto_Installation('UK','DVBT','Advanced') Function")
    Auto_Installation('UK','DVBT','Advanced')
    print("Block 1 - End of Auto_Installation('UK','DVBT','Advanced') Function")
    
    print("Block 4 - Start of Auto_Installation('Czech','DVBC','Advanced') Function")
    Auto_Installation('Czech','DVBC','Advanced')
    SendKey("Standby")
    time.sleep(20)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)  
    
    print("Block 4 - End of Auto_Installation('Czech','DVBC','Advanced') Function")
    
    print("Block 4 - Start of PostConditionchecks() Function")
#    PostConditionchecks()
    print("Block 4 - End of PostConditionchecks()) Function")
    
    print("Block 4 - Start of Auto_Installation('Slovakia','DVBC','Advanced') Function")
    Auto_Installation('Slovakia','DVBC','Advanced')

    SendKey("Standby")
    time.sleep(20)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)  
    
    print("Block 4 - End of Auto_Installation('Slovakia','DVBC','Advanced') Function")
    
    print("Block 4 - Start of PostConditionchecks() Function")
#    PostConditionchecks()
    print("Block 4 - End of PostConditionchecks() Function")
    
    print("Block 4 - Start of Auto_Installation('Luxembourg','DVBC','Advanced') Function")
    Auto_Installation('Luxembourg','DVBC','Advanced')
    SendKey("Standby")
    time.sleep(14)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)  

    print("Block 4 - End of Auto_Installation('Luxembourg','DVBC','Advanced') Function")
    
    print("Block 4 - Start of PostConditionchecks() Function")
#    PostConditionchecks()
    print("Block 4 - End of PostConditionchecks() Function")
    
    print("Block 4 - Start of Auto_Installation('UK','DVBT','Advanced') Function")
    Auto_Installation('UK','DVBT','Advanced')
    SendKey("Standby")
    time.sleep(17)
    SendKey(random.choice(Random_Standby_Wakeup_List))
    time.sleep(6)  

    print("Block 4 - End of Auto_Installation('UK','DVBT','Advanced') Function")
    
    print("Block 4 - Start of PostConditionchecks() Function")
#    PostConditionchecks()
    print("Block 4 - End of PostConditionchecks() Function")
    
    print("Block 4 - Start of DTR_Installation() Function")
    DTR_Installation()
    print("Block 4 - End of DTR_Installation() Function")
    
    print("Block 4 - Start of Auto_Installation('Other','DVBT','Advanced') Function")
    Auto_Installation('Other','DVBT','Advanced')
    print("Block 4 - End of Auto_Installation('Other','DVBT','Advanced') Function")
    
    print("Block 4 - Start of DTR_Installation() Function")
    DTR_Installation()
    SendKey("Standby")
    time.sleep(20)
    SendKey("Standby")
    time.sleep(6)  
    
    print("Block 4 - End of DTR_Installation() Function")
    
    print("Block 4 - Start of Freq_Installation(602) Function")
    Freq_Installation(602)
    print("Block 4 - End of Freq_Installation(602)Function")
    
    print("Block 4 - Start of DTR_Installation() Function")
    DTR_Installation()
    print("Block 4 - End of DTR_Installation() Function")
    
    print("Block 4 - Start of Freq_Installation(666) Function")
    Freq_Installation(666)
    print("Block 4 - End of Freq_Installation(666) Function")
    
    print("Block 4 - Start of DTR_Installation() Function")
    DTR_Installation()
    print("Block 4 - End of DTR_Installation() Function")
    
    print("Block 4 - Start of Manual_Analog_Installation_Tuner(133) Function")
    Manual_Analog_Installation_Tuner(133)
    SendKey("Standby")
    time.sleep(6)
    SendKey("Standby")
    time.sleep(6)  
    
    print("Block 4 - End of Manual_Analog_Installation_Tuner(133) Function")
            
def Start_RedRat_Script():
    print ("Start of the Function Start_RedRat_Script()")
    for i in range(1000):
        Block1()
        
if __name__ == "__main__":
    client = Client();
    client.OpenSocket('localhost', 40000);
    Counter = 1
    RedRat_Device_Name = "No name 10400"
    RedRat_Device_Port = "1"

    Start_RedRat_Script()
