#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  vector<int> input;

  while (!cin.eof()) {
    int val;
    cin >> val;
    input.push_back(val);
  }

  for (int x : input) {
    cout << x << " ";
  }

  return 0;
}