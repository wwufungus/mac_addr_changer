#!/usr/bin/env python
import subprocess
x = "0"
while x == "0":
    userChoice = input("Enter your Wifi device that you want to change: 1 = wlan0 2 = eth0 3 = lo : ")

    if userChoice == "1":
        wifiDevice = "wlan0"
        x = "1"
    elif userChoice == "2":
        wifiDevice = "eth0"
        x = "1"
    elif userChoice == "3":
        wifiDevice = "lo"
        x = "1"   
    else:
        print("Invalid choice")
        x = "0"
else:
    macChoice = input("Enter your MAC address that you want to change your interface to: example 12:22:33:44:55:66 <mac address>  ")            
    subprocess.call("ifconfig " + wifiDevice +  " down", shell=True)
    subprocess.call("ifconfig " + wifiDevice + " hw ether " + macChoice, shell=True)
    subprocess.call("ifconfig " + wifiDevice + " up", shell=True)
    print("You have succesfully changed your " + wifiDevice + " mac address")