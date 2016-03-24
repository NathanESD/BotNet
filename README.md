# BotNet

Manuel d’utilisation
Date : 22/03/2016
Auteurs : Guillaume SOARES, Nathan FIEVEZ et Alexandre VILLAIN

Ce manuel d’utilisation explique comment se servir du BotNet La Forme.

Table des matières :
Manuel d’utilisation
Explication de ce que notre programme peut faire
Exécution du programme
L’index du programme
Le sous Menu “DDOS”
Le sous Menu “Lister les clients / Reverse SHELL”
Le sous Menu “Quitter le programme”
Les conseils des développeurs

Explication des fonctionnalités :
Ce programme permet deux fonctionnalités :
- Faire des DDOS vers une adresse IP.
- Ouvrir des SHELL sur les machines infectés. 

Nos machine infectés se connectent au serveur “maître” après avoir téléchargé un payload dissimulé dans une version modifiée de CHROME.
Les prérequis :
Pour exécuter le programme, les prérequis sont d’avoir python d’installé sur votre machine. 
il vous suffit de tapez la commande “python serveur.py”  pour exécuter le BOTNET.
L’index du programme
L’index de notre programme offre 3 possibilités:

	-1- DDOS
	-2- Liste des zombies / Reverse SHELL
	-3- Quitter le programme

Le sous Menu “DDOS”
Ce sous menu offre la possibilité d’entrer une adresse IP “victime” sur laquelle lancer une attaque DDOS ou alors la possibilité de revenir au menu principal en tapant 0.
Il est possible de stopper le DDOS à tout moment et de revenir sur le menu principal en tapant stop.

Le sous Menu “Liste des zombies / Reverse SHELL”
Ce sous menu affiche la liste de tous les zombies connectés (nom + IP). 
Tous ces zombies sont associés à un numéro. 
Il est possible d’ouvrir un reverse shell vers une de ces machines infectées en tapant le numéro correspondant au client choisi.

Pour quitter le reverse shell et revenir au menu principal, tapez la commande stop.

Le sous Menu “Quitter le programme” 
Ce sous menu quitte le programme.

Les conseils des développeurs
Pour rester anonyme, les concepteurs vous conseils de toujours prendre le plus de précautions possible tel que vous connecter à votre serveur à partir d’un réseau anonyme de (tor), d’utiliser un VPN respectant la vie privée des utilisateurs, d'héberger son serveur dans un pays dans lequel il n’y a pas beaucoup de lois concernant l’utilisation d’internet.
