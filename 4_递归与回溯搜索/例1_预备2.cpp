#include <stdio.h>
#include <vector>

void generate(int i, std::vector<int>& nums,
              std::vector<int> &item,
              std::vector<std::vector<int> > &result){
	if (i >= nums.size()){
		return;
	}
	item.push_back(nums[i]);
	result.push_back(item);
	generate(i + 1, nums, item, result);
}

int main(){
	std::vector<int> nums;
	nums.push_back(1);
	nums.push_back(2);
	nums.push_back(3);
	
	std::vector<int> item;
	std::vector<std::vector<int> > result;
	generate(0, nums, item, result);
	
	for (int i = 0; i < result.size(); i++){
		for (int j = 0; j < result[i].size(); j++){
			printf("[%d]", result[i][j]);
		}
		printf("\n");
	}
	return 0;
} 
