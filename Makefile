CC := gcc

main : serveur client client_socket serveur_socket

serveur : serveur.c
	$(CC)  sources/Handlers_Serv.c serveur.c -o serveur
	
client : client.c
	$(CC)  sources/Handlers_Cli.c client.c -o client
	
client_socket : client_socket.c
	$(CC)  sources/Handlers_Cli.c client_socket.c -o client_socket
	
serveur_socket : serveur_socket.c 
	$(CC)  sources/Handlers_Serv.c serveur_socket.c -o serveur_socket
