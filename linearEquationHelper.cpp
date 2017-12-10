//A simple program created to find the point slope of a line give two points
//or to find the least common multiple of two numbers

#include <iostream>


//TODO: Error check the inputs after the menu selection

using namespace std;

double twoPoint();
double slope(double x1, double y1, double x2, double y2);
double leastCommon();
double multi(double &find, double &found, double &multi1, double &multi2);
double greaterthan(double &find,double &found, double &multi1, double &multi2);
double lessthan(double &find, double &found, double &multi1, double &multi2);

int menu(int choice);

int main(void) {
  int choice = 0;

  menu(choice);

  return 0;
}

int menu(int choice) {
  do {
    cout <<" -----Linear Equation Helper-----" << endl;
    cout << "1: Find slope, point slope, and y-intercept using two points"
         << endl << "2: Find the least common multiple of two numbers"
         << endl << "3: Exit" << endl;
    cout << "Enter menu option: ";
    cin >> choice;


    //If the input was anything other than 1, 2 or 3 we need to flush whatever is in there and reset the stream
    //oh, and notify the user that their selection was incorrect
    if (choice > 3 || choice < 1) {
      cout << "Invalid choice please enter again" << endl << endl;
      //If the input is a character we need to clear the buffer and then ignore whats in there
      cin.clear();
      //call cin.ignore() to get rid of the new line character thats been added to the stream
      cin.ignore();
    }

    if (choice == 1)
      twoPoint();
    if (choice == 2)
      leastCommon();
    if (choice == 3)
      return 0;

  }
  while (choice > 3 || choice < 1);

  return choice;
}

double twoPoint() {

  double x1, y1, x2, y2, m, x1dist;

  //to get the slope m= y2-y1 / x2-x1
  //slope intercept y=m*x+b
  //point slope is y-y1=m(x-x1)
  cout << endl << "----- Get the slope for two points -----"<< endl << endl;
  cout << "Enter your first x point: ";
  cin >> x1;
  cout << "Enter your first y point: ";
  cin >> y1;
  cout << "Enter your second x point: ";
  cin >> x2;
  cout << "Enter your second y point: ";
  cin >> y2;
  m = slope(x1, y1, x2, y2);
  //  m = (x2 - x1) / (y2 - y1);
  cout << "Your slope is " << m <<endl <<endl;
  cout << "To get your slope intercept form we need to use the slope point form.  Now that we have the slope we can use the equation y-y1=m(x-x1)" <<endl;
  cout <<"We got the slope and know its " << m <<" and we already have the two points so you get: " <<endl;
  cout << " y" << -y1 << "=" << m <<"(x" << -x1 << ")" <<endl <<endl;
  cout << "After distributing you get "<<endl;
  cout << " y" << -y1 << "=" << m << "x" << m * -x1 <<endl << endl;
  x1dist = m * -x1;
  cout << "So then you would simplify that putting it in slope intercept form"<<endl;
  cout << " y=" << m <<"x" << x1dist + y1 <<endl <<endl;

  return 0;
}

double leastCommon() {

  double number1=0,number2=0, multi1=0, multi2=0;
  //these variables are used to find the values needed to multiply the x or y to get rid of them
  double div1, div2;

  cout << endl;
  cout << "Enter the first number ";
  cin >> number1;
  cout << "Enter the second number ";
  cin >> number2;
  multi1 = number1;
  multi2 = number2;
  multi(number1, number2, multi1, multi2);
  //multi1 and multi2 are actually the same number at this point, but i added both for a bit of clarity, i suppose
  div1 = multi1 / number1;
  cout << "you will need to multiply " << number1 << " by " << div1;
  cout << endl;
  div2 = multi2 / number2;
  cout << "you will need to multiply " << number2 << " by " << div2;
  cout << endl;

  return 0;
}


double slope(double x1, double y1, double x2, double y2) {
  double m, num, den;

  num = y2 - y1;        //get the numerator
  den = x2 - x1;        //get the denominator
  m = num / den;        //get the slope

  return m;
}


//find and found are really just number 1 and number 2 from above
double multi(double &find,double &found, double &multi1, double &multi2) {
  do{
    if(multi1 > multi2)
      greaterthan(find, found, multi1, multi2);
    else if(multi1 < multi2)
      lessthan(find, found, multi1, multi2);
  }while(multi1!=multi2);
  //when the two passed in values are equal, we have found our match
  cout << "The least common multiple is "<< multi1 <<endl;
  return multi1;
}

//find and found are really just number 1 and number 2 from above
double greaterthan(double &find, double &found, double &multi1, double &multi2) {
  double count=0;
  do {
    count++;
    multi2 = found * count;
  }while(multi1 > multi2);
  return 0;
}

//find and found are really just number 1 and number 2 from above
double lessthan(double &find, double &found,  double &multi1, double &multi2) {
  double count=0;
  do {
    count++;
    multi1 = find * count;
  }while(multi1 < multi2);
  return 0;
}
