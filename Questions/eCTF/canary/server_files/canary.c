// gcc -o canary canary.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
# define LEN 90

void ignore_me_init_buffering() {
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
    printf("[!] Anti DoS Signal.\n");
    exit(0);
  }
}

void ignore_me_init_signal() {
  signal(SIGALRM, kill_on_timeout);
  alarm(60*2);
}

void win(void)
{
  execve("/bin/sh",(char **)0x0,(char **)0x0);
  return;
}


typedef struct counter {
	char buf[100];
	int rep;
} counter;

void start(void)
{
  	counter c1;

    printf("How many times do you want to repeat? (e.g., 2): ");
    scanf("%d", &c1.rep);
    for(int i=0; i<c1.rep; i++){
		memset(c1.buf, 0, 100);
		printf("\necho: ");
		read(0,c1.buf, 150);
		printf("%s", c1.buf);
    } 
}



void banner(){
    printf("              _______________________________       _______________   ________ ________  \n  ____   _____\\_   ___ \\__    ___/\\_   _____/       \\_____  \\   _  \\  \\_____  \\\\_____  \\ \n_/ __ \\ /  ___/    \\  \\/ |    |    |    __)  ______  /  ____/  /_\\  \\  /  ____/ /  ____/ \n\\  ___/ \\___ \\\\     \\____|    |    |     \\  /_____/ /       \\  \\_/   \\/       \\/       \\ \n \\___  >____  >\\______  /|____|    \\___  /          \\_______ \\_____  /\\_______ \\_______ \\\n     \\/     \\/        \\/               \\/                   \\/     \\/         \\/       \\/\n\n");
}

void main(){


	ignore_me_init_buffering();
	ignore_me_init_signal();

	banner();
	start();
}