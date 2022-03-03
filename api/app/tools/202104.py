from math import ceil


def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))


def find_str_index(str1, str2):
    if not str2:
        return "str2 not none"
    for x in str2:
        if x in str1:
            return str1.index(x)


def find_sub_string(s, words):
    if not words:
        return []
    tmp = []
    str1 = ''
    str2 = ''
    for x in words:
        str1 += x
    if str1 in s:
        tmp.append(s.index(str1))

    words.reverse()
    for x in words:
        str2 += x

    if str2 in s:
        tmp.append(s.index(str2))
    return tmp


def longest_valid_parentheses(s: str) -> int:
    left = '('
    right = ')'
    n = 0
    stack = [-1]

    for x in range(len(s)):
        if x == left:
            stack.append(x)
        else:
            stack.pop()
            if not stack:
                stack.append(x)
            if stack:
                n = max(n, x - stack[-1])
    return n


def search(nums, target) -> int:
    if target in nums:
        return nums.index(target)
    else:
        return -1


def search_range(nums, target):
    indices = [i for i, x in enumerate(nums) if x == target]
    if not indices:
        return [-1, -1]
    return indices


def binary_search(l, item):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == item:
            return mid
        if l[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def bin_search(l, item):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2
        if item == l[mid]:
            return mid

        if item > l[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


def b_search(l, item):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2
        if item == l[mid]:
            return mid

        if item > l[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None


def b_sort(l):
    for index in range(len(l) - 1):
        for k in range(len(l) - 1):
            if l[k] > l[k + 1]:
                l[k], l[k + 1] = l[k + 1], l[k]
                k += 1
    return l


# 插入排序
def i_sort():
    pass


# 选择排序
def s_sort(l):
    low = 0
    high = len(l) - 1
    while low >= high:
        n = min(l[low:])
        n, l[low] = l[low], n
        low += 1
    return l


# 快速排序
def q_sort(l):
    pass


# 递归算法

# 匹配括号
def find_k(strings):
    stack = []
    count = 0
    for s in strings:
        if s == '(':
            stack.append(s)
        elif len(stack) > 0 and s == ')':
            stack.pop()
            count += 1
        else:
            return 0
    return count * 2


def insert_index(l, target):
    l.append(target)
    l.sort()
    return l.index(target)


def multiply(n1, n2):
    return f"{eval(f'{n1}*{n2}')}"


if __name__ == '__main__':
    a = find_str_index('hello', 'l')
    b = find_sub_string("barfoothefoobarman", ["foo", "bar", 'aaa'])
    l = [1, 2, 3, 4, 5, 6]
    k = "(()()())()"
    # c = longest_valid_parentheses("(()()()))")
    # print(c)
    nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 6
    # s = search(nums,target)
    # ss = search_range([5, 7, 7, 8, 8, 10], 18)
    # print(ss)

    # x = [1, 3, 5, 7, 8, 9]
    # # bs = binary_search(x, 9)
    # bs = bin_search(l, 4)
    # b = b_search(x, 9)
    # print(bs, b)

    s = b_sort(nums)
    print(s)

    f = find_k(k)
    print(f)

    select = s_sort(nums)
    print(select)

    print(multiply("12", "12"))

# t = [1, 3, 5, 6]
# st = insert_index(t, 7)
# print(st)
