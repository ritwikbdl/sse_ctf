// #include <sys/types.h>
// #include <sys/stat.h>
// #include <libgen.h>
// #include <unistd.h>
// #include <string.h>
// #include <assert.h>
// #include <stdlib.h>
// #include <fcntl.h>

// int main(int argc, char **argv) {
//     int fd = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC, 0755);
//     write(fd, "#!/bin/sh\necho SAFE\n", 20);
//     close(fd);
//     execl("/bin/sh", "/bin/sh", argv[1], NULL);
// }


#include <string.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

int main(int argc, char* argv[]) {
    int fd;
    int size = 0;
    char buf[256];

    if(argc != 2) {
        printf("usage: %s <file>\n", argv[0]);
        exit(1);
    }

    struct stat stat_data;
    if (stat(argv[1], &stat_data) < 0) {
        fprintf(stderr, "Failed to stat %s: %s\n", argv[1], strerror(errno));
        exit(1);
    }

    if(stat_data.st_uid == 0)
    {
        fprintf(stderr, "File %s is owned by root\n", argv[1]);
        exit(1);
    }

    fd = open(argv[1], 'r');
     /*	    
    if(fd <= 0)
    {
        fprintf(stderr, "Couldn't open %s\n", argv[1]);
        exit(1);
    }
    */
    do {
        size = read(fd, buf, 256);
        write(1, buf, size);
    } while(size>0);

}
