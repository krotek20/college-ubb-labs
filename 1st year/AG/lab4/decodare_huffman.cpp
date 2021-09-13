#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <string>

using namespace std;

struct Node {
	int freq;
	char ch;
	Node* left, * right;
};

Node* makeLeaf(int freq, char ch, Node* left, Node* right) {
	Node* node = new Node();
	node->freq = freq;
	node->ch = ch;
	node->left = left;
	node->right = right;
	return node;
}

void decode(Node* root, int& index, string code, char& c) {
	if (root == nullptr) return;
	if (!root->left && !root->right) {
		c = root->ch;
		return;
	}
	++index;
	if (code[index] == '0')
		decode(root->left, index, code, c);
	else
		decode(root->right, index, code, c);
}

Node* getRoot(const unordered_map<char, int>& freq) {
	auto compare = [](Node* l, Node* r) { return l->freq > r->freq || (l->freq == r->freq && l->ch > r->ch); };
	priority_queue<Node*, vector<Node*>, decltype(compare)> coada(compare);

	for (auto leaf : freq) {
		coada.push(makeLeaf(leaf.second, leaf.first, nullptr, nullptr));
	}

	while (coada.size() != 1) {
		Node* left = coada.top(); coada.pop();
		Node* right = coada.top(); coada.pop();

		int sum = left->freq + right->freq;
		char ch = min(left->ch, right->ch);
		coada.push(makeLeaf(sum, ch, left, right));
	}
	Node* root = coada.top();

	return root;
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

	int n;
	char ch;
	fin >> n;
	fin.get();
	unordered_map<char, int> freq;
	for (int i = 0; i < n; ++i) {
		fin.get(ch);
		fin >> freq[ch];
		fin.get();
	}

	string code;
	getline(fin, code);

	int index = -1;
	char c;
	Node* root = getRoot(freq);
	while (index < (int)code.size() - 2) {
		decode(root, index, code, c);
		fout << c;
	}

	fin.close();
	fout.close();
	return 0;
}