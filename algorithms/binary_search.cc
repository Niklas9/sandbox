
//-----------------------------------------------------------------------------
// File: binary_search.cc
// Date: 2012-08-29
//
// Description: C++ implementation of the binary search algorithm, it's
// up to the client to sort the provided list of integers in a
// efficient manner
//-----------------------------------------------------------------------------

#include <iostream>

using namespace std;

class BinarySearch
{
  private:
    int *l;  // list array
    int l_len;  // length of list array

    // this is where the real magic happens
    bool bs(int v, int n)
    {
        cout << n << endl;
        if( n > (this->l_len-1))
        {
            // upper bound reached, no no here 
            return false;
        }
        if(this->l[n] == v)
        {
            // win!!
            return true;
        }
        if(n == 0)
        {
            // lower bound reached, value is hiding somewhere else..
            return false;
        }
        else if(this->l[n] < v)
        {
            n = n + n/2;
        }
        else if(this->l[n] > v)
        {
            n = n/2;
        }
        return this->bs(v, n);

    }

  public:
    ~BinarySearch()
    {
        // need to delete this reference ??! freaks f** out
        //delete this->l;
    }
    void set_list(int *list, int list_len)
    {
        this->l = list;
        this->l_len = list_len;
    }
    // if the provided value v exists in the array, pop it from the list
    // and return it, returns -1 if it doesn't exist
    int pop(int v)
    {
        if( !this->search(v) )
        {
            return -1; // not possible, -1 should be a valid value in list
        }

        return v;
    }

    bool search(int v)
    {
        return this->bs(v, this->l_len/2);
    }

};

// do some magic self-tests..
int main()
{
    cout << "testing this shit.." << endl << endl;

    int list_len = 20;
    int list[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                  17, 18, 19, 20};
    BinarySearch bs = BinarySearch();
    bs.set_list(list, list_len);
    
    int v = 12;
    cout << "Checking if " << v << " exists in list: " << bs.search(v) << endl;

    return 0;
}
