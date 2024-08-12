import pyfiglet #(A library that lets you create text banners in ASCII art. )
import sys #(rovides access to command-line arguments and system functions.)
import socket #(Used for network connections, like creating a port scanner.)
from datetime import datetime #(Used for network connections, like creating a port scanner.)
   
ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 
print(ascii_banner) 
   
if len(sys.argv) == 2: 
    target = socket.gethostbyname(sys.argv[1]) #(Converts the provided hostname to an IP address.)
else: 
    print("Invalid amount of Argument you must enter the IP") 
    sys.exit()  # Exit the script if the IP is not provided

print("-" * 50) #Creates a line of 50 dashes for visual separation.
print("Scanning Target: " + target) #Shows which IP or hostname is being scanned.
print("Scanning started at:" + str(datetime.now())) 
print("-" * 50) 

try: 
    for port in range(1, 100): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a new network connection.
        socket.setdefaulttimeout(1) #Sets the time to wait (1 second) before deciding the port is closed.
          
        result = s.connect_ex((target, port)) #Tries to connect to the specified port on the target IP
        if result == 0: 
            print("Port {} is open".format(port)) 
        s.close() 
          
except KeyboardInterrupt: 
        print("\n Exiting Program !!!!") 
        sys.exit() 
except socket.gaierror: #Handles errors if the hostname can't be resolved to an IP address.
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit() 
except socket.error: #Handles general network errors, like if the server isn't responding.
        print("Server not responding !!!!")  # Removed the backslash to avoid the syntax warning
        sys.exit() 
