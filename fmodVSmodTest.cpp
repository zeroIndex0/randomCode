// fmodVSmodTest.cpp
//
//Testing speeds of regular mod '%' and fmod() at a total of one billion iterations

//My guess was that a regular mod '%' was going to be twice as fast since integers are much smaller
// But I was not expecting an at best 9 times increase speed for a call to fmod().
// Now I'm really curious as to what goes on under the hood of fmod().

// Out of the tests, my biggest surprise was when passing two integers into fmod(), it increase the run time
//  I was expecting a faster result when using integers.
//  The best results came from passing in two doubles, which makes sense when thinking about fmod() being created for doubles,
//  But still surprising.


//--------------============= RESULTS:  On a fourth gen i5 Intel CPU ================---------------\\
//Run time of 3 seconds for a regular mod '%' operation
//Run time of 28 seconds is an 89.29% increase of speed on fmod(double, double) compared to regular mod '%'
//Run time of 34 seconds is an 91.18% increase of speed on fmod(double, int) compared to regular mod '%'
//Run time of 29 seconds is an 89.66% increase of speed on fmod(int, int) compared to regular mod '%'
//--------------=====================================================================---------------\\

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main(void) {

int a = 1e8, b = 1e9;
double x = 1e8,y = 1e9;

cout << setprecision(30);  // get rid of scientific notation output


/*
//run time of 3 seconds.... yeah, the speed difference is huge
for (int i = 1; i <= b; i++) {

    if ( i % a == 0) {
        cout << "100,000,000" << endl;
        cout << i << endl;
    }
}
*/


/*
//run time of 28 seconds
for (double i = 1; i <= y; i++) {

    if (fmod (i,x) == 0) {
        cout << "100,000,000" << endl;
        cout << i << endl;
    }
}
*/


/*
//run time of 34 seconds, wow, wasnt expecting that
for (double i = 1; i <= b; i++) {

    if (fmod (i,a) == 0) {
        cout << "100,000,000" << endl;
        cout << i << endl;
    }
}
*/


/*
//run time of 29 seconds when swapping the double to an int in the for loop
for (int i = 1; i <= b; i++) {

    if (fmod (i,a) == 0) {
        cout << "100,000,000" << endl;
        cout << i << endl;
    }
}
*/


return 0;
}
