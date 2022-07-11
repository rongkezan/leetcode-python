def length_of_lis(nums):
    n = len(nums)  # n = 5
    l = [1] * n  # [1, 1, 1, 1, 1]

    for i in reversed(range(n)):  # i -> 4,3,2,1,0
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                l[i] = max(l[i], l[j] + 1)
    return max(l)


max_length = length_of_lis([1, 5, 2, 4, 3])
print(max_length)