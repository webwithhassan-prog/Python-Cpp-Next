#include <iostream>
using namespace std;

int main(){
    string arr[5] = {};
    for (int i = 0 ; i < 5 ; i++){
        cout << "Enter cities names : " ;
        cin >> arr[i] ;
    }
    for (int i = 0 ; i < 5 ; i++){
        cout << arr[i] << endl ;
    }
}