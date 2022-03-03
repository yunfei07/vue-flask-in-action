def word_break(s, word_list):
    """
    输入:
    s = "catsanddog"
    s1 = "catsandog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    输出:
    ["cats and dog","cat sand dog"]
    []
    """

    if not s:
        return True
    lenth = len(s)
    dp = [False for i in range(lenth + 1)]
    dp[0] = True
    for i in range(1, lenth + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_list:
                dp[i] = True
                break
    return dp[-1]


def find_string(string):
    for x in range(1, len(string)):
        substring = string[:x]

        if substring * (len(string) // len(substring)) + (substring[:len(string) % len(substring)]) == string:
            print(substring)


def remove_duplicates(nums):
    return list(set(nums))


def rotate(nums, k):
    """
    输入: nums = [1,2,3,4,5,6,7], k = 3
    输出: [5,6,7,1,2,3,4]
    """

    for i in range(k):
        print(i)
        nums.insert(i, nums.pop(i + k + 1))
    print(nums)


def is_duplicate(nums):
    is_flag = False
    for i in nums:
        if nums.count(i) > 1:
            is_flag = True
            break
    return is_flag


def intersect(nums1, nums2):
    arr = []
    for i in range(len(nums2) - 1):
        if nums2[i] == nums1[i]:
            arr.append(i)


def plusone(digits):
    return digits.append(digits.pop() + 1)


def move_zeroes(nums):
    for i in range(nums.count(0)):
        nums.append(nums.pop(nums.index(0)))
    return nums


def tow_sum(nums, target):
    if len(nums) < 2:
        return None
    else:
        low = 0
        while low <= len(nums):
            for i in range(len(nums) - 1):
                if nums[low] + nums[i + 1] == target:
                    return [low, i + 1]
            low += 1


def reverse_string(s):
    arr = []
    for i in range(len(s)):
        arr.append(s.pop())
    return arr


def first_uniq_char(s):
    low = 0
    while low <= len(s):
        for i in range(len(s)):
            if s[low] not in s[low + 1:]:
                return low
        low += 1
    return -1


# 枚举实现案例
class Seasons:
    Spring = 0
    Summer = 1
    Autumn = 2
    Winter = 3


# 枚举实现案例
class Season1:
    Spring, Summer, Autumn, Winter = range(4)


if __name__ == '__main__':
    # w = word_break('catsanddog', ["cat", "cats", "and", "sand", "dog"])
    # a = [1, 2, 3, 3, 4]
    # print(remove_duplicates(a))

    # rotate([1,2,3,4,5,6,7],3)
    # print(is_duplicate(a))
    # print(move_zeroes([0, 1, 0, 3, 12]))
    # print(tow_sum([2, 7, 22, 12], 9))
    # print(reverse_string(["h", "e", "l", "l", "o"]))
    print(first_uniq_char('leetcode'))






