#include <iostream>
#include <string>

using namespace std;

string toBin(int num) {
    if(num == 0) return "0b";
    return toBin(num >> 1) + ((num & 1) ? "1" : "0");
}

int main() {
    cout << toBin((1<<31)-1) << endl;
}
