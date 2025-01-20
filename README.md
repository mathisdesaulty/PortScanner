# Port Scanner

This project is a simple port scanner written in Python. It allows you to check if TCP and UDP ports are open on a specified target and retrieve the services associated with these ports.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/PortScanner.git
    ```
2. Navigate to the project directory:
    ```bash
    cd PortScanner
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can use the port scanner by running the `port_scanner.py` script. For example:

```bash
python port_scanner.py
```

### Code Example

Here is an example of code to scan ports 440 to 445 on the target `8.8.8.8`:

```python
if __name__ == "__main__":
    target = "8.8.8.8"
    scanner = PortScanner(target)
    print(scanner.getServices(440, 445))
```

### Using argparse

You can also use the project with `argparse` for command-line arguments:

```python
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
```

## Features

- **isPortOpenTCP(port)**: Checks if a TCP port is open.
- **isPortOpenUDP(port)**: Checks if a UDP port is open.
- **scan(start, end)**: Scans a range of ports and returns the open ports with their protocol (TCP or UDP).
- **getServices(start, end)**: Retrieves the services associated with open ports in a specified range.

## Authors

- [Your Name](https://github.com/your-username)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
