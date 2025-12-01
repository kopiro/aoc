#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINES 1000
#define MAX_LINE_LENGTH 256

char lines[MAX_LINES][MAX_LINE_LENGTH];
int line_count = 0;

void read_input_file() {
    FILE *file = fopen("input.txt", "r");
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

int puzzle_1() {
    return 0;
}

int puzzle_2() {
    return 0;
}

int main() {
    read_input_file();
    printf("Puzzle 1: %d\n", puzzle_1());
    // printf("Puzzle 2: %d\n", puzzle_2());
    return 0;
}
