#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINES 1048576
#define MAX_LINE_LENGTH 1024

char lines[MAX_LINES][MAX_LINE_LENGTH];
int line_count = 0;

void read_input_file() {
  FILE *file = fopen("input.txt", "r");
  if (!file) {
    perror("Failed to open input.txt");
    exit(1);
  }
  while (fgets(lines[line_count], MAX_LINE_LENGTH, file) &&
         line_count < MAX_LINES) {
    lines[line_count][strcspn(lines[line_count], "\n")] = '\0';
    line_count++;
  }
  fclose(file);
}

long long puzzle_2() {
  long long result = 0;
  int battery_count = 12;

  for (int i = 0; i < line_count; i++) {
    char *battery = lines[i];

    long long total = 0;
    int max_index_before = -1;
    for (int bc = battery_count - 1; bc >= 0; bc--) {
      // Find the first max in the first [0:len-bc], with bc slowly decreasing
      // from 12 to 0
      int max = 0, max_index = 0;
      for (int j = max_index_before + 1; j < strlen(battery) - bc; j++) {
        int current = (int)(battery[j] - '0');
        if (current > max) {
          max = current;
          max_index = j;
        }
      }
      max_index_before = max_index;
      total += max * pow(10, bc);
      printf("max: %d, max_index: %d, total: %lld\n", max, max_index, total);
    }
    printf("----> total: %lld\n", total);

    result += total;
  }

  return result;
}

long long puzzle_1() {
  long long result = 0;

  for (int i = 0; i < line_count; i++) {
    char *battery = lines[i];
    // Find the first max unless it's last
    int max = 0, max_index = 0;
    for (int j = 0; j < strlen(battery) - 1; j++) {
      int current = (int)(battery[j] - '0');
      if (current > max) {
        max = current;
        max_index = j;
      }
    }
    // Find the second max AFTER the first max index
    int second_max = 0, second_max_index = 0;
    for (int j = max_index + 1; j < strlen(battery); j++) {
      int current = (int)(battery[j] - '0');
      if (current > second_max) {
        second_max = current;
        second_max_index = j;
      }
    }
    int total = (max * 10) + second_max;

    result += total;

    printf("max: %d, max_index: %d, second_max: %d, second_max_index: %d, "
           "total: %d\n",
           max, max_index, second_max, second_max_index, total);
  }

  return result;
}

int main() {
  read_input_file();
  // printf("Puzzle 1: %lld\n", puzzle_1());
  printf("Puzzle 2: %lld\n", puzzle_2());
  return 0;
}
