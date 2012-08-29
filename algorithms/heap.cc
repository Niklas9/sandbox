
//-----------------------------------------------------------------------------
// File: heap.cc
// Date: 2012-08-28
//
// Description: C++ implementation of the Heap data structure
//-----------------------------------------------------------------------------

#include <iostream>

using namespace std;

// TODO(nandersson):
// * be able to choose if it's supposed to be a max or min heap in the
//   constructor?
// * client should be able to pass an integer array to the constructor,
//   so we don't end up having to call insert method for init purposes 
// * dynamic heap array of ints? or should it be maxed at 1000? NULL for
//   not used columns? can it self grow in some efficient manner?
//

class Heap
{
  private:
    int heap[3]; // defined in constructor?
    bool is_min;

  public:
    Heap(bool is_min)
    {
        this->is_min = is_min;
    }
   
    ~Heap()
    {
    //    delete this->heap;
    }

    // debug printer of the whole heap stack
    void dprint()
    {
        cout << "{";
        for(int i = 0; i < this->length(); i++)
        {
            cout << this->heap[i];
            if( (i+1) != this->length() )
            {
                cout << ", ";
            }
        }
        cout << "}\n";
    }

    int pop()
    {
        int v = this->heap[0];
        // remove heap[0] and move everything 1 up 
        return v;
    }

    bool insert(int v) // how do we handle duplicates??!
    {
        // add v to heap
        for(int i = 0; i < this->length(); i++)
        {
            if(this->heap[i] > v)
            {
                this->heap[i] = v;
            }
        }
        return true; // false if not successful
    }

    bool remove(int v)
    {
        // delete from heap
        return true; // false if not successful 
    }

    int length()
    {
        return sizeof(heap) / sizeof(int);
    }
};


// test this stuff..
int main()
{
    cout << "Heap BEAP!" << endl << endl;

    Heap h = Heap(true);
    h.insert(1);
    h.insert(2);
    h.insert(3);
    h.dprint();
    cout << h.pop() << endl;
    h.dprint();
}

