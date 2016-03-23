import socket
import threading

print""""*********************************************************
*********************************************************
**  _            ______                                **
** | |           |  ___|                         _     **
** | |     __ _  | |_ ___  _ __ _ __ ___   ___  (_)    **
** | |    / _` | |  _/ _ \| '__| '_ ` _ \ / _ \        **
** | |___| (_| | | || (_) | |  | | | | | |  __/  _     **
** \_____/\__,_| \_| \___/|_|  |_| |_| |_|\___| (_)    **
**                                                     **
** _____ _   _  _____  ______       _   _   _      _   **
**|_   _| | | ||  ___| | ___ \     | | | \ | |    | |  **
**  | | | |_| || |__   | |_/ / ___ | |_|  \| | ___| |_ **
**  | | |  _  ||  __|  | ___ \/ _ \| __| . ` |/ _ \ __|**
**  | | | | | || |___  | |_/ / (_) | |_| |\  |  __/ |_ **
**  \_/ \_| |_/\____/  \____/ \___/ \__\_| \_/\___|\__|**
*********************************************************
*********************************************************
****BotNet La Forme Developpe  par: Guillaume Soares,****
***********Nathan  Fievez Et Alexandre Villain***********
*********************************************************"""

# Import the modules needed to run the script.
import sys, os
 
# Main definition - constants
menu_actions  = {}  
 
# =======================
#     MENUS FUNCTIONS
# =======================
 
# Main menu
def main_menu():
    os.system('clear')
    
    print "Quel est votre choix ?"
    print "Appuyez sur 1 pour DDOS"
    print "Appuyez sur 2 pour Voir le nombre de Bots et/ou ouvrir un SHELL sur l'un d'entre eux"
    print "Appuyez sur 3 pour quitter"
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
    print "9. retour au menu principal"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
 
# Menu 2
def menu2():
    print "Bienvenue sur le menu Bots\n"
    print "Sur ce menu, il est possible de voir le nombre de Bots connectes et d'ouvrir un SHELL sur l'un d'entre eux"
    print "9. Back"
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