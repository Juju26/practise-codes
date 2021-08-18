'''
#class Solution:
#def findPeakElement(self, nums: List[int]) -> int:

            
Input:
[6,5,4,3,2,3,2]
Output:
3
Expected:
0


Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where t


nums=[1,2,4,3,5]
c=0
l=0
if len(nums)==2:
    c=nums.index(max(c,nums[1]))
    
elif len(nums)==1:
    c=nums.index(nums[0])
    
else:
    for i in range(1,len(nums)-1):
        if  nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            c=nums.index(nums[i]) 
            
        else:
            print(c) 
'''
def fn(nums):
    n=len(nums)
    if n==1:
        return 0
    elif (nums[0]>=nums[1]):
        return 0
    elif (nums[n-1]>=nums[n-2]):
        return n-1 
    else:
        for i in range(1,n-1):
            if (nums[i]>=nums[i-1] and nums[i]>=nums[i+1]):
                return i
nums=[1,3,2,5,3]
p=fn(nums)
print(p)