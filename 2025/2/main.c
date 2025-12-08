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

int compare_ll(const void *a, const void *b) {
  long long x = *(long long *)a;
  long long y = *(long long *)b;
  if (x < y)
    return -1;
  if (x > y)
    return 1;
  return 0;
}

// Generate repeating-pattern numbers directly instead of brute forcing
long long puzzle_2_fast() {
  char line_copy[MAX_LINE_LENGTH];
  strcpy(line_copy, lines[0]);
  char *token = strtok(line_copy, ",");
  long long total = 0;

  while (token) {
    long long a = 0, b = 0;
    sscanf(token, "%lld-%lld", &a, &b);

    if (b < a) {
      long long tmp = a;
      a = b;
      b = tmp;
    }

    // Collect all matching numbers (static to avoid stack issues)
    static long long matches[2000000];
    int match_count = 0;

    // For each pattern length (1 to 10 digits)
    for (int pattern_len = 1; pattern_len <= 10; pattern_len++) {
      // Calculate range of base patterns (e.g., 1-9 for len=1, 10-99 for len=2)
      long long min_base = 1;
      for (int i = 1; i < pattern_len; i++)
        min_base *= 10;
      long long max_base = min_base * 10 - 1;

      // Multiplier for concatenation
      long long multiplier = 1;
      for (int i = 0; i < pattern_len; i++)
        multiplier *= 10;

      // For each number of repetitions (at least 2)
      for (int num_repeats = 2; pattern_len * num_repeats <= 20;
           num_repeats++) {
        for (long long base = min_base; base <= max_base; base++) {
          // Construct the repeated number: base repeated num_repeats times
          long long num = 0;
          for (int r = 0; r < num_repeats; r++) {
            num = num * multiplier + base;
          }

          if (num >= a && num <= b) {
            matches[match_count++] = num;
          }
        }
      }
    }

    // Sort and sum unique values
    qsort(matches, match_count, sizeof(long long), compare_ll);

    long long prev = -1;
    for (int i = 0; i < match_count; i++) {
      if (matches[i] != prev) {
        total += matches[i];
        prev = matches[i];
      }
    }

    token = strtok(NULL, ",");
  }
  return total;
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
