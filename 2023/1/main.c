#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAXSIZE 128

FILE* fptr = NULL;
char line[MAXSIZE];
char* words[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

unsigned int parse_line_puzzle_one(char* line) {
	char a, b, ab[3];
	int i, len = strlen(line);
	for (i = 0; i < len; i++) {
		if (isdigit(line[i])) {
			a = line[i];
			break;
		}
	}
	for (i = len-1; i >= 0; i--) {
		if (isdigit(line[i])) {
			b = line[i];
			break;
		}
	}
	sprintf(ab, "%c%c", a, b);
	return atoi(ab);
}

void puzzle_one() {
	unsigned long int result = 0;

	while (fgets(line, MAXSIZE, fptr) != NULL) {
		int s = parse_line_puzzle_one(line);
		result = result + (unsigned long)s;
	}

	printf("Result: %lu \n", result);
}


unsigned int parse_line_puzzle_two(char* line) {
	char* ab = malloc(2 * sizeof(char));
	int verse, len = strlen(line);
	ab[2] = '\0';
	
	for (verse = -1; verse <= 1; verse++) {
		int i, j;
		int index = verse == 1 ? 0 : 1;
		int found = 0;
		if (verse == 0) continue;
	
		for (i = (verse == 1) ? 0 : len-1; (verse == 1) ? i < len : i >= 0; i += verse) {
			if (found == 1) break;
			if (isdigit(line[i])) {
				ab[index] = line[i];
				found = 1;
				break;
			}
			for (j = 0; j < 10; j++) {
				char* word = words[j];
				int k, wlen = strlen(word);
				for (k = 0; k < wlen && i+k < len; k++) {
					if (line[i+k] != word[k]) {
						break;
					}
				}
				if (k == wlen) {
					ab[index] = j + '0';
					found = 1;
					break;
				}
			}
		}
	}

	return atoi(ab);
}

void puzzle_two() {
	unsigned long int result = 0;

	while (fgets(line, MAXSIZE, fptr) != NULL) {
		int s = parse_line_puzzle_two(line);
		result = result + (unsigned long)s;
	}

	printf("Result: %lu \n", result);
}


int main() {
 	fptr = fopen("input.txt", "r");
	
	if (fptr == NULL) {
		perror("Error opening file");
		return 1;
	}
	 
	// puzzle_one();
	puzzle_two();
	
	fclose(fptr);
	
	return 0;
}