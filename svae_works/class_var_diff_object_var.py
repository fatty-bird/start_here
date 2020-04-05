import os

class Check(object):
    class_var = 10

    def __init__(self, name):
        self.local_var = name

    def change_class_var(self, tnum):
        self.class_var = tnum


if __name__ == "__main__":
    t1 = Check("dog")
    t2 = Check("cat")

    # print("t1 local_var: %s" % t1.local_var)
    # print("t2 local_var: %s" % t2.local_var)
    # print("Check var : %s" % Check.class_var)

    # 类变量变化，实例中的类变量同步变化，以下输出全为400
    Check.class_var = 400
    print("Check var : %s" % Check.class_var)
    print("t1 class_var: %s" % t1.class_var)
    print("t2 class_var: %s" % t2.class_var)
    print("ID Check var : %s" % id(Check.class_var))
    print("ID t1 class_var: %s" % id(t1.class_var))
    print("ID t2 class_var: %s" % id(t2.class_var))

    print("*" * 20)
    # 实例中自己修改类变量，会复制类变量生成自己的同名实例变量，并不再跟随类变量变化，以下t1实例class_var为399
    t1.change_class_var(399)
    print("Check var : %s" % Check.class_var)
    print("t1 class_var: %s" % t1.class_var)
    print("t2 class_var: %s" % t2.class_var)
    print("ID Check var : %s" % id(Check.class_var))
    print("ID t1 class_var: %s" % id(t1.class_var))
    print("ID t2 class_var: %s" % id(t2.class_var))

    print("*" * 20)
    Check.class_var = 401
    print("Check var : %s" % Check.class_var)
    print("t1 class_var: %s" % t1.class_var)
    print("t2 class_var: %s" % t2.class_var)
    print("ID Check var : %s" % id(Check.class_var))
    print("ID t1 class_var: %s" % id(t1.class_var))
    print("ID t2 class_var: %s" % id(t2.class_var))