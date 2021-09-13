// Flux maxim Ford Fulkerson algoritm 
#include <iostream>
#include <fstream>
#include <climits>
#include <string>
#include <vector>
#include <queue>

using namespace std;

#define VMAX 1005

bool BFS(vector<vector<int>>& Gf, int s, int t, vector<int>& PI) {
    bool visited[VMAX] = { false };
    queue<int> q;

    q.push(s), visited[s] = true, PI[s] = -1;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (size_t v = 0; v < Gf.size(); ++v) {
            if (!visited[v] && Gf[u][v] > 0) {
                q.push(v);
                PI[v] = u;
                visited[v] = true;
            }
        }
    }

    return visited[t];
}

int EdmondsKarp(vector<vector<int>>& G, int s, int t) {
    int cf = 0;
    vector<int> PI;
    vector<vector<int>> Gf;
    for (size_t i = 0; i < G.size(); ++i) {
        vector<int> row;
        Gf.push_back(row);
        for (size_t j = 0; j < G[i].size(); ++j) {
            Gf[i].push_back(G[i][j]);
        }
    }

    for (size_t i = 0; i < G.size(); ++i) {
        PI.push_back(-1);
    }

    while (BFS(Gf, s, t, PI)) {
        int cfp = INT_MAX;

        for (size_t v = t; v != s; v = PI[v]) {
            size_t u = PI[v];
            cfp = min(cfp, Gf[u][v]);
        }

        for (size_t v = t; v != s; v = PI[v]) {
            size_t u = PI[v];
            Gf[u][v] -= cfp;
            Gf[v][u] += cfp;
        }

        cf += cfp;
    }
    return cf;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cout << "Usage: " << argv[0] << " input_file output_file";
        exit(EXIT_FAILURE);
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    if (argv[1] == nullptr) {
        perror(argv[1]);
        exit(EXIT_FAILURE);
    }

    vector<vector<int>> G;
    int V, E;
    fin >> V >> E;
    for (size_t i = 0; i < V; ++i) {
        vector<int> row;
        G.push_back(row);
        for (size_t j = 0; j < V; ++j) {
            G[i].push_back(0);
        }
    }

    int x, y, c;
    for (int i = 0; i < E; ++i) {
        fin >> x >> y >> c;
        G[x][y] = c;
    }

    fout << EdmondsKarp(G, 0, V - 1);

    fin.close();
    fout.close();
    return 0;
}