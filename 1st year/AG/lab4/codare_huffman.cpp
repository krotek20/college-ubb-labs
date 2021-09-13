#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <unordered_map>
#include <vector>

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

void encode(Node* root, string code, unordered_map<char, string>& charCodes) {
	if (root == nullptr)
		return;
	if (!root->left && !root->right) {
		charCodes[root->ch] = code;
	}
	encode(root->left, code + "0", charCodes);
	encode(root->right, code + "1", charCodes);
}

unordered_map<char, string> Huffman(const unordered_map<char, int>& freq) {
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

	unordered_map<char, string> charCodes;
	encode(root, "", charCodes);

	return charCodes;
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

	string text;
	getline(fin, text);

	unordered_map<char, int> freq;
	for (char ch : text) ++freq[ch];

	fout << freq.size() << '\n';
	vector<pair<char, int>> freqForSort(freq.begin(), freq.end());
	sort(freqForSort.begin(), freqForSort.end());
	for (auto fr : freqForSort) {
		fout << fr.first << ' ' << fr.second << '\n';
	}

	unordered_map<char, string> charCodes{ Huffman(freq) };

	string finalCode = "";
	for (char ch : text) {
		finalCode += charCodes[ch];
	}
	fout << finalCode;

	fin.close();
	fout.close();
	return 0;
}