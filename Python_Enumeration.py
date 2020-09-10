"""Importing Modules for functionality and use of the Python Interpreter"""

import threading  # A multi-tasking library imported
import subprocess # Allows for communication with ai program 
import time       # This is required to include time module
import os         # module provides a portable way of using operating system dependent functionality
import sys        # module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import ipaddress  # module provides factory functions to conveniently create IP addresses, networks and interfaces
import socket
import time
from queue import Queue
import re


""" These are the variables used within the program """

active_ip={"active":[]}





""" These are the functions used/called within the program """
def ping_sweep(ip):
    try:
        subprocess.check_output(["ping", "-c", "1","-q",ip ], stderr=subprocess.DEVNULL) # ping 1 packet to the ip address i.e. ip_range variable
        print("Active " + ip)
        active_ip['active'].append(ip)
    except:
        pass


def pscan(target,port):
    s = socket.socket(2,1)   # (2,1) 2 is IPv4 and 1 is TCP Connection
    try:
        con = s.connect((target,port))
        s.close()
        return True
    except:
        return False

def ip_list(ip_subnet):





       """START OF THE PROGRAM"""


print("===========================================================")
print("             Welcome to the Python Enumerater" + "\n" + "Here you will be able to enumerate your production networks")
print("===========================================================")
time.sleep(5)
print("\n")
print("===================================================================================================")

print("You will be prompted to enter the subnet and cidr to conduct a (PING SWEEP) of your network shortly " + "\n" + "if icmp is disabled you will not receieve a response from a device on your network")
print("===================================================================================================")
print("\n")
time.sleep(6)


""" Ping Sweep IPs in a subnet """
while(True):
    while(True):
            ip_subnet = input("Enter the subnet to be scanned (e.x. 192.168.1.0/24): ")
            try:
                ip_list = ipaddress.IPv4Network(ip_subnet)
                break
            except:
             print("\n")
             print("No results from the netwok entered, please check your input and verify the network is entered correctly")
             print("\n")
             continue




    for ip in ipaddress.IPv4Network(ip_subnet):
        x=threading.Thread(target=ping_sweep, args=[str(ip)])   # threading means simultaneously exeuting a function without wait on iterations
        x.start()

    if (len(active_ip['active'])==0):
     print("\n")
     print('The network entered has no results, please check the network entered and re-run')
     continue 
    else:
      break



""" Port Scan live hosts that have been found """

print("\n")
print("==========================================================================================")
print("You will be prompted to enter a host to be (PORT SCANNED) scanned")
print("==========================================================================================")
print("\n")
time.sleep(6)


socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

while(True):

    target = input('Enter the host to be scanned: ')
    pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}$')
    if(re.match(pattern,target)):
        break
    else:
        continue
    
t_IP = socket.gethostbyname(target)
print ('Starting scan on host: ', t_IP)

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'is open')
      con.close()
   except:
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 500):
   q.put(worker)
   
q.join()
print('Time taken:', time.time() - startTime)
