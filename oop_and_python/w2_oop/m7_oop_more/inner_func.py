# function is a first class object
def double_decker():
    print("starting the double decker")

    def innner_func():
        print("inside the inner func")
        return 3000

    return innner_func


# double_decker()()
# print(double_decker()())


# wrapper func
def do_something(work):
    print("inside the wrapper func")
    # print(work)
    work()
    print('work ended')


# do_something("kola khao")
def coding():
    print("doding in python")


# do_something(coding)
def sleeping():
    print('sleeping in python')
do_something(sleeping)