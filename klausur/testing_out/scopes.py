def myfunc():
    # print(x)
    x = 'local to myfunc'
    print(x)

    def inner_1():
        # print(x)
        x = 'local to inner 1'
        print(x)

        def inner_2():
            # print(x)
            nonlocal x
            x = 'local to inner 2'
            print(x)

        inner_2()

        print(x)

    inner_1()

    print(x)


myfunc()
