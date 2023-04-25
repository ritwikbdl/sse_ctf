// gcc -o hippy hippy.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#define SIZE 12

char *Notes [12]; 
int idx = 0;

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


void print_menu(){
    printf("\na. Add note");
    printf("\nb. View notes");
    printf("\nc. View all notes");
    printf("\nd. Delete note");
    printf("\ne. Exit");
    printf("\n\nSelect an option: ");
}


void add_note(){
    int n;
    printf("\nEnter the index of page: ");
    scanf("%d", &n);
    fflush(stdin);
    if(n<0 || n>SIZE){
        printf("\nInvalid index.\n");
        return;
    }
    Notes[n] = (char *)malloc(24);
    printf("\nEnter your note: ");
    read(0, Notes[n], 24);
}

void view_note(){
    int n;
    printf("\nEnter the index of page: ");
    scanf("%d", &n);
    fflush(stdin);
    if(n<0 || n>=SIZE || Notes[n] == NULL) return;
    printf("\n%s", Notes[n]);
}

void view_all_note(){
    int i = 0;
    for(i=0; i<12; i++){
        if(Notes[i] != NULL){
            printf("\n%d\t%s",i ,Notes[i]);
        }
    }
}


void delete_note(){
    int n;
    printf("\nEnter the index of page: ");
    scanf("%d", &n);
    fflush(stdin);
    if(n<0 || n>=SIZE) return;
    free(Notes[n]);
    printf("\n Deleted!");
    return;
}


void start(void)
{
    while(1){
        print_menu();
        char choice;
        scanf(" %c", &choice);
        fflush(stdin);
        switch(choice){
            case 'a':
                add_note();
                break;
            case 'b':
                view_note();
                break;
            case 'c':
                view_all_note();
                break;
            case 'd':
                delete_note();
                break;
            case 'e':
                exit(0);
            default:
                printf("\nInvalid choice!\n");
        }
    }
}



void banner(){
    printf("___________      _______________________________\n\\_   _____/ _____\\_   ___ \\__    ___/\\_   _____/\n |    __)_ /  ___/    \\  \\/ |    |    |    __)  \n |        \\\\___ \\\\     \\____|    |    |     \\   \n/_______  /____  >\\______  /|____|    \\___  /   \n        \\/     \\/        \\/               \\/    \n");
}

int main(){
	ignore_me_init_buffering();
	ignore_me_init_signal();
    printf("system: %p\n", system);
    banner();
    printf("\nNote: You have just 12 pages available for notes, use them judiciously!\n\t\t\t\t\t\t\t~waldo(dev team)\n");
    start();
	return 0;
}
