#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> digitsOf(int n) {
  vector<int> digits;

  while (n != 0) {
    int digit = n % 10;
    digits.push_back(digit);
    n = n / 10;
  }

  reverse(digits.begin(), digits.end());
  return digits;
}

bool isPotychnikovNumber(int num) { return true; }

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int l, r;
  cin >> l >> r;

  for (int num = l; num <= r; num++) {
    if (isPotychnikovNumber(num)) {
      cout << num << endl;
    }
  }

  auto digits = digitsOf(1234);

  for (int digit : digits) {
    cout << digit << endl;
  }

  return 0;
}