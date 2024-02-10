#include<iostream>
using namespace std;

int main()
{
    int n, i, j;
    cout << "Enter a positive number: " << endl;
    cin >> n;
    if (n <= 0) {
        cout << "Not valid\n";
    } else {
        for (i = 2; i < n + 1; i++) {
            bool isprime = true;
            for (j = 2; j < i; j++) {
                if (i % j == 0) {
                    isprime = false;
                    break;
                }
            }
            if (isprime == true) {
                cout << i << endl;
            }
        }
    }
    return 0;
}


