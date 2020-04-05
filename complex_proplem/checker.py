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

    print("t1 local_var: %s" % t1.local_var)
    print("t2 local_var: %s" % t2.local_var)
    print("Check var : %s" % Check.class_var)


    # t1.change_class_var(399)
    # print("Check var : %s" % Check.class_var)
    # print("t1 class_var: %s" % t1.class_var)
    # print("t2 class_var: %s" % t2.class_var)

    Check.class_var = 400
    print("Check var : %s" % Check.class_var)
    print("t1 class_var: %s" % t1.class_var)
    print("t2 class_var: %s" % t2.class_var)