
//-----------------------------------------------------------------------------
// File: fibonacci.cc
// Date: 2012-09-17
//
// Description: tested and implemented some ideas Richard Buckland
// shared in his brilliant introductory lecture to Dynamic Porgramming,
// http://www.youtube.com/watch?v=w0SiN5bWFOc
//-----------------------------------------------------------------------------

#include <iostream>
#include <map>

using namespace std;

class Fibonacci
{
  private:
    int n;
    bool is_created;
    bool use_mem;
    static map<int, int> fm; // fibonacci memory 

  public:
    static int count;

    Fibonacci(int n, bool use_mem)
    {
        this->n = n;
        this->use_mem = use_mem;
        if(use_mem && this->fm[n])
        {
            this->is_created = true;
        }
        else
        {
            this->is_created = false;
            this->count++;
        }
    }

    int get_value()
    {
        int v;
        if(n < 2)
        {
            v = this->n;
        }
        else
        {
            if(this->is_created)
            {
                v = this->fm[n];
            }
            else
            {
                Fibonacci f1 = Fibonacci(this->n - 1, this->use_mem);
                Fibonacci f2 = Fibonacci(this->n - 2, this->use_mem);
                v = f1.get_value() + f2.get_value();
                if(this->use_mem)
                {
                    this->fm[n] = v;
                }
            }
        }
        return v;
    }

};

// init static vars
int Fibonacci::count = 0;
map<int, int> Fibonacci::fm;


int main()
{
    int n = 42;
    
    // with memory
    Fibonacci f1 = Fibonacci(n, true);
    cout << "fibonacci(" << n << ")==" << f1.get_value() << endl;
    cout << "created " << f1.count << " objects.." << endl; // n=42 => 86 objs

    cout << endl;
    // without memory, takes an aweful lot of time
    Fibonacci f2 = Fibonacci(n, false);
    cout << "fibonacci(" << n << ")==" << f2.get_value() << endl;
    cout << "created " << f2.count << " objects.." << endl; // n=42 => 866988959 objs 

    return 0;
}
