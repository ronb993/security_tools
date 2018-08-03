# Simple port scanner for learning purposes with sockets


import socket
import os



def TCP_connect(ip, port_number, delay, output):
    theSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    theSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    theSock.settimeout(delay)
    try:
        theSock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''


def scan_ports(host_ip, delay, first_port, second_port):
    output = {}
    for i in range(first_port, second_port):
        TCP_connect(host_ip, i, delay, output)
        if output[i] == 'Listening':
            print(str(i) + ': ' + output[i])

def single_port(host_ip, one_port, delay=1):
    output = {}
    TCP_connect(host_ip, one_port, delay, output)
    if output[one_port] == 'Listening':
        print(str(one_port) + ': ' + output[one_port])
    else:
        print("Closed")


def main():
    choice = '0'
    while choice == '0':
        print("Welcome to my port checker program")
        print("1) Scan single ports")
        print("2) Scan multiple ports")
        print("3) Quit the program")
   
        choice = input("Please Make a Choice: ")

        if choice == '1':
            pick_ip = input("Enter IP: ")
            pick_port = int(input("Port: "))
            single_port(pick_ip, pick_port)
    
        elif choice == '2':
            scan_ip = input("Enter IP: ")
            delay = int(input("Timeout Seconds: "))
            port_start = (int(input("Starting Port: ")))
            port_end = (int(input("Ending Port: ")))
            scan_ports(scan_ip, delay, port_start, port_end)

        elif choice == '3':
            print("Good bye")
            break
    
        else:
            print("I do not understand")
            os.system('clear')
            main()



if __name__ == "__main__":
    main()
