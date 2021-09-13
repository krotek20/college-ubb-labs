#include <fstream>
#include <iostream>
#include <string>
#include <queue>
#include <stack>
#include <iomanip>

#define WMAX 1001
#define HMAX 1001

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const int dx[4] = { 1, -1, 0, 0 };
const int dy[4] = { 0, 0, 1, -1 };
queue < pair <int, int> > coada;
stack < pair <int, int> > result;

int Maze[HMAX][WMAX];

void Read(int &n, int &m, int &sx, int &sy, int &fx, int &fy) {
    string buffer;
    n = m = 0;
    while (getline(fin, buffer)) {
        if (m == 0) m = buffer.length();
        for (int i = 0; i < buffer.length(); ++i) {
            if (buffer[i] == '1') Maze[n][i] = -1;
            else if (buffer[i] == ' ') Maze[n][i] = 0;
            else if (buffer[i] == 'S') {
                Maze[n][i] = 1;
                sx = n;
                sy = i;
            }
            else if (buffer[i] == 'F') {
                Maze[n][i] = 0;
                fx = n;
                fy = i;
            }
        }
        ++n;
    }
    fin.close();
}

void print_matrix(int n, int m) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << Maze[i][j] << ' ';
        }
        cout << '\n';
    }
}

void print_result(int fx, int fy) {
    fout << Maze[fx][fy] << '\n';
    while (!result.empty()) {
        fout << result.top().first << ' ' << result.top().second << '\n';
        result.pop();
    }
}

bool Ok(int i, int j, int n, int m) {
    if (i<0 || j<0 || i>=n || j>=m)
        return false;
    if (Maze[i][j] == -1)
        return false;
    return true;
}

void Lee(int n, int m, int sx, int sy, int fx, int fy) {
    int i, j, iNext, jNext;
    coada.push(make_pair(sx, sy));
    while (!coada.empty()) {
        i = coada.front().first;
        j = coada.front().second;
        coada.pop();
        for (int dir = 0; dir < 4; dir++) {
            iNext = i + dx[dir];
            jNext = j + dy[dir];
            if (Ok(iNext, jNext, n, m) && Maze[iNext][jNext] < 1) {
                Maze[iNext][jNext] = Maze[i][j] + 1;
                coada.push(make_pair(iNext, jNext));
            }
        }
    }
}

void find_path(int n, int m, int sx, int sy, int fx, int fy) {
    int i = fx, j = fy, iNext, jNext;
    result.push(make_pair(fx, fy));
    while (i != sx || j != sy) {
        for (int dir = 0; dir < 4; dir++) {
            iNext = i + dx[dir];
            jNext = j + dy[dir];
            if (Ok(iNext, jNext, n, m) && Maze[iNext][jNext] == Maze[i][j] - 1) {
                result.push(make_pair(iNext, jNext));
                i = iNext;
                j = jNext;
                break;
            }
        }
    }
}

int main()
{
    int height, width;
    int sx, sy, fx, fy;
    Read(height, width, sx, sy, fx, fy);
    Lee(height, width, sx, sy, fx, fy);
    find_path(height, width, sx, sy, fx, fy);
    //print_matrix(height, width);
    print_result(fx, fy);
    
    return 0;
}