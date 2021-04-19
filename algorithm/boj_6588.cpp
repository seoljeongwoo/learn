#include <iostream>
#include <vector>
using namespace std;

const int mn = 1e6+1;
bool isprime[mn];
vector<int> prime;
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    for(int i=3; i<mn; i++) isprime[i] = true;
    for(int i=3 ; i*i<mn ; i++){
        if(isprime[i] == true){
            for(int j=i*i; j<mn; j+=i){
                isprime[j] = false;
            }
        }
    }

    for(int i=3; i<mn; i++){
        if(isprime[i] == true){
            prime.push_back(i);
        }
    }

    while(true){
        int n ; cin>> n;
        if(n == 0) break;
        int a=0;
        int b=0;

        for(int i=0; i<prime.size()/2; i++){
            if(n-prime[i] <=0) break;
            if((n-prime[i])%2==0) continue;
            if(isprime[n-prime[i]] == true){
                a = prime[i];
                b = n - prime[i];
                break;
            }
        }

        if(a == 0){
            cout << "Goldbach's conjecture is wrong.\n";
        }
        else{
            cout << n << " = " << a << " + " << b << "\n"; 
        }
    }

}