#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH 80

void freeList(char** lines, int c){
	int i;

	for (i = 0; i < c; i++){
		free(lines[i]);
	}

	free(lines);
	return;
}

int solve(char **k, int *v, int c){
	int i;
	int forward = 0;
	int up = 0;
	int down = 0;
	
	for (i = 0; i < c; i++){
		if (strcmp("forward", k[i]) == 0){
				forward += v[i];	
		} else if (strcmp("up", k[i]) == 0){
				up += v[i];	
		} else if (strcmp("down", k[i]) == 0){
				down += v[i];	
		}
	}
	return forward * (down - up);
}

int main(int argc, char **argv){
	FILE *fo;
	char *key = malloc(sizeof(char) * MAX_LINE_LENGTH);
	char **keys;
	int value;
	int *values;
	char c;
	int lineCount = 0;
	int i = 0;

	fo = fopen(argv[1], "r");

	for (c = getc(fo); c != EOF; c = getc(fo)){
		if (c == '\n') lineCount++;
	}

	rewind(fo);

	keys = malloc(sizeof(char*) * lineCount);
	values = malloc(sizeof(int) * lineCount);

	while(fscanf(fo, "%s %d\n", key, &value) != EOF){
		keys[i] = malloc(sizeof(char) * MAX_LINE_LENGTH);
		strcpy(keys[i], key);
		values[i++] = value;
	}

	printf("%d\n", solve(keys, values, lineCount));
	
	freeList(keys, lineCount);
	free(values);
	fclose(fo);
}

