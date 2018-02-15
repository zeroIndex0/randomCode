//
//
//
// throwingErrors.cpp

// just trying to throw some errors as ive been interested in messing with them for a while now since I have seen them a few times
// and really haven't had much of an understanding of what exactly they are doing.
// Ive found most of these online and have just been messing around trying out the exceptions to familiarize myself a little bit
// and to see if my complier will accept the errors or if it will give other kinds of errors before i compile the program




#include <iostream>
#include <exception>
#include <new>
#include <typeinfo>
#include <functional>
#include <memory>
#include <vector>
using namespace std;

class Base {virtual void memeber(){}};
class Derived : Base {};



class WillBeABad_Alloc{
public:
    WillBeABad_Alloc() {
    char *p = new char[9999999999999999999];  // much too large
    delete [] p;
    }

};



//couldnt get this one to work
void fail() {
throw 'x';
}


int main(void) {

    //Just trying out ways to catch errors
    try{
        Base b;
        Derived &rd = dynamic_cast<Derived&>(b);
    }
    catch (bad_cast & bc) {
    cout << "Bad cast caught: " << bc.what() << endl;
    }


    //my frist proper use of typeid is to catch an error.  I hope i didnt just curse myself
    try {
        Base *b = 0;
        cout << typeid(*b).name();
    }
    catch(bad_typeid &e) {
        cout << "Bad typeid caught: " << e.what() << endl;
    }


    //first time using function, but I know i can catch a bad call!
    function<int()> f = nullptr;
    try{
        f();
    }
    catch(bad_function_call &e) {
        cout << "Caught: " << e.what() << endl;
    }


    //Ive never used this so im a bit fuzzy on the details, but it catches the error
    shared_ptr<int> p1(new int(42));
    weak_ptr<int> wp(p1);
    p1.reset();
    try{
        shared_ptr<int> p2(wp);
    }
    catch(bad_weak_ptr &e) {
        cout << "Caught bad pointer: " << e.what() << endl;
    }


    vector<int> myVec(5);
    try {
        myVec.at(10) = 30;
    }
    catch(out_of_range &e) {
        cout << "Caught vector out of range: " << e.what() << endl;
    }

    //doesn't give an error, just outputs garbage thats stored in the next memory address, which makes sense it wont catch the error
    //now that i think about it
    int array[9];
    try{
        cout << array[10] << " <-- Is just garbage and the error isn't caught " << endl;
    }
    catch(length_error &e) {
        cout << "Caught length error: " << e.what() << endl;
    }

    //good ole vector not letting me down with passing errors
    vector<int> myVector;
    try{
        //cannot resize a vector bigger than its max size
        myVector.resize(myVector.max_size()+1);
    }
    catch(length_error &e) {
        cout << "Caught length error: " << e.what() << endl;
    }

    //trying to allocate far too much memory
    try{
        WillBeABad_Alloc badBad_Alloc;
    }
    catch(bad_alloc &e) {
        cout << "Caught bad_alloc: " << e.what() << endl;
    }



return 0;
}
