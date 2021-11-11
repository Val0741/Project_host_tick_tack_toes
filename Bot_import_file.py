def move_x():
    f = open('ListX.txt', 'r')
    List = [line.strip() for line in f]
    f.close()
    g = open('ListX_1.txt', 'r')
    ListX = [line.strip() for line in g]
    g.close()
    from random import randint
    x = randint(0, 24)
    if str(0) not in ListX and str(1) in ListX and str(2) in ListX and str(3) in ListX and str(0) not in List:
        x = 0
    elif str(0) in ListX and str(1) not in ListX and str(2) in ListX and str(3) in ListX and str(1) not in List:
        x = 1
    elif str(0) in ListX and str(1) in ListX and str(2) not in ListX and str(3) in ListX and str(2) not in List:
        x = 2
    elif str(0) in ListX and str(1) in ListX and str(2) in ListX and str(3) not in ListX and str(3) not in List:
        x = 3
    elif str(0) not in ListX and str(5) in ListX and str(10) in ListX and str(15) in ListX and str(0) not in List:
        x = 0
    elif str(0) in ListX and str(5) not in ListX and str(10) in ListX and str(15) in ListX and str(5) not in List:
        x = 5
    elif str(0) in ListX and str(5) in ListX and str(10) not in ListX and str(15) in ListX and str(10) not in List:
        x = 10
    elif str(0) in ListX and str(5) in ListX and str(10) in ListX and not str(15) in ListX and str(15) not in List:
        x = 15
    elif str(0) not in ListX and str(6) in ListX and str(12) in ListX and str(18) in ListX and str(0) not in List:
        x = 0
    elif str(0) in ListX and str(6) not in ListX and str(12) in ListX and str(18) in ListX and str(6) not in List:
        x = 6
    elif str(0) in ListX and str(6) in ListX and str(12) not in ListX and str(18) in ListX and str(12) not in List:
        x = 12
    elif str(0) in ListX and str(6) in ListX and str(12) in ListX and str(18) not in ListX and str(18) not in List:
        x = 18
    elif str(1) not in ListX and str(2) in ListX and str(3) in ListX and str(4) in ListX and str(1) not in List:
        x = 1
    elif str(1) in ListX and str(2) not in ListX and str(3) in ListX and str(4) in ListX and str(2) not in List:
        x = 2
    elif str(1) in ListX and str(2) in ListX and str(3) not in ListX and str(4) in ListX and str(3) not in List:
        x = 3
    elif str(1) in ListX and str(2) in ListX and str(3) in ListX and str(4) not in ListX and str(4) not in List:
        x = 4
    elif str(1) not in ListX and str(7) in ListX and str(13) in ListX and str(19) in ListX and str(1) not in List:
        x = 1
    elif str(1) in ListX and str(7) not in ListX and str(13) in ListX and str(19) in ListX and str(7) not in List:
        x = 7
    elif str(1) in ListX and str(7) in ListX and str(13) not in ListX and str(19) in ListX and str(13) not in List:
        x = 13
    elif str(1) in ListX and str(7) in ListX and str(13) in ListX and str(19) not in ListX and str(19) not in List:
        x = 19
    elif str(1) not in ListX and str(6) in ListX and str(11) in ListX and str(16) in ListX and str(1) not in List:
        x = 1
    elif str(1) in ListX and str(6) not in ListX and str(11) in ListX and str(16) in ListX and str(6) not in List:
        x = 6
    elif str(1) in ListX and str(6) in ListX and str(11) not in ListX and str(16) in ListX and str(11) not in List:
        x = 11
    elif str(1) in ListX and str(6) in ListX and str(11) in ListX and str(16) not in ListX and str(16) not in List:
        x = 16
    elif str(2) not in ListX and str(7) in ListX and str(12) in ListX and str(17) in ListX and str(2) not in List:
        x = 2
    elif str(2) in ListX and str(7) not in ListX and str(12) in ListX and str(17) in ListX and str(7) not in List:
        x = 7
    elif str(2) in ListX and str(7) in ListX and str(12) not in ListX and str(17) in ListX and str(12) not in List:
        x = 12
    elif str(2) in ListX and str(7) in ListX and str(12) in ListX and str(17) not in ListX and str(17) not in List:
        x = 17
    elif str(3) not in ListX and str(8) in ListX and str(13) in ListX and str(18) in ListX and str(3) not in List:
        x = 3
    elif str(3) in ListX and str(8) not in ListX and str(13) in ListX and str(18) in ListX and str(8) not in List:
        x = 8
    elif str(3) in ListX and str(8) in ListX and str(13) not in ListX and str(18) in ListX and str(13) not in List:
        x = 13
    elif str(3) in ListX and str(8) in ListX and str(13) in ListX and str(18) not in ListX and str(18) not in List:
        x = 18
    elif str(3) not in ListX and str(7) in ListX and str(11) in ListX and str(15) in ListX and str(3) not in List:
        x = 3
    elif str(3) in ListX and str(7) not in ListX and str(11) in ListX and str(15) in ListX and str(7) not in List:
        x = 7
    elif str(3) in ListX and str(7) in ListX and str(11) not in ListX and str(15) in ListX and str(11) not in List:
        x = 11
    elif str(3) in ListX and str(7) in ListX and str(11) in ListX and str(15) not in ListX and str(15) not in List:
        x = 15
    elif str(4) not in ListX and str(9) in ListX and str(14) in ListX and str(19) in ListX and str(4) not in List:
        x = 4
    elif str(4) in ListX and str(9) not in ListX and str(14) in ListX and str(19) in ListX and str(9) not in List:
        x = 9
    elif str(4) in ListX and str(9) in ListX and str(14) not in ListX and str(19) in ListX and str(14) not in List:
        x = 14
    elif str(4) in ListX and str(9) in ListX and str(14) in ListX and str(19) not in ListX and str(19) not in List:
        x = 19
    elif str(4) not in ListX and str(8) in ListX and str(12) in ListX and str(16) in ListX and str(4) not in List:
        x = 4
    elif str(4) in ListX and str(8) not in ListX and str(12) in ListX and str(16) in ListX and str(8) not in List:
        x = 8
    elif str(4) in ListX and str(8) in ListX and str(12) not in ListX and str(16) in ListX and str(12) not in List:
        x = 12
    elif str(4) in ListX and str(8) in ListX and str(12) in ListX and str(16) not in ListX and str(16) not in List:
        x = 16
    elif str(5) not in ListX and str(6) in ListX and str(7) in ListX and str(8) in ListX and str(5) not in List:
        x = 5
    elif str(5) in ListX and str(6) not in ListX and str(7) in ListX and str(8) in ListX and str(6) not in List:
        x = 6
    elif str(5) in ListX and str(6) in ListX and str(7) not in ListX and str(8) in ListX and str(7) not in List:
        x = 7
    elif str(5) in ListX and str(6) in ListX and str(7) in ListX and str(8) not in ListX and str(8) not in List:
        x = 8
    elif str(5) not in ListX and str(11) in ListX and str(17) in ListX and str(23) in ListX and str(5) not in List:
        x = 5
    elif str(5) in ListX and str(11) not in ListX and str(17) in ListX and str(23) in ListX and str(11) not in List:
        x = 11
    elif str(5) in ListX and str(11) in ListX and str(17) not in ListX and str(23) in ListX and str(17) not in List:
        x = 17
    elif str(5) in ListX and str(11) in ListX and str(17) in ListX and str(23) not in ListX and str(23) not in List:
        x = 23
    elif str(5) not in ListX and str(10) in ListX and str(15) in ListX and str(20) in ListX and str(5) not in List:
        x = 5
    elif str(5) in ListX and str(10) not in ListX and str(15) in ListX and str(20) in ListX and str(10) not in List:
        x = 10
    elif str(5) in ListX and str(10) in ListX and str(15) not in ListX and str(20) in ListX and str(15) not in List:
        x = 15
    elif str(5) in ListX and str(10) in ListX and str(15) in ListX and str(20) not in ListX and str(20) not in List:
        x = 20
    elif str(8) not in ListX and str(12) in ListX and str(16) in ListX and str(20) in ListX and str(8) not in List:
        x = 8
    elif str(8) in ListX and str(12) not in ListX and str(16) in ListX and str(20) in ListX and str(12) not in List:
        x = 12
    elif str(8) in ListX and str(12) in ListX and str(16) not in ListX and str(20) in ListX and str(16) not in List:
        x = 16
    elif str(8) in ListX and str(12) in ListX and str(16) in ListX and str(20) not in ListX and str(20) not in List:
        x = 20
    elif str(6) not in ListX and str(11) in ListX and str(16) in ListX and str(21) in ListX and str(6) not in List:
        x = 6
    elif str(6) in ListX and str(11) not in ListX and str(16) in ListX and str(21) in ListX and str(11) not in List:
        x = 11
    elif str(6) in ListX and str(11) in ListX and str(16) not in ListX and str(21) in ListX and str(16) not in List:
        x = 16
    elif str(6) in ListX and str(11) in ListX and str(16) in ListX and str(21) not in ListX and str(21) not in List:
        x = 21
    elif str(6) not in ListX and str(7) in ListX and str(8) in ListX and str(9) in ListX and str(6) not in List:
        x = 6
    elif str(6) in ListX and str(7) not in ListX and str(8) in ListX and str(9) in ListX and str(7) not in List:
        x = 7
    elif str(6) in ListX and str(7) in ListX and str(8) not in ListX and str(9) in ListX and str(8) not in List:
        x = 8
    elif str(6) in ListX and str(7) in ListX and str(8) in ListX and str(9) not in ListX and str(9) not in List:
        x = 9
    elif str(6) not in ListX and str(12) in ListX and str(18) in ListX and str(24) in ListX and str(6) not in List:
        x = 6
    elif str(6) in ListX and str(12) not in ListX and str(18) in ListX and str(24) in ListX and str(12) not in List:
        x = 12
    elif str(6) in ListX and str(12) in ListX and str(18) not in ListX and str(24) in ListX and str(18) not in List:
        x = 18
    elif str(6) in ListX and str(12) in ListX and str(18) in ListX and str(24) not in ListX and str(24) not in List:
        x = 24
    elif str(7) not in ListX and str(12) in ListX and str(17) in ListX and str(22) in ListX and str(7) not in List:
        x = 7
    elif str(7) in ListX and str(12) not in ListX and str(17) in ListX and str(22) in ListX and str(12) not in List:
        x = 12
    elif str(7) in ListX and str(12) in ListX and str(17) not in ListX and str(22) in ListX and str(17) not in List:
        x = 17
    elif str(7) in ListX and str(12) in ListX and str(17) in ListX and str(22) not in ListX and str(22) not in List:
        x = 22
    elif str(8) not in ListX and str(13) in ListX and str(18) in ListX and str(23) in ListX and str(8) not in List:
        x = 8
    elif str(8) in ListX and str(13) not in ListX and str(18) in ListX and str(23) in ListX and str(13) not in List:
        x = 13
    elif str(8) in ListX and str(13) in ListX and str(18) not in ListX and str(23) in ListX and str(18) not in List:
        x = 18
    elif str(8) in ListX and str(13) in ListX and str(18) in ListX and str(23) not in ListX and str(23) not in List:
        x = 23
    elif str(9) not in ListX and str(14) in ListX and str(19) in ListX and str(24) in ListX and str(9) not in List:
        x = 9
    elif str(9) in ListX and str(14) not in ListX and str(19) in ListX and str(24) in ListX and str(14) not in List:
        x = 14
    elif str(9) in ListX and str(14) in ListX and str(19) not in ListX and str(24) in ListX and str(19) not in List:
        x = 19
    elif str(9) in ListX and str(14) in ListX and str(19) in ListX and str(24) not in ListX and str(24) not in List:
        x = 24
    elif str(9) not in ListX and str(13) in ListX and str(17) in ListX and str(21) in ListX and str(9) not in List:
        x = 9
    elif str(9) in ListX and str(13) not in ListX and str(17) in ListX and str(21) in ListX and str(13) not in List:
        x = 13
    elif str(9) in ListX and str(13) in ListX and str(17) not in ListX and str(21) in ListX and str(17) not in List:
        x = 17
    elif str(9) in ListX and str(13) in ListX and str(17) in ListX and str(21) not in ListX and str(21) not in List:
        x = 21
    elif str(10) not in ListX and str(11) in ListX and str(12) in ListX and str(13) in ListX and str(10) not in List:
        x = 10
    elif str(10) in ListX and str(11) not in ListX and str(12) in ListX and str(13) in ListX and str(11) not in List:
        x = 11
    elif str(10) in ListX and str(11) in ListX and str(12) not in ListX and str(13) in ListX and str(12) not in List:
        x = 12
    elif str(10) in ListX and str(11) in ListX and str(12) in ListX and str(13) not in ListX and str(13) not in List:
        x = 13
    elif str(11) not in ListX and str(12) in ListX and str(13) in ListX and str(14) in ListX and str(11) not in List:
        x = 11
    elif str(11) in ListX and str(12) not in ListX and str(13) in ListX and str(14) in ListX and str(12) not in List:
        x = 12
    elif str(11) in ListX and str(12) in ListX and str(13) not in ListX and str(14) in ListX and str(13) not in List:
        x = 13
    elif str(11) in ListX and str(12) in ListX and str(13) in ListX and str(14) not in ListX and str(14) not in List:
        x = 14
    elif str(15) not in ListX and str(16) in ListX and str(17) in ListX and str(18) in ListX and str(15) not in List:
        x = 15
    elif str(15) in ListX and str(16) not in ListX and str(17) in ListX and str(18) in ListX and str(16) not in List:
        x = 16
    elif str(15) in ListX and str(16) in ListX and str(17) not in ListX and str(18) in ListX and str(17) not in List:
        x = 17
    elif str(15) in ListX and str(16) in ListX and str(17) in ListX and str(18) not in ListX and str(18) not in List:
        x = 18
    elif str(16) not in ListX and str(17) in ListX and str(18) in ListX and str(19) in ListX and str(16) not in List:
        x = 16
    elif str(16) in ListX and str(17) not in ListX and str(18) in ListX and str(19) in ListX and str(17) not in List:
        x = 17
    elif str(16) in ListX and str(17) in ListX and str(18) not in ListX and str(19) in ListX and str(18) not in List:
        x = 18
    elif str(16) in ListX and str(17) in ListX and str(18) in ListX and str(19) not in ListX and str(19) not in List:
        x = 19
    elif str(20) not in ListX and str(21) in ListX and str(22) in ListX and str(23) in ListX and str(20) not in List:
        x = 20
    elif str(20) in ListX and str(21) not in ListX and str(22) in ListX and str(23) in ListX and str(21) not in List:
        x = 21
    elif str(20) in ListX and str(21) in ListX and str(22) not in ListX and str(23) in ListX and str(22) not in List:
        x = 22
    elif str(20) in ListX and str(21) in ListX and str(22) in ListX and str(23) not in ListX and str(23) not in List:
        x = 23
    elif str(21) not in ListX and str(22) in ListX and str(23) in ListX and str(24) in ListX and str(21) not in List:
        x = 21
    elif str(21) in ListX and str(22) not in ListX and str(23) in ListX and str(24) in ListX and str(22) not in List:
        x = 22
    elif str(21) in ListX and str(22) in ListX and str(23) not in ListX and str(24) in ListX and str(23) not in List:
        x = 23
    elif str(21) in ListX and str(22) in ListX and str(23) in ListX and str(24) not in ListX and str(24) not in List:
        x = 24
    else:
        while str(x) in List:
            x = randint(0, 24)
            x = str(x)
    a = str(x)
    f = open('bot_x_testing.txt', 'w')
    f.write(str(a))
    f.close()

move_x()

