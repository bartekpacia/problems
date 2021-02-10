// INF011595
#include <stdio.h>

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
  FILE* inputFile = fopen("num-01.in", "r");
  FILE* outputFile = fopen("num-01.out", "w");

  int num = 0;
  while (1) {
    int ret = fscanf(inputFile, "%d\n", &num);
    if (num == 0 || ret == -1) {
      break;
    }

    int buildingCount = solve(num);
    if (buildingCount == -1) {
      fprintf(outputFile, "%s\n", "Niepoprawne!");
      continue;
    }

    fprintf(outputFile, "%i\n", buildingCount);
  }
  fclose(inputFile);
  fclose(outputFile);

  return 0;
}
