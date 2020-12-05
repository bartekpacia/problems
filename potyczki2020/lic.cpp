#include <math.h>

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

/**
 * Custom method for this task.
 * Returns a vector of digits of n, from left to right.
 * If n has any 0, returns an empty vector.
 */
vector<int> digitsOf(int n) {
  vector<int> digits;

  while (n != 0) {
    int digit = n % 10;

    if (digit == 0) {
      return vector<int>{};
    }

    digits.push_back(digit);
    n = n / 10;
  }

  reverse(digits.begin(), digits.end());
  return digits;
}

int sumOfVector(vector<int> nums) {
  int sum = 0;
  for (int num : nums) {
    sum += num;
  }

  return sum;
}

bool isPotychnikovNumber(int num) {
  // Fail early.
  if (num % 10 == 0) {
    return false;
  }

  vector<int> digits = digitsOf(num);

  if (digits.empty()) {
    return false;
  }

  for (int digit : digits) {
    if (num % digit != 0) {
      return false;
    }
  }

  return true;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int sum = 0;
  int l, r;
  cin >> l >> r;
  for (int num = l; num <= r; num++) {
    if (isPotychnikovNumber(num)) {
      sum++;
    }
  }

  cout << sum << endl;

  return 0;
}