import platform
import socket
import os

def system_scan():
    print("=== System Scan ===")
    print("OS:", platform.system())
    print("Release:", platform.release())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

def network_info():
    print("\n=== Network Info ===")
    print("Hostname:", socket.gethostname())
    print("IP Address:", socket.gethostbyname(socket.gethostname()))

def environment_variables():
    print("\n=== Environment Variables ===")
    for key, value in list(os.environ.items())[:10]:
        print(f"{key}: {value}")

if __name__ == "__main__":
    system_scan()
    network_info()
    environment_variables()import platform
import socket
import os

def system_scan():
    print("=== System Scan ===")
    print("OS:", platform.system())
    print("Release:", platform.release())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

def network_info():
    print("\n=== Network Info ===")
    print("Hostname:", socket.gethostname())
    print("IP Address:", socket.gethostbyname(socket.gethostname()))

def environment_variables():
    print("\n=== Environment Variables ===")
    for key, value in list(os.environ.items())[:10]:
        print(f"{key}: {value}")

if __name__ == "__main__":
    system_scan()
    network_info()
    environment_variables()
