#include <stdio.h>
struct node{
    int data;
    struct node* next;  
};
void insertatposition(int data,int posi)
{
    struct node* temp;
    struct node* newnode;
    newnode=(struct node*)malloc(sizeof(struct node));
    if(newnode == NULL){
        printf("memory allocation failed");
        return;
    }
    else{
        newnode->data=data;
        newnode->next=NULL;
        temp=head;
        for(int i=0;i<=posi-1;i++)
        {
            temp=temp->next;
            if(temp==NULL)
            {
                printf("cannot insert");
                return;
            }
            if(temp!=NULL)
            {
                newnode->next=temp->next;
                temp->next=newnode;
                printf("data inserted");
            }
        }
    }
}
int main()
{
    int posi,data;
    printf("enter the posi");
    scanf("%d",&posi);
    printf("enter the data:");
    scanf("%d",&data);
    insertatposition(data,posi);
}