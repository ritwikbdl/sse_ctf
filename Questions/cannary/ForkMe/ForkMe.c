// gcc forkme.c -o forkme
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
	alarm(60);
}

void win(void)
{
  // read flag and print it
  FILE *f = fopen("flag.txt", "r");
  char flag[64];
  fgets(flag, 64, f);
  printf("flag: %s", flag);
  return;
}

void print_menu(){
  puts("1. Authenticate");
  puts("2. Read Flag");
  puts("3. Exit");
  printf("> ");
}

void clean_stdin(){
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int authenticate(){
  int pid = fork();
  if (pid==0)
  {
    
    char buffer [100];
    printf("Enter Magic password: ");
    read(0, buffer, 0x100);
    puts("[!] Sorry, Your password is wrong!");
  }else
  {
    int status;
    wait(&status);
  }
  return pid;
}

void read_flag(){
  puts("[!] Please authenticate first.");
  return;
}


void start(void)
{
  while(1)
  {
    print_menu();
    int choice = 0;
    scanf(" %d", &choice);
    clean_stdin();
    
    switch(choice){
      case 1:
        int pid = authenticate();
        if(pid==0) exit(0);
        break;
      case 2:
        read_flag();
        break;
      case 3:
        puts("Bye");
        exit(0);
        break;
      default:
        puts("Invalid choice");
        break;
    }
  }
}


void banner(){
    printf("  _________ __________________________________________________________________   ________  ________  \n /   _____//   _____/\\_   _____/\\_   ___ \\__    ___/\\_   _____/\\_____  \\   _  \\  \\_____  \\ \\_____  \\ \n \\_____  \\ \\_____  \\  |    __)_ /    \\  \\/ |    |    |    __)   /  ____/  /_\\  \\  /  ____/   _(__  < \n /        \\/        \\ |        \\\\     \\____|    |    |     \\   /       \\  \\_/   \\/       \\  /       \\\n/_______  /_______  //_______  / \\______  /|____|    \\___  /   \\_______ \\_____  /\\_______ \\/______  /\n        \\/        \\/         \\/         \\/               \\/            \\/     \\/         \\/       \\/ ");
}

int main(){
	ignore_me_init_buffering();
	ignore_me_init_signal();
  banner();
  printf("\n[*] Call me to get flag: %p\n", &win);
  start();
	return 0;
}
