#include<iostream>
using namespace std;

class Base {
public:
    void fun() { cout << "Base::fun() called"; }
    void fun(int i) { cout << "Base::fun(int i) called"; }
};

class Derived : public Base {
public:
    void fun() { cout << "Derived::fun() called"; }
};

int main() {
    Derived d;
    d.fun(5);
    return 0;
}