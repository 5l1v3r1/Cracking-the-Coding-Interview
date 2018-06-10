#include <iostream>
#include <string>

using namespace std;

string toBin(int num) {
    if(num == 0) return "0b";
    return toBin(num >> 1) + ((num & 1) ? "1" : "0");
}

int mixBits(int N, int M, int i, int j) {
    int mask = (1<<30)-1;
    mask ^= (1<<j)-1;
    mask |= (1<<i)-1;

    N &= mask;
    N |= (M << i);

    return N;
}

int main() {
    int N = 0b10000011000;
    int M = 0b10101;
    int i = 2;
    int j = 6;

    mixBits(N, M, i, j);

    cout << toBin(mixBits(N, M, i, j)) << endl;
}
