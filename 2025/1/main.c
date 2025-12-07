#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LINES 10000
#define MAX_LINE_LENGTH 256

char lines[MAX_LINES][MAX_LINE_LENGTH];
int line_count = 0;

void read_input_file(char* filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Failed to open input.txt");
        exit(1);
    }
    while (fgets(lines[line_count], MAX_LINE_LENGTH, file) && line_count < MAX_LINES) {
        lines[line_count][strcspn(lines[line_count], "\n")] = '\0';
        line_count++;
    }
    fclose(file);
}

int max(int a, int b) {
    return a > b ? a : b;
}

int puzzle_1(char* filename) {
    read_input_file(filename);
    int result = 50;
    int zero_count = 0;
    int i = 0;
    for (i = 0; i < line_count; i++) {
        int prev_result = result;
        char* line = lines[i];
        char direction = line[0];
        char* digit = line + 1;
        int digit_int = atoi(digit);
        if (direction == 'L') {
            result -= digit_int % 100;
        } else {
            result += digit_int % 100;
        }
        if (result < 0) {
            result = 100 + result;
        }
        result = result % 100;
        if (result == 0) {
            zero_count++;
        }
        printf("%d -> %c%d -> %d, zero_count: %d\n", prev_result, direction, digit_int, result, zero_count);

    }
    return zero_count;
}

int puzzle_2(char* filename) {
    read_input_file(filename);
    int result = 50;
    int zero_count = 0;
    int i = 0;

    for (i = 0; i < line_count; i++) {
        char* line = lines[i];
        char direction = line[0];
        char* digit = line + 1;
        int digit_int = atoi(digit);

        int crossings = 0;
        if (direction == 'R') {
            // Moving right: we cross 0 each time we pass from 99 to 0
            crossings = (result + digit_int) / 100;
            result = (result + digit_int) % 100;
        } else {
            // Moving left: we cross 0 each time we pass from 0 to 99
            if (result == 0) {
                // Starting at 0, moving left - only cross when completing full loops
                crossings = digit_int / 100;
            } else if (digit_int >= result) {
                // We'll pass through 0 at least once
                crossings = 1 + (digit_int - result) / 100;
            } else {
                // We don't reach 0
                crossings = 0;
            }
            result = result - digit_int;
            result = ((result % 100) + 100) % 100;
        }

        zero_count += crossings;
    }
    return zero_count;
}

int main() {
    //printf("Puzzle 1: %d\n", puzzle_1());
    printf("Puzzle 2: %d\n", puzzle_2("input.txt"));
    return 0;
}
