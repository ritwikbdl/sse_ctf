// gcc -no-pie got2win.c -o got2win
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
  	printf("[!] Anti DoS Signal. Patch me out for testing.");
    exit(0);
  }
}

void ignore_me_init_signal() {
	signal(SIGALRM, kill_on_timeout);
	alarm(60*3);
}

void win(void)
{
  execve("/bin/sh",(char **)0x0,(char **)0x0);
  return;
}

void echo(void)
{
  char buffer [256];
  printf("Bend your knee Jon and repeat > ");
  fgets(buffer,0x8f,stdin);
  printf(buffer);
  fflush(stdin);
  return;
}

void banner(){
    printf("   _____ _____ ______    _____ _______ ______  \n  / ____/ ____|  ____|  / ____|__   __|  ____| \n | (___| (___ | |__    | |       | |  | |__    \n  \\___ \\\\___ \\|  __|   | |       | |  |  __|   \n  ____) |___) | |____  | |____   | |  | |      \n |_____/_____/|______|  \\_____|  |_|  |_|      \n                                               \n                                               \n");
}

int main(){
	ignore_me_init_buffering();
	ignore_me_init_signal();
  banner();
  echo();
  puts("\nOops! You haven't GOT it!\n");
	return 0;
}
