import socket
import sys


print(""" 

                            ########################################################################
                            #__        __   _                            _          _   _          #
                            #\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___ #
                            # \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \#
                            #  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/#
                            # _ \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|#
                            #            (_)_ __    / _(_)_ __   __| | ___ _ __                    #            
                            #            | | '_ \  | |_| | '_ \ / _` |/ _ \ '__|                   #            
                            #            | | |_) | |  _| | | | | (_| |  __/ |                      #            
                            #            |_| .__/  |_| |_|_| |_|\__,_|\___|_|                      #            
                            #              |_|                                                     #            
                            ########################################################################
      """)

tries = 5
correct_password = "fortnitebattlepass" 
ok = True
while ok:
    password = input("Enter password: ")
    print(" ")
    
    if password != correct_password:
        if tries > 0:
            tries -= 1
            print(f"You have {tries} tries left")
            print(" ")
        if tries == 0:
            print("The laptop will self destruct in 3 minutes")
            print("Run for your life!")
            sys.exit()

    if password == correct_password:
        print("You have enetered the correct password")
        print(" ")
        ok = False

idk = True

while idk:
    are_you_sure = input("Are you sure you want to continue: ")
    print(" ")

    if are_you_sure == "YES":
        idk == False
        break
    if are_you_sure == "NO":
        idk == False
        sys.exit()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket succesfully created")
    print(" ")
except socket.error as err:
    print(f"Socket creation failed with error as {err}")

port = int(input("Enter the port: "))
print(" ")
host_name = input("Enter the name of the website: ")
print(" ")

try:
    ip = socket.gethostbyname(host_name)
    print(f"IP address retrieved: {ip}")
    print(" ")
except socket.gaierror:
    print("Error resolving the host")
    sys.exit()

s.connect((ip, port))
print(f"Successfully connected to  {host_name}")