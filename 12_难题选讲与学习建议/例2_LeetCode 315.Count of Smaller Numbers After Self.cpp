#include <stdio.h>

#include <vector>
#include <algorithm>

void segment_tree_search(std::vector<int> &tree,
	int num, int pos, int left, int right, int &count_small){
	tree[pos]++;
	if (left == right && num == left){
		return;
	}
	int mid = (left + right) / 2;
	int left_child = pos * 2 + 1;
	int right_child = pos * 2 + 2;
	if (num <= mid){
		segment_tree_search(
			tree, num, left_child, left, mid, count_small);
	}
	else{
		count_small += tree[left_child];
		segment_tree_search(
			tree, num, right_child, mid + 1, right, count_small);
	}
}

struct discrete{
	int num;
	int dis_num;
	int id;
	discrete(int _num, int _dis_num, int _id) :
		num(_num), dis_num(_dis_num), id(_id){
	}
};

bool cmp1(const discrete &a, const discrete &b){
	return a.num < b.num;
}

bool cmp2(const discrete &a, const discrete &b){
	return a.id < b.id;
}

void discrete_number(std::vector<int>& nums, std::vector<int>& dis_num){
	std::vector<discrete> temp;
	for (int i = 0; i < nums.size(); i++){
		temp.push_back(discrete(nums[i], 0, i));
	}
	std::sort(temp.begin(), temp.end(), cmp1);
	temp[0].dis_num = 1;	
	for (int i = 1; i < temp.size(); i++){
		if (temp[i].num == temp[i-1].num){
			temp[i].dis_num = temp[i-1].dis_num;
		}
		else{
			temp[i].dis_num = temp[i-1].dis_num + 1;
		}
	}
	std::sort(temp.begin(), temp.end(), cmp2);
	for (int i = 0; i < temp.size(); i++){
		dis_num.push_back(temp[i].dis_num);
	}
}

class Solution {
public:
    std::vector<int> countSmaller(std::vector<int>& nums) {
    	std::vector<int> tree;
    	std::vector<int> result;
    	std::vector<int> count;
    	std::vector<int> dis_num;    	
    	if (nums.size() == 0){
	    	return result;
	    }
    	discrete_number(nums, dis_num);
    	for (int i = 0; i < 4 * dis_num.size(); i++){
	    	tree.push_back(0);
	    }
	    for (int i = dis_num.size() - 1; i >= 0; i--){
	    	int count_small = 0;
	    	segment_tree_search(
				tree, dis_num[i], 0, 1, dis_num.size(), count_small);
	    	count.push_back(count_small);
	    }
	    for (int i = count.size() - 1; i >= 0; i--){
        	result.push_back(count[i]);
        }
        return result;
    }
};

int main(){
	int test[] = {5, -7, 9, 1, 3, 5, -2, 1};
	std::vector<int> nums;
	for (int i = 0; i < 8; i++){
		nums.push_back(test[i]);
	}
	Solution solve;
	std::vector<int> result = solve.countSmaller(nums);
	for (int i = 0; i < result.size(); i++){
		printf("[%d]", result[i]);
	}
	printf("\n");
	return 0;
}

