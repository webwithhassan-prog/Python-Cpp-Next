#include <iostream>
using namespace std;

int main(){
   int n; 
   cout << " -----Enter Any number to check +(ive) or -(ive)-----" << endl;
   cout << "Enter a number : ";
   cin >>  n ;
   if(n > 0)
      cout << n << "  is a Positve Number";
   else if (n < 0)
      cout << n << "  is a Negative Number";
    else
       cout << "Entered Number is Zero";

    return 0;
    
}