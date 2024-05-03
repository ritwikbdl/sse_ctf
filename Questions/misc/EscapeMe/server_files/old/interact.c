#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_banner() {
    // ASCII art banner
    printf("\n");
    printf("░██████╗░██████╗███████╗  ██████╗░░█████╗░██████╗░░░██╗██╗\n");
    printf("██╔════╝██╔════╝██╔════╝  ╚════██╗██╔══██╗╚════██╗░██╔╝██║\n");
    printf("╚█████╗░╚█████╗░█████╗░░  ░░███╔═╝██║░░██║░░███╔═╝██╔╝░██║\n");
    printf("░╚═══██╗░╚═══██╗██╔══╝░░  ██╔══╝░░██║░░██║██╔══╝░░███████║\n");
    printf("██████╔╝██████╔╝███████╗  ███████╗╚█████╔╝███████╗╚════██║\n");
    printf("╚═════╝░╚═════╝░╚══════╝  ╚══════╝░╚════╝░╚══════╝░░░░░╚═╝\n\n");
}

void greet_user() {
    // Greet the user
    printf("Welcome! This program allows you to save some data.\n");
}

char *take_user_input() {
    // Ask user for input
    char *user_input = malloc(sizeof(char) * 100); // Assuming maximum input length is 100 characters
    printf("Enter your data: ");
    fgets(user_input, 100, stdin);
    user_input[strcspn(user_input, "\n")] = '\0'; // Remove newline character
    return user_input;
}

int main() {
    print_banner();
    greet_user();

    while (1) {
        char *user_input = take_user_input();

        // Call the C program with the user input as an argument
        char command[100 + 7]; // 100 for user input, 7 for "./test "
        snprintf(command, sizeof(command), "./test %s", user_input);
        FILE *devnull = fopen("/dev/null", "w");
        if (devnull == NULL) {
            perror("Error opening /dev/null");
            exit(EXIT_FAILURE);
        }
        int status = system(command);
        fclose(devnull);

        free(user_input);

        if (status == -1) {
            fprintf(stderr, "Error: Please reconnect to the server.\n");
            break;
        }

        char choice;
        printf("Do you want to continue writing data? (y/n): ");
        scanf(" %c", &choice);
        getchar(); // Clear input buffer

        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }

    return 0;
}

