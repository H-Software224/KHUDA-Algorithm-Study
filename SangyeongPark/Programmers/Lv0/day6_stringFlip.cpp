#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string new_string;

    for(int i = my_string.size()-1; i>=0; i--) {
        new_string.push_back(my_string[i]);
    }
    return new_string;
}