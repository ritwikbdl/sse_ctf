#include <stdio.h>
#include <unistd.h>

char FLAG [] = "5555555555";
char Digit[] = "0123456789";

void set()
{
    FLAG[0] = Digit[8];
    FLAG[1] = Digit[0];
    FLAG[2] = Digit[4];
    FLAG[3] = FLAG[9] = Digit[7];
    FLAG[4] = Digit[1];
    FLAG[6] = Digit[6];
    FLAG[7] = Digit[3];

}

int main(){
    unsigned int i=0;
    char temp [11];
    temp [10] = '\n';
    puts(" ____  __.__              __________.__        \n|    |/ _|__| ____    ____\\______   \\__| ____  \n|      < |  |/    \\  / ___\\|     ___/  |/    \\ \n|    |  \\|  |   |  \\/ /_/  >    |   |  |   |  \\\n|____|__ \\__|___|  /\\___  /|____|   |__|___|  /\n        \\/       \\//_____/                  \\/ \n                                               \n");
    set();
    printf("KingPin, Enter your pin > ");
    fgets(temp, 11, stdin);
    for( i = 0; i<11; i++){
        if(temp[i]==FLAG[i]) usleep(1);
        else break;
    }
    usleep(100*5000);
    if(i == 11) {
        printf("\nWelcome KingPin!!!\n\nHere is your flag: esCTF{%s}.\n", temp);
    }
    else{
        printf("\n\nUNAUTHORIZED!\nIt took me no \"time\" to verify its not KingPin.\n");
    }
    return 0;
}
