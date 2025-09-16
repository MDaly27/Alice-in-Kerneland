#include <stdio.h>
#include <string.h>

int main() {
    printf("Welcome to TagRabbit\n");
    printf("Type help for instructions\n");

    char input[100];

    while (1) {
        printf(">> ");
        //printf("%s", input);
        if (!fgets(input, sizeof(input), stdin)) break;

        input[strcspn(input, "\n")] = 0;
        
        if (strcmp(input, "help") == 0) {
            printf("Instructions for usage here.\n");
        } else if (strcmp(input, "tag") == 0) {
            printf("Enter filename for to generate tags (PDF files must be converted to text with >> ts). Press q to exit.\n");
            while (1) {
                 // remove newline at end
                fgets(input, sizeof(input), stdin);
                input[strcspn(input, "\n")] = 0;
                if (strcmp(input, "q") == 0) {
                    break;
                }
                // check if filename exists
            }
        } else if (strcmp(input, "q") == 0) {
            break;
        } else {
            printf("Command not recognized.\n");
        }
    }
}
