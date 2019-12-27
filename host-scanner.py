import os
import sys
import platform
from datetime import datetime
import socket    

t1 = datetime.now() #Taking starting time for time taken calculations
oper = platform.system() #Checking for OS
a='.'
IPAddr = socket.gethostbyname(socket.gethostname()) #Getting current systems IP      
tmp=IPAddr.split('.') #Splitting with delimeter '.'
net1=tmp[0]+a+tmp[1]+a+tmp[2]+a #Making new string accrording to /24 subnet
#Just a banner
print ("="*59)
print("Starting Scannig: {} at ".format(net1)+str(t1))
print("For {}0/24".format(net1))
print("="*59)
#Command according to OS
if (oper == "Windows"):
   ping1 = "ping -n 1 "
elif (oper == "Linux"):
   ping1 = "ping -c 1 "
else :
   ping1 = "ping -c 1 "

try:
    for ip in range(1,255):  #Brute forcing basically :P 
        fip=net1+str(ip)
        cmd=ping1+fip
        result=os.popen(cmd)
        for line in result.readlines():
            if(line.count("TTL")):
                print("[+] {} Host is alive on the network".format(fip))
    t2 = datetime.now() #Getting time after loop is completed
    total = t2 - t1  #Total time taken 
    #Just another banner
    print ("="*45)
    print ("Scanning completed in: ",total)
    print ("="*45)
#If keyboard interruption happens 
except KeyboardInterrupt:
    print("Someone pressed CTRL+C.....")
#Other errors
except:
    print("Somthing went wrong!")
