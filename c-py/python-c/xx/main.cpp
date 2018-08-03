/*************************************************************************
  > File Name:main 
  > Author: fengl 
  > Mail: 
  > Created Time: Sun 03 Jul 2016 11:43:00 PM CST
 ************************************************************************/
#include"threadpoll.h"
#include"message.h"
#include"stdlib.h"

static int			nthreads;
pthread_mutex_t		clifd_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t		clifd_cond = PTHREAD_COND_INITIALIZER;
Thread	*tptr;		/* array of Thread structures; calloc'ed */
int					clifd[MAXNCLI], iget, iput;

int fm(int argc, char *argvv)
{
    char ** argv = &argvv;
	int			i, listenfd, connfd;
	void		sig_int(int);
    void        thread_make(int);
	socklen_t	addrlen, clilen;
	struct sockaddr	*cliaddr;

	if (argc == 2)
		//listenfd = Tcp_listen(NULL, argv[1], &addrlen);
		listenfd = Tcp_listen(NULL, INADDR_ANY, &addrlen);
    else if (argc == 3)
		//listenfd = Tcp_listen(argv[1], argv[2], &addrlen);
		listenfd = Tcp_listen(INADDR_ANY, argv[1], &addrlen);
	else
		err_quit("usage: serv08 <port#> <#threads>");
		//err_quit("usage: serv08 [ <host> ] <port#> <#threads>");
	cliaddr = (struct sockaddr*) malloc(addrlen); //check

	nthreads = atoi(argv[argc-1]);
	tptr =(Thread*) calloc(nthreads, sizeof(Thread)); // check 
	iget = iput = 0;

		/* 4create all the threads */
	for (i = 0; i < nthreads; i++)
		thread_make(i);		/* only main thread returns */

	signal(SIGINT, sig_int); //check

	for ( ; ; ) {
		clilen = addrlen;
		connfd = accept(listenfd, cliaddr, &clilen); // check

		pthread_mutex_lock(&clifd_mutex);
		clifd[iput] = connfd;
		if (++iput == MAXNCLI)
			iput = 0;
		if (iput == iget)
			err_quit("iput = iget = %d", iput);
		pthread_cond_signal(&clifd_cond);
		pthread_mutex_unlock(&clifd_mutex);
	}
}
/* end serv08 */

void sig_int(int signo)
{
	int		i;
//	void	pr_cpu_time(void);

//	pr_cpu_time();

	for (i = 0; i < nthreads; i++)
//		printf("thread %d, %ld connections\n", i, tptr[i].thread_count);
//		printf("thread...%d...\n", i);

	exit(0);
}

