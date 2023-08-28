/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
       ListNode* l3=new ListNode(0);
       ListNode*curr=l3;
        int carry=0,x,y;
        while(l1!=NULL || l2!=NULL ||carry!=0){
            if(l1!=NULL) x=(l1->val);
            else x=0;
            if(l2!=NULL)  y=(l2->val);
            else  y=0;
            int sum= x + y + carry;
            carry=0;
            cout<<sum<<" ";
            if(sum>=10) carry=1;
            curr->next=new ListNode(sum%10);
            
            if(l1!=NULL) l1=l1->next;
            if(l2!=NULL)l2=l2->next;
            curr=curr->next;
            
        };
        return l3->next;
        
        
    }
};