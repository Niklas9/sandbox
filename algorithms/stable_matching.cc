
//-----------------------------------------------------------------------------
// File: stable_matching.cc
// Date: 2012-07-26
//
// Description: Basic program to simulate Stable Matching Problems.
//-----------------------------------------------------------------------------

#include <iostream>
#include <string>
#include <map>

using namespace std;


int main()
{
    string w[] = {"w1", "w2"};
    string m[] = {"m1", "m2"};
    map<string, string> p;  // prefers
    map<string, string> match;  // matched couples
    p[m[0]] = w[0];
    p[m[1]] = w[1];
    p[w[0]] = m[1];
    p[w[1]] = m[0];


    cout << "Wishlist looks like this:" << endl;
    for(map<string, string>::iterator ii=p.begin(); ii != p.end(); ii++)
    {
        cout << "|\t" << (*ii).first << " => " << (*ii).second << endl;
    }

   
    int w_len = sizeof(w) / sizeof(w[0]);
    int m_len = sizeof(m) / sizeof(m[0]);
    for(int i = 0; i < w_len; i++)
    {
        cout << w[i] << endl;
    }

    return 0;
}
