/*
Acoperire de cost minim (kruskal)
Arborele de cost minim al unui graf este un subgraf care contine toate
nodurile din graful initial si un numar minim de muchii (de lungime
minima) din acesta.
*/

#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <utility>
#include <tuple>
#include <algorithm>
#include <iostream>

#define VMAX 50005

using namespace std;

class Graph {
public:
	int v, e;
	map<pair<int, int>, int> edges;
};

vector<pair <int, int> > kruskal(Graph& G, int& cost) {
	cost = 0;
	vector<pair <int, int> > a;
	vector<int> rang;
	for (int i = 0; i < G.v; i++) {
		rang.push_back(i);
	}
	vector<tuple <int, int, int> > sortedEdges;
	for (auto it : G.edges) {
		sortedEdges.push_back(make_tuple(it.first.first, it.first.second, it.second));
	}
	auto comp = [](tuple<int, int, int> t1, tuple<int, int, int> t2) {return get<2>(t1) < get<2>(t2); };
	sort(sortedEdges.begin(), sortedEdges.end(), comp);

	for (auto it : sortedEdges) {
		int u = get<0>(it);
		int v = get<1>(it);
		if (rang[u] != rang[v]) {
			cost += get<2>(it);
			a.push_back({ u,v });
			int oldRang = rang[u];
			for (int i = 0; i < rang.size(); ++i) {
				if (rang.at(i) == oldRang) {
					rang[i] = rang[v];
				}
			}
		}
	}
	return a;
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

    Graph G;
    fin >> G.v >> G.e;
    for (int i = 0; i < G.e; ++i) {
        int x, y, w;
        fin >> x >> y >> w;
		G.edges[{x, y}] = w;
    }

    int cost;
    auto v = kruskal(G, cost);
    sort(v.begin(), v.end());
    fout << cost << '\n' << v.size() << '\n';
	for (auto it : v) {
		fout << it.first << ' ' << it.second << '\n';
	}

    fout.close();
    fin.close();
    return 0;
}