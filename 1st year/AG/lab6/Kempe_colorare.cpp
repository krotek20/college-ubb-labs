#include <fstream>
#include <iostream>
#include <algorithm>
#include <deque>
#include <vector>

#define VMAX 20

using namespace std;

vector<vector<int>> edges, copyEdges;
deque<int> kempe;
vector<int> k(VMAX, -1);

void Sterge_varf(int u) {
	while (copyEdges[u].size() > 0) {
		int varfAdj = copyEdges[u][0];
		for (int i = 0; i < copyEdges[varfAdj].size(); ++i) {
			if (copyEdges[varfAdj][i] == u) {
				copyEdges[varfAdj].erase(copyEdges[varfAdj].begin() + i);
			}
		}
		copyEdges[u].erase(copyEdges[u].begin());
	}
}

void Initialize_kempe() {
	bool ok;
	int x = 1, incx;
	do {
		ok = false;
		incx = 0;
		for (int i = 0; i < copyEdges.size(); ++i) {
			if (copyEdges[i].size() == 0) {
				if (find(kempe.begin(), kempe.end(), i) == kempe.end()) {
					kempe.push_front(i);
					ok = true;
				}
				else {
					continue;
				}
			}
			else if (copyEdges[i].size() < x) {
				Sterge_varf(i);
				kempe.push_front(i);
				ok = true;
			}
			else {
				incx++;
			}
		}
		if (!ok && incx == copyEdges.size()) {
			x++;
		}
		else if (!ok) {
			break;
		}
	} while (true);
}

int Coloreaza() {
	Initialize_kempe();

	int x = -1;
	while (!kempe.empty()) {
		int u = kempe.front();
		kempe.pop_front();
		vector<bool> colored(VMAX, false);
		for (int i = 0; i < edges[u].size(); ++i) {
			int v = edges[u][i];
			if (k[v] != -1) {
				colored[k[v]] = true;
			}
		}
		int culoare = 0;
		while (colored[culoare]) { ++culoare; }
		k[u] = culoare;
		if (x < culoare) x = culoare;
	}

	return x;
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int V, E, x, y;
	fin >> V >> E;
	for (size_t i = 0; i < V; ++i) {
		vector<int> row;
		edges.push_back(row);
		copyEdges.push_back(row);
	}

	for (int i = 0; i < E; ++i) {
		fin >> x >> y;
		edges[x].push_back(y);
		edges[y].push_back(x);
		copyEdges[x].push_back(y);
		copyEdges[y].push_back(x);
	}

	int C = Coloreaza();

	fout << C + 1 << '\n';
	for (int i = 0; i < V; ++i) {
		fout << k[i] << ' ';
	}

	fin.close();
	fout.close();
	return 0;
}