//
//
// startStopStep.cpp
// simple program that is meant to output a lot numbers to the screen
// there is no real benefit other than aesthetics, but still very fun

#include <iostream>
using namespace std;

int main(void) {
int start, stop, step;

cout << "What number would you like to start at? ";
cin >> start;
cout << "What number would you like to count to? ";
cin >> stop;
cout << "In what increments would you like to count by? ";
cin >> step;

for(int i = start; i < stop; i+=step) {
    cout << i << (i % 5 == 0 ? " " : "   ");
}
cout << endl;

return 0;
}
