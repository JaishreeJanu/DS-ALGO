#include<iostream>
#include<string>

using namespace std;

class convert{

private:
double get(){
    double num;
    cin>>num;

    return num;
}

public:
string getBinary(){
double num = get();

if(num>=1 || num<=0){
    return "ERROR";
}

string ans = ".";
while(num>0){
    if(ans.length()>32){
        return ans;
    }
double r = num*2;
if(r>=1){
    ans += "1";
    num = r-1;
}
else{
    ans += "0";
    num = r;
}
}

return ans;
}
};

int main(){
convert C;
string bin = C.getBinary();
cout<<bin<<endl;

    return 0;
}
