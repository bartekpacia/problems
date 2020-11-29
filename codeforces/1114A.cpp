#include <iostream>

using namespace std;

int main() {
    bool ok = true;
    int x, y, z;  // Andrew, Dmitry, Michal
    int a, b, c;  // green, purple, black
    cin >> x >> y >> z;
    cin >> a >> b >> c;

    if (a < x) {
        cout << "NO" << endl;
        return 0;
    }

    if (a + b - x < y) {
        cout << "NO" << endl;
        return 0;
    }

    if (a + b + c - x - y < z) {
        cout << "NO" << endl;
        return 0;
    }

    cout << "YES" << endl;
    return 0;
}
