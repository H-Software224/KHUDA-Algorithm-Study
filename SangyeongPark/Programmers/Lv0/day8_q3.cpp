#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> emergency) {
    vector<int> answer;
    vector<int> origin = emergency;
    sort(emergency.rbegin(), emergency.rend());

    for(int i = 0; i < origin.size()+1; i++) {
        for(int j = 0; j < emergency.size(); j++) {
            if(emergency[j] == origin[i]) {
                answer.push_back(j+1);
            }
        }
    }
    return answer;
}