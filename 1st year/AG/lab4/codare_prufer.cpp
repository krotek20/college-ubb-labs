#include <iostream>
#include <fstream>
#include <vector>

#define VMAX 100005

using namespace std;

vector<int> adj[VMAX];
vector<int> parinte;

vector<int> codare_prufer(int n) {
    int frz = -1;
    vector<int> grad(n);
    for (int i = 0; i < n; ++i) {
        grad[i] = adj[i].size();
        if (grad[i] == 0 && frz == -1)
            frz = i; // frunza minima
    }
    vector<int> prufer(n - 1);
    int min_frz = frz;
    for (int i = 0; i < n - 1; ++i) {
        int pi = parinte[min_frz];
        prufer[i] = pi;
        if (--grad[pi] == 0 && pi < frz) {
            min_frz = pi;
        }
        else {
            ++frz;
            while (grad[frz] != 0) ++frz;
            min_frz = frz;
        }
    }
    return prufer;
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

    int n, x;
    fin >> n;
    for (int i = 0; i < n; ++i) {
        fin >> x;
        if (x != -1) {
            adj[x].push_back(i);
        }
        parinte.push_back(x);
    }
    vector<int> prufer = codare_prufer(n);
    fout << prufer.size() << '\n';
    for (int i : prufer) {
        fout << i << ' ';
    }
	return 0;
}