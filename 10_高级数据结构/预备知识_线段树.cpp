#include <stdio.h>

#include <vector>

void build_segment_tree(std::vector<int> &value,
			std::vector<int> &nums,
		 	int pos, int left, int right){
	if (left == right){
		value[pos] = nums[left];
		return;
	}
	int mid = (left + right) / 2;
	build_segment_tree(value, nums, pos * 2 + 1, left, mid);
	build_segment_tree(value, nums, pos * 2 + 2, mid + 1, right);
	value[pos] = value[pos * 2 + 1] + value[pos * 2 + 2];
}

void print_segment_tree(std::vector<int> &value,
		int pos, int left, int right, int layer){
	for (int i = 0; i < layer; i++){
		printf("---");
	}
	printf("[%d %d][%d] : %d\n", left, right, pos, value[pos]);
	if (left == right){
		return;
	}
	int mid = (left + right) / 2;
	print_segment_tree(value, pos * 2 + 1, left, mid, layer + 1);
	print_segment_tree(value, pos * 2 + 2, mid + 1, right, layer + 1);
}

int sum_range_segment_tree(std::vector<int> &value,
						   int pos, int left, int right,
						   int qleft, int qright){
	if (qleft > right || qright < left){
		return 0;
	}
	if (qleft <= left && qright >= right){
		return value[pos];
	}
	int mid = (left + right) / 2;
	return sum_range_segment_tree(value, pos * 2 + 1, 
						left, mid, qleft, qright) +
	sum_range_segment_tree(value, pos * 2 + 2, mid + 1,
						right, qleft, qright);
}

void update_segment_tree(std::vector<int> &value,
						 int pos, int left, int right,
						 int index, int new_value){
	if (left == right && left == index){
		value[pos] = new_value;
		return;
	}
	int mid = (left + right) / 2;
	if (index <= mid){
		update_segment_tree(value, pos * 2 + 1,
						left, mid, index, new_value);
	}
	else{
		update_segment_tree(value, pos * 2 + 2, mid + 1,
						right, index, new_value);
	}
	value[pos] = value[pos * 2 + 1] + value[pos * 2 + 2];
}

int main(){
	std::vector<int> nums;
	for (int i = 0; i < 6; i++){
		nums.push_back(i);
	}
	std::vector<int> value;
	for (int i = 0; i < 24; i++){
		value.push_back(0);
	}
	build_segment_tree(value, nums, 0, 0, nums.size() - 1);
	printf("segment_tree:\n");
	print_segment_tree(value, 0, 0, nums.size() - 1, 0);	
	int sum_range = sum_range_segment_tree(
						value, 0, 0, nums.size() - 1, 2, 4);
	printf("sum_range [2, 5] = %d\n", sum_range);
	update_segment_tree(value, 0, 0, nums.size() - 1, 2, 10);
	printf("segment_tree:\n");
	print_segment_tree(value, 0, 0, nums.size() - 1, 0);
	return 0;
}
