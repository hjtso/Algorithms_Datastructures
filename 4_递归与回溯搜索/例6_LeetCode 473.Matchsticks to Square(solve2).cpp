#include <stdio.h>

#include <vector>

class Solution {
public:
    bool makesquare(std::vector<int>& nums) {
    	if (nums.size() < 4){
	    	return false;
	    }
        int sum = 0;
        for (int i = 0; i < nums.size(); i++){
        	sum += nums[i];
        }
        if (sum % 4){
        	return false;
        }
        int target = sum / 4;        
        std::vector<int> ok_subset;
        std::vector<int> ok_half;
        int all = 1 << nums.size();
        for (int i = 0; i < all; i++){
        	int sum = 0;
        	for (int j = 0; j < nums.size(); j++) {
        		if (i & (1 << j)){
        			sum += nums[j];
	    		}
            }
            if (sum == target){
            	ok_subset.push_back(i);
            }
        }
        for (int i = 0; i < ok_subset.size(); i++){
        	for (int j = i + 1; j < ok_subset.size(); j++){
	        	if ((ok_subset[i] & ok_subset[j]) == 0){
	        		ok_half.push_back(ok_subset[i] | ok_subset[j]);
	        	}
	        }
        }
        for (int i = 0; i < ok_half.size(); i++){
        	for (int j = i + 1; j < ok_half.size(); j++){
	        	if ((ok_half[i] & ok_half[j]) == 0){
					return true;
	        	}
	        }
        }
        return false;
    }
};

int main(){
	std::vector<int> nums;
	nums.push_back(1);
	nums.push_back(1);
	nums.push_back(2);
	nums.push_back(4);
	nums.push_back(3);
	nums.push_back(2);
	nums.push_back(3);	
	Solution solve;
	printf("%d\n", solve.makesquare(nums));	
	return 0;
}
