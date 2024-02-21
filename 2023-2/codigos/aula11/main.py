from test import Test

# from test.Test import test2 # error!
from test import func
from test import global_var


def testando_metodos():
    func("a argument")

    t = Test("a instance variable")
    t.test1("a argument")
    t.test2("a argument")

    Test.test2("other argument")
    Test.test3("other argument")

    # t.test3("cannot do this")  # error!
    # Test.test1("this is also forbidden")  # error!


def acessando_variaveis():
    t1 = Test("attribute 1")
    t2 = Test("attribute 2")

    print(t1.inst_var, "|", t1.class_var)
    print(t2.inst_var, "|", t2.class_var)
    print(Test.class_var, "|", global_var)

    t1.inst_var = "attribute 1 modified"
    t1.class_var = "new attribute"
    Test.class_var = "class var modified"
    # global_var = "a local var" # error!

    print(t1.inst_var, "|", t1.class_var)
    print(t2.inst_var, "|", t2.class_var)
    print(Test.class_var, "|", global_var)

    # print(Test.inst_var) # error!


if __name__ == "__main__":
    testando_metodos()
    acessando_variaveis()
