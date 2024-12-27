#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* next;
};

struct stack{
    struct node* top;
};

struct stack* create(){
    struct stack* stk=(struct stack*)malloc(sizeof(struct stack));
    stk->top=NULL;
    return stk; 
}
int isEmpty(struct stack* stk) {
 return (stk->top == NULL);
}
void push(struct stack* stk, int data)
{
    struct node* newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=data;
    newnode->next=stk->top;
    stk->top=newnode;
    printf("pushed");
}
int pop(struct stack* stk)
{
    if(isEmpty(stk)){
        printf("stack empty");
    }
    else{
        struct node* temp=stk->top;
        int poppeddata=temp->data;
        stk->top=temp->next;
        free(temp);
        return poppeddata;
    }
}
int main()
{
    struct stack* stk=create();
    push(stk,10);
    push(stk,20);
    push(stk,30);

    printf("popped element:%d",pop(stk));
    printf("popped element:%d",pop(stk));
    printf("popped element:%d",pop(stk));
    printf("popped element:%d",pop(stk));
}


