#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINES 5000
#define MAX_LINE_LENGTH 256

char lines[MAX_LINES][MAX_LINE_LENGTH];
int line_count = 0;

void read_input_file(const char* filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Failed to open file");
        exit(1);
    }
    while (fgets(lines[line_count], MAX_LINE_LENGTH, file) && line_count < MAX_LINES) {
        lines[line_count][strcspn(lines[line_count], "\n")] = '\0';
        line_count++;
    }
    fclose(file);
}

int puzzle_1() {
    int result = 50;
    int zero_count = 0;
    for (int i = 0; i < line_count; i++) {
        char* line = lines[i];
        char direction = line[0];
        char* digit = line + 1;
        int digit_int = atoi(digit);
        digit_int = digit_int % 100;
        if (direction == 'L') {
            result -= digit_int;
        } else {
            result += digit_int;
        }
        if (result < 0) {
            result = 100 + result;
        }
        result = result % 100;
        if (result == 0) {
            zero_count++;
        }
    }
    return zero_count;
}

int main() {
    read_input_file("example.txt");
    printf("Example: %d (expected 3)\n", puzzle_1());
    return 0;
}
