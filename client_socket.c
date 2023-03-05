#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <string.h>
#include <signal.h>

#include "headers/serv_cli_fifo.h"
#include "headers/Handlers_Cli.h"

int main(int argc, char** argv){

   /* Déclarations */
    Client_Question cli_question;
    Server_Response serv_response;
    
    struct sigaction sa;
    sa.sa_flags = 0;
    
    /* Installation des Handlers */
    //signal(SIGUSR1,hand_reveil);
    sa.sa_handler = &hand_reveil;
    sigaction(SIGUSR1, &sa, NULL);
    
   if(argc!=3){printf("Must enter IP and port\n"); exit(1);}
   /* ETAPE-I:  Créer un socket */
   int sockfd = socket(PF_INET, SOCK_STREAM, 0);
   /* ETAPE-II: Remplissez le DS de Socket pour l'adresse IP et le port distants, et laissez
   l'adresse IP et le port locaux être sélectionnés par le système d'exploitation lui-même */
   struct sockaddr_in dest_addr;
   dest_addr.sin_family = AF_INET;    
   dest_addr.sin_port = htons(atoi(argv[2]));
   inet_aton(argv[1], &dest_addr.sin_addr);
   memset(&(dest_addr.sin_zero), '\0', sizeof dest_addr.sin_zero); 
   
   /* ETAPE-III: Connecter les deux sockets du client et du serveur */
   connect(sockfd, (struct sockaddr*)& dest_addr, sizeof dest_addr);
   
  /* ETAPE-IV:  Le client lit la chaîne à partir de stdin et l'envoie au serveur, puis lit la
  chaîne renvoyée par le serveur et l'affiche sur stdout */
   char buff1[128],buff2[128] ;
   //while(1){
      //int n = read(0, buff1, sizeof buff1);   
      //buff1[n] = '\0';
      
      /* Construction et envoi d’une question */
	srand(time(NULL));
	cli_question.nbre_aleatoire = rand() % 10 + 1;
	strcpy(cli_question.question, "Envoie moi ");
	char nbre_ale[10];
	sprintf(nbre_ale, "%i", cli_question.nbre_aleatoire);
	strcat(cli_question.question, nbre_ale);
	strcat(cli_question.question, " nombres aléatoire");

	cli_question.pid_client = getpid();
	int question_size = strlen(cli_question.question);

	if (write(sockfd, &cli_question, sizeof(Client_Question)) == -1) {
	    //perror("write");
	    return 2;
	}
	
	pause(); 
	
        serv_response.pid_serveur = getpid();
	/* Lecture de la réponse */
	if (read(sockfd, &serv_response, sizeof(Server_Response)) == -1) {
		perror("read");
		return 2;
	}
	
	/* Envoi du signal SIGUSR1 au serveur */
	kill(serv_response.pid_serveur, SIGUSR1);
	
	/* Traitement local de la réponse */
	for(int i=0; i < cli_question.nbre_aleatoire; i++)
	{
	    printf("Received %d\n", serv_response.reponse[i]);
	}
	printf("Le PID serveur est %d\n", serv_response.pid_serveur);
	
      //buff2[n] = '\0';
      //write(1, buff2, n);
   //}
//*** ETAPE-V:  Fermer la socket
   close(sockfd);
   exit(0);
}
