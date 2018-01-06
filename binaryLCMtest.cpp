//binary gcd algorithm speed testing
//
//binaryLCMtest.cpp
//
//I obtained the binary algorithm from Daniel Lemire @ https://lemire.me/blog/2013/12/26/fastest-way-to-compute-the-greatest-common-divisor/

/*
 *I decided to test out the shifting binary algorithm since I have been looking into some least common multiple run times lately
 *and I have to say that this binary gcd is extremely fast.  At least compared to anything ive looked at and coded.
 *
 *I ran the two lcm functions through a nested for loop to give the function a high number of iterations to really test out the speed difference
 *
 */


 //If you want to test them out yourself ( maybe you have a much faster cpu than mine and would like to push the limits )
 // then all you have to do is uncomment each section and change the values in the for loops.


 //===================  Comparing Binary LCM to Euclidean LCM using nested for loops ==========================================\\
 //============================================================================================================================\\
 //            |             |                        |                          |          (time increase of Euclidean method \\
 //      i     |      n      |   Binary (seconds)     |  Euclidean  (seconds)    |  Result    over Binary method - percentage) \\
 //----------------------------------------------------------------------------------------------------------------------------\\
 //  1,000,000 |    100      |          10            |          29              |                     190%                    \\
 // ---------------------------------------------------------------------------------------------------------------------------\\
 //  1,000,000 |    500      |          55            |          183             |                     233%                    \\
 //----------------------------------------------------------------------------------------------------------------------------\\
 //  1,000,000 |    1000     |          113           |          389             |                     244%                    \\
 //============================================================================================================================\\

 //It is clear to see that the binary method outperforms the Euclidean method at around twice the speed.
 //I have to say, I am not exactly sure what a faster algorithm would be used for, but I had a lot of fun
 //testing them out and comparing the speeds, so I thought I would share my results.


 //Also, the binary algorithm uses built in compiler functions for gcc and its possible that could create some issues depending
 // on your set-up.  Personally, I had no issue getting the algorithm for the link complied.  I did just the size of the data type
 // and that was just for pushing in massive numbers for earlier tests, but those were much simple and without nested for loops, so
 // those results did not give much of a time difference so I did not include those tests.



#include <iostream>
#include <iomanip>   //used to eliminate scientific notation
#include <cmath>     //used for fmod() to mod doubles

using namespace std;


unsigned long long int gcd(unsigned long long int u, unsigned long long int v);
unsigned long long int lcm(unsigned long long int n, unsigned long long int i);

double gcd( double n, double i);
double lcm( double n, double i);



int main(void) {

cout << setprecision(50); //gets rid of scientific notation


/*
//10 second run time at n = 100
//55 second run tim at n = 500
//113 second run time at n = 1000
unsigned long long int z = 0;
for (unsigned long long int i = 1; i < 1e6; i++){
        for (unsigned long long int n = 1; n < 2000; n++) {
                z += lcm(n, i);
                //cout << lcm(n, i) << " binaryLCM " << endl;
        }
}
cout << z <<  " z" << endl;
*/


/*
//29 second run time at n = 100
//183 seond run tim at n = 500
//389 second run time at n = 1000
double y = 0;
for (double i = 1; i < 1e6; i++){
        for (double n = 1; n < 1000; n++) {
                y += lcm(n, i);
                //cout << lcm(n, i) << " EuclideanLCM " << endl;
        }
}
cout << y << " y" << endl;
*/


return 0;
}



unsigned long long int lcm(unsigned long long int n, unsigned long long int i) {
 return ((n * i) / gcd(n, i));
}


//taken from Daniel Lemire https://lemire.me/blog/2013/12/26/fastest-way-to-compute-the-greatest-common-divisor/
unsigned long long int gcd(unsigned long long int u, unsigned long long int v)
{
    int shift;
    if (u == 0) return v;
    if (v == 0) return u;
    shift = __builtin_ctz(u | v);
    u >>= __builtin_ctz(u);
    do {
        v >>= __builtin_ctz(v);
        if (u > v) {
            unsigned long long int t = v;
            v = u;
            u = t;
        }
        v = v - u;
    } while (v != 0);
    return u << shift;
}



//taken from my lcmTest.cpp
double lcm(double n, double i) {

return ((n * i ) / (gcd(n, i)));

}

double gcd( double n, double i) {
    double r = 0;

    while(i != 0){
        if(fmod(n, i) == 0) {
            //if n mod i == 0 then i is the greatest common divisor
            return i;
        } else {
        //The old i is the new n and take the remainder of n/i and thats the new i
         r = fmod(n, i);
         n = i;
         i = r;
        }
    }
//I dont see a case where total will actually be returned from here, but thats okay
return i;
}
