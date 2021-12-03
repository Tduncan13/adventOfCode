#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH 80

int solve(int *input, int c){
	int i;
	int count = 0;

	for (i = 0; i < c - 1; i++){
		if (input[i] < input[i + 1]){
			count++;
		}
	}

	return count;
}

int main(int argc, char **argv){
	FILE *fo;
	char line[MAX_LINE_LENGTH] = {0};
	int *lines;
	char c;
	int lineCount = 0;
	int i = 0;

	fo = fopen(argv[1], "r");

	for (c = getc(fo); c != EOF; c = getc(fo)){
		if (c == '\n') lineCount++;
	}

	lines = malloc(sizeof(int) * lineCount);
	rewind(fo);

	while(fgets(line, MAX_LINE_LENGTH, fo)){
		lines[i++] = atoi(line);
	}

	printf("%d\n", solve(lines, lineCount));
	
	free(lines);
	fclose(fo);
}

