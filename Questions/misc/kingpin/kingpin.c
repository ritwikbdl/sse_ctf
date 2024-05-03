#include <stdio.h>
#include <unistd.h>

char FLAG [] = "5555555555";
char Digit[] = "0123456789";

void set()
{
    FLAG[0] = Digit[5];
    FLAG[1] = Digit[0];
    FLAG[2] = Digit[2];
    FLAG[3] = FLAG[9] = Digit[7];
    FLAG[4] = Digit[4];
    FLAG[6] = Digit[8];
    FLAG[7] = Digit[6];

}

int main(){
    unsigned int i=0;
    char temp [11];
    temp [10] = '\n';
    puts(
"░██████╗░██████╗███████╗  ██████╗░░█████╗░██████╗░░░██╗██╗\n"
"██╔════╝██╔════╝██╔════╝  ╚════██╗██╔══██╗╚════██╗░██╔╝██║\n"
"╚█████╗░╚█████╗░█████╗░░  ░░███╔═╝██║░░██║░░███╔═╝██╔╝░██║\n"
"░╚═══██╗░╚═══██╗██╔══╝░░  ██╔══╝░░██║░░██║██╔══╝░░███████║\n"
"██████╔╝██████╔╝███████╗  ███████╗╚█████╔╝███████╗╚════██║\n"
"╚═════╝░╚═════╝░╚══════╝  ╚══════╝░╚════╝░╚══════╝░░░░░╚═╝\n");
    set();
    printf("If you are KingPin, Enter your pin > ");
    fgets(temp, 11, stdin);
    for( i = 0; i<11; i++){
        if(temp[i]==FLAG[i]) usleep(100);
        else break;
    }
    usleep(100*5000);
    if(i == 11) {
        printf("\nWelcome KingPin!!!\n\nHere is your flag: SSECTF{%s}.\n", temp);
    }
    else{
        printf("\n\nUNAUTHORIZED!\nIt took me no \"time\" to verify its not KingPin.\n");
    }
    return 0;
}
