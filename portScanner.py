import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set timeout to skip longer scan port
# s.settimeout(5)



host = input('Enter the IP to scan: ')
port = int(input('Enter the port to scan: '))

# host = '137.74.187.104' # hackthissite.org
# port = 21

print('Scanning port %s...' % str(port))
portScan(port)


# TODO: create a menu with different options.
def menu():
    print('What do you want to do?')

def portScan(port):
    if s.connect_ex((host, port)):
        print('The port is closed!')
    else:
        print('The port is open')