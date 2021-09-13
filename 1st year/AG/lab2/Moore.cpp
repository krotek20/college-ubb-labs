#include <fstream>
#include <vector>
#include <queue>

#define NMAX 5001
#define VMAX 1001
#define INF (1<<30)

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

void read_graph(vector < int > g[], int e) {
	int x, y;
	for (int i = 0; i < e; ++i) {
		fin >> x >> y;
		g[x].push_back(y);
	}
}

void moore(vector < int > g[], int v, int u, int l[], int p[]) {
	queue <int> q;
	for (int i = 0; i < v; ++i) {
		p[i] = -1;
		l[i] = INF;
	}
	l[u] = 0;
	q.push(u);
	while (!q.empty()) {
		int node = q.front();
		for (int i = 0; i < g[node].size(); ++i) {
			int neighbor = g[node][i];
			if (l[neighbor] == INF) {
				l[neighbor] = l[node] + 1;
				p[neighbor] = node;
				q.push(neighbor);
			}
		}
		q.pop();
	}
}

void print_path(int node, int p[]) {
	if (p[node] != -1)	{
		print_path(p[node], p);
	}
	fout << node << ' ';
}

void print_moore(int v, int p[], int l[]) {
	for (int i = 0; i < v; ++i) {
		if (l[i] != INF) {
			fout << l[i] + 1 << ' ';
			print_path(i, p);
			fout << '\n';
		}
	}
}

int main() {
	vector < int > Muchii[NMAX];
	int n, m, s, l[VMAX], p[VMAX];
	fin >> n >> m >> s;

	read_graph(Muchii, m);

	moore(Muchii, n, s, l, p);
	print_moore(n, p, l);
	return 0;
}