import socket 
import threading
from queue import Queue

target = '127.0.0.1'

queue = Queue()
open_ports = list()

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
      
'''
#print(portscan(80))

for port in range(1, 1024):    #FTP, HTTP, SSH
    result = portscan(port)
    if result == True:
        print("Port {} is open!".format(port))
    else:
        print("Port {} is closed".format(port))
'''

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open! \n".format(port))
            open_ports.append(port)
        else:
            print("Port {} is closed! \n".format(port))

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = list()

for t in range(50):
    thread = threading.Thread(target = worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)

