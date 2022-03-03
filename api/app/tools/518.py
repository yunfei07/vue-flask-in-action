def b_search(l, item):
    low = 0
    high = len(l) - 0

    while low <= high:
        mid = (low + high) // 2
        if item == l[mid]:
            return mid

        if item > l[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


def s_sort(l):
    new_arr = []
    for i in range(len(l)):
        new_arr.append(l.pop(l.index(min(l))))

    return new_arr


def b_sort(l):
    for i in range(len(l) - 1):
        for y in range(len(l) - 1):
            if l[y] > l[y + 1]:
                l[y], l[y + 1] = l[y + 1], l[y]

    return l


def q_sort(l):
    if len(l) < 2:
        return l
    else:
        p = l[0]  # 基准值
        less = [i for i in l[1:] if i <= p]  # 所有小元素
        greater = [i for i in l[1:] if i > p]  # 所有大元素3
        return q_sort(less) + [p] + q_sort(greater)


def q_sort2(l):
    if len(l) < 2:
        return l
    else:
        p = l[0]
        less = [i for i in l[1:] if i <= p]
        greater = [i for i in l[1:] if i > p]
    return q_sort2(less) + [p] + q_sort2(greater)


def m_sort(l):
    pass


def f(i):
    if i <= 1:
        return 1
    else:
        f(i - 1)


def b_find(l, item):
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


def bo_sort(l):
    for x in range(len(l) - 1):
        for y in range(len(l) - 1):
            if l[y] > l[y + 1]:
                l[y], l[y + 1] = l[y + 1], l[y]
    return l


def sl_sort(l):
    new_arr = []
    for x in range(len(l)):
        new_arr.append(l.pop(l.index(min(l))))
    return new_arr


def qu_sort(l):
    if len(l) < 2:
        return l
    else:
        p = l[0]
        less = [i for i in l if i < p]
        greater = [i for i in l if i > p]
    return qu_sort(less) + [p] + qu_sort(greater)


def min_distance(word1, word2):
    count = 0
    if word1 == word2:
        return 0
    else:
        count = abs(len(word1) - len(word2))
        for c in word1:
            if c not in word2:
                count += 1
            else:
                pass
    return count


def merge(num1, m, num2, n):
    return (num1 + num2).sort()


def single_number(nums):
    s = ''.join(str(x) for x in nums)
    for i in s:
        if s.count(i) == 1:
            return int(i)


def majority_element(nums) -> int:
    s = ''.join(str(x) for x in nums)
    for i in s:
        if s.count(i) >= 2:
            return int(i)


def search(l, item):
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


def bb_sort(l):
    for x in range(len(l) - 1):
        for y in range(len(l) - 1):
            if l[y] > l[y + 1]:
                l[y], l[y + 1] = l[y + 1], l[y]

    return l


def ss_sort(l):
    arr = []
    for i in range(len(l)):
        arr.append(l.pop(l.index(min(l))))

    return arr


def qq_sort(l):
    if len(l) < 2:
        return l
    else:
        p = l[0]
        less = [i for i in l if i < p]
        greater = [i for i in l if i > p]
    return qq_sort(less) + [p] + qq_sort(greater)


def word_break(s, word_list):
    is_flag = False

    for w in word_list:
        if s.count(w) > 0:
            is_flag = True
            s = s.replace(w, '')
        else:
            is_flag = False
    return is_flag


if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    li = [2, 3, 1, 0, 5, 4, 8]
    # b = b_search(lis, 6)
    # print(b)
    # s = s_sort(li)
    # print(s)

    # s1 = b_sort(li)
    # print(s1)
    # q = q_sort2(li)
    # print(q)
    #
    # m = min_distance('horse', 'ros')
    # print(m)
    #
    # f = b_find(lis, 3)
    # print(f)

    # print(bo_sort(li))
    # print(sl_sort(li))
    # print(qu_sort(li))
    #
    # a = [2, 2, 1]
    # sn = single_number(a)
    # print(majority_element(a))
    # print(ss_sort(li))
    print(word_break('leetcode', ['leet', 'code']))
    print(word_break('applepenapple', ["apple", "pen"]))
    print(word_break('catsandog', ["cats", "dog", "sand", "and", "cat"]))
