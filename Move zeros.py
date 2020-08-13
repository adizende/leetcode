def movezeros(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
print(movezeros([14,0,1,0,3,12]))

# two pointer i and j
# I will increase i if and only if swaping nums[j] and nums[i] and will only swap when nums[j] not zero
# i=0 and j = 0      j=1 i=0 (swap)  j=1 i=1 [1,0,0,3,12]  j=2 i=1  j=3 i=2[1,3,0,0,12]  j=4 i=3[1,3,12,0,0]

