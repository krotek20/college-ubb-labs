#include <exception>
#include <iostream>
#include <utility>
#include <climits>
#include <fstream>
#include <vector>
#include <queue>
#include <map>

#define INF (1<<30)
#define VMAX 10005

using namespace std;

class Node {
public:
	int value;
	int d;
	int pi;

	bool operator <(Node& n1) {
		return d < n1.d;
	}
};


class Graph {
public:
	int v = 0, e = 0;
	vector <Node*> vertiges;
	map < pair < int, int >, int > edges;
	vector < Node* > adj[VMAX];

	Graph() = default;
	Graph(const Graph& G) : v{ G.v + 1 }, e{ e + G.e + G.v }, vertiges{ G.vertiges }, edges{ G.edges }, adj{ G.adj[v] } {
		Node* s = new Node;
		s->value = G.v;
		vertiges.push_back(s);
		for (auto node : G.vertiges) {
			adj[G.v].push_back(node);
			edges[{G.v, node->value}] = 0;
		}
	}
};

void Initializare_s(Graph& G, Node& s) {
	for (auto v : G.vertiges) {
		v->d = INF;
		v->pi = -1;
	}
	s.d = 0;
}

void Relax(Node* u, Node* v, Graph& G) {
	if (v->d > u->d + G.edges[{u->value, v->value}]) {
		v->d = u->d + G.edges[{u->value, v->value}];
		v->pi = u->value;
	}
}

bool Bellman_Ford(Graph& G, Node& s) {
	Initializare_s(G, s);
	for (size_t i = 0; i < G.vertiges.size() - 1; ++i) {
		for (auto arc = G.edges.begin(); arc != G.edges.end(); ++arc) {
			Relax(G.vertiges[arc->first.first], G.vertiges[arc->first.second], G);
		}
	}

	for (auto arc = G.edges.begin(); arc != G.edges.end(); ++arc) {
		if (G.vertiges[arc->first.second]->d > G.vertiges[arc->first.first]->d + arc->second) {
			return false;
		}
	}
	return true;
}

void Dijkstra(Graph& G, Node& s) {
	Initializare_s(G, s);
	auto compare = [](Node* n1, Node* n2) {return n1->d > n2->d; };
	priority_queue<Node*, vector <Node*>, decltype(compare)> q(compare);
	vector <bool> visited;
	for (int i = 0; i < G.v; ++i) {
		visited.push_back(false);
	}
	q.push(&s);
	while (!q.empty()) {
		Node* u = q.top();
		q.pop();
		visited[u->value] = false;
		for (auto v : G.adj[u->value]) {
			int oldDistance = v->d;
			Relax(u, v, G);
			if (oldDistance != v->d && visited[v->value] == false) {
				q.push(v);
				visited[v->value] = true;
			}
		}
	}
}

vector < vector < int > > Johnson(Graph& G) {
	Graph Gprim(G);
	Node* s = Gprim.vertiges[Gprim.v - 1];
	if (Bellman_Ford(Gprim, *s) == false) {
		throw exception("Exista circuit cu cost negativ!");
	}
	int h[VMAX];
	for (auto v : Gprim.vertiges) {
		h[v->value] = v->d;
	}
	for (auto it = G.edges.begin(); it != G.edges.end(); ++it) {
		it->second = it->second + h[it->first.first] - h[it->first.second];
	}
	delete s;
	vector < vector < int > > d;
	for (auto u : G.vertiges) {
		Dijkstra(G, *u);
		vector < int > aux;
		for (auto v : G.vertiges) {
			if (G.vertiges[v->value]->d != INF) {
				aux.push_back(G.vertiges[v->value]->d - h[u->value] + h[v->value]);
			}
			else {
				aux.push_back(G.vertiges[v->value]->d);
			}
		}
		d.push_back(aux);
	}
	return d;
}

int main(int argc, char* argv[]) {
	if (argc != 3) {
		cout << "Usage: " << argv[0] << " file_input file_output";
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
	Node nodes[VMAX];
	for (int i = 0; i < G.v; ++i) {
		nodes[i].value = i;
		G.vertiges.push_back(&nodes[i]);
	}

	for (int i = 0; i < G.e; ++i) {
		int x, y, w;
		fin >> x >> y >> w;
		G.edges[make_pair(x, y)] = w;
		G.adj[x].push_back(&nodes[y]);
	}

	vector < vector < int > > d;
	try {
		d = Johnson(G);
	}
	catch (exception&) {
		fout << -1;
		fout.close();
		fin.close();
		return 0;
	}

	for (auto it = G.edges.begin(); it != G.edges.end(); ++it) {
		fout << it->first.first << ' ' << it->first.second << ' ' << it->second << "\n";
	}

	for (int i = 0; i < d.size(); ++i) {
		for (int j = 0; j < d[i].size(); ++j) {
			if (d[i][j] != INF) {
				fout << d[i][j] << ' ';
			}
			else {
				fout << "INF ";
			}
		}
		fout << '\n';
	}

	fout.close();
	fin.close();
	return 0;
}