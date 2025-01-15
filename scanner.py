import argparse
from Object.port_scanner import PortScanner

def parse_port_range(port_range):
    start, end = map(int, port_range.split('-'))
    return (start, end)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("action", choices=["scan"], help="Action to perform (e.g., 'scan')")
    parser.add_argument("target", help="Target IP address or hostname to scan")
    parser.add_argument("ports", type=parse_port_range, help="Port range to scan (e.g., '1-1100')")

    args = parser.parse_args()
    print(args.ports)
    if args.action == "scan":
        scanner = PortScanner(args.target)
        print(scanner.getServices(args.ports[0], args.ports[1]))
        