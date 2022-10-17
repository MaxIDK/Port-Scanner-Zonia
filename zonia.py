import os
import time

from socket import *


class Zonia():
    def __init__(self):
        self.start()
        self.input()

    def start(self):
        os.system('cls')
        print('''                                                                                                                                                  
ZZZZZZZZZZZZZZZZZZZ                                     iiii                    
Z:::::::::::::::::Z                                    i::::i                   
Z:::::::::::::::::Z                                     iiii                    
Z:::ZZZZZZZZ:::::Z                                                              
ZZZZZ     Z:::::Z     ooooooooooo   nnnn  nnnnnnnn    iiiiiii   aaaaaaaaaaaaa   
        Z:::::Z     oo:::::::::::oo n:::nn::::::::nn  i:::::i   a::::::::::::a  
       Z:::::Z     o:::::::::::::::on::::::::::::::nn  i::::i   aaaaaaaaa:::::a 
      Z:::::Z      o:::::ooooo:::::onn:::::::::::::::n i::::i            a::::a 
     Z:::::Z       o::::o     o::::o  n:::::nnnn:::::n i::::i     aaaaaaa:::::a 
    Z:::::Z        o::::o     o::::o  n::::n    n::::n i::::i   aa::::::::::::a 
   Z:::::Z         o::::o     o::::o  n::::n    n::::n i::::i  a::::aaaa::::::a 
ZZZ:::::Z     ZZZZZo::::o     o::::o  n::::n    n::::n i::::i a::::a    a:::::a 
Z::::::ZZZZZZZZ:::Zo:::::ooooo:::::o  n::::n    n::::ni::::::ia::::a    a:::::a 
Z:::::::::::::::::Zo:::::::::::::::o  n::::n    n::::ni::::::ia:::::aaaa::::::a 
Z:::::::::::::::::Z oo:::::::::::oo   n::::n    n::::ni::::::i a::::::::::aa:::a
ZZZZZZZZZZZZZZZZZZZ   ooooooooooo     nnnnnn    nnnnnniiiiiiii  aaaaaaaaaa  aaaa


# A very simple port scanner called zonia.
# This tool is for educational purposes only.  
# Created by MaxIDK.''')

    def input(self):
        open_ports = []
        target = input('\nEnter the host: ')
        port_start = input("\nEnter the lower searching boundary: ")
        port_end = input("\nEnter the upper searching boundary: ")

        startTime = time.time()
        t_IP = gethostbyname(target)

        print(f"\nRange: {port_start} - {port_end}")
        print(f"Starting scan on target: {t_IP}\n")
        
        for i in range(int(port_start), int(port_end)):

            print(f'Port: {str(i)}', end="\r")

            s = socket(AF_INET, SOCK_STREAM)

            con = s.connect_ex((t_IP, i))
            if (con == 0):
                open_ports.append(i)
                s.close()
            else:
                s.close()
        os.system('cls')
        print(f'IPV4-Address. . . . . . . . . . . . : {t_IP}')
        print(f'Range . . . . . . . . . . . . . . . : {port_start} - {port_end}')
        print(f'Open ports. . . . . . . . . . . . . : {open_ports if len(open_ports) != 0 else "No ports open"}')
        print(f'Time taken. . . . . . . . . . . . . : {time.time() - startTime}')

        self.input()

App = Zonia()