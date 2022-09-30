#include <stdio.h>

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* BST_search(TreeNode *node, int value, TreeNode *&parent){
	while(node){
		if (node->val == value){
			break;
		}
		parent = node;
		if (value < node->val){
			node = node->left;
		}
		else{
			node = node->right;
		}
	}
	return node;
}

void delete_node(TreeNode *parent, TreeNode *node){
	if (node->val < parent->val){
		if (node->left && !node->right){
			parent->left = node->left;
		}
		else if (!node->left && node->right){
			parent->left = node->right;
		}
		else{
			parent->left = NULL;
		}
	}
	else if(node->val > parent->val){
		if (node->left && !node->right){
			parent->right = node->left;
		}
		else if (!node->left && node->right){
			parent->right = node->right;
		}
		else{
			parent->right = NULL;
		}
	}
}

TreeNode* find_successor(TreeNode *node, TreeNode *&parent){
	parent = node;
	TreeNode *ptr = node->right;
	while(ptr->left){
		parent = ptr;
		ptr = ptr->left;
	}
	return ptr;
}

class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
    	TreeNode *parent = NULL;
    	TreeNode *node = BST_search(root, key, parent);
		if (!node){
			return root;
		}
        if (node->left && node->right){
        	TreeNode *successor = find_successor(node, parent);
        	delete_node(parent, successor);
        	node->val = successor->val;
        	return root;
        }
        if (parent){
       		delete_node(parent, node);
       		return root;
        }
       	if (node->left){
       		root = node->left;
        }
        else{
       		root = node->right;
        }
        return root;
    }
};

void preorder_print(TreeNode *node,int layer){
	if (!node){
		return;
	}
	for (int i = 0; i < layer; i++){
		printf("-----");
	}
	printf("[%d]\n", node->val);
	preorder_print(node->left, layer + 1);
	preorder_print(node->right, layer + 1);
}

int main(){
	for (int i = 1; i <= 7; i++){
		printf("key = %d\n", i);
		TreeNode a(5);
		TreeNode b(3);
		TreeNode c(6);
		TreeNode d(2);
		TreeNode e(4);
		TreeNode f(7);
		a.left = &b;
		a.right = &c;
		b.left = &d;
		b.right = &e;
		c.right = &f;
		Solution solve;
		TreeNode *root = solve.deleteNode(&a, i);
		preorder_print(root, 0);
		printf("\n");
	}
	return 0;
}

