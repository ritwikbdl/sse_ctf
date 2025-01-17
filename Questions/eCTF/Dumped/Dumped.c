// gcc -fno-stack-protector -z execstack -g -o stars Dumped.c
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
	alarm(60*3);
}

void start(void)
{
    char buf [LEN];
    int len;
    printf("You are dumping your trash in dumpster number: %p\n", buf);
    printf("Enter the size of trash you're throwing: ");
    scanf("%d", &len);
    fflush(stdin);

    if(len > LEN) {
        printf("I cannot accept to much trash in one go!\n");
        exit(0);
    }
    printf("Enter your trash: ");
    int input_len = read(0, buf, (unsigned)len);
    fflush(stdin);
    printf("Dumped your trash.\n");  
}

void banner(){
    printf("                                                                                \n           (/////////////////////////////////////////////////////////*          \n         (((//////////////////////////////////////////////////////////(/        \n        ((((////////////////////////////////////////////////////////((((*       \n       /(((((///////////////////////////////////////////////////////(((((,      \n      (((((((//////////////////////////////////////////////////////(((((((      \n      ,*******************************************************************      \n       *******************************************************************      \n       ******************************************************************,      \n       ******************************************************************.      \n       ,*****************************************************************       \n        *********/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*//       \n        /**********************//*,,/,         *////////////////////////*       \n        *////////////////////*/.      .,         ///////////////////////.       \n        ,////////////////////*         */          *////////////////////        \n         ///////////////////,         ////,       //////////////////////        \n         //////////////////////*    .////*****,,,//////////////////////*        \n         //////////////**,,*,,,////*//////////////.   /////////////////.        \n         .//////////////*       //////////////.        ,///////////////         \n          /////////////.         */////////////*         //////////////         \n          /////////////        //////////////////       ,//////////////         \n          (/////////////,    ,/////////////( //////**//*//////////////.         \n          ,///////////////. /          ///.           ////////////////          \n           ////////////////*.          //.          ./////////////////          \n           //////////////////,         (/(/        *//////////////////          \n           //(/(/(/(/(/(/(/(//(//(/(/(/(/(/(.//(///(/(/(/(/(/(/(/(/(/.          \n           ,(((((((((((((((((((((((((((((((((/(((((((((((((((((((((((           \n            ((((((((((((((((((((((((((((((((((((((((((((((((((((((((/           \n            ((((((((((((((((((((((((((((((((((((((((((((((((((((((((/           \n            /(((((((((((((((((((((((((((((((((((((((((((((((((((((((.           \n            ,(((((((((((((((((((((((((((((((((((((((((((((((((((((((            \n                                                                                \n ___________      _______________________________           ________                                  .___\n\\_   _____/ _____\\_   ___ \\__    ___/\\_   _____/           \\______ \\  __ __  _____ ______   ____   __| _/\n |    __)_ /  ___/    \\  \\/ |    |    |    __)     ______   |    |  \\|  |  \\/     \\\\____ \\_/ __ \\ / __ | \n |        \\\\___ \\\\     \\____|    |    |     \\     /_____/   |    `   \\  |  /  Y Y  \\  |_> >  ___// /_/ | \n/_______  /____  >\\______  /|____|    \\___  /              /_______  /____/|__|_|  /   __/ \\___  >____ | \n        \\/     \\/        \\/               \\/                       \\/            \\/|__|        \\/     \\/ \n");
}

int main(){
    char option = 'y';

    ignore_me_init_buffering();
	ignore_me_init_signal();
    banner();

    printf("You have trash to dump? (y/n): ");

    while(1){
        scanf("%c", &option);
        if (option == 'y'){
            start();
            printf("More trash? (y/n): ");
        }
        else if (option == 'n')
            return 0;
        else
            printf("Ohh ho! Wrong option. Try again? (y/n): ");

    }
	return 0;
}
