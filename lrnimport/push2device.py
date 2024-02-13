#!/usr/bin/env python3

import crayons

#function to push command?
def commandpush(devicecmd): 

    for ip in devicecmd.keys(): #looping
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') #an fstring
        
        for mycmds in devicecmd[ip]:
            print(f'Attempting to send command --> {mycmds}')
    return None

#Now heres the main
def main():
    """Called at runtime"""

    #dict containing IPs mapped to a list of physical interfaces
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("Welcome ot the network device command pusher")

    print("\nData set found\n" )

    commandpush(devicecmd)

main()