def summaryRanges(nums):
    if not len(nums):
        return list()
    ret = list()
    start, end = nums[0], nums[0]
    
    for i in range(1, len(nums)):
        if nums[i]-1 == nums[i-1]:
            end = nums[i]
        else:
            if start != end:
                ret.append(f"{start}->{end}")
            else:
                ret.append(str(start))
            start, end = nums[i], nums[i]
            
    if start != end:
        ret.append(f"{start}->{end}")
    else:
        ret.append(str(start))
    return ret
    
nums = [0,1,2,4,5,7]
print(summaryRanges(nums))
# Output: ['0->2', '4->5', '7']
