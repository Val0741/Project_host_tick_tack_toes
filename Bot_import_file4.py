def move_y():
    from random import randint
    f = open('ListY.txt', 'r')
    List = [line.strip() for line in f]



    b = randint(0, 24)
    y = str(b)

    if y not in List:
        f = open('bot_y_testing.txt', 'w')
        f.write(str(y))
        f.close()
    else:
        while y in List:
            b = randint(0, 24)
            y = str(b)
            f = open('bot_y_testing.txt', 'w')
            f.write(str(y))
            f.close()



move_y()
