import socket
import re
import sys


class PortScanner:
    def __init__(self, addressFamily, host, port) -> None:
        self.host = host
        self.portRange = port
        self.addressFamily = addressFamily
        self.openPorts: list = []
        self.portScanner()

    def createSocket(self, port) -> None:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, port))
        s.close()

    def scanPort(self, port):
        try:
            self.createSocket(port)
            self.openPorts.append(port)
            print(f"{port}    open")
        except (OSError, ConnectionRefusedError) as e:
            if e.errno == 113:
                print("[!] No route to host. Make sure the host is reachable")
                return
            if e.errno == 10061:
                print(
                    "[!] No connection could be made because the target machine actively refused it. Check your firewall settings."
                )
                return

    def findOpenPorts(self, rangeStart: int, rangeEnd: int) -> None:
        portRange = range(int(rangeStart), int(rangeEnd) + 1)

        if portRange[-1] > 65535:
            return print("[!] Port rangeEnd is greater than 65535")

        print("Attempting to Scan...\n")
        for port in portRange:
            self.scanPort(port)

        if len(self.openPorts) == 0:
            print("\n[!] No open ports found")
            return

        print(
            f"\n[#] {len(self.openPorts)} open port{'s' if len(self.openPorts) > 1 else ''} were found"
        )

    def getPortRange(self):
        portRe: str = "([\d]+[/][\d]+)"

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
            return self.ipv4Scan()
        print("[!] Address family must be ipv4. ipv6 is not supported yet")


if __name__ == "__main__":
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if all(opt in opts for opt in ["-af", "-h", "-pr"]):
        addressFamily, ip, port = args
        PortScanner(addressFamily, ip, port)
    else:
        raise SystemExit(
            f"Usage: {sys.argv[0]} -af <address family (ipv4)> -h <ip address> -pr <port range (e.g. 300/100)>"
        )


# socket.AF_INET = Internet Address Family ipv6
# socket.SOCK_STREAM = Socket type TCP
# Port max = 65535
