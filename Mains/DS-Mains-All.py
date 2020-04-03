import time
import telnetlib
import time
import datetime
#from datetime import datetime
from multiprocessing import Pool, TimeoutError
import socket
import random
import itertools
from  win32gui import GetWindowText, GetForegroundWindow, SetForegroundWindow, EnumWindows, BringWindowToTop, ShowWindow,CloseWindow,PostMessage
import subprocess
import configparser,traceback
import threading
import re
from os.path import basename
import os
import sys
import win32con

class WindowsForeground:

    def send_commands_to_hwnd(self, hwnd ,COM):
        """sets first command prompt to forgeround"""
        #print GetWindowText(hwnd)
        COM_PORT = str(COM) + ":115200"
        #COM_PORT1 = str(COM) + " - Tera Term VT"
        #print COM_PORT
        #PostMessage = ctypes.windll.user32.PostMessageA
        if (COM_PORT) in GetWindowText(hwnd):
            print (GetWindowText(hwnd))
            print (hwnd)
            PostMessage(hwnd,win32con.WM_CLOSE,0,0)
            time.sleep(2)           
            print ("found")
            #SetForegroundWindow(hwnd)
            return

def Start_UART_Commandline(TTL,UART_File_name,COM,i,k,UART_Folder):
    j = i + 1
    #TTL = "C:\\MSAF_TTL\\Null.ttl"
    COM_PORT = COM.rsplit("COM")[1] 
    Log_file_name = "C:\\" + UART_Folder + "\\TV" + str(k) + "\\" + UART_File_name           
    COM_PORT_CMD = "/C=" + COM_PORT
    Save_log = "/L=" + "\"" + Log_file_name + "\""
    Load_TTL = "/M=" + "\"" + TTL + "\""
    #Teraterm_Path = "\"C:\\Program Files (x86)\\teraterm\\ttermpro.exe \""
    Teraterm_Path = "ttermpro.exe "
    UART_Command = Teraterm_Path + COM_PORT_CMD + " "+ Save_log + " " + Load_TTL

    print (UART_Command)
    Start_Command = subprocess.Popen(
            UART_Command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
                )
    return UART_File_name

def Start_UART_log_Temp(i):
    COM_ports = open("COM_PORT.txt", "r")
    #shell = client.Dispatch("WScript.Shell")
    run_venv = WindowsForeground()
    
    try:
        config = configparser.RawConfigParser()
        config.optionxform = str
        Setup_ini_Path = os.getcwd() + "\\INI\\" + "Stab_Setup.ini"
        config.read(Setup_ini_Path)
        FTP_Folder = config.get("Setup","FTP_Folder")
        UART_Folder = config.get("Setup", "UART_Folder")
        TV_Start_No = config.get("Setup", "TV_Start_No")
        TTL_Folder = config.get("Setup","TTL_Folder")
    except:
        print (traceback.print_exc())
    k = int(TV_Start_No)    
    UART_Temp = []
    for line in COM_ports:
        COM = line.strip('\n\r')
        Timestamp = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        UART_File_name = "TV" + str(k) + "_"+ str(COM) + "_" + Timestamp +"_UART_TEMP_" + str(i) + ".txt"
        UART_Temp.append(UART_File_name)
        TTL = "C:\\" + str(TTL_Folder)+ "\\Rename_TV" + str(k) + ".ttl"
        if not ((line.strip('\n\r')).rsplit("_")[-1] == "SKIP"):
            Start_UART_Commandline(TTL,UART_File_name,COM,i,k,UART_Folder)
        k = k + 1
        
        time.sleep(5)
    print (UART_Temp)
    return UART_Temp

def Start_UART_log(TTL,i,UART_Folder,TV_Start_No):
    COM_ports = open("COM_PORT.txt", "r")
    #shell = client.Dispatch("WScript.Shell")
    run_venv = WindowsForeground()
    k = int(TV_Start_No)
    UART = []
    for line in COM_ports:
        COM = line.strip('\n\r')
        Timestamp = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        UART_File_name = "TV" + str(k) + "_"+ str(COM) + "_" + Timestamp +"_UART_" + str(i+1) + ".txt"
        UART.append(UART_File_name)
        if not ((line.strip('\n\r')).rsplit("_")[-1] == "SKIP"):
            Start_UART_Commandline(TTL,UART_File_name,COM,i,k,UART_Folder)
        k = k + 1
        
        time.sleep(5)
    print (UART)
    return UART

def Stop_UART_log():
    COM_ports = open("COM_PORT.txt", "r")
    #shell = client.Dispatch("WScript.Shell")
    run_venv = WindowsForeground()
    for line in COM_ports:
        if not ((line.strip('\n\r')).rsplit("_")[-1] == "SKIP"):            
            COM = line.strip('\n\r')
            if "COM" in COM:                
                EnumWindows(run_venv.send_commands_to_hwnd, COM)
                time.sleep(2)
                
def Create_TTL(i,k):
    try:
        config = configparser.RawConfigParser()
        config.optionxform = str
        Setup_ini_Path = os.getcwd() + "\\INI\\" + "Stab_Setup.ini"
        config.read(Setup_ini_Path)
        FTP_Folder = config.get("Setup","FTP_Folder")
        TTL_Folder = config.get("Setup","TTL_Folder")
        #FTP_Server_IP = config.get("Setup", "FTP_Server")
        Local_Server_Upload  = config.get("Setup", "Local_Server_Upload")
        FTP_Server_IP = config.get("Setup", "FTP_Server")
        Local_Server_IP = config.get("Setup", "Local_Server")
        UART_Folder = config.get("Setup", "UART_Folder")
        Energenie_Support = config.get("Setup", "Energenie_Support")
        Android_OS = config.get("Setup", "Android_OS")
        BugReport = config.get("Setup", "BugReport")
        
    except:
        print (traceback.print_exc())
        
    Rename_TTL_Name = "C:\\" + TTL_Folder + "\\" + "Rename_" + "TV" + str(k) + ".ttl"
    Rename_TTL = open(Rename_TTL_Name,'w')
    print  (Rename_TTL_Name)
    Down_Key = "sendln 'input keyevent 20'\n"
    Enter_Key = "sendln 'input keyevent 66'\n"
    Ok_Key = "sendln 'input keyevent 23'\n"
    Back_Key = "sendln 'input keyevent 4'\n"
    Pause_2 = "pause 3\n"
    Pause_5 = "pause 5\n"
    TAB_Key = "sendln 'input keyevent 61'\n"
    Timestamp = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    Rename_file = "input text " + "TV" + str(k) + "_" + Timestamp +"_TPVisionDebug_" + str(i)
    Zip_File_Name = "TV" + str(k) + "_" + Timestamp +"_TPVisionDebug_" + str(i) + "zip"
    #Logcat_command = "'logcat | grep System.out&'"
    Rename_TTL.write(Pause_5)
    Rename_TTL.write( "sendln " + "'logcat -c'" + "\n")
    Rename_TTL.write(Pause_5)
    Rename_TTL.write( "sendln " + "'logcat | grep -i -e System.out&'" + "\n")
    Rename_TTL.write(Pause_5)
    Rename_TTL.write( "sendln " + "'am start -a android.intent.action.MAIN -n com.tpvision.sw_download_to_upgrades/.Main_Activity'" + "\n")
    Rename_TTL.write("pause 10\n")
    Rename_TTL.write(TAB_Key)
    Rename_TTL.write(Pause_5)
    Rename_TTL.write(TAB_Key)
    Rename_TTL.write(Pause_2)
    Rename_TTL.write(TAB_Key)
    Rename_TTL.write(Pause_2)
    Rename_TTL.write("sendln " + "'" + Rename_file + "'" + "\n")
    Rename_TTL.write(Pause_5)
    Rename_TTL.write(TAB_Key)
    Rename_TTL.write(Pause_5)
    Rename_TTL.write(Enter_Key)
    Rename_TTL.write("pause 10\n")
    return Rename_TTL_Name,Zip_File_Name

def Rename_TPVision_Debug_PyScript(i):
    COM_ports = open("COM_PORT.txt", "r")
    #shell = client.Dispatch("WScript.Shell")
    run_venv = WindowsForeground()
    #ttl = "C:\MSAF_TTL\Rename_TPVision_debug.ttl"
    try:
        config = configparser.RawConfigParser()
        config.optionxform = str
        Setup_ini_Path = os.getcwd() + "\\INI\\" + "Stab_Setup.ini"
        config.read(Setup_ini_Path)
        FTP_Folder = config.get("Setup","FTP_Folder")
        UART_Folder = config.get("Setup", "UART_Folder")
        TV_Start_No = config.get("Setup", "TV_Start_No")
        Energenie_Support = config.get("Setup", "Energenie_Support")
        BugReport = config.get("Setup", "BugReport")
        TV_Mains_Port = config.get("Setup", "TV_Mains_Port")
    except:
        print (traceback.print_exc())
        
    k = int(TV_Start_No)    
    Logcat = []
    for line in COM_ports:
        COM = line.strip('\n\r')
        TTL,Zip_File_Name = Create_TTL(i,k)
        #TTL = "Rename_" + "TV" + str(k) + ".ttl"
        #print TTL
        print (Zip_File_Name)
        Logcat.append(Zip_File_Name)
        time.sleep(2)
        k = k + 1    
    print ("Waiting for Files to Rename")
    UART_Temp = Start_UART_log_Temp(i)
    print (UART_Temp)
    print (Logcat)
    time.sleep(120)
    Stop_UART_log()
    
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
RedRat_Device_Name = "RedRat-X 23188"
RedRat_Device_Port = "1"
apc_port = 4
global delay_variable
delay_variable = 50

Random_Standby_Wakeup_List = ["Blue","Exit","Home","Netflix","Ambilight",0, "Channel_Up", "Channel_Down"]
LongPress_List = ["Right_longpress","Up_longpress","Down_longpress","Left_longpress"]
NavigationKey_List = ["Right","Up","Down","Left"]

Text_Zap_List = [10,11,12,13,14]
Text_Random_Standby_Wakeup_List = ["Blue","Exit","Home","Netflix","Ambilight",0, "Channel_Up", "Channel_Down"]
Wakeup_Time_List = [[7,8],[15,9], [25,9],[3,6], [2,5],[13,10], [14,12],[1,7], [10,10],[12.5,8]]

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
        
def Trick_List_Navigations_Fixed(Trick_List):
    Key_1stArg = 0
    SleepTime_2ndArg = 1
    for count in range(len(Trick_List)):
        SendKey(Trick_List[count][Key_1stArg], Trick_List[count][SleepTime_2ndArg])

def AC_OFF_ON_Random_1():
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(5)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(45)
    
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(5)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(25)

    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(3)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(30)

    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(8)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(4)

    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(2)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(20)

def AC_OFF_ON_Random_2():
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(10)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(10)

    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(4)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(48)

    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(3)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(3)

    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(5)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(20)
 
def AC_OFF_ON_Random_3():
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(5)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(50)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(3)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(45)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(9)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(35)
    
def AC_OFF_ON_Random_4():
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(5)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(25)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(3)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(30)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(7)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(22)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(2)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(19)
    
def AC_OFF_ON_Random_5():
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(2)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(9)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(4)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(4)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(5)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(12)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(5)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(14)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(3)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(17)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(1)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(19)
    
def AC_OFF_ON_Random_6():
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(2)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(9)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(4)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(4)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(5)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(25)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(3)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(30)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(7)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(22)
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(2)
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(19)
    
    
def APC_Switch_ON_OFF(Command,port):
    telnet = telnetlib.Telnet()
    try:
        
        telnet.open("192.168.10.12")
        time.sleep(0.5)
        telnet.read_until("User Name :")
        telnet.write("apc\r\n")
        time.sleep(.5)
        telnet.read_until("Password  :")
        
        telnet.write("apc\r\n")
        telnet.read_until("apc>")
        if Command == "ON":
            ON = "olOn " + str(port) + "\r\n"
            telnet.write(ON)
        elif Command == "OFF":    
            OFF = "olOff " + str(port) + "\r\n"
            telnet.write(OFF)
        print (telnet.read_until("E000: Success"))
        telnet.close()
    except:
        print ("Failed telnet Session once")
        time.sleep(2)
        telnet.close()
        try:
            telnet = telnetlib.Telnet()
            telnet.open("192.168.1.18")
            time.sleep(0.5)
            telnet.read_until("User Name :")
            telnet.write("apc\r\n")
            time.sleep(.5)
            telnet.read_until("Password  :")
            
            telnet.write("apc\r\n")
            telnet.read_until("apc>")
            if Command == "ON":
                ON = "olOn " + str(port) + "\r\n"
                telnet.write(ON)
            elif Command == "OFF":    
                OFF = "olOff " + str(port) + "\r\n"
                telnet.write(OFF)
            print (telnet.read_until("E000: Success"))
            telnet.close()
        except:
            print ("failed telnet session again")
            return
    
def AC_OFF_ON_Fixed(delay):
    APC_Switch_ON_OFF("OFF",apc_port)
    time.sleep(delay)
    
    APC_Switch_ON_OFF("ON",apc_port)
    time.sleep(1)  
    
Apps_In_Row1 = [1,2,3,4]
Apps_In_Row2 = [5,6,7,8]
Apps_In_Row3 = [9,10,11,12]
Apps_In_Row4 = [13,14,15,16]
Apps_In_Row5 = [17,18,19,20]

def Home_Positioning_Launch_App(App_Number):
    SendKey('Home_longpress', 5, 1)
    
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

def Random_Standby_Wakeup(Wakeup_Time): # Performing Random Standby Wakeups in Teletext Page while Navigations
    SendKey('Standby', 1, Wakeup_Time[0])
    Wakeup_Key = random.choice(Text_Random_Standby_Wakeup_List)
    
    if (Wakeup_Key == "Ambilight"):
        SendKey(Wakeup_Key, 2, 4)
        SendKey("Blue",Wakeup_Time[1],1)
    else:
        SendKey(Wakeup_Key,8,1)

#### Arun Additional Scripts Start
        
def Test_Function_Arun_Satellite_OTR_Mains():
    print ("Start of function-Test_Function_Arun_Satellite_OTR_Standby_Mains_wakeup")
    Digit_Channel_Selection('Satellite', 85)
    time.sleep(3)
    SendKey("Rec")
    time.sleep(1)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    Digit_Channel_Selection('Satellite', 83)
    time.sleep(3)
    SendKey("Rec")
    time.sleep(5)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    Digit_Channel_Selection('Satellite', 88)
    time.sleep(3)
    SendKey("Rec")
    time.sleep(9)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    Digit_Channel_Selection('Satellite', 157)
    time.sleep(3)
    SendKey("Rec")
    time.sleep(15)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    Digit_Channel_Selection('Satellite', 96)
    SendKey("Rec")
    time.sleep(30)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)    
    
def Test_Function_Arun_Satellite_Timeshift_Mains():
    Digit_Channel_Selection('Satellite', 97)
    time.sleep(3)
    SendKey("Pause")
    time.sleep(10)
    Random_TrickModes(5)
    time.sleep(9)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    SendKey("Exit")
    time.sleep(0.5)
    SendKey("Channel_Up")
    time.sleep(0.1)
    SendKey("9")
    time.sleep(0.1)
    SendKey("9")
    time.sleep(3)    
    SendKey("Pause")
    time.sleep(15)
    Random_TrickModes(10)
    time.sleep(22)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    Switch_To_Satellite()
    SendKey("Channel_Up")
    time.sleep(0.1)
    SendKey("1")
    time.sleep(0.1)
    SendKey("5")
    time.sleep(3)
    SendKey("5")
    time.sleep(3)
    SendKey("Pause")
    time.sleep(20)
    Random_TrickModes(7)
    time.sleep(4)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    SendKey("Exit")
    time.sleep(0.5)
    SendKey("Channel_Up")
    time.sleep(0.1)
    SendKey("8")
    time.sleep(0.1)
    SendKey("6")
    time.sleep(3)
    SendKey("Pause")
    time.sleep(30)
    Random_TrickModes(9)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    Switch_To_Satellite()
    SendKey("Channel_Up")
    time.sleep(0.1)
    SendKey("8")
    time.sleep(0.1)
    SendKey("2")
    time.sleep(3)
    SendKey("Pause")
    time.sleep(30)
    Random_TrickModes(4)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
      
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
    Random_Navigation(15)
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
    print ("Start of function-Test_Function_Arun_Tuner_MHEG_Navigation_PLyaback_With_Standby")
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
        Random_Navigation(13)
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
    Random_Navigation(9)
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
    
    print ("End of function-Test_Function_Arun_Tuner_MHEG_Navigation_PLyaback_With_Standby")
    
#### Arun Script End    

def Megogo_Revanth_AC_OFF_ON_Wakeup():
    Home_Positioning_Launch_App(13)
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
    AC_OFF_ON_Fixed(5)    
    time.sleep(delay_variable)
    
    Home_Positioning_Launch_App(13)
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
    
    AC_OFF_ON_Fixed(5)   
    time.sleep(delay_variable)
        
def Random_List_Handler(count,whichlist,delay):
    for count in range(count):        
        sublist = random.choice(whichlist)
        if type(sublist) is int:
            for x in range(0,len(str(sublist))):
                sublist_temp =str(sublist)
                time.sleep(0.15)
                SendKey(str(sublist_temp[x]), 1, 0)                
            time.sleep(delay)    
        else:
             SendKey(str(sublist), delay, 1)

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
    
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
#launch-ext
    for count in range(0,3):
        SendKey("Home_longpress",3,1)
        SendKey("Down",0.3,2)
        SendKey("Ok",2,1)
        SendKey("Down",0.3,1)
        SendKey("Right",0.3,2)
        SendKey("Ok",3,1)

    for count in range(0,3):
        SendKey("Home_longpress",3,1)
        SendKey("Down",0.3,2)
        SendKey("Ok",2,1)
        SendKey("Down",0.3,1)
        SendKey("Right",0.3,2)
        SendKey("Ok",5,1)   
        
    AC_OFF_ON_Fixed(7)
    time.sleep(delay_variable)
    
 #Ambilight demo   
    SendKey("Home_longpress",3,1)
    SendKey("Down",0.3,2)
    SendKey("Ok",2,1)
    SendKey("Left",0.2,2)
    SendKey("Up",0.3,4)
    SendKey("Down",0.3,3)
    SendKey("Ok",15,1)
    
    AC_OFF_ON_Fixed(4)
    time.sleep(delay_variable)

def Teletext_Nav_Tuner_AC_OFF_ON():
    ## Launch Teletext and perform Navigation and increase volume on teletext page
    Digit_Channel_Selection('Tuner', 14) # EinsPlus Channel
    SendKey('Text', 2, 1)
    Random_Text(10)
    AC_OFF_ON_Fixed(4)
    time.sleep(delay_variable)
    
    SendKey('Text', 2, 1)
    for count in range(0,12):
        SendKey('Channel_Up', 0.3,1)
        SendKey('Mute',0.3,1)
        SendKey('Volume_Down',0.3,2)
        SendKey('Mute',0.3,1)
    SendKey('Volume_Up', 0.3,1)
    SendKey('Mute', 0.3,1)
    SendKey('Volume_Down',0.3,2)
    SendKey('Mute',0.3,2)
    for count in range(0,13):
       SendKey('Up', 0.3,1)
       SendKey('Volume_Up', 0.3,1) 
    SendKey('Mute', 0.3,1)
    SendKey('Volume_Down', 0.3,2)
    SendKey('Mute',0.3,1)
    SendKey('Down', 0.2,15)
    SendKey('Mute', 0.3,1)
    SendKey('Volume_Down', 0.3,2)
    SendKey('Mute',0.3,1)
    
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    SendKey('Exit', 2, 1)
    
    Random_Teletext_Zap_AC_OFF_ON(1)
    AC_OFF_ON_Fixed(9)
    time.sleep(delay_variable)
    SendKey('Exit', 2, 1)
    
def Random_Teletext_Zap(Text_Zap_Count):
    SendKey("Exit")
    time.sleep(2)
    for count in range(Text_Zap_Count):
        Text_Zap_List = [["1","1"],["1","3"],["1","5"],["1","6"]]

        Text_List_Temp = random.choice(Text_Zap_List)
        if type(Text_List_Temp) is list:
            for x in range(0,len(Text_List_Temp)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            #time.sleep(.3)
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
            #time.sleep(.3)
        time.sleep(4)
        Random_Text(25)
                                      
def Random_Text(Text_Count):
    print ("Teletext Navigations")
    SendKey("Text")
    time.sleep(4)
                   
    for count in range(3):
        SendKey("8")
    time.sleep(5)
                   
    for count in range(Text_Count):
        Text_List = ["Channel_Up","Down",["8","8","8"],["1","1","1"],"Channel_Down",["3","3","3"],"Up","Up_longpress","Down_longpress",["2","2","2"],["7","7","7"],["9","9","9"],["5","5","6"],
                     ["5","5","5"],["7","5","6"],["1","2","5"],["2","7","0"],["3","0","2"],"Yellow","Red","Green",["3","2","5"],["3","8","2"],["4","1","2"],["4","3","5"],["5","1","2"],["6","2","2"],["7","5","0"]]
        Text_List_Temp = random.choice(Text_List)
        if type(Text_List_Temp) is list:
            for x in range(0,len(Text_List_Temp)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            time.sleep(.5)    
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp) + '\"" output=\"' + RedRat_Device_Port+"\"\'")

        time.sleep(0.4)
        
        if (count%5 == 0):
            Random_Volume(5)
        if (count%4 == 0)    :
            Text_Yellow_Green_Red_Nav(20)

    SendKey("Text")
    time.sleep(2)
    SendKey("Exit")
    time.sleep(2)
    Text_Yellow_Green_Red_Nav(20)

def Text_Yellow_Green_Red_Nav(Text_Count):
                  
    for count in range(Text_Count):
        Text_List = ["Yellow","Red","Green"]
        Text_List_Temp = random.choice(Text_List)
        if type(Text_List_Temp) is list:
            for x in range(0,len(Text_List_Temp)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(0.1)
            time.sleep(0.2)    
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(0.2)    

def Random_Teletext_Zap_AC_OFF_ON(Text_Zap_Count):
    SendKey("Exit")
    time.sleep(2)
    for count in range(Text_Zap_Count):
        Text_Zap_List = [["1","1"],["1","3"],["1","5"],["1","6"],["3","2"]]

        Text_List_Temp = random.choice(Text_Zap_List)
        if type(Text_List_Temp) is list:
            for x in range(0,len(Text_List_Temp)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            #time.sleep(.3)
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
            #time.sleep(.3)
        time.sleep(4)
        Random_Text_AC_OFF_ON(20)
                                      
def Random_Text_AC_OFF_ON(Text_Count):
    print (" Teletext Navigations")
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
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(.1)
            time.sleep(.5)    
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp) + '\"" output=\"' + RedRat_Device_Port+"\"\'")

        time.sleep(0.4)
        
        if (count%5 == 0):
            Random_Volume(5)
        if (count%4 == 0)    :
            Text_Yellow_Green_Red_Nav_AC_OFF_ON(20)

    SendKey("Text")
    time.sleep(2)
    SendKey("Exit")
    time.sleep(2)
    Text_Yellow_Green_Red_Nav_AC_OFF_ON(20)

def Text_Yellow_Green_Red_Nav_AC_OFF_ON(Text_Count):
    for count in range(Text_Count):
        Text_List = ["Yellow","Red","Green"]
        Text_List_Temp = random.choice(Text_List)
        if type(Text_List_Temp) is list:
            for x in range(0,len(Text_List_Temp)):
                client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp[x]) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
                time.sleep(0.1)
            time.sleep(0.2)    
        else:
            client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + str(Text_List_Temp) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(0.2) 

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
    
def Guide_Nav_AC_OFF_ON():
    ## Launch Guide and perform Navigation inside it
    
    Switch_To_Tuner()    
    for count in range(0,2):
        SendKey('TVGuide', 5, 1)
        Guide_Yellow_AC_OFF_ON()

        AC_OFF_ON_Fixed(5)
        time.sleep(delay_variable)
        
        SendKey('Channel_Down', 4, 1)

        SendKey('TVGuide', 5, 1)
        SendKey('Right', 0.2, 25)
        Random_List_Handler(10,NavigationKey_List,0.2)
        SendKey('Down_longpress', 0.15, 4)

        AC_OFF_ON_Fixed(3)
        time.sleep(delay_variable)
        SendKey('Exit', 2, 1)

        SendKey('TVGuide', 5,1)       
        Guide_Yellow_AC_OFF_ON()
        Random_List_Handler(10,LongPress_List,0.2)
        SendKey('Left', 0.23, 23)
        Random_List_Handler(20,NavigationKey_List,0.2)
        AC_OFF_ON_Fixed(7)
        time.sleep(delay_variable)
        
def Guide_Launch_Exit_AC_OFF_ON():
    ## Perform Guide Launching and Exiting
        
    SendKey('TVGuide',3,2)
    for count in range(3):
        SendKey('TVGuide', 3,1)
        SendKey('Right_longpress', 0.5,1)
        SendKey('Exit',3, 1 )
    SendKey('TVGuide',2, 1)  
    SendKey('Right_longpress', 0.5,1)
    SendKey('Exit',3, 1 )
    
    SendKey('TVGuide', 4,2)
    
    SendKey('TVGuide',4, 1)
    Random_longpress(7)
    
    SendKey('TVGuide', 2,7)
    SendKey('Home', 14,1)
    
    for count in range(0,7):
        SendKey('TVGuide', 2,1)
    
    SendKey('TVGuide', 2,1)
    AC_OFF_ON_Fixed(7)
    time.sleep(delay_variable)
     
def Guide_Tuning_AC_OFF_ON():
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
    
def Guide_Yellow_AC_OFF_ON():
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
        
def Random_Volume(Volume_Count):
    for count in range(Volume_Count):
        Volume_List = ["Volume_Up","Mute","Volume_Down"]
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal=\"' + random.choice(Volume_List) + '\"" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(0.3)
                      
def Netflix_ACOffOn(number, number1):
    SendKey('Netflix',25,1)
    SendKey('Ok',1,1)
    SendKey('Back',0.4,4)
    SendKey('Left',0.3,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',0.6,3)
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
    

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    SendKey('Netflix',25,1)
    SendKey('Ok',1,1)
    SendKey('Back',0.4,4)
    SendKey('Left',0.3,5)     
    SendKey('Down',0.3,8)
    SendKey('Up',0.6,3)
    SendKey('Ok',0.6,1)
    SendKey('Up',0.6,4)
    
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

    AC_OFF_ON_Fixed(4)
    time.sleep(delay_variable)
    
def DropBox():
    Down_Count = [0,1,2,3,4,5]
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)

    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    time.sleep(8)
    SendKey('Up',2,1)
    SendKey('Ok',2,1)
    SendKey("Right",2,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    
    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    time.sleep(8)
    SendKey('Up',2,1)
    SendKey('Ok',2,1)
    SendKey("Right",2,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_3)
    
    AC_OFF_ON_Fixed(6)
    time.sleep(delay_variable)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',2,2)
    time.sleep(8)
    SendKey('Up',2,1)
    SendKey('Ok',2,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    AC_OFF_ON_Fixed(4)
    time.sleep(delay_variable)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Left',0.3,7)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',2,2)
    time.sleep(8)
    SendKey('Up',2,1)
    SendKey('Ok',2,1)
    SendKey('Right',3,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',5,1)
    Trick_List_Navigations_Fixed(Trick_List_1)
    
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
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
    SendKey('Up',0.7,2)
    time.sleep(8)
    SendKey('Up',2,1)
    SendKey('Ok',3,1)
    
    SendKey("Down", 3,1)
    SendKey('Right',1,1)
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',20,1)
    Trick_List_Navigations_Fixed(Trick_List_6)
    
    AC_OFF_ON_Fixed(4)
    time.sleep(delay_variable)
    
#audio
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey('Left',0.3,4)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',2,2)
    time.sleep(8)
    SendKey('Up',2,1)
    SendKey('Ok',3,1)
  
    SendKey("Down", 3,1)
    SendKey('Right',1,1)
    SendKey("Down", 0.3,random.choice(Down_Count1))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
 #Images   
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.3,5)
    SendKey('Ok',1,1)
    SendKey('Left',0.3,4)
    SendKey('Down_longpress',0.3,2)
    SendKey('Up',0.7,2)
    time.sleep(8)
    SendKey('Up',2,1)
    SendKey('Ok',3,1)
    
    SendKey("Down", 3,1)
    SendKey('Right',1,1)
    SendKey("Down", 0.3,random.choice(Down_Count2))
    SendKey('Ok',3,1)
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    AC_OFF_ON_Fixed(6)
    time.sleep(delay_variable)

def App_Gallery_Nav_ACOffOn():
    time.sleep(23)
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

    AC_OFF_ON_Fixed(8)
    time.sleep(delay_variable)

 #All category
    time.sleep(23)
    SendKey("Smart_Home",15,1)
    SendKey("Left",1,1)
    SendKey("Ok",3,1)
    SendKey("Smart_Home",7,1)
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
        
    AC_OFF_ON_Fixed(7)
    time.sleep(delay_variable)
    
# New Category
    time.sleep(23)
    SendKey("Smart_Home",20,1)
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
        
    AC_OFF_ON_Fixed(10)
    time.sleep(delay_variable) 
    
#Video category
    time.sleep(23)
    SendKey("Smart_Home",20,1)
        
    SendKey("Up_longpress",1,4)
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
        
    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)

def OIB():
##    AC_OFF_ON_Fixed(3)
##    time.sleep(delay_variable)
##    time.sleep(23)
    time.sleep(10)
    Home_Positioning_Launch_App(3)

    SendKey("Ok")
    time.sleep(5)

    SendKey("Down_longpress",0.2,2)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,1)
    Random_longpress(15)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,2)
    Random_longpress(15)

    SendKey("Back",0.8,1)
    SendKey('Right',1,1)
    SendKey('Ok',3,1)

    SendKey("Down_longpress",0.2,2)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,1)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,2)
    
    Random_longpress(22)

    
    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)
    time.sleep(23)

    Home_Positioning_Launch_App(3)

    SendKey('Right',1,2)
    SendKey('Ok',5,1)

    SendKey("Down_longpress",0.2,2)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,1)
    Random_longpress(10)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,2)
    Random_longpress(10)

    SendKey("Back",0.8,1)
    SendKey('Right',1,1)
    SendKey('Ok',3,1)

    Random_longpress(8)
    SendKey("Down_longpress",0.2,2)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,1)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,2)

    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)
    time.sleep(23)

    Home_Positioning_Launch_App(3)

    SendKey('Down',1,1)
    SendKey('Ok',5,1)

    SendKey("Down_longpress",0.2,2)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,1)
    Random_longpress(18)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,2)
    Random_longpress(12)

    SendKey("Back",0.8,1)
    SendKey('Right',1,1)
    SendKey('Ok',3,1)

    Random_longpress(10)
    SendKey("Down_longpress",0.2,2)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,1)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,2)

    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)
    time.sleep(23)

    Home_Positioning_Launch_App(3)

    SendKey('Down',1,1)
    SendKey('Right',1,2)
    SendKey('Ok',5,1)

    SendKey("Down_longpress",0.2,2)
    SendKey("Left_longpress",0.2,2)
    SendKey("Right_longpress",0.2,2)
    SendKey("Down_longpress",0.2,1)
    Random_longpress(25)

    SendKey("Back",0.8,1)
    SendKey('Right',1,1)
    SendKey('Ok',3,1)

    SendKey("Down_longpress",0.2,3)
    Random_longpress(25)

    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)
        

def Amazon_ACOffOn_Revanth(VideoNo,VideoNo1):
    Home_Positioning_Launch_App(12)
    time.sleep(30)    
    SendKey('Right',1,5) # If we give 6 Rights, then My List will be seen. If we give 5 Rights, It will take to Video Library
    SendKey('Ok',3,1)
    SendKey('Right',2,VideoNo-1)
    SendKey('Ok',7,1)
    SendKey('Ok',5,1)
    SendKey('Left',0.2,4)
    SendKey('Ok',1,1) #Playback starts
    Trick_List_Navigations_Fixed(Trick_List_5)

   
    AC_OFF_ON_Fixed(12)
    time.sleep(delay_variable)

    Home_Positioning_Launch_App(12)
    time.sleep(30)    
    SendKey('Right',1,5) # If we give 6 Rights, then My List will be seen. If we give 5 Rights, It will take to Video Library
    SendKey('Ok',3,1)
    SendKey('Right',2,VideoNo1-1)
    SendKey('Ok',7,1)
    SendKey('Ok',5,1)
    SendKey('Left',0.2,4)
    SendKey('Ok',1,1) #Playback starts
    Trick_List_Navigations_Fixed(Trick_List_5)

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)

def GoogleAssistant_ACOffOn():    
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.7,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",4,1)
    for count in range(0,5):
        SendKey("Down",0.6,1)
        SendKey("Ok",6,1)
        
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.7,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",4,1)
    SendKey("Down",0.5,1)
    SendKey("Right",0.6,1)
    for count in range(0,4):
        SendKey("Down",0.5,1)
        SendKey("Right",0.6,count)
        SendKey("Ok",7,1)
        
    AC_OFF_ON_Fixed(8)
    time.sleep(delay_variable)
    
    # Back to Back Voice Search Operations
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.5,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",6,1)
    SendKey("Down",0.5,1)
    #SendKey("Right",0.6,2)
    SendKey("Ok",1,1)
    for count in range(0,4):
        SendKey("Home",3.5,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",6,1)
        SendKey("Down",0.3,1)
        SendKey("Right",0.4,count)
        SendKey("Ok",3,1)

    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)
    
    # In Weather , Exit to TV (TV is in Background), Voice Search is in Foreground
    SendKey("Home",4,1)
    SendKey("Up_longpress",0.5,1)
    SendKey("Left_longpress",0.5,1)
    SendKey("Ok",6,1)
    SendKey("Down",0.5,1)
    SendKey("Right",0.6,1)
    SendKey("Ok",1,1)    
    SendKey("Exit",1,1) 
    for count in range(0,6):
        SendKey("Down",5,1)
        SendKey("Right",0.6,count)
        SendKey("Ok",5,1)

    AC_OFF_ON_Fixed(10)
    time.sleep(delay_variable)

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

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)

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
        

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)

def Pacman_Revanth():
    Home_Positioning_Launch_App(1)
    time.sleep(20)
    SendKey("Ok",1,10)
    for count in range(0,4):
        SendKey("Up",0.5,1)
        SendKey("Right",0.4,1)
        SendKey("Up",0.4,1)
        SendKey("Left",0.4,1)
    SendKey("Ok",0.6,5)
    SendKey("Exit",2,1)

    
    AC_OFF_ON_Fixed(10)
    time.sleep(delay_variable)

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
    
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey("Left",0.2,4)
    SendKey('Down_Longpress',0.4,2)
    SendKey('Up',0.7,2)
    SendKey('Right',0.8,2) 
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)          

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
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
    
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
    SendKey('Sources',4,1)
    SendKey('Up_Longpress',1,1)
    SendKey('Down',0.4,5)
    SendKey('Ok',1,1)
    SendKey("Left",0.2,4)
    SendKey('Down_Longpress',0.4,2)
    SendKey('Up',0.7,2)
    SendKey('Right',0.8,2) 
    SendKey("Down", 0.3,random.choice(Down_Count))
    SendKey('Ok',10,1)
    Trick_List_Navigations_Fixed(Trick_List_5)     
    
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
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
    
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable) 

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

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable) 

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

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable) 

    
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
    
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable) 
    
#audios
    
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
    
def AudioOut_AC_0FF_0N_Revanth():
    for count in range(0,6):
        SendKey("Settings")
        SendKey("UP_longpress",0.2,1)
        SendKey("Down",0.2,6)
        SendKey("Right",0.2,1)
        SendKey("UP_longpress",0.2,1)
        SendKey("Down",0.2,count)
        SendKey("Ok",4,1)
        AC_OFF_ON_Fixed(5)
        time.sleep(50)

    SendKey("Settings")
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,6)
    SendKey("Right",0.2,1)
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,2)
    SendKey("Ok",4,1)
    AC_OFF_ON_Fixed(6)
    time.sleep(45)
   

    SendKey("Settings")
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,6)
    SendKey("Right",0.2,1)
    SendKey("UP_longpress",0.2,1)
    SendKey("Up",0.2,2)
    SendKey("Ok",4,1)
    AC_OFF_ON_Fixed(4)
    time.sleep(45)

    SendKey("Settings")
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,6)
    SendKey("Right",0.2,1)
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,3)
    SendKey("Ok",4,1)
    AC_OFF_ON_Fixed(3)
    time.sleep(45)

    SendKey("Settings")
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,6)
    SendKey("Right",0.2,1)
    SendKey("UP_longpress",0.2,1)
    SendKey("Up",0.2,2)
    SendKey("Ok",4,1)
    AC_OFF_ON_Fixed(4)
    time.sleep(45)

    SendKey("Settings")
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,6)
    SendKey("Right",0.2,1)
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,2)
    SendKey("Ok",4,1)
    AC_OFF_ON_Fixed(6)
    time.sleep(45)
    
    SendKey("Settings")
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,6)
    SendKey("Right",0.2,1)
    SendKey("UP_longpress",0.2,1)
    SendKey("Up",0.2,3)
    SendKey("Ok",4,1)
    AC_OFF_ON_Fixed(4)
    time.sleep(45)

    SendKey("Settings")
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,6)
    SendKey("Right",0.2,1)
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,4)
    SendKey("Ok",4,1)
    AC_OFF_ON_Fixed(6)
    time.sleep(45)

    SendKey("Settings")
    SendKey("UP_longpress",0.2,1)
    SendKey("Down",0.2,6)
    SendKey("Right",0.2,1)
    SendKey("UP_longpress",0.2,1)
    SendKey("Up",0.2,2)
    SendKey("Ok",4,1)
    AC_OFF_ON_Fixed(4)
    time.sleep(45)

def Channel_SubtitleChange_AC_OFF_ON_Revanth():
    print ('channel subtitile change')
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
    
    
    AC_OFF_ON_Fixed(4)
    time.sleep(delay_variable)
     
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

   
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable) 
    
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
   
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    SendKey("Exit",1,1) 

def Youtube_Row1():
    AC_OFF_ON_Fixed(1)
    time.sleep(delay_variable)
    time.sleep(10)
    Home_Positioning_Launch_App(1)
    SendKey("Back",0.4, 4)
    Home_Positioning_Launch_App(1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.3, 1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down_longpress", 0.4, 3)
    SendKey("Right", 0.3, 1)
    
# 1st Video    
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_5)

    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)
    
# 2nd Video
    Home_Positioning_Launch_App(1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.3, 1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down_longpress", 0.4, 3)
    SendKey("Right", 0.3, 2)
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_3)
    
    AC_OFF_ON_Fixed(4)
    time.sleep(delay_variable)

#3rd Video
    Home_Positioning_Launch_App(1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.3, 1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down_longpress", 0.4, 3)
    SendKey("Right", 0.3, 3)
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_4)
    
    AC_OFF_ON_Fixed(8)
    time.sleep(delay_variable)
    
def Youtube_Row2():
    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)
    time.sleep(10)
    Home_Positioning_Launch_App(1)
    SendKey("Back",0.4, 4)
    Home_Positioning_Launch_App(1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.3, 1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down_longpress", 0.4, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down", 0.3, 1)
    
# 1st Video    
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_6)

    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)
    
# 2nd Video
    Home_Positioning_Launch_App(1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.3, 1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down_longpress", 0.4, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down", 0.3, 1)
    SendKey("Right", 0.3, 1)
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_2)
    
    AC_OFF_ON_Fixed(2)
    time.sleep(delay_variable)

#3rd Video
    Home_Positioning_Launch_App(1)
    SendKey("Down_longpress", 0.5, 2)
    SendKey("Up", 0.3, 1)
    SendKey("Right", 0.3, 1) # Takes you to the 1st Video of the Fav List "Stability" Created. i.e. Focus is on Astra Ultra HD Demo Video
    SendKey("Down_longpress", 0.4, 3)
    SendKey("Right", 0.3, 1)
    SendKey("Down", 0.3, 1)
    SendKey("Right", 0.3, 2)
    SendKey("Ok", 20.0, 1) # Play the content for 30 Seconds
    Trick_List_Navigations_Fixed(Trick_List_1)
    
    AC_OFF_ON_Fixed(8)
    time.sleep(delay_variable)

def Youtube_Row3():
    AC_OFF_ON_Fixed(4)
    time.sleep(delay_variable)
    time.sleep(10)
    
    Home_Positioning_Launch_App(1)
    Random_Navigation(10)
        
    SendKey("Ok", 5, 1) 

    AC_OFF_ON_Fixed(6)
    time.sleep(delay_variable)
    
    Home_Positioning_Launch_App(1)
    Random_Navigation(20)
    SendKey("Ok", 2, 1)
    
    for count in range(0,4):
        SendKey("Back",4,1)
        SendKey("Right",4,1)
        SendKey("Ok", 2, 1)
  
    AC_OFF_ON_Fixed(2)
    time.sleep(delay_variable)
    
    Home_Positioning_Launch_App(1)
    Random_Navigation(15)
    SendKey("Ok", 2, 1)
    
    for count in range(0,3):
        SendKey("Back",4,1)
        SendKey("Right",4,1)
        SendKey("Ok", 2, 1)
  
    AC_OFF_ON_Fixed(2)
    time.sleep(delay_variable)

def Channel_AudioLanguage_ACOffOn_Revanth():
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

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)            

def SwitchingChannels_ACOffOn_Revanth(): 
    Digit_Channel_Selection("Tuner",5)
    time.sleep(5)
    SendKey("Up_longpress",4,1)
    SendKey("Up",0.3,6)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,1)
    SendKey("Down_longpress",3,1)
    SendKey("Down",0.3,6)
    SendKey("Volume_Down",0.1,7)
    
    Digit_Channel_Selection("Satellite",153)
    time.sleep(5)
    SendKey("Channel_Down_longpress",0.2,1)
    SendKey("Channel_Up",0.3,6)
    SendKey("Volume_Down",0.1,7)
    SendKey("Channel_Up_longpress",0.2,1)
    SendKey("Channel_Down",0.3,5)
    SendKey("Mute",0.3,4)
    SendKey("Volume_Up",0.1,7)
    
    Digit_Channel_Selection("Tuner",14)
    time.sleep(5)
    SendKey("Up_longpress",0.5,1)
    SendKey("Channel_Down",0.3,3)
    SendKey("Volume_Down",0.1,4)
    SendKey("Channel_Down_longpress",0.2,1)
    SendKey("Channel_Up",1,3)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,2)
    
    Digit_Channel_Selection("Satellite",90)
    time.sleep(5)
    SendKey("Volume_Up",0.1,7)
    SendKey("Mute",0.3,1)
    SendKey("Channel_Up_longpress",0.2,1)
    SendKey("Channel_Down",0.3,4)
    SendKey("Volume_Down",0.1,5)
    SendKey("Channel_Up",0.3,2)
    SendKey("Down_longpress",5,1)

    AC_OFF_ON_Fixed(6)
    time.sleep(delay_variable)

    Digit_Channel_Selection("Tuner",20)
    time.sleep(5)
    SendKey("Volume_Down",0.1,7)
    SendKey("Channel_Up_longpress",0.3,1)
    SendKey("Mute",0.3,3)
    SendKey("Up_longpress",0.2,1)
    SendKey("Volume_Up",0.1,7)
    SendKey("Channel_Down",0.2,6)
    SendKey("Volume_Down",0.1,4)
    
    Digit_Channel_Selection("Satellite",81)
    time.sleep(5)
    SendKey("Up_longpress",0.2,1)
    SendKey("Down_longpress",0.2,1)
    SendKey("Volume_Up",0.1,8)
    SendKey("Mute",0.3,5)
    SendKey("Volume_Down",0.1,7)
    
    Digit_Channel_Selection("Tuner",10)
    time.sleep(5)
    SendKey("Volume_Up",0.1,3)
    SendKey("Volume_Down",0.1,4)
    SendKey("Up_longpress",0.3,1)
    SendKey("Channel_Down",0.2,4)
    SendKey("Down_longpress",0.2,1)
    SendKey("Mute",0.3,3)
    SendKey("Channel_Up_longpress",0.5,1)
    
    Digit_Channel_Selection("Satellite",87)
    time.sleep(5)
    SendKey("Down_longpress",0.2,1)
    SendKey("Channel_Up_longpress",0.5,1)
    SendKey("Volume_Down",0.1,7)
    SendKey("Volume_Up",0.1,5)
    SendKey("Channel_Down",0.2,4)
    SendKey("Mute",0.3,1)
    
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
    
    Digit_Channel_Selection("Satellite",157)
    time.sleep(5)
    SendKey("Up_longpress",0.2,1)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,5)
    SendKey("Channel_Down_longpress",5,1)
    SendKey("Volume_Up",0.1,7)
    SendKey("Down_longpress",0.2,1)
    SendKey("Channel_Up_longpress",3,1)

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)

def Switching_Satellite_Channels_ACOffOn_Revanth():
    Digit_Channel_Selection("Satellite",84)
    time.sleep(5)
    SendKey("9",0.2,1)
    SendKey("1",0.2,1)
    time.sleep(4)
    SendKey("Ok",3,1)
    SendKey("Volume_Up",0.1,10)
    SendKey("Volume_Down",0.1,3)
    SendKey("Mute",0.2,11)
    SendKey("9",0.2,1)
    SendKey("5",0.2,1)
    SendKey("Ok",1,2)
    
    SendKey("5",0.2,1)
    time.sleep(4)
    SendKey("Volume_Up",0.1,4)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,6)
    
    SendKey("8",0.2,1)
    SendKey("1",0.2,1)
    time.sleep(2)
    SendKey("Volume_Down",0.1,10)
    

    AC_OFF_ON_Fixed(8)
    time.sleep(delay_variable)
    
    SendKey("8",0.2,1)
    SendKey("3",0.2,1)
    time.sleep(6)
    SendKey("Volume_Up",0.1,8)
    SendKey("Volume_Down",0.1,5)
    SendKey("Mute",0.3,3)
    SendKey("1",0.2,1)
    SendKey("5",0.2,1)
    SendKey("1",0.2,1)
    time.sleep(8)
    SendKey("Volume_Up",0.1,6)
    SendKey("Volume_Down",0.1,4)
    SendKey("9",0.2,1)
    SendKey("3",0.2,1)
    time.sleep(5)
    SendKey("8",0.2,1)
    SendKey("2",0.2,1)
    SendKey("Mute",0.3,4)
    time.sleep(4)
    SendKey("Ok",0.4,1)
    SendKey("Up_longpress",0.2,1)
    SendKey("Ok",3,1)


    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
def Switching_Tuner_Channels_ACOffOn_Revanth():
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

    AC_OFF_ON_Fixed(10)
    time.sleep(delay_variable)
    
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

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)
    
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
    
def PVRRecording_Playback_ACoffon_Revanth():
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


    AC_OFF_ON_Fixed(8)
    time.sleep(delay_variable)
    
    
    Switch_To_Recordings()
    SendKey("Up", 0.3,2)
    SendKey("Down", 0.3,3)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Ok")
    time.sleep(1)
    SendKey("Play")

    Trick_List_Navigations_Fixed(Trick_List_4) # At the End of this Trick List, This will be in Forward Trick

    AC_OFF_ON_Fixed(8)
    time.sleep(delay_variable)
        
def Swtich_Sources_ACOffOn_Revanth():
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

    SendKey("Forward",10,1)
    AC_OFF_ON_Fixed(8)
    time.sleep(delay_variable)

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

    SendKey("Pause",10,1)
    SendKey("Forward",2,2)
    SendKey("Rewind",2,1)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)

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
#hdmi1-tuner
    SendKey("Sources",4,1)
    SendKey("Up",0.3,5)
    SendKey("Ok",3,1)
    
    SendKey("Pause",10,1)
    SendKey("Forward",2,2)
    SendKey("Rewind",2,1)
    AC_OFF_ON_Fixed(7)
    time.sleep(delay_variable)

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


def Set_Date_Time():
    
    print (time.time())
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Settings" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(5)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down_longpress" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(2)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Up" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.5)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(8)

    for i in range(0,5):
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Left" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(.5)
        
    for i in range(0,5):
        client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
        time.sleep(.5)

    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.5)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.5)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Right" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.5)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Right" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.5)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.5)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.5)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.5)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(1)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Left" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.5)    
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(1)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Right" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(1)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Right" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(1)

    current_month = datetime.datetime.now().strftime('%m')
    current_month1 = int(current_month[:1])
    current_month2 = int(current_month[1:2])

    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(current_month1) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(current_month2) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    current_year = datetime.datetime.now().strftime('%Y')

    current_year1 = current_year[:1]
    current_year2 = current_year[1:2]
    current_year3 = current_year[2:3]
    current_year4 = current_year[3:4]

    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(current_year1) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(current_year2) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(current_year3) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(current_year4) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    
                       
    time.sleep(1)
    current_day = datetime.datetime.now().strftime('%d')
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Right" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(1)
    current_day1 = current_day[:1]
    current_day2 = current_day[1:2]

    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(current_day1) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(current_day2) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    
    time.sleep(1)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(1)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")


    time.sleep(1)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Down" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(1)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Ok" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(1)

    Current_Hour = str(datetime.datetime.now().strftime('%H'))

    Current_Hour1 = Current_Hour[:1]
    Current_Hour2 = Current_Hour[1:2]

    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(Current_Hour1) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(Current_Hour2) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)

    Current_Min = str(datetime.datetime.now().strftime('%M'))
    Current_Min1 = Current_Min[:1]
    Current_Min2 = Current_Min[1:2]

    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(Current_Min1) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(Current_Min2) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)


    Current_Sec = str(datetime.datetime.now().strftime('%S'))
    Current_Sec1 = Current_Sec[:1]
    Current_Sec2 = Current_Sec[1:2]
    
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(Current_Sec1) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="' + str(Current_Sec2) + "\"" 'output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.25)


    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Left" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.2)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Left" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.2)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Left" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.2)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Left" output=\"' + RedRat_Device_Port+"\"\'")
    time.sleep(.2)
    client.SendMessage('name="' +  RedRat_Device_Name + "\"" +  'dataset="PhilipsTV" signal="Exit" output=\"' + RedRat_Device_Port+"\"\'")
    print (time.time())

def HDMI_ACOffOn_Revanth():
    SendKey("Sources",4,1)
    SendKey("Up_longpress",0.3,1)
    SendKey("Down",0.3,1)
    SendKey("Ok",4,1)

    for count in range(0,14):
        SendKey("Sources",4,1)
        SendKey("Down",0.3,1)
        SendKey("Ok",4,1)

#HDM3
    SendKey("Sources",4,1)
    SendKey("Up",0.3,2)
    SendKey("Ok",3,1)

#HDMI4
    SendKey("Sources",4,1)
    SendKey("Down",0.3,1)
    SendKey("Ok",3,1)

    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)

    for count in range(0,5):    
    #HDMI3
        SendKey("Sources",4,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",3,1)
        AC_OFF_ON_Fixed(10)
        time.sleep(delay_variable)
        
    #HDMI4
        SendKey("Sources",4,1)
        SendKey("Down",0.3,1)
        SendKey("Ok",3,1)
    
        AC_OFF_ON_Fixed(5)
        time.sleep(delay_variable)
    
#HDMI1
    SendKey("Sources",4,1)
    SendKey("Up",0.3,3)
    SendKey("Ok",3,1)

    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)    

#HDMI2
    SendKey("Sources",4,1)
    SendKey("Down",0.3,1)
    SendKey("Ok",3,1)

    AC_OFF_ON_Fixed(2)
    time.sleep(delay_variable)   

    for count in range(0,5):     
    #HDMI1
        SendKey("Sources",4,1)
        SendKey("Up",0.3,1)
        SendKey("Ok",3,1)
    
        AC_OFF_ON_Fixed(3)
        time.sleep(delay_variable)    
    
    #HDMI2
        SendKey("Sources",4,1)
        SendKey("Down",0.3,1)
        SendKey("Ok",3,1)
    
        AC_OFF_ON_Fixed(2)
        time.sleep(delay_variable) 
        
    SendKey("Sources",4,1)
    SendKey("Up_longpress",0.3,2)
    SendKey("Down",0.3,10)
    SendKey("Ok",60,1)
    AC_OFF_ON_Fixed(2)
    time.sleep(delay_variable)
    
    SendKey("Sources",4,1)
    SendKey("Down",0.3,1)
    SendKey("Ok",120,1)
    AC_OFF_ON_Fixed(1)
    time.sleep(delay_variable)    

#HDMI3
    SendKey("Sources",4,1)
    SendKey("Up",0.3,1)
    SendKey("Ok",5,1)
    
    AC_OFF_ON_Fixed(1)
    time.sleep(delay_variable)
    AC_OFF_ON_Random_2()
    AC_OFF_ON_Random_3()
    AC_OFF_ON_Random_5()
    
#HDMI4
    SendKey("Sources",4,1)
    SendKey("Down",0.3,1)
    SendKey("Ok",5,1)
    
    AC_OFF_ON_Fixed(1)
    time.sleep(delay_variable)
    AC_OFF_ON_Random_1()
    AC_OFF_ON_Random_4()        
    
def Block1():
    
    Digit_Channel_Selection("Satellite",81)
    time.sleep(5)
    AC_OFF_ON_Fixed(5)
    time.sleep(60)

    SendKey("8",0.2,1)
    SendKey("6",0.2,1)
    time.sleep(5)
    SendKey("Pause",15,1)
    SendKey("Forward",2,3)
    
    AC_OFF_ON_Fixed(10)
    time.sleep(delay_variable)

    AC_OFF_ON_Random_5()

    SendKey("1",0.2,1)
    SendKey("5",0.2,1)
    SendKey("8",0.2,1)
    time.sleep(10)
    SendKey("Pause",10,1)
    
    AC_OFF_ON_Fixed(15)
    time.sleep(delay_variable)

    Swtich_Sources_ACOffOn_Revanth()

    AC_OFF_ON_Random_1()

    Digit_Channel_Selection("Satellite",94)
    time.sleep(5)
    SendKey("Rec",20,1)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)

    Digit_Channel_Selection("Tuner",9)
    time.sleep(5)
    SendKey("Pause",20,1)
    Trick_List_Navigations_Fixed(Trick_List_5)
    SendKey("Forward",3,1)
    AC_OFF_ON_Fixed(3)
    time.sleep(delay_variable)

    AC_OFF_ON_Random_2()
  
    Test_Function_Arun_Satellite_OTR_Mains()
    
    Digit_Channel_Selection("Tuner",28)
    time.sleep(5)
    SendKey("Rec",20,1)
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)

    Channel_AudioLanguage_ACOffOn_Revanth()
    
    Digit_Channel_Selection("Tuner",31)
    AC_OFF_ON_Fixed(4)
    time.sleep(delay_variable)

    Digit_Channel_Selection("Satellite",98)
    time.sleep(5)
    AC_OFF_ON_Fixed(6)
    time.sleep(delay_variable)

    #TimeShift_With_StandbyOperations_Revanth()
    AC_OFF_ON_Fixed(6)
    time.sleep(delay_variable)

    AC_OFF_ON_Random_3()
    
    Digit_Channel_Selection("Satellite",86)
    time.sleep(15)
    SendKey("Red",4,1)
    SendKey("Ok",1,1)
    SendKey("Down",0.5,1)
    SendKey("Ok",15,1)
    AC_OFF_ON_Fixed(7)
    time.sleep(delay_variable)

    SwitchingChannels_ACOffOn_Revanth()

    Test_Function_Arun_Tuner_MHEG_Navigation_PLyaback_Without_Standby()

    Digit_Channel_Selection("Tuner",1)
    AC_OFF_ON_Fixed(8)  
    time.sleep(delay_variable)

    Guide_Nav_AC_OFF_ON()
    
    AC_OFF_ON_Random_4()
    
    SwitchingChannels_ACOffOn_Revanth()

    Digit_Channel_Selection("Tuner",512)
    AC_OFF_ON_Fixed(8)  
    time.sleep(delay_variable)

    Switching_Tuner_Channels_ACOffOn_Revanth()

    Teletext_Nav_Tuner_AC_OFF_ON()
    
    AC_OFF_ON_Random_5()
    
    Switching_Satellite_Channels_ACOffOn_Revanth()

    Guide_Launch_Exit_AC_OFF_ON()

    PVRRecording_Playback_ACoffon_Revanth()
    
    AC_OFF_ON_Fixed(9)
    time.sleep(delay_variable)
    
    Channel_SubtitleChange_AC_OFF_ON_Revanth()

    Test_Function_Arun_Satellite_Timeshift_Mains()

    AC_OFF_ON_Random_4()   
    AC_OFF_ON_Random_5()
    AC_OFF_ON_Random_6()


def Block2():  
    
    Digit_Channel_Selection("Satellite",83)
    AC_OFF_ON_Fixed(5)
    time.sleep(35)

    Youtube_Row1()
    App_Gallery_Nav_ACOffOn()

    AC_OFF_ON_Random_1()
    
    Netflix_ACOffOn(1,2)
    OIB()
       
    AC_OFF_ON_Random_2()
    
    CBPlayback_Audios()
    GoogleAssistant_ACOffOn()
    
    AC_OFF_ON_Random_3()
    
    Netflix_ACOffOn(3,4)
    DropBox_StabilityFolder()

    AC_OFF_ON_Random_4()
    
    Amazon_ACOffOn_Revanth(1,2)
    CBPlayback_Videos()
  
    AC_OFF_ON_Random_5()
    
    Youtube_Row3()
    DropBox()

    AC_OFF_ON_Random_6()
    
    Netflix_ACOffOn(5,6)
    CBPlayback_Images()

    AC_OFF_ON_Random_3()
    
    Youtube_Row2()
    Amazon_ACOffOn_Revanth(3,4)
    
    AC_OFF_ON_Random_4()

    CBPlayback()
    DemoMe_App()
    GoogleAssistant_ACOffOn()

    AC_OFF_ON_Random_1()     
    AC_OFF_ON_Random_2()
    AC_OFF_ON_Random_3()

def Block3():
    Digit_Channel_Selection("Satellite",153)
    time.sleep(5)
    AC_OFF_ON_Fixed(5)
    time.sleep(60)    
    Netflix_ACOffOn(3,5)
    SwitchingChannels_ACOffOn_Revanth()
    Youtube_Row1()
    Switching_Satellite_Channels_ACOffOn_Revanth()
    CBPlayback()
    Switching_Tuner_Channels_ACOffOn_Revanth()
    DropBox_StabilityFolder()
    Swtich_Sources_ACOffOn_Revanth()
    Amazon_ACOffOn_Revanth(1,3)
    Channel_AudioLanguage_ACOffOn_Revanth()
    GoogleAssistant_ACOffOn()
    AC_OFF_ON_Random_1()     
    AC_OFF_ON_Random_4()
    AC_OFF_ON_Random_6()

def Block4():
    Digit_Channel_Selection("Satellite",85)
    AC_OFF_ON_Fixed(5)
    time.sleep(35)
    CBPlayback()
    AC_OFF_ON_Random_5()
    DropBox_StabilityFolder()
    CBPlayback_Audios()
    DropBox()
    AC_OFF_ON_Random_3()
    CBPlayback_Images()
    CBPlayback_Videos()
    AC_OFF_ON_Random_2()
    
def Start_Blocks():
    for count in range(0,1):
        #HDMI_ACOffOn_Revanth()    
        Block4()
        #HDMI_ACOffOn_Revanth()    
##        Block2()

def Start_Script():
    y = time.time()
    for x in range(100):
        print ("Round Number %d" %x)
        Start_Blocks()
        z = time.time()-y
        print (z)
        if int(z) >= 28800:
            print ("time exceeded 8hrs")
            return
   
def Execute_Script():
    
    COM_ports = open("COM_PORT.txt", "r")
    i = 0
    try:
        config = configparser.RawConfigParser()
        config.optionxform = str
        Setup_ini_Path = os.getcwd() + "\\INI\\" + "Stab_Setup.ini"
        config.read(Setup_ini_Path)
        FTP_Folder = config.get("Setup","FTP_Folder")
        UART_Folder = config.get("Setup", "UART_Folder")
        TV_Start_No = config.get("Setup", "TV_Start_No")
        Compair_Port = config.get("Setup", "Compair_Port")
        TV_Mains_Port = config.get("Setup", "TV_Mains_Port")
        TTL_Folder = config.get("Setup", "TTL_Folder")
        Date_time_TTL = config.get("Setup", "Date_time_TTL")
        Energenie_Support = config.get("Setup", "Energenie_Support")
    except:
        print (traceback.print_exc())
    Stab_Logs_Folder = "C:\\" + str(UART_Folder)
    print (Stab_Logs_Folder)
    if not os.path.exists(Stab_Logs_Folder):
        os.makedirs(Stab_Logs_Folder)
    COM_ports = open("COM_PORT.txt", "r")
    Folder = int(TV_Start_No) - 1
    print (Folder)
    TTL_Path = "C:\\" + str(TTL_Folder)
    if not os.path.exists(TTL_Path):
        os.makedirs(TV_Number_Path)
        
    TTL_File_Name = TTL_Path + str("\\") + Date_time_TTL
    if not os.path.exists(TTL_File_Name):
        TTL_File = open(TTL_File_Name,"w")
        TTL_File.write("pause 2")
        TTL_File.close()

    for line in COM_ports:
        Folder = Folder + 1
        TV_Number_Path = Stab_Logs_Folder + "\\" + str("TV") + str(Folder)
        if not os.path.exists(TV_Number_Path):
            os.makedirs(TV_Number_Path)    
    #shell = client.Dispatch("WScript.Shell")
    run_venv = WindowsForeground()
    print ("Closing UART logs If any are Opened")
    Stop_UART_log()
    time.sleep(2)
    TTL = "C:\MSAF_TTL\\" + Date_time_TTL
    UART = Start_UART_log(TTL,i,UART_Folder,TV_Start_No)
    time.sleep(5)
    

    i = 1
    for i in range(1,1000):
        Start_Script()
        print ("Test Cycle no is %d " %i)
        time.sleep(80)
        Stop_UART_log()        
        Rename_TPVision_Debug_PyScript(i)
        AC_OFF_ON_Fixed(10)
        time.sleep(60)
        if Energenie_Support == "YES":
            print ("Start UART Logs with current date time of PC")
            TTL = "C:\MSAF_TTL\\" + Date_time_TTL
            UART = Start_UART_log(TTL,i,UART_Folder,TV_Start_No)
            time.sleep(10)             
        else:
            TTL = "C:\MSAF_TTL\\" + Date_time_TTL
            UART = Start_UART_log(TTL,i,UART_Folder,TV_Start_No)
        #Start_Script_1()
        
if __name__ == "__main__":
    AC_OFF_ON_Fixed(5)
    time.sleep(delay_variable)

    for x in range(0,10000):
        Start_Blocks()

    
