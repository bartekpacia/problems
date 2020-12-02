#include <stdio.h>
#include <stdlib.h>

int numberOfDigits(int num) {
  int digits = 0;
  while (num != 0) {
    num = num / 10;
    digits++;
  }

  return digits;
}

int solve(int countOfPlates) {
  int numberOfBuildings = 1;
  while (countOfPlates > 0) {
    int numOfDigits = numberOfDigits(numberOfBuildings);
    countOfPlates -= numOfDigits;

    numberOfBuildings++;
  }

  if (countOfPlates != 0) {
    return -1;  // let's signal that it's invalid
  }

  int countOfBuildings = numberOfBuildings - 1;
  return countOfBuildings;
}

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
  fclose(inputFile);

  FILE* outputFile = fopen("num-01.out", "w");
  for (int i = 0; i < 10; i++) {
    if (plateNumbers[i] == 0) {
      break;
    }

    int buildingCount = solve(plateNumbers[i]);
    // int size = numberOfDigits(buildingCount);
    // char str[size];
    // sprintf(str, "%d", buildingCount);

    fprintf(outputFile, "%i", buildingCount);
  }
  fclose(outputFile);

  return 0;
}