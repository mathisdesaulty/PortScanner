import socket
from scapy.all import *
from scapy.layers.inet import ICMP, IP

class PortScanner:
    def __init__(self, target):
        self.target = target

    def isPortOpenTCP(self,port):
        try:
            print("Checking TCP port ", port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)  # Timeout de 1 seconde
            sock.connect((self.target, port))
            return True
        except:
            return False
        
    def isPortOpenUDP(self,port):
        try:
            print("Checking UDP port ", port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(0.1)  # Timeout de 1 seconde
            sock.sendto(b'', (self.target, port))
            try:
                data, addr = sock.recvfrom(1024)
                return True
            except:
                return False
        except:
            return False
    
    def scan(self, start, end):
        ports = {}
        for port in range(start, end+1):
            if self.isPortOpenTCP(port):
                ports[port] = "TCP"
            elif self.isPortOpenUDP(port):
                ports[port] = "UDP"
        return ports
    
    def getServices(self, start, end):
        services = {}
        proto = self.scan(start, end)
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
    print(scanner.getServices(440,445))