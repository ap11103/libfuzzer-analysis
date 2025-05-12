#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>


//simple function to demonstrate a vulnerability
void process_input(char *input) {
    char buffer[64];

    //vulnerability here: not checking the length of the input before copying it into the buffer
    //causes buffer overflow
    strcpy(buffer, input);

    printf("Processed input: %s\n", buffer);
}

//main function to interact with libFuzzer
int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    //convert the fuzzer input into a string (null-terminated)
    char *input = malloc(size + 1);
    if (!input) {
        return 0;
    }
    memcpy(input, data, size);
    input[size] = '\0';

    //triggering the vulnerability
    process_input(input);

    free(input);
    return 0;
}
