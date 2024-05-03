//gcc escapeme.c -o test
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#define LEN 20

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
    
    snprintf(buf, LEN, "echo %s > /tmp/data.txt", data);
    system(buf);
    // char *cmd[] = {"sh", "-c", buf, NULL};
    // execv("/bin/sh", cmd);

}


int main(int argc, char *argv[])
{
    char *data = NULL;

    for (int i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]); // Print each argument followed by a newline
    }
    ignore_me_init_signal();


    //if (argc != 2)
    //{
    //    printf("Usage: %s <data>\n", argv[0]);
    //    return 1;
    //}

    data = argv[1];
    // printf("Data received: %s\n", data);
    start(data);

    return 0;
}
