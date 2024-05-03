//gcc test -o escapeme.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#define LEN 42

void ignore_me_init_buffering()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig)
{
    if (sig == SIGALRM)
    {
        printf("[!] Anti DoS Signal.\n");
        exit(0);
    }
}

void ignore_me_init_signal()
{
    signal(SIGALRM, kill_on_timeout);
    alarm(10000);
}

void clear_stdin()
{
    while (getchar() != '\n')
        ;
}

void start(const char *data)
{
    char buf[LEN];
    //Write to /tmp because the TA's don't allow home to be touched
    snprintf(buf, LEN, "echo %s > /tmp/data.txt", data);
    char *cmd[] = {"sh", "-c", buf, NULL};
    execv("/bin/sh", cmd);
}


int main(int argc, char *argv[])
{
    char *data = NULL;


    ignore_me_init_signal();



    data = argv[1];
    start(data);

    return 0;
}
