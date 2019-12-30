import os
import sys
import platform
from datetime import datetime
import socket    
import threading

time1 = datetime.now() #Taking starting time for time taken calculations
allips=[]
threads=[]
oper = platform.system() #Checking for OS
a='.'
IPAddr = socket.gethostbyname(socket.gethostname()) #Getting current systems IP      
tmp=IPAddr.split('.') #Splitting with delimeter '.'
net1=tmp[0]+a+tmp[1]+a+tmp[2]+a #Making new string accrording to /24 subnet
#Just a banner
print ("="*59)
print("Starting Scannig: {}0/24 at ".format(net1)+str(time1))
print("="*59)
#Command according to OS
if (oper == "Windows"):
   ping1 = "ping -n 1 "
elif (oper == "Linux"):
   ping1 = "ping -c 1 "
else :
   ping1 = "ping -c 1 "

for ip in range(1,255):  #Brute forcing basically :P 
        fip=net1+str(ip)
        cmd=ping1+fip
        allips.append(cmd)

def scan(a): 
    for line in os.popen(a).readlines():
        if(line.count("TTL")):
            cutline=line.split(' ')
            print("[+] {} Host is alive on the network".format(cutline[2]))



for xyz in allips:
    t1 = threading.Thread(target=scan,args=(xyz,))
    t1.start()

t1.join()


time2 = datetime.now() #Getting time after loop is completed
total = time2 - time1  #Total time taken 
#Just another banner
print ("="*45)
print ("Scanning completed in: ",total)
print ("="*45)
