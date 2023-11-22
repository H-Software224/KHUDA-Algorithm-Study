#include <string>
#include <vector>

using namespace std;

string solution(int age) {
    string answer = "";
    answer = to_string(age);

    for(int i = 0; i < answer.size(); i++) {
        answer[i] += 97;
    }
    return answer;
}