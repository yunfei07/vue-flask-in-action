# 二分查找
def q_search(l, item):
    low = 0
    high = (len(l) - 1)

    while low <= high:
        mid = (low + high) // 2

        if l[mid] == item:
            return mid

        if item > l[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None


# 冒泡排序
def b_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return l


# 插入排序
def c_sort(l):
    arr = []
    for i in range(len(l)):
        arr.append(l.pop(l.index(min(l))))

    return arr


# 快速排序
def q_sort(l):
    if len(l) < 2:
        return l
    else:
        p = l[0]
        less = [i for i in l if i < p]
        greater = [i for i in l if i > p]

    return q_sort(less) + [p] + q_sort(greater)





if __name__ == '__main__':
    pass
