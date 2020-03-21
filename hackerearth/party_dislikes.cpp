// Problem link: https://www.hackerearth.com/challenges/competitive/march-circuits-20/algorithm/dislikes-and-party-567b9605/

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>


using namespace std;

int main(){
 	//Take input
	long long N;
	cin >> N;
	long long dl[10][10];
	for(int i=0;i<10;i++){
		for(int j=0;j<10;j++){
			cin >> dl[i][j];
		}
	}

	long long total = (N*(N-1))/2;
	total -= (9*10);

	long long doubles = 0;
	//map for storing pairs of handshakes
	map<pair<long,long>,int> mp;

	//Find redundant handshakes
	for(int i=0 ; i<10 ; i++){
		int curr_num = dl[i][0];
		for(int j=1 ; j<10 ; j++){
			pair <long,long> this_pair = make_pair(dl[i][j],curr_num);
			if(mp.find(this_pair) != mp.end()){
				doubles++;
			}
			else{
				this_pair = make_pair(curr_num,dl[i][j]);
				mp[this_pair] = 1;
			}
		}
	}
	total += doubles;
	cout<<total;

    
    return 0;
}
