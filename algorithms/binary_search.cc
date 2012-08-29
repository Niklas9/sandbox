
//-----------------------------------------------------------------------------
// File: binary_search.cc
// Date: 2012-08-29
//
// Description: C++ implementation of the binary search algorithm, recursive 
//              It's up to the client to sort the provided list of integers
//              in an efficient manner
//
// Time complexity: O(log n)
// Space complexity: O(1)
//-----------------------------------------------------------------------------

#include <iostream>

using namespace std;

class BinarySearch
{
  private:

    int *l;  // list array
    int len;  // length of list array

    // this is where the real magic happens,
    // returns the element position of the array, -1 if it doesn't exist
    int bs(int k, int start, int stop)
    {
        if(start < stop)
        {
            int mid = start + (stop - start) / 2;
            if(k < this->l[mid])
            {
                return this->bs(k, start, mid);
            }
            else if(k > this->l[mid])
            {
                return this->bs(k, mid+1, stop);
            }
            return mid; // yay!! return the element position
        }
        return -1; // element not found
    }

  public:

    // list feeeeeder 
    void set(int *l, int len)
    {
        this->l = l;
        this->len = len;
    }

    // if the provided value v exists in the array, pop it from the list
    bool pop(int k)
    {
        if( !this->search(k) )
        {
            return false; // couldn't find the moth* f*kr
        }
        
        return true; // done deal
    }

    // plain search for a specific key
    bool search(int k)
    {
        return this->bs(k, 0, this->len-1) != -1;
    }

};


// do some magic self-tests..
int main()
{
    cout << "testing this shit.." << endl << endl;

    int list[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                  17, 18, 19, 20};
    int length = sizeof(list) / sizeof(int);
    BinarySearch bs = BinarySearch();
    bs.set(list, length);
     
    int v = 3;
    cout << "Checking if <<" << v << ">> exists in list; " << bs.search(v) << endl;

    v = 19;
    cout << "Checking if <<" << v << ">> exists in list; " << bs.search(v) << endl;

    return 0;
}