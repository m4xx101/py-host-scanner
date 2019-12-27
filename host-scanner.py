import os
import sys
import platform
from datetime import datetime
import socket    

t1 = datetime.now()
oper = platform.system()
a='.'
IPAddr = socket.gethostbyname(socket.gethostname())      
tmp=IPAddr.split('.')
net1=tmp[0]+a+tmp[1]+a+tmp[2]+a
#python3 host-scanner.py <specify IP-range with bites =0>
print ("="*59)
print("Starting Scannig: {} at ".format(net1)+str(t1))
print("For {}0/24".format(net1))
print("="*59)
if (oper == "Windows"):
   ping1 = "ping -n 1 "
elif (oper == "Linux"):
   ping1 = "ping -c 1 "
else :
   ping1 = "ping -c 1 "

try:
    for ip in range(1,255):
        fip=net1+str(ip)
        cmd=ping1+fip
        result=os.popen(cmd)
        for line in result.readlines():
            if(line.count("TTL")):
                print("[+] {} Host is alive on the network".format(fip))
    t2 = datetime.now()
    total = t2 - t1
    print ("="*45)
    print ("Scanning completed in: ",total)
    print ("="*45)

except KeyboardInterrupt:
    print("Someone pressed CTRL+C.....")
except:
    print("Somthing went wrong!")
