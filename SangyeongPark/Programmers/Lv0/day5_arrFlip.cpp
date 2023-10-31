#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> new_list;

    for(int i = num_list.size()-1; i>=0; i--) {
        new_list.push_back(num_list[i]);
    }
    return new_list;
}