//least common multiple test
//I created this after messing around with my linearEquationHelper's lcm function and realized that is was actually really slow
//This is my implementation of the Euclidean algorithm for finding the gcd, which can be used to find the lcm
//This is way faster than my previous attempt at solving the lcm

#include <iostream>
#include <cmath>   //cmath is needed to mod a double
#include <iomanip> //used to print out large numbers without scientific notation


double gcd( double n, double i);
double lcm( double n, double i);

double a, b, total;

using namespace std;
int main(void) {

    cout << "What is your first value? ";
    cin >> a;
    cout << endl << "What is your second value? ";
    cin >> b;

    total = lcm(a,b);

    cout << setprecision(50) << endl << "Your LCM is " << total << endl;
    //set precision to a large number since you might want to enter two huge numbers

return 0;
}


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
