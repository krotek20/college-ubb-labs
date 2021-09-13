#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <queue>

#define INF INT_MAX

using namespace std;

int V, E;
vector<vector<int>> capacitate, flux;
vector<int> h, e, adj;
queue<int> nodes_exces;

void pompare(int u, int v) {
    int d = min(e[u], capacitate[u][v] - flux[u][v]);
    flux[u][v] += d;
    flux[v][u] -= d;
    e[u] -= d;
    e[v] += d;
    if (d && e[v] == d) {
        nodes_exces.push(v);
    }
}

void inaltare(int u) {
    int d = INF;
    for (int i = 0; i < V; ++i) {
        if (capacitate[u][i] - flux[u][i] > 0) {
            d = min(d, h[i]);
        }
    }
    if (d < INF) {
        h[u] = d + 1;
    }
}

void initializare_preflux() {
    h.assign(V, 0);
    h[0] = V;

    flux.assign(V, vector<int>(V, 0));
    e.assign(V, 0);
    e[0] = INF;

    for (int i = 1; i < V; ++i) {
        pompare(0, i);
    }
    adj.assign(V, 0);
}

void descarcare(int u) {
    while (e[u] > 0) {
        if (adj[u] < V) {
            int v = adj[u];
            if (capacitate[u][v] - flux[u][v] > 0 && h[u] > h[v]) {
                pompare(u, v);
            }
            else {
                ++adj[u];
            }
        }
        else {
            inaltare(u);
            adj[u] = 0;
        }
    }
}

int pompare_preflux() {
    initializare_preflux();
    while (!nodes_exces.empty()) {
        int u = nodes_exces.front();
        nodes_exces.pop();
        if (u != 0 && u != V - 1) {
            descarcare(u);
        }
    }

    int f = 0;
    for (int i = 0; i < V; ++i) {
        f += flux[0][i];
    }
    return f;
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

    fin >> V >> E;
    for (size_t i = 0; i < V; ++i) {
        vector<int> row;
        capacitate.push_back(row);
        for (size_t j = 0; j < V; ++j) {
            capacitate[i].push_back(0);
        }
    }

    int x, y, c;
    for (int i = 0; i < E; ++i) {
        fin >> x >> y >> c;
        capacitate[x][y] = c;
    }

    fout << pompare_preflux();

    fin.close();
    fout.close();
    return 0;
}