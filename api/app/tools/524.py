def b_search(l, item):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2

        if item == l[mid]:
            return l

        if item > l[mid]:
            low = mid + 1
        else:
            high = mid + 1

    return None


def b_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def s_sort(l):
    arr = []
    for i in range(len(l)):
        arr.append(l.pop(l.index(min(l))))
    return arr


def q_sort(l):
    if len(l) < 2:
        return l
    else:
        p = l[0]
        less = [i for i in l if l[i] < p]
        great = [i for i in l if l[i] > p]
    return q_sort(less) + [p] + q_sort(great)


class Product:

    def __init__(self):
        self.name = 'hello'

    def __del__(self):
        self.name = 'fei'

    def __len__(self):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass


class Rectangle:

    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self,size):
        self.width,self.height = size

    def get_size(self):
        return self.width,self.height

    size = property(get_size, set_size)

# 静态方法(staticmethod)，没有self参数，通常被命名为cls。
# 类方法(classmethod)，可以通过对象直接调用，但参数cls将自动化关联到类。
class MyHome:

    def __init__(self):
        self.name = 'aa'

    @staticmethod
    def smeth(a):
        print('this is a static method',a)

    @classmethod
    def cmeth(cls):
        print('this is a class method')


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('aaa')
            self.hungry = False
        else:
            print("No,thanks")


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)

def merge(nums1,m,nums2,n):
    pass


class Card:

    # 属性被访问时自动调用
    def __getattribute__(self, item):
        pass

    # 试图给属性赋值时自动调用
    def __setattr__(self, key, value):
        pass

    # 属性被访问而对象没有这样的属性是自动调用
    def __getattr__(self, item):
        pass

    # 试图删除属性时自动调用
    def __delattr__(self, item):
        pass





if __name__ == '__main__':
    # p = Product()
    # sb = SongBird()
    # sb.sing()
    # sb.eat()
    # r = Rectangle()
    # r.width = 5
    # r.height = 10
    # print(r.size)
    MyHome.smeth('aaaa')
    MyHome.cmeth()


