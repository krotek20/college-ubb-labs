#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<int> prufer;

vector<int> decodare_prufer() {
    int frz = 0;
    int n = prufer.size() + 1;
    vector<int> grad(n, 0);
    for (int i : prufer) ++grad[i];
    while (grad[frz] != 0) ++frz;
    int min_frz = frz;

    vector<int> arbore(n);
    for (int v : prufer) {
        arbore[min_frz] = v;
        if (--grad[v] == 0 && v < frz) {
            min_frz = v;
        }
        else {
            ++frz;
            while (grad[frz] != 0) ++frz;
            min_frz = frz;
        }
    }
    arbore[min_frz] = -1;
    return arbore;
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

	int m, x;
    fin >> m;
    for (int i = 0; i < m; ++i) {
        fin >> x;
        prufer.push_back(x);
    }
    
    vector<int> arbore{ decodare_prufer() };
    fout << arbore.size() << '\n';
    for (auto a : arbore) {
        fout << a << ' ';
    }
	return 0;
}