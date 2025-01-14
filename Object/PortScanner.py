import socket
from scapy.all import *
from scapy.layers.inet import ICMP, IP

class PortScanner:
    def __init__(self, target):
        self.target = target

    def isPortOpenTCP(self,port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target, port))
            return True
        except:
            return False
        
    def isPortOpenUDP(self,port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect((self.target, port))
            return True
        except:
            return False
    
    def scan(self, start, end):
        l = []
        tcpPorts = []
        udpPorts = []
        for port in range(start, end+1):
            if self.isPortOpenTCP(port):
                l.append(port)
                tcpPorts.append(port)
            elif self.isPortOpenUDP(port):
                l.append(port)
                udpPorts.append(port)
        return l, tcpPorts, udpPorts

    def getProtocols(self, start, end):
        dico = {}
        for i in range(start, end+1):
            if self.isPortOpenTCP(i):
                dico[i] = "TCP"
            elif self.isPortOpenUDP(i):
                dico[i] = "UDP"
            elif sr1(IP(dst=self.target)/ICMP(), timeout=2, verbose=0):
                dico[i] = "ICMP"
        return dico
    
    def getServices(self, start, end):
        services = {}
        proto = self.getProtocols(start, end)
        for port in proto.keys():
            if proto[port] == "TCP":
                try:
                    service = socket.getservbyport(port, 'tcp')
                    services[port] = service
                except:
                    services[port] = "Unknown"
            elif proto[port] == "UDP":
                try:
                    service = socket.getservbyport(port, 'udp')
                    services[port] = service
                except:
                    services[port] = "Unknown"
            elif proto[port] == "ICMP":
                services[port] = "ICMP"
        return services
    
if __name__ == "__main__":
    target = "8.8.8.8"
    scanner = PortScanner(target)
    print(scanner.getServices(1, 1000))