// gcc -fno-stack-protector  -g -o main main.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <time.h>
#include <dlfcn.h>
#include <link.h>
// add include for random



# define LEN 8
int COIN = 10;

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
	alarm(2*60);
}

void print_menu(){
    printf("\na. Play");
    printf("\nb. Withdraw");
    printf("\ne. Exit");
    printf("\n\nSelect an option: ");
}

void clean_stdin(){
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int play(){
    srand(time(0)); // seed the random number generator

    if (COIN>0){
        char buf [LEN]="\0";
        printf("\nEnter your number: ");
        read(0, buf, 10);
        printf("\nYou entered: ");
	struct link_map *lm = (struct link_map *)dlopen("libc.so.6", RTLD_NOW);
        printf(buf);
        printf("My libc base is here btw: %p\n", (void *)lm->l_addr);
        // check if the entered string coresponds to a number if yes is it equal to a randomly generated number
        int number = atoi(buf);
        int random_number = rand() % 10000;
        printf("\nThe random number is: %d\n", random_number);
        if (number != 0 && random_number == number){
            printf("\nYou won\n");
            return COIN*=2;
        }
        else{
            printf("\nYou lost a coin\n");
            return --COIN;
        }
    }
    else{
        printf("You don't have any coins\n");
        return COIN;
    }
}

void withdraw(){
    char wallet_addr[120] = "\0"; 
    printf("You have %d coins\n", COIN);
    if (COIN == 0){
        printf("You don't have any coins\n");
        return;
    }
    printf("Enter your wallet address: ");
    
    // gets(wallet_addr);
    read(0, wallet_addr, 200);

    printf("This transaction will take two days to reflect. Thank you!");
    COIN = 0;
}


void start(void)
{   
    
    while(1){
        print_menu();
        char choice;
        scanf(" %c", &choice);
        clean_stdin();

        switch(choice){
            case 'a':
                play();
                break;
            case 'b':
                withdraw();
                break;
            case 'e':
                exit(0);
        }
    }
}


int main(){
    ignore_me_init_buffering();
	ignore_me_init_signal();
    start();
    
	return 0;
}
