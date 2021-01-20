# include <bits/stdc++.h>
using namespace std;

struct list_node{
    int val;
    struct list_node * next;
}; //链表的节点

list_node * input_list(void) //读入链表
{
    int n, val;
    list_node * phead = new list_node();
    list_node * cur_pnode = phead;
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {
        scanf("%d", &val);
        if (i == 1) {
            cur_pnode->val = val;
            cur_pnode->next = NULL;
        }
        else {
            list_node * new_pnode = new list_node();
            new_pnode->val = val;
            new_pnode->next = NULL;
            cur_pnode->next = new_pnode;
            cur_pnode = new_pnode;
        }
    }
    return phead;
}

void sol(list_node * a_head, list_node * b_head)
{
    list_node* a_pointer = a_head;
    list_node* b_pointer = b_head;
    while(a_pointer && b_pointer){
        if (a_pointer->val < b_pointer->val){
            a_pointer = a_pointer->next;
        }else if(a_pointer->val > b_pointer->val){
            b_pointer = b_pointer->next;
        }else{
            cout << a_pointer->val << ' ';
            a_pointer = a_pointer->next;
            b_pointer = b_pointer->next;
        }
    }
    


}

int main ()
{
    list_node * a_head = input_list(); // A 链表的头节点
    list_node * b_head = input_list(); // B 链表的头节点
    sol(a_head, b_head);
    return 0;
}