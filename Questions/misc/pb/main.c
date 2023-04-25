#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <openssl/sha.h>

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

void banner(){
    printf("___________      _______________________________\n\\_   _____/ _____\\_   ___ \\__    ___/\\_   _____/\n |    __)_ /  ___/    \\  \\/ |    |    |    __)  \n |        \\\\___ \\\\     \\____|    |    |     \\   \n/_______  /____  >\\______  /|____|    \\___  /   \n        \\/     \\/        \\/               \\/    \n");
}


int main(int argc, char* argv[]){
	ignore_me_init_buffering();
	ignore_me_init_signal();
	banner();
	printf("We will check your password against the sha1 hash. If it matches, you will get the flag.\n");
	printf("Please wait while we initialize the system...\n");

	int fd;

	if(fd=open("/home/ctf/hash.txt",'r') < 0){
		printf("can't open password hash %d\n", fd);
		return 0;
	}

	sleep(time(0)%10);
	
	unsigned char hash_buf [22] = {0};
	
	if(read(fd, hash_buf, SHA_DIGEST_LENGTH) < 0){
	 	printf("read error\n");
	 	close(fd);
	 	return 0;		
	 }

	char user_input[22];
	unsigned char result[SHA_DIGEST_LENGTH];

	printf("Input password : ");
	scanf("%21s", user_input);
    	user_input[21] = '\0';

    	SHA1(user_input, strlen(user_input), result);

	if(!strncmp(hash_buf, result, SHA_DIGEST_LENGTH)){
		printf("Password OK\n");
		system("/bin/cat flag.txt\n");
	}
	else{
		printf("Wrong Password\n");
	}

	close(fd);
	return 0;
}
