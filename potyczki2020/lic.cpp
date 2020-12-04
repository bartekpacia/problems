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

  cout << endl;

  for (int x : input) {
    cout << x << endl;
  }

  return 0;
}