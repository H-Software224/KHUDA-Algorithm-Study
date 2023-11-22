
// 1. target number(타켓 넘버)(programmers)(43165)
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers, int target) {
    if (!numbers.empty()) {
        int extract = numbers[numbers.size() - 1];
        numbers.pop_back();
        return solution(numbers, target - extract) + solution(numbers, target + extract);
    }
    else {
        if (target == 0)
            return 1;
        else
            return 0;
    }
}

// 2. 네트워크(programmers)(43162)
#include <string>
#include <vector>

using namespace std;

bool isvisited[200] = { false, };
vector<vector<int>> v1(200, vector<int>(0));
void dfs(int x) {
    isvisited[x] = true;
    for (int i = 0; i < v1[x].size(); i++) {
        if (!isvisited[v1[x][i]])
            dfs(v1[x][i]);
    }
}
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (computers[i][j] == 1 && i != j) {
                v1[i].push_back(j);
            }
        }
    }
    for (int y = 0; y < n; y++) {
        if (!isvisited[y]) {
            dfs(y);
            answer++;
        }
    }
    return answer;
}

// 3. 상근이의 여행(baekjoon)(9372)
#include <iostream>
#include <vector>

using namespace std;
vector<vector<int>> v1;
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M;
        cin >> N >> M;
        v1.resize(1001, vector<int>(0));
        for (int j = 0; j < M; j++) {
            int first, second;
            cin >> first >> second;
            v1[first].push_back(second);
            v1[second].push_back(first);
        }
        cout << N - 1 << '\n';
    }
    return 0;
}

// 4. 트리의 지름(baekjoon) (1167)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N;
vector<vector<pair<int, int>>> v1(100001);
int max_value = 0, max_node;
vector<bool> isvisited1(100001, false);
void dfs(int root, int distance) {
    isvisited1[root] = true;
    if (max_value < distance) {
        max_node = root;
        max_value = distance;
    }
    for (int i = 0; i < v1[root].size(); i++) {
        if (!isvisited1[v1[root][i].first]) {
            dfs(v1[root][i].first, distance + v1[root][i].second);
        }
    }
}
int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        int a, b, c;
        cin >> a;
        cin >> b;
        while (b != -1) {
            if (b != -1) {
                cin >> c;
                v1[a].push_back(make_pair(b, c));
            }
            cin >> b;
        }
    }
    dfs(1, 0);
    for (int i = 1; i <= N; i++) {
        isvisited1[i] = false;
    }
    dfs(max_node, 0);
    cout << max_value;
    return 0;
}