import socket
import re
import sys

# socket.AF_INET = Internet Address Family ipv6
# socket.SOCK_STREAM = Socket type TCP
# Port max = 65535
class PortScanner:
    def __init__(self, addressFamily, host, port) -> None:
        self.host = host
        self.portRange = port
        self.addressFamily = addressFamily
        self.portScanner()
    
    def createSocket(self, port) -> None:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, port))
        s.close()

    def findOpenPorts(self, rangeStart: int, rangeEnd: int) -> None:
        openPortsCount: int = 0

        for port in range(int(rangeStart), int(rangeEnd) + 1):
            try:
                self.createSocket(port)
                openPortsCount += 1
                print(f"{port}   Open")
            except:
                pass
        if openPortsCount == 0:
            print("\n[!] No open ports found")
            return
        print(f"\n[#] {openPortsCount} open port{'s' if openPortsCount > 1 else ''} were found")

    def getPortRange(self):
        portRe: str = "([\d]+[/][\d]+)"
        # portRange: str = input("[?] Port range to scan (e.g. 20/300): ")

        validatePort: object = re.match(portRe, self.portRange)
        portMatch: bool = hasattr(validatePort, "group")

        if portMatch:
            if validatePort.group() != self.portRange:
                print("\n[!] Type a valid port range")
                return
            rangeStart, rangeEnd = self.portRange.split("/")
            return rangeStart, rangeEnd
        print("\n[!] Type a valid port range")

    def ipv4Scan(self):
        ipv4Re: str = "([\d]+[.][\d]+[.][\d]+[.][\d]+)"

        validateIp: object = re.match(ipv4Re, self.host)
        ipMatch: bool = hasattr(validateIp, "group")

        if ipMatch:
            if validateIp.group() != self.host:
                print("\n[!] Type a valid ip address")
                return
            rangeStart, rangeEnd = self.getPortRange()
            self.findOpenPorts(int(rangeStart), int(rangeEnd))
            return
        print("\n[!] Type a valid ip address")

    def portScanner(self) -> None:
        if self.addressFamily == "ipv4":
            self.ipv4Scan()
            return

if __name__ == "__main__":
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if all(opt in opts for opt in ['-af', '-h', '-pr']):
        addressFamily, ip, port = args
        PortScanner(addressFamily, ip, port)
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} -af <address family (ipv4 or ipv6)> -h <ip address> -pr <port range (e.g. 300/100)>")
