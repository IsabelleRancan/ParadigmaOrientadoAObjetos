global_var = "a global variable"


def func(par):  # Function
    print(global_var, "and", par)


class Test:
    class_var = "a class variable"  # Class variable

    def __init__(self, par):
        self.inst_var = par  # Instance variable

    def test1(self, par):  # Instance method
        print(self.inst_var, "and", par)

    @staticmethod
    def test2(par):  # Static method
        print(Test.class_var, "and", par)

    def test3(par):  # Static method
        print(Test.class_var, "and", par)
