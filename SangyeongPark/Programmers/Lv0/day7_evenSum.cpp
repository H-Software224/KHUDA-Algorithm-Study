#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    //even, odd
    if(n % 2 == 0) {
        answer = (n / 2) * (n / 2 + 1) ;
    } 
    else {
        answer = ((n - 1) / 2) * ((n - 1) / 2 + 1) ;
    }
    return answer;
}