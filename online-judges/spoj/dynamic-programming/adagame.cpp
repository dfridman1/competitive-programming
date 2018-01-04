// http://www.spoj.com/problems/ADAGAME/
// TAGS: dynamic-programming

#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>


using namespace std;


string int_to_string(int len, int n) {
    stringstream ss;
    ss << setw(len) << setfill('0') << n;
    return ss.str();
}

int count_digits(int n) {
    int num_digits;
    for (num_digits = 0; n > 0; num_digits++, n /= 10) {}
    return num_digits;
}

bool all(const vector<bool> &xs) {
    for (bool b : xs) {
        if (!b) return false;
    }
    return true;
}

bool any(const vector<bool> &xs) {
    for (bool b : xs) {
        if (b) return true;
    }
    return false;
}

char next_digit(char d) {
    int n = d - '0';
    return '0' + (n+1)%10;
}

class Solver {
public:
    Solver() : max_n(9999), max_m(100) { init(); }
    string solve(const string &s, int m);
private:
    int max_n, max_m;
    vector< vector<int> >next_numbers;
    bool **dp;
    void init() { precompute(); init_dp(); }
    void init_dp();
    void precompute();
    bool will_ada_win(const vector<bool> &xs, int i, int m);
};

void Solver::precompute() {
    int num_digits = count_digits(max_n);
    for (int i = 0; i <= max_n; i++) {
        string s = int_to_string(num_digits, i);
        vector<int>next;
        for (int i = 0; i < (int)s.size(); i++) {
            char prev = s[i];
            s[i] = next_digit(prev);
            next.push_back(atoi(s.c_str()));
            s[i] = prev;
        }
        next_numbers.push_back(next);
    }
}

void Solver::init_dp() {
    dp = (bool **)malloc((max_m+1)*sizeof(bool *));
    for (int i = 0; i <= max_m; i++) {
        dp[i] = (bool *)malloc((max_n+1)*sizeof(bool));
    }
}

bool Solver::will_ada_win(const vector<bool> &xs, int i, int m) {
    if (m & 1) {
        return (i & 1) ? any(xs) : all(xs);
    } else {
        return (i & 1) ? all(xs) : any(xs);
    }
}

string Solver::solve(const string &s, int m) {
    int N = atoi(s.c_str());
    for (int i = 0; i <= N; i++) dp[0][i] = false;
    for (int i = N+1; i <= max_n; i++) dp[0][i] = true;
    for (int i = 1; i <= m; i++) {
        for (int j = 0; j <= max_n; j++) {
            vector<bool> bs;
            for (int x : next_numbers[j]) {
                bs.push_back(dp[i-1][x]);
            }
            dp[i][j] = will_ada_win(bs, i, m);
        }
    }
    string winner = dp[m][N] ? "Ada" : "Vinit";
    return winner;
}


int main() {
    int N, m;
    string s;
    Solver solver;

    cin >> N;
    while (N-- > 0) {
        cin >> s >> m;
        cout << solver.solve(s, m) << endl;
    }
    return 0;
}
