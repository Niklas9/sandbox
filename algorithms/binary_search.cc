
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
#include <cassert>
#include <cstdlib>
#include <ctime>

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
        for(int i = p; i < this->len; i++)
        {
            this->l[i] = this->l[i+1];
        }
        // decrease total length by 1
        this->len -= 1;
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
        if(p != -1)
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
// -- should try some unit test framework instead some day
unsigned int get_rand_int(int low, int high)
{
    return (rand() % (high - low +1)) + low;
}

int *random_list(int size)
{
    int start = get_rand_int(-10000, 10000);
    int diff = 0;
    int *list = new int[size];
    for(int i = 0; i < size; i++)
    {
        list[i] = start + diff;
        start = list[i];
        diff = get_rand_int(-999, 999);
        if(diff < 0)
        {
            diff = -diff; // make sure it's sorted
        }
        if(diff == 0)
        {
            diff += 1; // can end up with non-unique values if not
        }
    }
    return list;
}

int main()
{
    cout << "testing this shit.." << endl;
 
    int test_times = 1000000;
    BinarySearch bs = BinarySearch();
    //assert(bs.search(v)==false);
    srand(time(0));
 
    for(int i = 0; i < test_times; i++)
    {
        int len = get_rand_int(1, 100);
        int *list = random_list(len);
        bs.set(list, len);
        // test searching
        for(int j = 0; j < len; j++)
        {
            assert(bs.search(list[j])==true);
        }
         
        // test searching for invalid values
        assert(bs.search(list[len-1]+1)==false);
        // test popping
        int v = list[len/2];
        assert(bs.pop(v)==true); // pop it
        assert(bs.search(v)==false); // make sure it's not there
    }

    return 0;
}
