#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <cstring>
#include <iomanip>

#define VMAX 5001

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

vector <int> Muchii[VMAX];
queue <int> coada;
int dist[VMAX];

void BFS(int s) {
	int nod;
	coada.push(s);
	while (!coada.empty()) {
		nod = coada.front();
		coada.pop();
		for (unsigned i = 0; i < Muchii[nod].size(); ++i) {
			if (dist[Muchii[nod][i]] == 0) {
				coada.push(Muchii[nod][i]);
				dist[Muchii[nod][i]] = 1;
			}
		}
	}
}

void afisare(int n, int v) {
	for (int i = 0; i < n; ++i) {
		if (v == i) dist[i] = 1;
		fout << dist[i] << ' ';
		dist[i] = 0;
	}
	fout << '\n';
}

int main() {
	int n, m, x, y;
	fin >> n >> m;
	for (int i = 1; i <= m; ++i) {
		fin >> x >> y;
		Muchii[x].push_back(y);
	}
	for (int v = 0; v < n; ++v) {
		BFS(v);
		afisare(n, v);
	}

	return 0;
}