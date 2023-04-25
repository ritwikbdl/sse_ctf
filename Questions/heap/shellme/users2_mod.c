#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>

#define MAX_SIZE 30

int current_index = 0;

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

struct _users_t{
	char *name;
	// int lvl;
} users[MAX_SIZE];

void call_system()
{
	system("/bin/sh\n");
}

void adduser()
{
	int i=0, lvli, size = 0, c;

	printf("Enter size of username (MAX = 255 chars):");
	scanf("%d", &size);

	// if (size > 255)
	// {
	// 	printf("Size exceeds bounds\n");
	// 	return;
	// }

	char *p = (char *) malloc(size + 1);
	// char lvl[2];

	while(((c = fgetc(stdin)) != '\n') && (c != EOF));
	printf("Enter user name:\n");
	fgets(&(*p), size + 1, stdin);

	// printf("Enter user privilege level from 1 (highest) to 4 (lowest)\n");

	// gets(lvl);
	// lvli = atoi(lvl);

	if(current_index < MAX_SIZE)
	{
		users[current_index++].name = p;
	}
	else
		printf("Userlist full... user not added\n");

	// while(i != SIZE){
	// 	// if(users[i].lvl == 0){
	// 		users[i].name = p;
	// 		// users[i].lvl = lvli;
	// 		p = NULL;
	// 		break;
	// 	}
	// 	i++;
	// }
	// if (p != NULL){
	// 	printf("Userlist full... user not added\n");
	// }
}

void printuser()
{
	int i, j=1;

	for(i=0; i<MAX_SIZE; ++i){
		//if (users[i].lvl != 0)
		{
			printf("%d %s\n", j++, users[i].name);	
		}
	}
}

void removeuser()
{
	char n[2];
	int ni;

	printf("Enter user number to remove : ");
	gets(&n);
	// scanf("%d", &n);
	ni = atoi(n)-1;
	if (ni >= MAX_SIZE){
		printf("Invalid number\n");
		return;	
	}

	free(users[ni].name);
	// users[ni].lvl = 0;
}

int main(int argc, char **argv)
{
	ignore_me_init_buffering();
	ignore_me_init_signal();

    printf("What would you like to do?\n");

    char end=0;
	char option;

	while(!end){
		printf("....................\n");
		printf("[a]dd a user\n");
		printf("[r]emove a user\n");
		printf("[p]rint all users\n");
		printf("e[x]it program\n");
		gets(&option);

		switch(option){
		case 'a': adduser(); break;
		case 'r': removeuser(); break;
		case 'p': printuser("p\n"); break;
		case 'x': printf("That's all folks!\n"); end=1; break;
		default : printf("Invalid option\n"); break;
		}
	}
}
