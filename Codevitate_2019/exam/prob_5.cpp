#include <iostream>


using namespace std;

int N[10000];
int monkey[10][10000];




    int lcm(int x, int y) {
        int greater;
        if (x > y)
            greater = x;
        else
            greater = y;

        int lcm;
        while(true) {
            if((greater % x == 0) && (greater % y == 0)){
                lcm = greater;
                break;
            }
            greater += 1;
        }

        return lcm;

    }


    int calculate_pos(int* mon, int xx) {
        int timing [N[xx]];

        for (int i=0; i< N[xx]; i++) {
            int desired = i;
            int current = i;
            int count = 0;
            while(true) {
                count += 1;
                current = mon[current] - 1;
                if (current == desired) {
                    timing[i] = count;
                    break;
                }
            }

        }

        int alist[10000];
      int gg = 0;
        for (int i = 0; i < N[xx]; i++) {
          int ff = 0;

          for (int j = 0; j < gg; j++)
          {
              if (alist[j] == timing[i])
              {
                  ff = 1;
                  break;
              }
              
          }
          
          
            if (ff == 0) {
                alist[gg] = timing[i];
              gg++;
            }
        }

        int ll = 1;
        for ( int i=0; i<gg; i++) {
            ll = lcm(ll, alist[i]);
        }

        return  ll;
    }


    int main() {

        int t;
      cin >> t;
        
        for (int i=0; i<t; i++) {
            cin >> N[i];
            
            for (int j = 0; j < N[i]; j++) {
                cin >> monkey[i][j];
            }
        }

        for (int i=0; i<t; i++){
            cout << calculate_pos(monkey[i], i) << endl;
        }

        return 0;

    }


/*

1
6
3 6 5 4 1 2


 */