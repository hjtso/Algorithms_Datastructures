#include <stdio.h>

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

void print_list(ListNode *head, const char *list_name){
	printf("%s :", list_name);
	if (!head){
		printf("NULL\n");
		return;
	}
	while(head){
		printf("[%d] ", head->val);
		head = head->next;
	}
	printf("\n");
}

int main(){
	ListNode a(1);
	ListNode b(2);
	ListNode c(3);
	ListNode d(4);
	ListNode e(5);
	a.next = &b;
	b.next = &c;
	c.next = &d;
	d.next = &e;
	
	ListNode *head = &a;
	ListNode *new_head = NULL;
	ListNode *next = NULL;
	print_list(head, "old");
	print_list(new_head, "new");
	
	for (int i = 0; i < 5; i++){
		next = head->next;
		head->next = new_head;
		new_head = head;
		head = next;
		print_list(head, "old");
		print_list(new_head, "new");
	}
	return 0;
}

