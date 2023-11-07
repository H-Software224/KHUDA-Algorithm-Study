#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> new_list(2, 0);

    for(int i = 0; i < num_list.size(); i++) {
        if(num_list[i] % 2 == 0) {
            new_list[0]++;
        }
        else {
            new_list[1]++;
        }
    }
    return new_list;
}