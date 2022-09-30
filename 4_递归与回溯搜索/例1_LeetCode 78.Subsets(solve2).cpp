#include <stdio.h>

#include <vector>
class Solution {
public:
    std::vector<std::vector<int> > subsets(std::vector<int>& nums) {
    	std::vector<std::vector<int> > result;
    	int all_set = 1 << nums.size();
    	for (int i = 0; i < all_set; i++){
    		std::vector<int> item;
    		for (int j = 0; j < nums.size(); j++){
		    	if (i & (1 << j)){
	    			item.push_back(nums[j]);
	    		}
		    }
		    result.push_back(item);
	    }
        return result;
    }
};

int main(){
	std::vector<int> nums;
	nums.push_back(1);
	nums.push_back(2);
	nums.push_back(3);
	std::vector<std::vector<int> > result;
	Solution solve;
	result = solve.subsets(nums);
	for (int i = 0; i < result.size(); i++){
		if (result[i].size() == 0){
			printf("[]");
		}
		for (int j = 0; j < result[i].size(); j++){
			printf("[%d]", result[i][j]);
		}
		printf("\n");
	}
	return 0;
}
