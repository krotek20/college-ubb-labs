#include <vector>

#define calcul(t) (t)

using std::vector;

class Point {
public:
	int x, y;
	Point(int x, int y) : x{ x }, y{ y } {};
};

int function(const vector<Point>& points) {
	Point aux { 0, 0 };
	for (const auto& p : points) {
		aux.x += calcul(p.x);
		aux.y += calcul(p.y);
	}
	if (aux.x > 10 || aux.y > 10) {
		return -1;
	}
	const int rez = aux.x + aux.y;
	return rez;
}