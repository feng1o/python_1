/*************************************************************************
  > File Name: threadpoll.h
  > Author: fengl 
  > Mail: 
  > Created Time: Sun 03 Jul 2016 11:43:00 PM CST
 ************************************************************************/

#ifndef _THREADPOLL_H
#define _THREADPOLL_H

#include	<sys/types.h>	/* basic system data types */
#include	<sys/socket.h>	/* basic socket definitions */
#if TIME_WITH_SYS_TIME
#include	<sys/time.h>	/* timeval{} for select() */
#include	<time.h>		/* timespec{} for pselect() */
#else
#if HAVE_SYS_TIME_H
#include	<sys/time.h>	/* includes <time.h> unsafely */
#else
#include	<time.h>		/* old system? */
#endif
#endif
#include	<netinet/in.h>	/* sockaddr_in{} and other Internet defns */
#include	<arpa/inet.h>	/* inet(3) functions */
#include	<errno.h>
#include	<fcntl.h>		/* for nonblocking */
#include	<netdb.h>
#include	<signal.h>
#include	<stdio.h>
#include	<stdlib.h>
#include	<string.h>
#include	<sys/stat.h>	/* for S_xxx file mode constants */
#include	<sys/uio.h>		/* for iovec{} and readv/writev */
#include	<unistd.h>
#include	<sys/wait.h>
#include	<sys/un.h>		/* for Unix domain sockets */

#ifdef	HAVE_SYS_SELECT_H
# include	<sys/select.h>	/* for convenience */
#endif

#ifdef	HAVE_SYS_SYSCTL_H
#ifdef	HAVE_SYS_PARAM_H
# include	<sys/param.h>	/* OpenBSD prereq for sysctl.h */
#endif
# include	<sys/sysctl.h>
#endif

#ifdef	HAVE_POLL_H
# include	<poll.h>		/* for convenience */
#endif
#ifdef	HAVE_SYS_EVENT_H
# include	<sys/event.h>	/* for kqueue */
#endif

#ifdef	HAVE_STRINGS_H
# include	<strings.h>		/* for convenience */
#endif

/* Three headers are normally needed for socket/file ioctl's:
 * <sys/ioctl.h>, <sys/filio.h>, and <sys/sockio.h>.
 */
#ifdef	HAVE_SYS_IOCTL_H
# include	<sys/ioctl.h>
#endif
#ifdef	HAVE_SYS_FILIO_H
# include	<sys/filio.h>
#endif
#ifdef	HAVE_SYS_SOCKIO_H
# include	<sys/sockio.h>
#endif

//#ifdef	HAVE_PTHREAD_H
# include	<pthread.h>
//#endif

#ifdef HAVE_NET_IF_DL_H
# include	<net/if_dl.h>
#endif

#ifdef HAVE_NETINET_SCTP_H
#include	<netinet/sctp.h>
#endif

#define	MAXLINE		4096	/* max text line length */

int		 tcp_listen(const char *, const char *, socklen_t *);
int		 Tcp_listen(const char *, const char *, socklen_t *);

void	 err_dump(const char *, ...);
void	 err_msg(const char *, ...);
void	 err_quit(const char *, ...);
void	 err_ret(const char *, ...);
void	 err_sys(const char *, ...);



void rw_data(int sockfd);
//static ssize_t my_read(int fd, char *ptr) ;
ssize_t readline(int fd, void *vptr, size_t maxlen);
ssize_t readlinebuf(void **vptrptr) ;
ssize_t Readline(int fd, void *ptr, size_t maxlen);
void Writen(int fd, void *ptr, size_t nbytes);
#endif
