import SIP_proxy as proxy
import socketserver
import socket
import threading


default_IP = '10.10.37.255'
IP = default_IP

default_PORT = 5060
PORT = default_PORT

default_FILENAME = "proxyLOG"


def validate_IP(addr):
    parts = addr.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        if int(part) < 0 or int(part) > 255:
            return False
 
    return True 

def set_IP():
    global IP 
    IP = input()

    if not IP:
        IP = default_IP

    elif IP == "127.0.0.1" or not validate_IP(IP):
        print("IP address \'" + IP + "\' is not valid! IP address reset to default.")
        IP = default_IP

def set_PORT():
    global PORT 
    temp = input()

    if not temp:
        PORT = default_PORT

    elif not temp.isdigit():
        print ("Wrong port number! Port number reset to default.")
        PORT = default_PORT
    
    else:
        PORT = int (temp)
        if PORT > 65535 or PORT < 1:
             print ("Wrong port number! Port number reset to default.")
             PORT = default_PORT

def init_server():
    print ("Write name of log file (blank for default): ")
    temp = input()

    if not temp:
        temp = default_FILENAME

    proxy.init_log(temp, IP, PORT)
    proxy.set_var(IP, PORT)

if __name__ == "__main__":
    print ("   ------ PROXY SERVER ------")
    print ("   --------------------------\n")
    print ("   TIP: Write 'help' for available commands")

    while True:
        str = input()

        if str == "exit":
            break

        elif str == "help":
            print("\'ip\' - set IP address of Proxy server (for correct functioning use IP address from 'ipconfig' command)")
            print("\'port\' - set PORT number of Proxy server")
            print("\'start\' - initializes and turns on Proxy server")
            print("\'exit\' - closes program")

        elif str == "ip":
            print ("Set IP address of Proxy Server (blank for default): ")
            set_IP()
            print ("Server IP address is: " + IP)

        elif str == "port":
            print ("Set PORT number of Proxy Server (blank for default): ")
            set_PORT()
            print ("Server port number is:", PORT)

        elif str == "start":
            init_server()

            print ("---------------------------------------")
            print ("  Proxy Server started")
            print ("  Pressing \'Ctrl + C\' will stop the server")
            print ("  Server IP address: " + IP)
            print ("  Server PORT number ", PORT)
            print ("---------------------------------------")

            server = socketserver.UDPServer((IP, PORT), proxy.UDPHandler)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass
            server.server_close()
            print ("Server closed")

        else:
            print ("Wrong command!")



