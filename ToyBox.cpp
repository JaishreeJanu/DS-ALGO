// Problem link is here: https://www.hackerearth.com/challenges/competitive/february-circuits-19/algorithm/toy-box-5044b3ed/
// GREEDY SOLUTION


#include <iostream>
#include <algorithm>
#include <map>
#include <vector>


using namespace std;

int main(){
 
int N,M;
cin >>N>>M;
int sum=0;
int ans=0;
 
 
map<int, vector <int>> m;
 
for(int i=0;i<N;i++){
	int price;
	cin>>price;
	int box;
	cin>>box;
     
	m[box].push_back(price);     
 }
 
 map<int,vector<int>> :: iterator it=m.begin();
 while(it!=m.end()){

 	// sort the prices of toys for each box
	sort(it->second.begin(),it->second.end());
	// pick the toy with highest price
 	vector<int> temp = it->second;
	ans += temp[temp.size()-1];
	it++;
     
 }
 
 cout<<ans<<'\n';
    
    return 0;
}
