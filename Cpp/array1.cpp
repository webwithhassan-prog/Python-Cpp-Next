#include <iostream>

using namespace std;

int main() {
	int arr[5] = {40, 32, 67, 88, -23};
	int sum = 0;
	
	for (int i = 0; i < 5; i++ ) {
			if(arr[i] > 0){
			sum = sum + arr[i];
		}
	}
	cout << "Sum  is : " <<sum << endl ;
}
