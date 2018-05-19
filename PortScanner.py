import socket

ports = []
open_ports = []
closed_ports = []

ip = input("Enter ip: ")
file = open("ports.txt","w")

def port_scanner():
    for port in range(65536):
        _socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        _socket.settimeout(0.01)
        try:
            _socket.connect((ip,port))
        except:
            file.write("[ CLOSED ] - %s.\n" %port)
        else:
            open_ports.append(port)
            file.write("[ OPENED ] - %s.\n" %port)
        _socket.close()          
    print("Scan finished")
    file.write("####################\n")
    if len(open_ports) != 0:        
        for port in open_ports:
            file.write("[ OPENED ] - %s:%s\n" % (ip, port))
    else:
        file.write("All ports is closed.\n")    
    file.close()    

port_scanner()
