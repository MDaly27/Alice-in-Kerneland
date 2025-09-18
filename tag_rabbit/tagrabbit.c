#include <stdio.h>
#include <string.h>
#include <stdlib.h>



int printFile(char *filename) {
    char line[1024];
    FILE *r;
    if (!(r = fopen(filename, "r"))) {
        fprintf(stderr, "Text art not found.\n");
        return -1;
    }
    while (fgets(line, sizeof(line), r)) {
        printf("%s", line);
    }

    fclose(r);
    return 0;
}

int main() {
    printf("Welcome to TagRabbit\n");
    
    printFile("rabbit.txt");
    printFile("logo.txt");
    printf("Type help for instructions\n");

    char input[100];

    while (1) {
        printf(">> ");
        //printf("%s", input);
        
        if (!fgets(input, sizeof(input), stdin)) break;
        
        input[strcspn(input, "\n")] = 0; // remove final +-
        
        if (strcmp(input, "help") == 0) {
            printf("Type tag to enter file names to create tags for.\n");
            printf("type q to quit.\n");
        } else if (strcmp(input, "tag") == 0) {
            printf("Enter file name to generate tags (only .txt files permitted). Press q to exit.\n");
            while (1) {
                 // remove newline at end
                fgets(input, sizeof(input), stdin);
                input[strcspn(input, "\n")] = 0;
                if (strcmp(input, "q") == 0) {
                    break;
                }
                // make sure filename ends in .txt
                if (!(strcmp(input + strlen(input) - 4, ".txt") == 0)) {
                    fprintf(stderr, "Error, not a text file.\n");
                    continue;
                }


                // check if filename exists
                FILE* f;
                if (!(f = fopen(input, "r"))) {
                    printf("File name not present\n");
                    continue;
                }
                fclose(f);

               char command[256];
               sprintf(command, "python3 ../Droid/droid.py %s | lolcat", input);
               printf("executing this command: %s\n", command);



                int rc = system(command);
                if (rc != 0) {
                   fprintf(stderr, "Failed to execute command.\n");
                } else {
                    printf("Command successfully executed\n");  
                }
            }


                // execute python command 
        } else if (strcmp(input, "q") == 0) {
            break;
        } else {
            printf("Command not recognized.\n");
        }
    }
}
