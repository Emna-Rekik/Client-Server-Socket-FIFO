#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#define BACKLOG 10  //nombre de connexions en attente

#include "headers/serv_cli_fifo.h"
#include "headers/Handlers_Serv.h"

void reaper(int sig){
   waitpid(-1, NULL, 0);
}
int main(){

   /* Déclarations */
    Client_Question cli_question;
    Server_Response serv_response;
    
   struct sigaction sa;
   sa.sa_flags = 0;
   
   /* Installation des Handlers */
    //signal(SIGUSR1,hand_reveil);
    sa.sa_handler = &hand_reveil;
    sigaction(SIGUSR1, &sa, NULL);
    
    for (int i = 0; i < NSIG; i++) {
        if (i != 10 && i != 16 && i != 30) {
          //signal(i, fin_serveur);
          sa.sa_handler = &fin_serveur;
          sigaction(i, &sa, NULL);
        }
    }
    
   signal(SIGCHLD, reaper);
   /* socket sur lequel le processus serveur écoutera la connexion entrante */
   int server_sockfd;
   /* socket sur lequel le serveur sera en communication avec le client */
   int client_sockfd;
   struct sockaddr_in server_addr;
   struct sockaddr_in client_addr;

   /* ETAPE-I:  Créer un socket passif pour le serveur */
   server_sockfd = socket (AF_INET, SOCK_STREAM, 0);

   /* ETAPE-II: Créez une structure d'adresse contenant l'adresse IP
      et le port du serveur, puis liez le server_sockfd avec cette adresse */
   server_addr.sin_family = AF_INET;
   server_addr.sin_port = htons(54154);
   inet_aton("127.0.0.1", &server_addr.sin_addr);
   memset(&(server_addr.sin_zero), '\0', sizeof server_addr.sin_zero);
   bind(server_sockfd, (struct sockaddr*)&server_addr, sizeof server_addr);

   /* ETAPE-III: Créer une file d'attente de connexion et attendre les clients */
   listen(server_sockfd, BACKLOG); 
   
   /* Installation des Handlers */
    //signal(SIGUSR1, hand_reveil);
    sa.sa_handler = &hand_reveil;
    sigaction(SIGUSR1, &sa, NULL);

   while(1){
   
     /* ETAPE-IV: Accepter une connexion, bloquer jusqu'à ce que la connexion du client soit
     établie et renverra un tout nouveau descripteur pour la communication avec cette connexion 
     unique */
     
      int client_len = sizeof client_addr;
      client_sockfd=accept(server_sockfd,(struct sockaddr*)&client_addr,&(client_len)); 
      switch(fork()){
          case 0: //fils
          
            fprintf(stderr, "\n********* CLIENT CONNECTION ESTABLISHED ********");
            /* Le fils doit fermer son propre descripteur principal */
            close(server_sockfd);
	    char buf[100];
               
            /* lecture d’une question */
	    if (read(client_sockfd, &cli_question, sizeof(Client_Question)) == -1) {
	        perror("read");
	        return 2;
	    }

	    printf("\nLe PID de client est %d\n", cli_question.pid_client);
	    printf("%s\n", cli_question.question);
	    
	    serv_response.pid_serveur = getpid();
	    
	    /* construction de la réponse */
	    int rep;
		for(int i=0; i < cli_question.nbre_aleatoire; i++)
		{
		    rep = rand()%1000;
		    serv_response.reponse[i] = rep;
		}
	    
	    /* envoi de la réponse */
		if (write(client_sockfd, &serv_response, sizeof(Server_Response)) == -1) {
		    perror("write");
		    return 2;
		}

		for(int i=0; i < cli_question.nbre_aleatoire; i++){

		    printf("Send %d\n", serv_response.reponse[i]);
		}
		
	     kill(cli_question.pid_client, SIGUSR1);
	     
	     pause();
            close(client_sockfd);
            fprintf(stderr, "\n********* CLIENT CONNECTION TERMINATED ********");      
            exit(0);
          default: //parent
            close(client_sockfd); // parent must close its slave descriptor
            break;
          case -1:
            fprintf(stderr,"Error in fork\n");
            exit(1);
      }
    }
   return 0;
 }
