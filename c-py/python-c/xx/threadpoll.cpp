/*************************************************************************
  > File Name: threadpoll.c
  > Author: fengl 
  > Mail: 
  > Created Time: Sun 03 Jul 2016 11:43:00 PM CST
 ************************************************************************/

#include"threadpoll.h"
#include"iostream"
#include "message.h"
extern pthread_mutex_t		clifd_mutex;
extern pthread_cond_t		clifd_cond ;
extern Thread	*tptr;		/* array of Thread structures; calloc'ed */
extern int					clifd[MAXNCLI], iget, iput;

void thread_make(int i)
{
	void	*thread_main(void *);

	pthread_create(&tptr[i].thread_tid, NULL, &thread_main, (void *) i);// check it!
	return;		/* main thread returns */
}

void * thread_main(void *arg)
{
	int		connfd;
	//void	rw_child(int);

	printf("thread %d starting\n", (int) arg);
	for ( ; ; ) {
    	pthread_mutex_lock(&clifd_mutex);  // checke  
		while (iget == iput)
			pthread_cond_wait(&clifd_cond, &clifd_mutex);
		connfd = clifd[iget];	/* connected socket to service */
		if (++iget == MAXNCLI)
			iget = 0;
		pthread_mutex_unlock(&clifd_mutex); // check
		tptr[(int) arg].thread_count++;
        
        std::cout << "...线程活的锁..." << pthread_self() << std::endl;
		rw_data(connfd);		/* process request */
        std::cout << "...线程处理data完毕..." << pthread_self() << std::endl;
		close(connfd);
	}
}

