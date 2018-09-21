#include <stdio.h>
#include <stdlib.h>

typedef struct LIST
{
  int data;
  struct LIST *next;
} LIST;

LIST *start = NULL;


void insert(int d)
{
  LIST * temp;
  if(start == NULL)
  {
    start = (LIST *) malloc(sizeof(LIST));
    start->data = d;
    start->next = NULL;
    return;
  }

  temp = start;

  while(temp->next != NULL)
  {
    temp = temp->next;
  }

  temp->next = (LIST *) malloc(sizeof(LIST));
  temp = temp->next;
  temp->data = d;
  temp->next = NULL;
  //temp->next->data = d;
  //temp->next->next = NULL;

}

void show()
{
  LIST *t;
  t = start;

  while (t != NULL) {
    printf("%d\n", t->data);
    t = t->next;
  }
}


int main()
{

  int n, i, d;

  printf("How many: ");
  scanf("%d", &n);

  for (i = 0; i < n; i++)
  {
    printf("Enter %d: ", i);
    scanf("%d", &d);
    insert(d);
  }

  show();


  return 0;
}
