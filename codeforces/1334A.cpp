#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;

    cin >> T;

    for (int t = 0; t < T; t++) {
        bool valid = true;
        int n;
        cin >> n;

        int p, c;
        int prev_p, prev_c;
        for (int i = 1; i <= n; i++) {
            if (i == 1) {
                cin >> p >> c;

                if (c > p) {
                    valid = false;
                }

            } else {
                prev_p = p;
                prev_c = c;
                cin >> p >> c;

                if (p < prev_p || c < prev_c) {
                    valid = false;
                }

                if (c > p) {
                    valid = false;
                }

                if (p == prev_p) {
                    if (c != prev_c) {
                        valid = false;
                    }
                }
            }
        }

        if (valid) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
