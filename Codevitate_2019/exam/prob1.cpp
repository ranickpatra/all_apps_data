#include <iostream>

using namespace std;

int fact(int x)
{
    if (x <=0 )
    {
        return 1;
    }
    
    int f = 1;
    for (int i = 1; i <= x; i++)
    {
        f *= i;
    }

    return f;
    
}

int comb(int x, int r) {
    return fact(x) / fact(x-r) / fact(r);
}



int main()
{
    int N;
    cin >> N;
    int tmp = comb(N-1, N-2);
    tmp = tmp * tmp;
    cout << tmp;

}