class Segment_Tree(object):
    def add(self,start,end,llist):
        self.start = start
        self.end = end
        self.middle = (start+end)/2
        self.num = 0

        if self.start + 1 == self.end:
            self.num = llist[self.start]
            return self.num
        else:
            left = Segment_Tree()
            self.left = left
            self.num += left.add(start,self.middle,llist)

            right = Segment_Tree()
            self.right = right
            self.num += right.add(self.middle,end,llist)

            return self.num

    def update(self,index,num):
        if self.start == index and self.start + 1 == self.end:
            cha = num - self.num
            self.num = num
            return cha

        if index >= self.middle:
            cha = self.right.update(index,num)
            self.num += cha
            return cha
        else:
            cha = self.left.update(index,num)
            self.num += cha
            return cha

    def sum(self,start,end):
        if start == self.start and end == self.end:
            return self.num


        if end <= self.middle:
            return self.left.sum(start,end)
        elif start>= self.middle:
            return self.right.sum(start,end)
        else:
            left_val = self.left.sum(start,self.middle)
            right_val = self.right.sum(self.middle,end)

            return left_val + right_val


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """

        if len(nums) == 0:
            nums.append(0)

        self.nums = nums
        self.st = Segment_Tree()
        self.st.add(0,len(self.nums),self.nums)



    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.st.update(i,val)
        return val


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.st.sum(i,j+1)

# https://blog.csdn.net/wds2006sdo/article/details/51951693