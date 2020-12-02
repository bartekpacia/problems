#include <stdio.h>
#include <stdlib.h>

int main() {
  int plateNumbers[10] = {0};

  FILE* inputFile = fopen("num-01.in", "r");
  char* line;
  size_t len;
  ssize_t read = getline(&line, &len, inputFile);

  int i = 0;
  while (read != -1) {
    int num = strtol(line, NULL, 10);
    read = getline(&line, &len, inputFile);
    plateNumbers[i] = num;

    i++;
  }

  FILE* outputFile = fopen("num-01.out", "w");
  for (int i = 0; i < 10; i++) {
    printf("%i: %i\n", i, plateNumbers[i]);
  }

  return 0;
}