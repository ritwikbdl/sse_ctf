// gcc -fno-stack-protector -z execstack -g -o stars AsciiFullof*.c
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
  	printf("[!] Anti DoS Signal. Patch me out for testing.");
    exit(0);
  }
}

void ignore_me_init_signal() {
	signal(SIGALRM, kill_on_timeout);
	alarm(60*3);
}

void start(void)
{
    char buf [LEN];
    int len;
    printf("Here's your token:%p\n", buf);
    printf("Enter the length of your name: ");
    scanf("%d", &len);
    fflush(stdin);

    if(len > LEN) {
        printf("Your name is too long to remember\n");
        exit(0);
    }
    printf("Enter your name: ");
    int input_len = read(0, buf, (unsigned)len);
    // int input_len = fread(buf, (unsigned int)len, 1, stdin);
    fflush(stdin);

    for(int i = 0; i < input_len-1 && i < LEN; i++){
    	if(buf[i] < 32 || buf[i] > 126){
          puts("Even Elon Musk would not name his kids that!");
        	exit(0);
        }
    }

    printf("Registered your name \n");  
}

void banner(){
    printf("   _____ _____ ______    _____ _______ ______  \n  / ____/ ____|  ____|  / ____|__   __|  ____| \n | (___| (___ | |__    | |       | |  | |__    \n  \\___ \\\\___ \\|  __|   | |       | |  |  __|   \n  ____) |___) | |____  | |____   | |  | |      \n |_____/_____/|______|  \\_____|  |_|  |_|      \n                                               \n                                               \n");
}

int main(){
	ignore_me_init_buffering();
	ignore_me_init_signal();
    banner();
    start();
    puts("Oops! you haven't pushed your limits!\n");
	return 0;
}
