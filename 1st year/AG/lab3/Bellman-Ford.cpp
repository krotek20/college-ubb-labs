#include <fstream>
#include <climits>
#include <iostream>
#include <vector>
#include <map>

#define INF INT16_MAX
#define VMAX 50005

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

Node nodes[VMAX];

class Graph {
public:
	int v = 0, e = 0;
	vector <Node*> vertiges;
	map < pair < int, int >, int > edges;
	map < int, vector <Node*> > adj;

	Graph() = default;
	Graph(const Graph& G) : v{ G.v + 1 }, e{ e + G.e + G.v }, vertiges{ G.vertiges }, edges{ G.edges }, adj{ G.adj } {
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
	int s;
	fin >> G.v >> G.e >> s;
	for (int i = 0; i < G.v; ++i) {
		nodes[i].value = i;
		G.vertiges.push_back(&nodes[i]);
	}
	for (int i = 0; i < G.e; ++i) {
		int x, y, w;
		fin >> x >> y >> w;
		G.edges[{x, y}] = w;
		//G.adj[x].push_back(&nodes[y]);
	}

	if (Bellman_Ford(G, nodes[s])) {
		for (int i = 0; i < G.v; ++i) {
			if (nodes[i].d == INF) fout << "INF ";
			else fout << nodes[i].d << " ";
		}
	}
	else fout << "Exista un ciclu negativ";

	fin.close();
	fout.close();
	return 0;
}