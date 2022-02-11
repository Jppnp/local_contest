#include <bits/stdc++.h>

using namespace std;

int findRange(int game[], int n){
    int max = game[0],i;
    int curr_max = game[0];
    int rangeStart = 0, rangeStop;
    for(int j = 1; j < n; j++){
        if( game[j] > (curr_max + game[j])){
            rangeStart = j;
        }
        curr_max = std::max(curr_max + game[j], game[j]);
        if(curr_max > max){
            rangeStop = j;
        }
        max = std::max(curr_max, max);
    }
    cout << rangeStart << " " << rangeStop << "\n" ;
    cout << max << "\n";

    return max;
}


int main(){
    int sign, row;
    cin >> sign;
    cin >> row;
    int game[sign], max = 0;
    for(int i = 0; i < row; i++){
        for(int j = 0; j < sign; j++){
            cin >> game[j];
        }
        max += findRange(game, sign);
        
    }
    cout << max ;
}