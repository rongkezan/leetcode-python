memo = {}


def get_max_length(nums, i):
    if i in memo:
        return memo[i]

    if i == len(nums) - 1:
        return 1

    max_len = 1
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            max_len = max(max_len, get_max_length(nums, j) + 1)
    memo[i] = max_len

    return max_len


def get_max_length_in_list(nums):
    return max(get_max_length(nums, i) for i in range(len(nums)))


max_length = get_max_length_in_list([1, 5, 2, 4, 3])
print(max_length)
