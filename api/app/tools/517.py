# 二分查找
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


# 冒泡排序
def b_sort(l):
    for x in range(len(l) - 1):
        for y in range(len(l) - 1):
            if l[y] > l[y + 1]:
                l[y], l[y + 1] = l[y + 1], l[y]
    return l


# 选择排序
def s_sort(l):
    new_arr = []
    for i in range(len(l)):
        new_arr.append(l.pop(l.index(min(l))))
    return new_arr


# 插入排序
def i_sort(l):
    pass


# 快速排序
def q_sort(l):
    pass

# 递归算法

# 匹配括号


if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    li = [2, 3, 1, 0, 5, 4, 8]
    # b = b_search(lis, 0)
    # print(b)
    # b = b_sort(li)
    # print(b)

    s = s_sort(li)
    print(s)
