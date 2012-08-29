
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

    // removes a specified element from list
    void remove(int p)
    {
        // move every element above p one step down
        for( int i = p; i < this->len; i++)
        {
            this->l[i] = this->l[i+1];
        }
        // decrease total length by 1
        this->len = this->len -1;
    }

  public:

    // list feeeeeder 
    void set(int *l, int len)
    {
        this->l = l;
        this->len = len;
    }

    // if the provided key v exists in the list, pop it baby!
    bool pop(int k)
    {
        int p = this->bs(k, 0, this->len); // key position
        if( p != -1 )
        {
            this->remove(p);
            return true; // done deal
        }
        return false; // couldn't find the moth* f*ckr
    }

    // plain search for a specific key
    bool search(int k)
    {
        return this->bs(k, 0, this->len) != -1;
    }

};


// do some magic self-tests..
int main()
{
    cout << "testing this shit.." << endl << endl;

    int list[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                  17, 18, 19, 20};
    int length = sizeof(list) / sizeof(int);
    BinarySearch bs = BinarySearch();
    bs.set(list, length);
     
    int v = 3;
    cout << "Checking if <<" << v << ">> exists in list; " << bs.pop(v) << endl;

    v = 20;
    cout << "Checking if <<" << v << ">> exists in list; " << bs.search(v) << endl;

    return 0;
}
