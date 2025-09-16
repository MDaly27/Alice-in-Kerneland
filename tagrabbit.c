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
            printf("Enter file name for to generate tags (PDF files must be converted to text with >> ts). Press q to exit.\n");
            while (1) {
                 // remove newline at end
                fgets(input, sizeof(input), stdin);
                input[strcspn(input, "\n")] = 0;
                if (strcmp(input, "q") == 0) {
                    break;
                }
                // check if filename exists
                FILE* f;
                if (!(f = fopen(input, "r"))) {
                    printf("File name not present\n");
                    continue;
                }
                fclose(f);

               char command[256];
               sprintf(command, "python3 droid.py %s", input);
               printf("executing this command: %s\n", command);


                FILE* p;
                if (!(p = popen(command, "r"))) {
                    fprintf(stderr, "Unable to run sh for this command: %s\n", command);
                    return -1;
                }
                pclose(p);
                printf("Command sucesfilly executed\n");  
            }


                // execute python command 
        } else if (strcmp(input, "q") == 0) {
            break;
        } else {
            printf("Command not recognized.\n");
        }
    }
}
