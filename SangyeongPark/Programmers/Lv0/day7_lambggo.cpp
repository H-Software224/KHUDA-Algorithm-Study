#include <string>
#include <vector>

using namespace std;

int solution(int n, int k) {
    int answer = 0;
    int service = n / 10;
    
    k -= service;
    
    if(k <= 0) {
        k = 0;
    }
    
    answer = (n * 12000) + (k * 2000); 
    
    return answer;
}