/*************************************************************************
    > File Name: server.c
  > Author: 
  > Mail: 
  > Created Time: Sat 09 Jul 2016 02:31:51 PM CST
 ************************************************************************/

#include<stdio.h>
#include"stdlib.h"
#include"string.h"
#include"sys/socket.h"
#include"unistd.h"

void server_c(char* ip, int port){
   // struct sockaddr_in   *servaddr,  *cliaddr;
    //int i, listenfd, connfd;
    //socklen_t addrlen, clilen;
   
    //servaddr =(struct sockaddr_in*) malloc(sizeof(struct sockaddr_in));
    //servaddr.sa_family = AF_INET;
    //listenfd = listen()
    printf("ip=%s,,port=%d", ip, port);
    printf("...ok\n\n");


}
