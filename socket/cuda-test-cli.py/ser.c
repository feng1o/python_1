

#include<unistd.h>
#include<sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>
//#include <string>

#include <pthread.h>
#include <sys/time.h>
#include <errno.h>

#include <stdlib.h>
//#include <cstdint>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include "dark.h"

#define INVALID_SOCKET (-1)
int sockfd=INVALID_SOCKET;

const char* SERVER_IP="120.25.241.211";
//const char* SERVER_IP="127.0.0.1";
#define SERVPORT 9999
#define HEAD_LEN  4
#define SOCKET_SIZE 1024
#define  false  0
#define true  1
char   Ctime[16] = {};
int  closeSocket()
{
	if(sockfd!=INVALID_SOCKET)
	{
		close(sockfd);
		sockfd=INVALID_SOCKET;
	}
	return 1;
}
int  connectSocket(){
	struct sockaddr_in server_addr;
	if ((sockfd=socket(AF_INET,SOCK_STREAM,0))== -1)
	{
		printf("create socket failed!");
		sockfd=INVALID_SOCKET;
		return false;
	}

	bzero(&(server_addr),sizeof(struct sockaddr_in));
	server_addr.sin_family=AF_INET;
	server_addr.sin_port=htons(SERVPORT);

	if(inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr) == 0)
	{
		printf("bind IP failed!");
		sockfd=INVALID_SOCKET;
		return false;
	}	
	struct timeval timeout={3,0};//3s
    	setsockopt(sockfd,SOL_SOCKET,SO_SNDTIMEO,&timeout,sizeof(timeout));
    	setsockopt(sockfd,SOL_SOCKET,SO_RCVTIMEO,&timeout,sizeof(timeout));

	if (connect(sockfd,(struct sockaddr *)&server_addr,\
			sizeof(struct sockaddr))== -1)
	{
		printf("connect server failed  ");
		close(sockfd);
		sockfd=INVALID_SOCKET;
		return false;
	}
	return true;	
}

int  recvPic(){
			char* len_buf = (char*) malloc(sizeof(char)*HEAD_LEN);
			if(len_buf ==NULL){
				perror("malloc error!\n");
				exit(1);
				}
			int n = read(sockfd, len_buf, HEAD_LEN);
			if(n != HEAD_LEN){
				perror("get headlen error!\n");
				free(len_buf);
				exit(1);
				}
			int picLen = atoi(len_buf);
			free(len_buf);
			char* pic_buf = (char*) malloc(sizeof(char)*picLen);
			if(pic_buf ==NULL){
				perror("malloc error!\n");
				exit(1);
				}
		int left = picLen;
	    	int fix = 0;
		ssize_t nRead = 0;
		//char * buff_t = (char*)malloc(sizeof(char)*20);
        while(left > 0)
        {
            //cout << "nleft = " << left << endl;
            printf("nleft=%d\n", left);
			nRead = 0;
			if(left > 4096){
	            nRead = read(sockfd, pic_buf + fix,4096);
		        //nRead = read(fd, getPic->getFileBodyChar() + fix,left);
			    //cout << "nread = " << nRead << endl;
			    printf("nread=%d\n", nRead );
			}
			else {
		        nRead = read(sockfd, pic_buf + fix,left);
		        //nRead = read(fd, buff_t,left);
			}
			if(nRead > left){
				//cout << "nRead > left " <<endl;
				printf("nRead > left\n");
				//string str = "format error,connection  closed!";
				//write(sockfd,const_cast<char*>(str.c_str()), str.size());
				free(pic_buf);
				return 0;
			}
            if(nRead < 0 && errno == EINTR)
                continue;
            else if(nRead <= 0){
            //else if(nRead == 0){
                //cout << "client closed " << "return \n" ;
                printf("client close!\n");
		 free(pic_buf);
                return 0;
			}
            left -= nRead;
            //cout << "nleft......... = " << left << endl;
            printf("(nleft = %d\n", left);
            fix += nRead; 
		}
	    time_t  t=time(NULL);
	    sprintf(Ctime, "pic_%d", t);
	    FILE* fp = fopen(Ctime, "wb+");
	    fwrite(pic_buf, picLen, 1, fp);
	    fclose(fp);
	    free(pic_buf);
	    return 1;		
}

ssize_t writen(int fd, const void *vptr, size_t n)
{
	size_t		nleft;
	ssize_t		nwritten;
	const char	*ptr;
//	signal(SIGPIPE, SIG_IGN);

	ptr = (char*)vptr;
	nleft = n;
	while (nleft > 0) {
		if ( (nwritten = write(fd, ptr, nleft)) <= 0) {
			if (nwritten < 0 && errno == EINTR)
				nwritten = 0;		/* and call write() again */
			/*else if(errno == SIGPIPE){
				std::cout << "\n write pipe error \n\n";
				return(-1);		
			}*/	
			else 
				return -1;
		}

		nleft -= nwritten;
		ptr   += nwritten;
	}
	return(n);
}
/* end writen */
void Writen(int fd, void *ptr, size_t nbytes)
{
	if (writen(fd, ptr, nbytes) != nbytes)
		perror("writen error");
}

int sendPic(char buf[200]){
	FILE* fp;
	if ((fp = fopen("/home/fengl/darknet-r2/data/predictions.png", "rb+")) == NULL){
		perror("open error...\n");
		exit(1);
	}
	fseek(fp, 0, SEEK_END);
	int len = ftell(fp);
	printf("send piclength= %d", ftell(fp));
	rewind(fp);
	fseek(fp, 0, SEEK_SET); //begin
	char*  picbuf = (char*)malloc(sizeof(char)*len);
	if(picbuf ==NULL){
		perror("malloc error!\n");
		exit(1);
	}
	fread(picbuf, len, 1, fp);
	fclose(fp);
	char len_buf[HEAD_LEN];
	sprintf(len_buf, "%d", len);
	Writen(sockfd, len_buf, HEAD_LEN);
	Writen(sockfd, picbuf, len);
	free(picbuf);
	return 1;

}
int main(){
	 char *argv[200]={ };      
	 argv[1] = "yolo"; 
	 argv[2] = "test"; 
	 argv[3] ="/home/fengl/darknet-r2/cfg/yolo-tiny.cfg"; 
	 argv[4] =  "/home/fengl/darknet-r2/yolo-tiny.weights";
	 argv[5] =   "/home/fengl/darknet-r2/data/dog.jpg";
	 //argv[300]="test";
	 if(connectSocket()){
	 	while(1){
			recvPic();
			char* buffer = (char*)malloc(sizeof(char)*160);
			if(NULL== buffer){
				perror("error malloc!");
				exit(1);
				}
			sprintf(buffer, "/home/fengl/darknet-r2/data/%s", Ctime);
			argv[5] = buffer;
			inf_main(6, argv);
			sendPic(argv[5]);
			free(buffer);
	 	}
	 }
	 else {
	 	printf("connect error!\n");
		exit(1);
	 	}
	 closeSocket();
	 //struct sockaddr_in  servaddr;
	 
	// inf_main(6,  argv);  //must > 5
	return 0;
}

/*
#include<stdio.h>
#include<stdlib.h>
#include"dark.h"
#include<iostream>

using namespace std;

int main(){
	printf("...test.\n");
	cout << "test" << endl;
	
	//yolo  test cfg/yolo-tiny.cfg  yolo-tiny.weights   data/dog.jpg
	char *argv[200]={
	};
	 argv[1] = "yolo";
    	 argv[2] = "test";
    	 argv[3] ="/home/fengl/darknet-lf/cfg/yolo-tiny.cfg";
  	 argv[4] =  "/home/fengl/darknet-lf/yolo-tiny.weights";
    	 argv[5] =   "/home/fengl/darknet-lf/data/dog.jpg";
    	 argv[300]="test";
	inf_main(6,  argv);  //must > 5
	printf("%s\n", argv[1]);
	printf("%s\n", argv[300]);
	return 0;
}
*/