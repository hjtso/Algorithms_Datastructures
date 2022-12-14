#include <stdio.h>
#include <vector>

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool BST_search(TreeNode *node, int value){
	while(node){
		if (node->val == value){
			return true;
		}
		if (value < node->val){
			node = node->left;
		}
		else{
			node = node->right;
		}
	}
	return false;
}

int main(){
	TreeNode a(8);
	TreeNode b(3);
	TreeNode c(10);
	TreeNode d(1);
	TreeNode e(6);
	TreeNode f(15);
	a.left = &b;
	a.right = &c;
	b.left = &d;
	b.right = &e;
	c.right = &f;
	for (int i = 0; i < 20; i++){
		if (BST_search(&a, i)){
			printf("%d is in the BST.\n", i);
		}
		else{
			printf("%d is not in the BST.\n", i);
		}
	}
	return 0;
}
