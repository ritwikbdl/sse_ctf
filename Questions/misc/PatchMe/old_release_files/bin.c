// gcc -o bin bin.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
char flag[]="Your flag is: SSECTF{AAAAAAAAAABBBBBBBBBBCCCCCC}";

void ignore_me_init_buffering() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
  	printf("[!] Anti DoS Signal.");
    exit(0);
  }
}

void ignore_me_init_signal() {
	signal(SIGALRM, kill_on_timeout);
	alarm(60*3);
}

void print(){
	printf("len %d", strlen(flag));
	return;
}


void start(void)
{
	volatile int x = 0x1246;
	if (!x){
		printf("Sorry not here!");
	}
}


int main(){
	ignore_me_init_buffering();
	ignore_me_init_signal();
    start();
	return 0;
}
