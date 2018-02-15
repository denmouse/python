def twoSum(nums, target):
	for i in range(len(nums)):
		rest = target - nums[i]
		if rest in nums[i+1:]:
			return [i, nums.index(rest)]
nums = [1, 3, 5, 9, 12, 9, 2]
outlist = twoSum(nums,15)
print outlist

			
