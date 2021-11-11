def move_x():
    from random import randint
    f = open('ListX.txt', 'r')
    List = [line.strip() for line in f]



    a = randint(0, 24)
    x = str(a)

    if x not in List:
        f = open('bot_x_testing.txt', 'w')
        f.write(str(x))
        f.close()
    else:
        while x in List:
            a = randint(0, 24)
            x = str(a)
            f = open('bot_x_testing.txt', 'w')
            f.write(str(x))
            f.close()



move_x()
