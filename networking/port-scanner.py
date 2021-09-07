import socket
import re

# socket.AF_INET = Internet Address Family ipv6
# socket.SOCK_STREAM = Socket type TCP
# Port max = 65535
def portScanner() -> None:
    ipv4Re = "([\d]+[.][\d]+[.][\d]+[.][\d]+)"
    portRe = "([\d]+[/][\d]+)"
    openPortsCount = 0

    print(
        """
Select Address Family:

[1] ipv4
[2] ipv6
""")
    
    addressFamily = input("Choose an option number: ")

    if addressFamily == "1":
        host = input("\n[?] Host ip: ")
        validateIp = re.match(ipv4Re, host)

        if hasattr(validateIp, "group"):
            if validateIp.group() != host:
                print("\n[!] Type a valid ip address")
                return

            portRange = input("[?] Port range to scan (e.g. 20/300): ")
            validatePort = re.match(portRe, portRange)

            if hasattr(validatePort, "group"):
                if validatePort.group() != portRange:
                    print("\n[!] Type a valid port range")
                    return
                rangeStart, rangeEnd = portRange.split("/")

                for port in range(int(rangeStart), int(rangeEnd) + 1):
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((host, port))
                        s.close()
                        openPortsCount += 1
                        print(f"{port}   Open")
                    except:
                        pass

                if openPortsCount == 0:
                    print("\n[!] No open ports found")
                return
            print("\n[!] Type a valid port range")
            return
        print("\n[!] Type a valid ip address")


portScanner()
