#include <iostream>
#include <vector>

class Greetable {
public:
    virtual void greet() const = 0;
};

class Person : public Greetable {
private:
    std::string name;

public:
    Person(const std::string& name) : name(name) {}

    void greet() const override {
        std::cout << "Hello, " << name << "!" << std::endl;
    }
};

int main() {
    Greetable* person = new Person("Alice");
    person->greet();

    std::vector<int> numbers = {1, 2, 3};
    for(int n : numbers) {
        std::cout << "Number: " << n << std::endl;
    }

    delete person;
    return 0;
}
