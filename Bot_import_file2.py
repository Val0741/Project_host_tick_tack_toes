def move_y():
    f = open('ListY.txt', 'r')
    List = [line.strip() for line in f]
    f.close()
    g = open('ListY_1.txt', 'r')
    ListY = [line.strip() for line in g]
    g.close()
    from random import randint
    y = randint(0, 24)
    if str(0) not in ListY and str(1) in ListY and str(2) in ListY and str(3) in ListY and str(0) not in List:
        y = 0
    elif str(0) in ListY and str(1) not in ListY and str(2) in ListY and str(3) in ListY and str(1) not in List:
        y = 1
    elif str(0) in ListY and str(1) in ListY and str(2) not in ListY and str(3) in ListY and str(2) not in List:
        y = 2
    elif str(0) in ListY and str(1) in ListY and str(2) in ListY and str(3) not in ListY and str(3) not in List:
        y = 3
    elif str(0) not in ListY and str(5) in ListY and str(10) in ListY and str(15) in ListY and str(0) not in List:
        y = 0
    elif str(0) in ListY and str(5) not in ListY and str(10) in ListY and str(15) in ListY and str(5) not in List:
        y = 5
    elif str(0) in ListY and str(5) in ListY and str(10) not in ListY and str(15) in ListY and str(10) not in List:
        y = 10
    elif str(0) in ListY and str(5) in ListY and str(10) in ListY and not str(15) in ListY and str(15) not in List:
        y = 15
    elif str(0) not in ListY and str(6) in ListY and str(12) in ListY and str(18) in ListY and str(0) not in List:
        y = 0
    elif str(0) in ListY and str(6) not in ListY and str(12) in ListY and str(18) in ListY and str(6) not in List:
        y = 6
    elif str(0) in ListY and str(6) in ListY and str(12) not in ListY and str(18) in ListY and str(12) not in List:
        y = 12
    elif str(0) in ListY and str(6) in ListY and str(12) in ListY and str(18) not in ListY and str(18) not in List:
        y = 18
    elif str(1) not in ListY and str(2) in ListY and str(3) in ListY and str(4) in ListY and str(1) not in List:
        y = 1
    elif str(1) in ListY and str(2) not in ListY and str(3) in ListY and str(4) in ListY and str(2) not in List:
        y = 2
    elif str(1) in ListY and str(2) in ListY and str(3) not in ListY and str(4) in ListY and str(3) not in List:
        y = 3
    elif str(1) in ListY and str(2) in ListY and str(3) in ListY and str(4) not in ListY and str(4) not in List:
        y = 4
    elif str(1) not in ListY and str(7) in ListY and str(13) in ListY and str(19) in ListY and str(1) not in List:
        y = 1
    elif str(1) in ListY and str(7) not in ListY and str(13) in ListY and str(19) in ListY and str(7) not in List:
        y = 7
    elif str(1) in ListY and str(7) in ListY and str(13) not in ListY and str(19) in ListY and str(13) not in List:
        y = 13
    elif str(1) in ListY and str(7) in ListY and str(13) in ListY and str(19) not in ListY and str(19) not in List:
        y = 19
    elif str(1) not in ListY and str(6) in ListY and str(11) in ListY and str(16) in ListY and str(1) not in List:
        y = 1
    elif str(1) in ListY and str(6) not in ListY and str(11) in ListY and str(16) in ListY and str(6) not in List:
        y = 6
    elif str(1) in ListY and str(6) in ListY and str(11) not in ListY and str(16) in ListY and str(11) not in List:
        y = 11
    elif str(1) in ListY and str(6) in ListY and str(11) in ListY and str(16) not in ListY and str(16) not in List:
        y = 16
    elif str(2) not in ListY and str(7) in ListY and str(12) in ListY and str(17) in ListY and str(2) not in List:
        y = 2
    elif str(2) in ListY and str(7) not in ListY and str(12) in ListY and str(17) in ListY and str(7) not in List:
        y = 7
    elif str(2) in ListY and str(7) in ListY and str(12) not in ListY and str(17) in ListY and str(12) not in List:
        y = 12
    elif str(2) in ListY and str(7) in ListY and str(12) in ListY and str(17) not in ListY and str(17) not in List:
        y = 17
    elif str(3) not in ListY and str(8) in ListY and str(13) in ListY and str(18) in ListY and str(3) not in List:
        y = 3
    elif str(3) in ListY and str(8) not in ListY and str(13) in ListY and str(18) in ListY and str(8) not in List:
        y = 8
    elif str(3) in ListY and str(8) in ListY and str(13) not in ListY and str(18) in ListY and str(13) not in List:
        y = 13
    elif str(3) in ListY and str(8) in ListY and str(13) in ListY and str(18) not in ListY and str(18) not in List:
        y = 18
    elif str(3) not in ListY and str(7) in ListY and str(11) in ListY and str(15) in ListY and str(3) not in List:
        y = 3
    elif str(3) in ListY and str(7) not in ListY and str(11) in ListY and str(15) in ListY and str(7) not in List:
        y = 7
    elif str(3) in ListY and str(7) in ListY and str(11) not in ListY and str(15) in ListY and str(11) not in List:
        y = 11
    elif str(3) in ListY and str(7) in ListY and str(11) in ListY and str(15) not in ListY and str(15) not in List:
        y = 15
    elif str(4) not in ListY and str(9) in ListY and str(14) in ListY and str(19) in ListY and str(4) not in List:
        y = 4
    elif str(4) in ListY and str(9) not in ListY and str(14) in ListY and str(19) in ListY and str(9) not in List:
        y = 9
    elif str(4) in ListY and str(9) in ListY and str(14) not in ListY and str(19) in ListY and str(14) not in List:
        y = 14
    elif str(4) in ListY and str(9) in ListY and str(14) in ListY and str(19) not in ListY and str(19) not in List:
        y = 19
    elif str(4) not in ListY and str(8) in ListY and str(12) in ListY and str(16) in ListY and str(4) not in List:
        y = 4
    elif str(4) in ListY and str(8) not in ListY and str(12) in ListY and str(16) in ListY and str(8) not in List:
        y = 8
    elif str(4) in ListY and str(8) in ListY and str(12) not in ListY and str(16) in ListY and str(12) not in List:
        y = 12
    elif str(4) in ListY and str(8) in ListY and str(12) in ListY and str(16) not in ListY and str(16) not in List:
        y = 16
    elif str(5) not in ListY and str(6) in ListY and str(7) in ListY and str(8) in ListY and str(5) not in List:
        y = 5
    elif str(5) in ListY and str(6) not in ListY and str(7) in ListY and str(8) in ListY and str(6) not in List:
        y = 6
    elif str(5) in ListY and str(6) in ListY and str(7) not in ListY and str(8) in ListY and str(7) not in List:
        y = 7
    elif str(5) in ListY and str(6) in ListY and str(7) in ListY and str(8) not in ListY and str(8) not in List:
        y = 8
    elif str(5) not in ListY and str(11) in ListY and str(17) in ListY and str(23) in ListY and str(5) not in List:
        y = 5
    elif str(5) in ListY and str(11) not in ListY and str(17) in ListY and str(23) in ListY and str(11) not in List:
        y = 11
    elif str(5) in ListY and str(11) in ListY and str(17) not in ListY and str(23) in ListY and str(17) not in List:
        y = 17
    elif str(5) in ListY and str(11) in ListY and str(17) in ListY and str(23) not in ListY and str(23) not in List:
        y = 23
    elif str(5) not in ListY and str(10) in ListY and str(15) in ListY and str(20) in ListY and str(5) not in List:
        y = 5
    elif str(5) in ListY and str(10) not in ListY and str(15) in ListY and str(20) in ListY and str(10) not in List:
        y = 10
    elif str(5) in ListY and str(10) in ListY and str(15) not in ListY and str(20) in ListY and str(15) not in List:
        y = 15
    elif str(5) in ListY and str(10) in ListY and str(15) in ListY and str(20) not in ListY and str(20) not in List:
        y = 20
    elif str(8) not in ListY and str(12) in ListY and str(16) in ListY and str(20) in ListY and str(8) not in List:
        y = 8
    elif str(8) in ListY and str(12) not in ListY and str(16) in ListY and str(20) in ListY and str(12) not in List:
        y = 12
    elif str(8) in ListY and str(12) in ListY and str(16) not in ListY and str(20) in ListY and str(16) not in List:
        y = 16
    elif str(8) in ListY and str(12) in ListY and str(16) in ListY and str(20) not in ListY and str(20) not in List:
        y = 20
    elif str(6) not in ListY and str(11) in ListY and str(16) in ListY and str(21) in ListY and str(6) not in List:
        y = 6
    elif str(6) in ListY and str(11) not in ListY and str(16) in ListY and str(21) in ListY and str(11) not in List:
        y = 11
    elif str(6) in ListY and str(11) in ListY and str(16) not in ListY and str(21) in ListY and str(16) not in List:
        y = 16
    elif str(6) in ListY and str(11) in ListY and str(16) in ListY and str(21) not in ListY and str(21) not in List:
        y = 21
    elif str(6) not in ListY and str(7) in ListY and str(8) in ListY and str(9) in ListY and str(6) not in List:
        y = 6
    elif str(6) in ListY and str(7) not in ListY and str(8) in ListY and str(9) in ListY and str(7) not in List:
        y = 7
    elif str(6) in ListY and str(7) in ListY and str(8) not in ListY and str(9) in ListY and str(8) not in List:
        y = 8
    elif str(6) in ListY and str(7) in ListY and str(8) in ListY and str(9) not in ListY and str(9) not in List:
        y = 9
    elif str(6) not in ListY and str(12) in ListY and str(18) in ListY and str(24) in ListY and str(6) not in List:
        y = 6
    elif str(6) in ListY and str(12) not in ListY and str(18) in ListY and str(24) in ListY and str(12) not in List:
        y = 12
    elif str(6) in ListY and str(12) in ListY and str(18) not in ListY and str(24) in ListY and str(18) not in List:
        y = 18
    elif str(6) in ListY and str(12) in ListY and str(18) in ListY and str(24) not in ListY and str(24) not in List:
        y = 24
    elif str(7) not in ListY and str(12) in ListY and str(17) in ListY and str(22) in ListY and str(7) not in List:
        y = 7
    elif str(7) in ListY and str(12) not in ListY and str(17) in ListY and str(22) in ListY and str(12) not in List:
        y = 12
    elif str(7) in ListY and str(12) in ListY and str(17) not in ListY and str(22) in ListY and str(17) not in List:
        y = 17
    elif str(7) in ListY and str(12) in ListY and str(17) in ListY and str(22) not in ListY and str(22) not in List:
        y = 22
    elif str(8) not in ListY and str(13) in ListY and str(18) in ListY and str(23) in ListY and str(8) not in List:
        y = 8
    elif str(8) in ListY and str(13) not in ListY and str(18) in ListY and str(23) in ListY and str(13) not in List:
        y = 13
    elif str(8) in ListY and str(13) in ListY and str(18) not in ListY and str(23) in ListY and str(18) not in List:
        y = 18
    elif str(8) in ListY and str(13) in ListY and str(18) in ListY and str(23) not in ListY and str(23) not in List:
        y = 23
    elif str(9) not in ListY and str(14) in ListY and str(19) in ListY and str(24) in ListY and str(9) not in List:
        y = 9
    elif str(9) in ListY and str(14) not in ListY and str(19) in ListY and str(24) in ListY and str(14) not in List:
        y = 14
    elif str(9) in ListY and str(14) in ListY and str(19) not in ListY and str(24) in ListY and str(19) not in List:
        y = 19
    elif str(9) in ListY and str(14) in ListY and str(19) in ListY and str(24) not in ListY and str(24) not in List:
        y = 24
    elif str(9) not in ListY and str(13) in ListY and str(17) in ListY and str(21) in ListY and str(9) not in List:
        y = 9
    elif str(9) in ListY and str(13) not in ListY and str(17) in ListY and str(21) in ListY and str(13) not in List:
        y = 13
    elif str(9) in ListY and str(13) in ListY and str(17) not in ListY and str(21) in ListY and str(17) not in List:
        y = 17
    elif str(9) in ListY and str(13) in ListY and str(17) in ListY and str(21) not in ListY and str(21) not in List:
        y = 21
    elif str(10) not in ListY and str(11) in ListY and str(12) in ListY and str(13) in ListY and str(10) not in List:
        y = 10
    elif str(10) in ListY and str(11) not in ListY and str(12) in ListY and str(13) in ListY and str(11) not in List:
        y = 11
    elif str(10) in ListY and str(11) in ListY and str(12) not in ListY and str(13) in ListY and str(12) not in List:
        y = 12
    elif str(10) in ListY and str(11) in ListY and str(12) in ListY and str(13) not in ListY and str(13) not in List:
        y = 13
    elif str(11) not in ListY and str(12) in ListY and str(13) in ListY and str(14) in ListY and str(11) not in List:
        y = 11
    elif str(11) in ListY and str(12) not in ListY and str(13) in ListY and str(14) in ListY and str(12) not in List:
        y = 12
    elif str(11) in ListY and str(12) in ListY and str(13) not in ListY and str(14) in ListY and str(13) not in List:
        y = 13
    elif str(11) in ListY and str(12) in ListY and str(13) in ListY and str(14) not in ListY and str(14) not in List:
        y = 14
    elif str(15) not in ListY and str(16) in ListY and str(17) in ListY and str(18) in ListY and str(15) not in List:
        y = 15
    elif str(15) in ListY and str(16) not in ListY and str(17) in ListY and str(18) in ListY and str(16) not in List:
        y = 16
    elif str(15) in ListY and str(16) in ListY and str(17) not in ListY and str(18) in ListY and str(17) not in List:
        y = 17
    elif str(15) in ListY and str(16) in ListY and str(17) in ListY and str(18) not in ListY and str(18) not in List:
        y = 18
    elif str(16) not in ListY and str(17) in ListY and str(18) in ListY and str(19) in ListY and str(16) not in List:
        y = 16
    elif str(16) in ListY and str(17) not in ListY and str(18) in ListY and str(19) in ListY and str(17) not in List:
        y = 17
    elif str(16) in ListY and str(17) in ListY and str(18) not in ListY and str(19) in ListY and str(18) not in List:
        y = 18
    elif str(16) in ListY and str(17) in ListY and str(18) in ListY and str(19) not in ListY and str(19) not in List:
        y = 19
    elif str(20) not in ListY and str(21) in ListY and str(22) in ListY and str(23) in ListY and str(20) not in List:
        y = 20
    elif str(20) in ListY and str(21) not in ListY and str(22) in ListY and str(23) in ListY and str(21) not in List:
        y = 21
    elif str(20) in ListY and str(21) in ListY and str(22) not in ListY and str(23) in ListY and str(22) not in List:
        y = 22
    elif str(20) in ListY and str(21) in ListY and str(22) in ListY and str(23) not in ListY and str(23) not in List:
        y = 23
    elif str(21) not in ListY and str(22) in ListY and str(23) in ListY and str(24) in ListY and str(21) not in List:
        y = 21
    elif str(21) in ListY and str(22) not in ListY and str(23) in ListY and str(24) in ListY and str(22) not in List:
        y = 22
    elif str(21) in ListY and str(22) in ListY and str(23) not in ListY and str(24) in ListY and str(23) not in List:
        y = 23
    elif str(21) in ListY and str(22) in ListY and str(23) in ListY and str(24) not in ListY and str(24) not in List:
        y = 24
    else:
        while str(y) in List:
            y = randint(0, 24)
            y = str(y)
    b = str(y)
    f = open('bot_y_testing.txt', 'w')
    f.write(str(b))
    f.close()

move_y()

