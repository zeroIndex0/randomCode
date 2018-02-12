//
//
//
// buildAGrid.cpp

//messing around with printing out shapes and decided to create a function that prints out a grid of a size of your choosing
//the current issue that that i dont error check for non alpha characters and if the grid number is too large the output is
//not pretty at all.  So i think i should just cap the size of the grid


#include <iostream>
using namespace std;


//how would i go about inserting values into these shapes?

void printSquare(){

  cout << " _________ " << "\n"
       << "|         |" << "\n"
       << "|         |" << "\n"
       << "|         |" << "\n"
       << "|         |" << "\n"
       << "|_________|" << "\n"
       << endl;

}

void printGridSmall() {
  cout << " _________ " << "\n"
       << "|_|_|_|_|_|" << "\n"
       << "|_|_|_|_|_|" << "\n"
       << "|_|_|_|_|_|" << "\n"
       << "|_|_|_|_|_|" << "\n"
       << "|_|_|_|_|_|" << "\n"
       << endl;
}


void printGridLarge() {
  cout << " __  __  __  __  __ " << "\n"
       << "|__||__||__||__||__|" << "\n"
       << "|__||__||__||__||__|" << "\n"
       << "|__||__||__||__||__|" << "\n"
       << "|__||__||__||__||__|" << "\n"
       << "|__||__||__||__||__|" << "\n"
       << "|__||__||__||__||__|" << "\n"
       << endl;

}

void printGrid(int rows, int columns) {


  if(rows > 0 && columns > 0) {
  //i need to build each row at a time and the first row has to be built separately
  for(int i = 0; i < columns; i++) {
    cout << " __ ";
  }
  cout << endl;

  for(int i = 0; i < rows; i++) {
    for(int j = 0; j < columns; j++) {
      cout << "|__|";
    }
    cout << endl;
  }
  cout << endl;
  } else {
    cout << endl << "Unable to build a grid of that size." << endl << endl;
  }
}



int main(void) {

  int rows = 0, columns = 0;
  printSquare();
  printGridSmall();
  printGridLarge();

  do{
    cout << "How many rows do you want in the grid? ";
    cin >> rows;
    cout << "How many columns do you want in the grid? ";
    cin >> columns;
    printGrid(rows, columns);
  }while(rows != -1 || columns != -1);

  return 0;
}
