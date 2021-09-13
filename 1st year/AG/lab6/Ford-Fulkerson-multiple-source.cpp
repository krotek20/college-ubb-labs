#include <climits>
#include <fstream>
#include <vector>
#include <queue>

#define NMAX 101
#define INF INT_MAX

using namespace std;

vector<vector<int>> G;

bool BFS(vector<vector<int>>& Gf, int s, int t, vector<int>& PI) {
    bool visited[NMAX] = { false };
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

vector<int> FordFulkerson(int s, int t, int C) {
    int cf = 0;
    vector<int> PI, flows;
    flows.assign(C, 0);
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
        size_t v, cv;
        for (v = t; v != s; v = PI[v]) {
            size_t u = PI[v];
            cfp = min(cfp, Gf[u][v]);
        }
        for (v = t; v != s; v = PI[v]) {
            size_t u = PI[v];
            Gf[u][v] -= cfp;
            Gf[v][u] += cfp;
            if (v != s) cv = v;
        }
        cf += cfp;
        flows[cv] += cfp;
    }
    flows.push_back(cf);
    return flows;
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int N, C, D;
	fin >> N >> C >> D;
	// initializare graf
	for (size_t i = 0; i <= N; ++i) {
		vector<int> row;
		G.push_back(row);
		for (size_t j = 0; j <= N; ++j) {
			G[i].push_back(0);
		}
	}

	int x, y, m;
	for (int i = 0; i < D; ++i) {
		fin >> x >> y >> m;
		G[x][y] = m;
	}

    // adaugare supersursa pe pozitia N
    for (int i = 0; i < C; ++i) {
        G[N][i] = INF;
    }
    vector<int> flows = FordFulkerson(N, N - 1, C);
    fout << flows[C] << '\n';
    for (int i = 0; i < C; ++i) {
        fout << flows[i] << ' ';
    }

	fin.close();
	fout.close();
}