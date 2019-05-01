#include<iostream>

using namespace std;

class insertion{

public:
int manipulate(int N,int M,int j,int i){
int x = ~0;
x = (x<<(j+1));
int y ;
y = (1<<i)-1;

int mask = x|y;
N = N & mask;
int value = M<<i;
int ans = value|N;
return ans;
}

};

int main(){
int N,M;
cout<<"Please enter integers N and M:\n";
cin >>N>>M;
cout<<"Please enter j and i positions:\n";
int j,i;
cin >>j>>i;
insertion I;
cout<<sizeof(N)<<"\n";
cout<<"manipulated bits=="<<I.manipulate(N,M,j,i);

return 0;
}