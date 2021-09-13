#include <iostream>
#include <vector>
#include <iterator>
#include <iostream>

template <typename TElem>
class grades /*: public std::vector<TElem>*/ {
private:
    std::vector <TElem> arr;
public:
    grades() = default;
    grades operator +(TElem t) {
        this->arr.push_back(t);
        return *this;
    }

    int getNRGrages() const {
        return this->arr.size();
    }
    
    class iterator {
    private:
        int poz = 0;
        const grades& gr;
    public:

        iterator(const grades& gr, int poz) : gr{ gr }, poz{ poz } {};

        bool operator != (iterator it) {
            return this->poz != it.poz;
        }

        TElem operator * () {
            return this->gr.arr[poz];
        }

        void operator ++() {
            this->poz++;
        }
    };

    iterator begin() {
        return iterator(*this, 0);
    }

    iterator end() {
        return iterator(*this, this->arr.size());
    }
};

int oldMain() {
    grades<int> myg;
    myg = myg + 10; // adaugam nota 10 la OOP
    myg = myg + 9; //adaugam nota 9 la FP
    double avg = 0.0;
    for (auto g : myg) { //iteram toate notele
        avg += g;
    }
    return avg / myg.getNRGrages();//compute average
}