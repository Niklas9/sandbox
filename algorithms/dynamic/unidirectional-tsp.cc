
//-----------------------------------------------------------------------------
// File: unidirectional-tsp.cc
// Date: 2012-09-21
//
// Description: TBD 
//-----------------------------------------------------------------------------

#include <iostream>
#include <cstdlib>

using namespace std;


class Input
{
  public:
    int *v;

    Input(int m, int n)
    {
        this->v = new int[m*n];
    }

    void print_matrix(int m, int n, int *M)
    {
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                cout << "M[" << i << ", " << j << "] = " << M[i, j] << " ";
            }

            cout << endl;
        }
    }

    string get_int(string M, int i)
    {
        int pos = M.find(" ");

        if(pos != -1)
        {
            this->v[i] = atoi(M.substr(0, pos).c_str());
            M = M.substr(pos+1, M.length());
            i++;
            return get_int(M, i);
        }
        else
        {
            this->v[i] = atoi(M.c_str());
            return "";
        }
    }

};


int main()
{
    cout << "Input m, n and matrix:" << endl;

    int m = 0, n = 0;
    cin >> m;
    cin >> n;

    // stupid thing to cause new line in input
    string tmp;
    getline(cin, tmp);

    string M_str;
    getline(cin, M_str);

    Input input = Input(m, n);

    int *M = new int[m, n]; // values on matrix form
    
    input.get_int(M_str, 0);

    int count = 0;
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cout << "M[" << i << ", " << j << "] == v[" << count << "]==" << input.v[count] << endl;
            M[i, j] = input.v[count];
            cout << M[i, j] << endl;

            count++;
        }
    }

    //input.print_matrix(m, n, M);

    cout << M[0, 0] << endl;
    cout << M[0, 1] << endl;
    cout << M[1, 0] << endl;
    cout << M[1, 1] << endl;

    return 0;
}
