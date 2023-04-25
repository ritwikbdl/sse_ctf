// gcc -o bin bin.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

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



void start(void)
{
    printf("Your flag is: SSECTF{XOR_with_known_plaintext_is_bad}");
}


int main(){
	ignore_me_init_buffering();
	ignore_me_init_signal();
    start();
	return 0;
}
