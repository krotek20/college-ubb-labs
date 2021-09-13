#pragma once
#include <vector>
#include <algorithm>

class Observable {
public:
	virtual void signal() = 0;

	virtual ~Observable() = default;
};

class Observer {
private:
	std::vector <Observable*> obs;
public:
	void addObservable(Observable* obs) {
		this->obs.push_back(obs);
	}

	void removeObservable(Observable* obs) {
		auto it = std::find(this->obs.begin(), this->obs.end(), obs);
		if (it == this->obs.end())
			return;
		this->obs.erase(it);
	}

	void signal() {
		for (auto it : this->obs)
			it->signal();
	}
};