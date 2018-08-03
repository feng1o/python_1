/*************************************************************************
  > File Name: message.h
  > Author: fengl 
  > Mail: 
  > Created Time: Sun 03 Jul 2016 11:43:00 PM CST
 ************************************************************************/
#ifndef _MESSAGE_H
#define _MESSAGE_H

#include <unistd.h>
#include <pthread.h>

typedef struct {
  pthread_t		thread_tid;		/* thread ID */
  long			thread_count;	/* # connections handled */
} Thread;

#define	MAXNCLI	32
//pthread_mutex_t		clifd_mutex;
//pthread_cond_t		clifd_cond;

#endif
