import socket


def portScan(port):
    if s.connect_ex((host, port)):
        print('The port is closed!')
    else:
        print('The port is open')


# Menu with lists of options
def menu():
    print('What do you want to do? Here a list of options:\n')
    print('[1] Scan a single port\n')
    print('[2] Scan a set of ports\n')
    print('[3] Scan all ports (display only opened ones)\n')
    print('[0] End program\n')
    action = int(input('Insert the number of the action: '))
    return action


# Function to scan a single port
def scanOnePort(host):
    port = int(input('Enter the port to scan: '))
    print('Scanning port %s...' % str(port))
    portScan(port)
    print('\n')


# Function to scan a series of ports
def scanSomePorts(host):
    ports_name = input(
        'Insert a list of ports following this format: ##, ##, ###, #, ####\n')
    ports = ports_name.split(', ')  # List of strings

    # Converts from a list of string to a list of int
    ports_int = []

    for port in ports:
        ports_int.append(int(port))

    # Checks every single port
    for port in ports_int:
        print('Scanning port %s...' % str(port))
        portScan(port)

    print('\n')


# TODO: return just opened ports in a list/set
def scanAllPorts(host):
    for i in range(1, 49151):
        port = i
        print('Scanning port %s...' % str(port))
        portScan(port)

    print('\n')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set timeout to skip longer scan port
# s.settimeout(10)

host = input('Enter the IP to scan: ')

while True:
    action = menu()

    if action == 0:
        break
    elif action == 1:           # Accept one port
        scanOnePort(host)
    elif action == 2:           # Accept indefined number of ports
        scanSomePorts(host)
    elif action == 3:           # Checks every single port from 1 to 49151
        scanAllPorts(host)
    # TODO: Add option to change host.
    else:
        print('This is not a correct option.\n')
        print('\n')

# host = '137.74.187.104'   # hackthissite.org
# port = 21
