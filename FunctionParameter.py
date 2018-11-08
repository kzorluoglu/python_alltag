def multi_print(number = 3, word="Selam"):
    for i in range(0, number):
        print(word)

multi_print(5, 'Hello')
multi_print(word="learning")


# parameters as params
def calculate_max(*params):
    print(params)
    print(params[0])

calculate_max(2,3,4)

# parameters as args
def f(**args):
    print(args)

f(key="value", test=3)
