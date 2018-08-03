/*************************************************************************
  > File Name: 
  > Author: fengl 
  > Mail: 
  > Created Time: Sun 03 Jul 2016 11:43:00 PM CST
 ************************************************************************/
#include"threadpoll.h"
#include"iostream"

#include"string"

#define	MAXN	16384		/* max # bytes client can request */

using namespace std;


void rw_data(int sockfd)
{
	int			ntowrite;
	ssize_t		nread;
	char		line[MAXLINE], result[MAXN];
    unsigned char headLen[4];
    unsigned char *rBody;
    pthread_t  p_id = pthread_self();
    // char* picName = ""
    string  picName("picture.jpg");
    
    int val = fcntl(sockfd, F_GETFL, 0);

	for ( ; ; ) {
    fcntl(sockfd, F_SETFL, val|~O_NONBLOCK);
        cout << "will read head length.." << p_id << ".\n";
        long int picLen = 0;
        unsigned int nRead = 0;
        memset(headLen, 0, sizeof(headLen));
        picLen = strtol((char*)headLen, NULL, 10);
        cout << "pic length.before read..... :" << picLen << endl;

        nRead = read(sockfd, headLen, sizeof(headLen));

    fcntl(sockfd, F_SETFL, val);
        picLen = strtol((char*)headLen, NULL, 10);
        cout << "pic length :" << picLen << endl;
        
        rBody = (unsigned char*) malloc(picLen);
        unsigned int fix = 0;
        int left = picLen;
        while(left > 0)
        {
            cout << "nleft = " << left << endl;
            nRead = read(sockfd, rBody + fix,left);
            cout << "nread = " << nRead << endl;
            if(nRead < 0 && errno == EINTR)
                continue;
            else if(nRead == 0){
                cout << "client closed " << "return \n" ;
                return;}
            left -= nRead;
            cout << "nleft......... = " << left << endl;
            fix += nRead; 
            //return ;
        }

        cout << "complete read data....\n";
        FILE *fp = fopen(picName.data(), "w+");
        fwrite(rBody, 1, picLen, fp);
        fclose(fp);
        free(rBody);
        
        /*
        cout << "pic size..." << picLen << endl;
         IShelter rShelter;
         Mat image;
         image = imread("picture.jpg", 1);
         if(!image.data)
            cout << "image is emmpty \n";
        else
            cout << "result ..." << rShelter.getResult(image) << endl; 
        */


        cout << "write ...." << endl;
                
        char* str = "12345";
        ntowrite = 5;
		Writen(sockfd, str, ntowrite);
	}
}
/*
void web_child(int sockfd)
{
	int			ntowrite;
	ssize_t		nread;
	char		line[MAXLINE], result[MAXN];

	for ( ; ; ) {
		if ( (nread = Readline(sockfd, line, MAXLINE)) == 0)
			return;

		ntowrite = atol(line);
		if ((ntowrite <= 0) || (ntowrite > MAXN))
			err_quit("client request for %d bytes", ntowrite);

		Writen(sockfd, result, ntowrite);
	}
}
*/
