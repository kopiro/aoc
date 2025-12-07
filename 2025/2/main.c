#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINES 10000
#define MAX_LINE_LENGTH 100000

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

long long puzzle_1() {
  char *line = lines[0];
  char *token = strtok(line, ",");
  long long result = 0;

  while (token) {
    // Now split token by '-'
    long long a = 0, b = 0;
    sscanf(token, "%lld-%lld", &a, &b);

    // Let's take naive approach and loop from a to b and count to_count
    if (b < a) {
      long long tmp = a;
      a = b;
      b = tmp;
    }

    for (long long j = a; j <= b; j++) {
      bool to_count = true;
      char j_str[512];
      sprintf(j_str, "%lld", j);
      int k = 0;
      int j_str_len = strlen(j_str);
      if (j_str_len % 2 == 0) {
        for (k = 0; k < j_str_len / 2; k++) {
          int k2 = (j_str_len / 2) + k;
          if (j_str[k] != j_str[k2]) {
            to_count = false;
            break;
          }
        }
      } else {
        to_count = false;
      }

      if (to_count) {
        result += j;
      }
    }

    token = strtok(NULL, ",");
  }
  return result;
}

long long puzzle_2() {
  char *line = lines[0];
  char *token = strtok(line, ",");
  long long result = 0;

  while (token) {
    // Now split token by '-'
    long long a = 0, b = 0;
    sscanf(token, "%lld-%lld", &a, &b);

    // Let's take naive approach and loop from a to b and count to_count
    if (b < a) {
      long long tmp = a;
      a = b;
      b = tmp;
    }

    for (long long j = a; j <= b; j++) {
      char j_str[512];
      sprintf(j_str, "%lld", j);

      int j_str_len = strlen(j_str);
      int jumper_max = j_str_len / 2;

      for (int jumper = 1; jumper <= jumper_max; jumper++) {
        // Only count if length is evenly divisible by jumper
        if (j_str_len % jumper != 0) {
          continue;
        }

        bool to_count_for_this_jumper = true;
        int k_start = 0;
        int k_end = k_start + jumper;
        while (k_end < j_str_len) {
          if (j_str[k_start] != j_str[k_end]) {
            to_count_for_this_jumper = false;
            break;
          }
          k_start++;
          k_end = k_start + jumper;
        }
        if (to_count_for_this_jumper) {
          result += j;
          break;
        }
      }
    }

    token = strtok(NULL, ",");
  }
  return result;
}

int main() {
  read_input_file();
  // printf("Puzzle 1: %lld\n", puzzle_1());
  printf("Puzzle 2: %lld\n", puzzle_2());
  return 0;
}
