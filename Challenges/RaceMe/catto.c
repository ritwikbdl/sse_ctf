#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

void super_secret_security_check(struct stat file_data);

int main(int argc, char* argv[]) {
    setuid(0);

    int file_descriptor;

    // Check if a file was provided
    if(argc != 2) {
        printf("Usage: %s <file>\n" \
		"Hi, I'm catto, a more secure implementation of cat!\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    struct stat file_data;

    // Check if the file exists
    if (stat(argv[1], &file_data) < 0) {
        fprintf(stderr, "No such file found: %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    // Check if it is owned by root
    if (file_data.st_uid != 1000)
    {
        fprintf(stderr, "File %s is owned by root, cannot open it :\(\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    super_secret_security_check(file_data);

    // Now we know that we can securely open it :^)
    file_descriptor = open(argv[1], O_RDONLY);
    if (file_descriptor <= 0)
    {
        fprintf(stderr, "Couldn't open %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    char read_buf[256];
    int read_size = 0;
    do {
        read_size = read(file_descriptor, read_buf, 256);
        write(1, read_buf, read_size);
    } while (read_size > 0);

}
