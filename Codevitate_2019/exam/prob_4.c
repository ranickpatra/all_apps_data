#include <stdio.h>
int n = 6;
void sort(int x[])
{
    int i, j, t;
    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (x[j] < x[j + 1])
            {
                t = x[j];
                x[j] = x[j + 1];
                x[j + 1] = t;
            }
        }
    }
}
int main()
{
    //int x[] = {16, 5, 21, 6, 10, 12};
    int x[] = {1,2, 3, 4, 5, 10, 11, 3, 6, 16};

    int i, s = 0, avg, st1 = 0, st2 = 0, avg1, j, flag;

    //for(i=0; i<)

    for (i = 0; i < n; i++)
        s = s + x[i];
    if (avg % 2 == 0)
        avg = s / 2;
    else
        avg = s / 2 + 1;
    sort(x);
    // for (i = 0; i < n; i++)
    // {
    //     // printf("%d  ", x[i]);
    // }
    st1 = x[0];

    //while(1)
    //{
    st1 = x[0];
    avg1 = avg - x[0];
    for (i = 1; i < n;)
    {
        if (x[i] <= avg1)
        {
            st1 = st1 + x[i];
            avg1 = avg1 - x[i];
            //printf("%d   %d\n", st1, avg1);
            flag = 0;
            for (j = i + 1; j < n; j++)
            {
                if (avg1 > x[j])
                {
                    flag = 1;
                    i = j;
                    break;
                }
            }
            if (flag == 0 && i != n - 1)
            {
                st1 = st1 - x[i];
                avg1 = avg1 + x[i];
                i++;
            }
        }
        else
        {
            st2 = st2 + x[i];
            i++;
        }
    }
    printf("%d", s - st1);
    if (s - st1 > st1)
        printf("% d", s - st1);
    else
        printf("% d", st1);
    
    return 0;
}