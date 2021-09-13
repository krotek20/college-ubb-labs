#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <stack>

#define EMAX 501005

using namespace std;

int V, E;
list<int> adj[EMAX];		// lista de adiacenta
vector<int> path;

void find_path(int v) {
	stack<int> stiva;
	stiva.push(v);
	while (!stiva.empty()) {
		if (adj[v].size()) {
			int vn = adj[v].front();
			adj[vn].erase(std::find(adj[vn].begin(), adj[vn].end(), v));
			adj[v].pop_front();
			stiva.push(v);
			v = vn;
		}
		else {
			path.push_back(v);
			v = stiva.top();
			stiva.pop();
		}
	}
}

void add_edge(int a, int b) {
	adj[a].push_front(b);
	adj[b].push_front(a);
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
	int x, y;
	for (int i = 0; i < E; ++i) {
		fin >> x >> y;
		add_edge(x, y);
	}

	find_path(0);
	for (int i = 0; i < path.size() - 1; ++i) {
		fout << path[i] << ' ';
	}

	fin.close();
	fout.close();
	return 0;
}