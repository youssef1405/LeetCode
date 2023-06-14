def move_zeros(nums:list) -> None:
    slow = 0

    for fast in range(len(nums)):
        if nums[slow] == 0 and nums[fast] !=0:
            nums[fast], nums[slow] = nums[slow], nums[fast]

        if nums[slow] != 0:
            slow += 1
    print(nums)

move_zeros([0,1,0, 3, 12]) 
