#include<stdio.h>
#include<stdlib.h>
#define N 10
typedef struct llist {
    int data;
    struct llist *point;
}list;
void reverselist(list **head)
{
list *p,*q=NULL,*a=*head;
while(a)
{
    p=q;
    q=a;a=a->point;
    q->point=p;
}
*head=q;
}
void addnode(list *head,int data)
{
    list *a;
    a=head;
    while(a->point){a=a->point;}
    list *p=malloc(sizeof(list));
    p->data=data;
    p->point=NULL;
    a->point=p;
}
int deletenode(list *head,int i)
{
int k=1;
list *a=head;
while(a->point && (k++)<i-1)a=a->point;
if (k<i-1)
return 0;
else
{list *temp=a->point;
int val=temp->data;
a->point=(a->point)->point;
free(temp);
return val;
}
}

int pop(list *head)//act as pop
{
    list *a;
    a=head;
    while((a->point)->point){a=a->point;}
    int val=a->point->data;
    free(a->point);
    a->point=NULL;
    return val;
}
void display(list *head)
{
    struct llist *t=head;
    while(t){
    printf("%d ",t->data);
    t=t->point;
    }
    printf("\n");
}