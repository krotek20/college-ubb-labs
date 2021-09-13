#include <random>
#include <string>
#include <iostream>

#define true (rand() % 100 > 98)

class Channel {
public:
	virtual void send(std::string msg) = 0;
};

class Telefon : public Channel {
private:
	int nrTel;
public:
	virtual void send(std::string msg) override {
		std::cout << "dial: " << nrTel << '\n';
		if (true)
			throw std::exception();
	}
};

class SMS : public Telefon {
public:
	void send(std::string msg) override {
		Telefon::send(msg);
		std::cout << "sending sms\n";
	}
};

class Fax : public Telefon {
public:
	void send(std::string msg) override {
		Telefon::send(msg);
		std::cout << "sending fax\n";
	}
};

class FailOver : public Channel {
private:
	std::unique_ptr<Channel> channel1;
	std::unique_ptr<Channel> channel2;
public:

	FailOver(std::unique_ptr<Channel> c1, std::unique_ptr<Channel> c2) {
		channel1 = std::move(c1);
		channel2 = std::move(c2);
	}

	void send(std::string msg) override {
		try {
			channel1->send(msg);
		}
		catch (std::exception) {
			try {
				channel2->send(msg);
			}
			catch (std::exception) {
				std::cout << "Failed\n";
			}
		}
	}
};

class Contact {
private:
	std::vector <std::unique_ptr <Channel> > channels;
public:
	void sendAlarm(std::string msg) {
		bool send = false;
		while (!send) {
			for (int i = 0; i < 3 && !send; i++)
				try {
					channels[i]->send(msg);
					send = !send;
				}
				catch (std::exception) {
					continue;
				}
		}
	}

	static Contact generateContact() {
		Contact c;
		c.channels.push_back(std::make_unique<Telefon>());
		c.channels.push_back(std::make_unique<FailOver>(std::make_unique<Telefon>(), std::make_unique<SMS>()));
		c.channels.push_back(std::make_unique<FailOver>(std::make_unique<Telefon>(), std::make_unique<FailOver>(std::make_unique<Fax>(), std::make_unique<SMS>())));
		return c;
	}
};

int main4() {
	Contact c = Contact::generateContact();
	return 0;
}