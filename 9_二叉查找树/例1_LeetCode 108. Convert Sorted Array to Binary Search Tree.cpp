#include <stdio.h>

#include <vector>
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void BST_insert(TreeNode *node, TreeNode *insert_node){
	if (insert_node->val < node->val){
		if (node->left){
			BST_insert(node->left, insert_node);
		}
		else{
			node->left = insert_node;
		}
	}
	else{
		if (node->right){
			BST_insert(node->right, insert_node);
		}
		else{
			node->right = insert_node;
		}
	}
}

void preorder_insert(const std::vector<int> &nums,
					 std::vector<TreeNode *> &node_vec,
					 int begin, int end){
	if (begin > end){
		return;
	}
	int mid = (begin + end) / 2;
	node_vec.push_back(new TreeNode(nums[mid]));
	preorder_insert(nums, node_vec, begin, mid - 1);
	preorder_insert(nums, node_vec, mid + 1, end);
}

class Solution {
public:
    TreeNode* sortedArrayToBST(std::vector<int>& nums) {
    	if (nums.size() == 0){
	    	return NULL;
	    }
    	std::vector<TreeNode *> node_vec;
    	preorder_insert(nums, node_vec, 0, nums.size() - 1);
    	for (int i = 1; i < node_vec.size(); i++){
			BST_insert(node_vec[0], node_vec[i]);
		}
		return node_vec[0];
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
	int test[] = {-10, -3, 0, 5, 9};
	std::vector<int> nums;
	for (int i = 0; i < 5; i++){
		nums.push_back(test[i]);
	}
	Solution solve;
	TreeNode *root = solve.sortedArrayToBST(nums);
	preorder_print(root, 0);
	return 0;
}

