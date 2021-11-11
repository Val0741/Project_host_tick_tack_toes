from tkinter import *
import time
import os
from tkinter import filedialog

root = Tk()
root.title('Тело Игры')
root.geometry('700x600')
canvas = Canvas(root, bg='white', height=600, width=700)
canvas.pack()
frame = Frame(root)
frame.place(relx=0.35, rely=0.8, relwidth=0.25, relheight=0.04)


def check1():
    k = entry1.get()
    entry1.delete(0, END)
    f = open('brbrbr.txt', 'w')
    f.write(str(k))
    f.close()


def check2():
    k = entry2.get()
    entry2.delete(0, END)
    f = open('brbrbr1.txt', 'w')
    f.write(str(k))
    f.close()







def art():
   canvas.create_rectangle(75, 75, 425, 425, width=3)
   canvas.create_line(145, 75, 145, 425, width=3)
   canvas.create_line(215, 75, 215, 425, width=3)
   canvas.create_line(285, 75, 285, 425, width=3)
   canvas.create_line(355, 75, 355, 425, width=3)
   canvas.create_line(75, 145, 425, 145, width=3)
   canvas.create_line(75, 215, 425, 215, width=3)
   canvas.create_line(75, 285, 425, 285, width=3)
   canvas.create_line(75, 355, 425, 355, width=3)


List = []
ListX = []
ListY = []
ListX_1 = []
ListY_1 = []
List_abc = []
List_def = []



def check():
   s = entry.get()
   if s != 0:
       play()


entry = Entry()
entry.place(relx=0.8, rely=0.05)
btn = Button(text='Выберите сколько игр сыграть', command=check)
btn.place(relx=0.8, rely=0)


s = -1


def restart():
    global s
    global m
    m = entry.get()
    if s == -1:
        s = int(m) - 1

    if s != 0:
        s = s - 1
        print(s)
        canvas.delete('all')
        List.clear()
        ListX.clear()
        ListY.clear()
        ListX_1.clear()
        ListY_1.clear()
        art()
        play()


def check3():
    n = entry3.get()
    f = open('abc.txt', 'w')
    f.write(n)
    f.close


entry3 = Entry()
entry3.place(relx=0.8, rely=0.65)
btn3 = Button(text='X', command=check3)
btn3.place(relx=0.8, rely=0.6)


def check4():
    n = entry4.get()
    f = open('def.txt', 'w')
    f.write(n)
    f.close


entry4 = Entry()
entry4.place(relx=0.8, rely=0.75)
btn4 = Button(text='Y', command=check4)
btn4.place(relx=0.8, rely=0.7)



btn3 = Button(text='Продолжить', command=restart)
btn3.place(relx=0.8, rely=0.9)



entry1 = Entry()
entry1.place(relx=0.8, rely=0.25)
btn1 = Button(text='Выберите time_x', command=check1)
btn1.place(relx=0.8, rely=0.2)


entry2 = Entry()
entry2.place(relx=0.8, rely=0.45)
btn2 = Button(text='Выберите time_o', command=check2)
btn2.place(relx=0.8, rely=0.4)


def play():
    t = 1
    while t != 0:
        art()
        if len(List) % 2 == 0:
            tic = time.perf_counter()
            f = open('ListX.txt', 'w')
            for i in List:
                f.write(str(i) + '\n')
            f.close()
            g = open('ListX_1.txt', 'w')
            for j in ListX:
                g.write(str(j) + '\n')
            g.close()
            f = open('abc.txt', 'r')
            x = f.read()
            print(x)
            os.system(x)
            f = open('bot_x_testing.txt', 'r')
            a = f.read()
            f.close()
            x = int(a)
            print('x= ', x)
            List.append(x)
            ListX_1.append(x)
            ListX.append(x)
            if int(x) == 0:
                canvas.create_line(76, 76, 144, 144, width=3, fill='red')
                canvas.create_line(144, 76, 76, 144, width=3, fill='red')
            elif int(x) == 1:
                canvas.create_line(146, 76, 214, 144, width=3, fill='red')
                canvas.create_line(146, 144, 214, 76, width=3, fill='red')
            elif int(x) == 2:
                canvas.create_line(216, 76, 284, 144, width=3, fill='red')
                canvas.create_line(216, 144, 284, 76, width=3, fill='red')
            elif int(x) == 3:
                canvas.create_line(286, 76, 354, 144, width=3, fill='red')
                canvas.create_line(286, 144, 354, 76, width=3, fill='red')
            elif int(x) == 4:
                canvas.create_line(356, 76, 424, 144, width=3, fill='red')
                canvas.create_line(356, 144, 424, 76, width=3, fill='red')
            elif int(x) == 5:
                canvas.create_line(76, 146, 144, 214, width=3, fill='red')
                canvas.create_line(144, 146, 76, 214, width=3, fill='red')
            elif int(x) == 6:
                canvas.create_line(146, 146, 214, 214, width=3, fill='red')
                canvas.create_line(214, 146, 146, 214, width=3, fill='red')
            elif int(x) == 7:
                canvas.create_line(216, 146, 284, 214, width=3, fill='red')
                canvas.create_line(284, 146, 216, 214, width=3, fill='red')
            elif int(x) == 8:
                canvas.create_line(286, 146, 354, 214, width=3, fill='red')
                canvas.create_line(354, 146, 286, 214, width=3, fill='red')
            elif int(x) == 9:
                canvas.create_line(356, 146, 424, 214, width=3, fill='red')
                canvas.create_line(424, 146, 356, 214, width=3, fill='red')
            elif int(x) == 10:
                canvas.create_line(76, 216, 144, 284, width=3, fill='red')
                canvas.create_line(144, 216, 76, 284, width=3, fill='red')
            elif int(x) == 11:
                canvas.create_line(146, 216, 214, 284, width=3, fill='red')
                canvas.create_line(214, 216, 146, 284, width=3, fill='red')
            elif int(x) == 12:
                canvas.create_line(216, 216, 284, 284, width=3, fill='red')
                canvas.create_line(284, 216, 216, 284, width=3, fill='red')
            elif int(x) == 13:
                canvas.create_line(286, 216, 354, 284, width=3, fill='red')
                canvas.create_line(354, 216, 286, 284, width=3, fill='red')
            elif int(x) == 14:
                canvas.create_line(356, 216, 424, 284, width=3, fill='red')
                canvas.create_line(424, 216, 356, 284, width=3, fill='red')
            elif int(x) == 15:
                canvas.create_line(76, 286, 144, 354, width=3, fill='red')
                canvas.create_line(144, 286, 76, 354, width=3, fill='red')
            elif int(x) == 16:
                canvas.create_line(146, 286, 214, 354, width=3, fill='red')
                canvas.create_line(214, 286, 146, 354, width=3, fill='red')
            elif int(x) == 17:
                canvas.create_line(216, 286, 284, 354, width=3, fill='red')
                canvas.create_line(284, 286, 216, 354, width=3, fill='red')
            elif int(x) == 18:
                canvas.create_line(286, 286, 354, 354, width=3, fill='red')
                canvas.create_line(354, 286, 286, 354, width=3, fill='red')
            elif int(x) == 19:
                canvas.create_line(356, 286, 424, 354, width=3, fill='red')
                canvas.create_line(424, 286, 356, 354, width=3, fill='red')
            elif int(x) == 20:
                canvas.create_line(76, 356, 144, 424, width=3, fill='red')
                canvas.create_line(144, 356, 76, 424, width=3, fill='red')
            elif int(x) == 21:
                canvas.create_line(146, 356, 214, 424, width=3, fill='red')
                canvas.create_line(214, 356, 146, 424, width=3, fill='red')
            elif int(x) == 22:
                canvas.create_line(216, 356, 284, 424, width=3, fill='red')
                canvas.create_line(284, 356, 216, 424, width=3, fill='red')
            elif int(x) == 23:
                canvas.create_line(286, 356, 354, 424, width=3, fill='red')
                canvas.create_line(354, 356, 286, 424, width=3, fill='red')
            else:
                canvas.create_line(356, 356, 424, 424, width=3, fill='red')
                canvas.create_line(424, 356, 356, 424, width=3, fill='red')
            toc = time.perf_counter()
            s = (toc - tic)
            print(s)
            f = open('brbrbr.txt', 'r')
            c = f.read()
            f.close()
            k = float(c)
            if s > k:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1...")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                break
        else:
            tec = time.perf_counter()
            f = open('ListY.txt', 'w')
            for i in List:
                f.write(str(i) + '\n')
            f.close()
            g = open('ListY_1.txt', 'w')
            for j in ListY:
                g.write(str(j) + '\n')
            g.close()
            d = open('def.txt', 'r')
            k = d.read()
            d.close()
            os.system(k)
            f = open('bot_y_testing.txt', 'r')
            a = f.read()
            f.close()
            y = int(a)
            print('y= ', y)
            List.append(y)
            ListY_1.append(y)
            ListY.append(y)
            if int(y) == 0:
                canvas.create_oval(76, 76, 144, 144, width=3, outline='blue')
            elif int(y) == 1:
                canvas.create_oval(146, 76, 214, 144, width=3, outline='blue')
            elif int(y) == 2:
                canvas.create_oval(216, 76, 284, 144, width=3, outline='blue')
            elif int(y) == 3:
                canvas.create_oval(286, 76, 354, 144, width=3, outline='blue')
            elif int(y) == 4:
                canvas.create_oval(356, 76, 424, 144, width=3, outline='blue')
            elif int(y) == 5:
                canvas.create_oval(76, 146, 144, 214, width=3, outline='blue')
            elif int(y) == 6:
                canvas.create_oval(146, 146, 214, 214, width=3, outline='blue')
            elif int(y) == 7:
                canvas.create_oval(216, 146, 284, 214, width=3, outline='blue')
            elif int(y) == 8:
                canvas.create_oval(286, 146, 354, 214, width=3, outline='blue')
            elif int(y) == 9:
                canvas.create_oval(356, 146, 424, 214, width=3, outline='blue')
            elif int(y) == 10:
                canvas.create_oval(76, 216, 144, 284, width=3, outline='blue')
            elif int(y) == 11:
                canvas.create_oval(146, 216, 214, 284, width=3, outline='blue')
            elif int(y) == 12:
                canvas.create_oval(216, 216, 284, 284, width=3, outline='blue')
            elif int(y) == 13:
                canvas.create_oval(286, 216, 354, 284, width=3, outline='blue')
            elif int(y) == 14:
                canvas.create_oval(356, 216, 424, 284, width=3, outline='blue')
            elif int(y) == 15:
                canvas.create_oval(76, 286, 144, 354, width=3, outline='blue')
            elif int(y) == 16:
                canvas.create_oval(146, 286, 214, 354, width=3, outline='blue')
            elif int(y) == 17:
                canvas.create_oval(216, 286, 284, 354, width=3, outline='blue')
            elif int(y) == 18:
                canvas.create_oval(286, 286, 354, 354, width=3, outline='blue')
            elif int(y) == 19:
                canvas.create_oval(356, 286, 424, 354, width=3, outline='blue')
            elif int(y) == 20:
                canvas.create_oval(76, 356, 144, 424, width=3, outline='blue')
            elif int(y) == 21:
                canvas.create_oval(146, 356, 214, 424, width=3, outline='blue')
            elif int(y) == 22:
                canvas.create_oval(216, 356, 284, 424, width=3, outline='blue')
            elif int(y) == 23:
                canvas.create_oval(286, 356, 354, 424, width=3, outline='blue')
            else:
                canvas.create_oval(356, 356, 424, 424, width=3, outline='blue')
            tac = time.perf_counter()
            z = (toc - tic)
            print(z)
            p = open('brbrbr1.txt', 'r')
            h = p.read()
            p.close()
            n = float(h)
            if z > n:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2...")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                break
        f = open('bot_x_testing.txt', 'r')
        a = f.read()
        f.close()
        x = int(a)
        w = open('bot_y_testing.txt', 'r')
        d = w.read()
        w.close()
        y = int(d)
        if x == 0 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(76, 76, 144, 144, width=3)
            canvas.create_line(144, 76, 76, 144, width=3)
            q = open('List.txt', 'a')
            for o in List:
                q.write(str(o) + '\n')
                q.write('\n')
                q.write('    ')
            t = 0
            break
        elif x == 1 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(146, 76, 214, 144, width=3)
            canvas.create_line(146, 144, 214, 76, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 2 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(216, 76, 284, 144, width=3)
            canvas.create_line(216, 144, 284, 76, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 3 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(286, 76, 354, 144, width=3)
            canvas.create_line(286, 144, 354, 76, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 4 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(356, 76, 424, 144, width=3)
            canvas.create_line(356, 144, 424, 76, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 5 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(76, 146, 144, 214, width=3)
            canvas.create_line(144, 146, 76, 214, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 6 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(146, 146, 214, 214, width=3)
            canvas.create_line(214, 146, 146, 214, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 7 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(216, 146, 284, 214, width=3)
            canvas.create_line(284, 146, 216, 214, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 8 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(286, 146, 354, 214, width=3)
            canvas.create_line(354, 146, 286, 214, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 9 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(356, 146, 424, 214, width=3)
            canvas.create_line(424, 146, 356, 214, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 10 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(76, 216, 144, 284, width=3)
            canvas.create_line(144, 216, 76, 284, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 11 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(146, 216, 214, 284, width=3)
            canvas.create_line(214, 216, 146, 284, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 12 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(216, 216, 284, 284, width=3)
            canvas.create_line(284, 216, 216, 284, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 13 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(286, 216, 354, 284, width=3)
            canvas.create_line(354, 216, 286, 284, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 14 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(356, 216, 424, 284, width=3)
            canvas.create_line(424, 216, 356, 284, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 15 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(76, 286, 144, 354, width=3)
            canvas.create_line(144, 286, 76, 354, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 16 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(146, 286, 214, 354, width=3)
            canvas.create_line(214, 286, 146, 354, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 17 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(216, 286, 284, 354, width=3)
            canvas.create_line(284, 286, 216, 354, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 18 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(286, 286, 354, 354, width=3)
            canvas.create_line(354, 286, 286, 354, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 19 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(356, 286, 424, 354, width=3)
            canvas.create_line(424, 286, 356, 354, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 20 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(76, 356, 144, 424, width=3)
            canvas.create_line(144, 356, 76, 424, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 21 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(146, 356, 214, 424, width=3)
            canvas.create_line(214, 356, 146, 424, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 22 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(216, 356, 284, 424, width=3)
            canvas.create_line(284, 356, 216, 424, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 23 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(286, 356, 354, 424, width=3)
            canvas.create_line(354, 356, 286, 424, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        elif x == 24 and ListX_1.count(x) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
            canvas.create_line(356, 356, 424, 424, width=3)
            canvas.create_line(424, 356, 356, 424, width=3)
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            break
        if x == 0 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 1 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 2 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 3 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 4 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 5 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 6 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 7 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 8 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 9 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 10 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 11 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 12 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 13 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 14 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 15 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 16 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 17 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 18 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 19 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 20 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 21 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 22 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 23 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        elif x == 24 and ListX_1.count(x) < 2:
            ListY_1.append(x)
            if ListY_1.count(x) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_1!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                break
            ListY_1.remove(x)
        if y == 0 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')

            t = 0
            canvas.create_oval(76, 76, 144, 144, width=3)
            break
        elif y == 1 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(146, 76, 214, 144, width=3)
            break
        elif y == 2 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(216, 76, 284, 144, width=3)
            break
        elif y == 3 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(286, 76, 354, 144, width=3)
            break
        elif y == 4 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(356, 76, 424, 144, width=3)
            break
        elif y == 5 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(76, 146, 144, 214, width=3)
            break
        elif y == 6 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(146, 146, 214, 214, width=3)
            break
        elif y == 7 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(216, 146, 284, 214, width=3)
            break
        elif y == 8 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(286, 146, 354, 214, width=3)
            break
        elif y == 9 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(356, 146, 424, 214, width=3)
            break
        elif y == 10 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(76, 216, 144, 284, width=3)
            break
        elif y == 11 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(146, 216, 214, 284, width=3)
            break
        elif y == 12 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(216, 216, 284, 284, width=3)
            break
        elif y == 13 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(286, 216, 354, 284, width=3)
            break
        elif y == 14 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(356, 216, 424, 284, width=3)
            break
        elif y == 15 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(76, 286, 144, 354, width=3)
            break
        elif y == 16 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(146, 286, 214, 354, width=3)
            break
        elif y == 17 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(216, 286, 284, 354, width=3)
            break
        elif y == 18 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(286, 286, 354, 354, width=3)
            break
        elif y == 19 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(356, 286, 424, 354, width=3)
            break
        elif y == 20 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(76, 356, 144, 424, width=3)
            break
        elif y == 21 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(146, 356, 214, 424, width=3)
            break
        elif y == 22 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(216, 356, 284, 424, width=3)
            break
        elif y == 23 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(286, 356, 354, 424, width=3)
            break
        elif y == 24 and ListY_1.count(y) > 1:
            canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            t = 0
            canvas.create_oval(356, 356, 424, 424, width=3)
            break
        if y == 0 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(76, 76, 144, 144, width=3)
                break
            ListX_1.remove(y)
        elif y == 1 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(146, 76, 214, 144, width=3)
                break
            ListX_1.remove(y)
        elif y == 2 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(216, 76, 284, 144, width=3)
                break
            ListX_1.remove(y)
        elif y == 3 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(286, 76, 354, 144, width=3)
                break
            ListX_1.remove(y)
        elif y == 4 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(356, 76, 424, 144, width=3)
                break
            ListX_1.remove(y)
        elif y == 5 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(76, 146, 144, 214, width=3)
                break
            ListX_1.remove(y)
        elif y == 6 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(146, 146, 214, 214, width=3)
                break
            ListX_1.remove(y)
        elif y == 7 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(216, 146, 284, 214, width=3)
                break
            ListX_1.remove(y)
        elif y == 8 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(286, 146, 354, 214, width=3)
            ListX_1.remove(y)
        elif y == 9 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                for o in List:
                    q.write('    ')
                    for o in List:
                        q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(356, 146, 424, 214, width=3)
                break
            ListX_1.remove(y)
        elif y == 10 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                for o in List:
                    q.write('    ')
                    for o in List:
                        q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(76, 216, 144, 284, width=3)
                break
            ListX_1.remove(y)
        elif y == 11 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                for o in List:
                    q.write('    ')
                    for o in List:
                        q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(146, 216, 214, 284, width=3)
                break
            ListX_1.remove(y)
        elif y == 12 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                for o in List:
                    q.write('    ')
                    for o in List:
                        q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(216, 216, 284, 284, width=3)
                break
            ListX_1.remove(y)
        elif y == 13 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(286, 216, 354, 284, width=3)
                break
            ListX_1.remove(y)
        elif y == 14 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(356, 216, 424, 284, width=3)
                break
            ListX_1.remove(y)
        elif y == 15 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(76, 286, 144, 354, width=3)
                break
            ListX_1.remove(y)
        elif y == 16 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(146, 286, 214, 354, width=3)
                break
            ListX_1.remove(y)
        elif y == 17 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(216, 286, 284, 354, width=3)
                break
            ListX_1.remove(y)
        elif y == 18 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(286, 286, 354, 354, width=3)
                break
            ListX_1.remove(y)
        elif y == 19 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(356, 286, 424, 354, width=3)
                break
            ListX_1.remove(y)
        elif y == 20 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(76, 356, 144, 424, width=3)
                break
            ListX_1.remove(y)
        elif y == 21 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(146, 356, 214, 424, width=3)
                break
            ListX_1.remove(y)
        elif y == 22 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(216, 356, 284, 424, width=3)
                break
            ListX_1.remove(y)
        elif y == 23 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(286, 356, 354, 424, width=3)
                break
            ListX_1.remove(y)
        elif y == 24 and ListY_1.count(y) < 2:
            ListX_1.append(y)
            if ListX_1.count(y) > 1:
                canvas.create_text(500, 97, text="Техническое поражение Бот_2!")
                q = open('List.txt', 'a')
                q.write('    ')
                for o in List:
                    q.write(str(o) + '\n')
                t = 0
                canvas.create_oval(356, 356, 424, 424, width=3)
                break
            ListX_1.remove(y)
        if 0 in ListX and 1 in ListX and 2 in ListX and 3 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 0 in ListX and 5 in ListX and 10 in ListX and 15 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 0 in ListX and 6 in ListX and 12 in ListX and 18 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 1 in ListX and 2 in ListX and 3 in ListX and 4 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 1 in ListX and 7 in ListX and 13 in ListX and 19 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 1 in ListX and 6 in ListX and 11 in ListX and 16 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 2 in ListX and 7 in ListX and 12 in ListX and 17 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 3 in ListX and 8 in ListX and 13 in ListX and 18 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 3 in ListX and 7 in ListX and 11 in ListX and 15 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 4 in ListX and 9 in ListX and 14 in ListX and 19 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 4 in ListX and 8 in ListX and 12 in ListX and 16 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 5 in ListX and 6 in ListX and 7 in ListX and 8 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 5 in ListX and 11 in ListX and 17 in ListX and 23 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 5 in ListX and 10 in ListX and 15 in ListX and 20 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 8 in ListX and 12 in ListX and 16 in ListX and 20 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 6 in ListX and 11 in ListX and 16 in ListX and 21 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 6 in ListX and 7 in ListX and 8 in ListX and 9 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 6 in ListX and 12 in ListX and 18 in ListX and 24 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 7 in ListX and 12 in ListX and 17 in ListX and 22 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 8 in ListX and 13 in ListX and 18 in ListX and 23 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 9 in ListX and 14 in ListX and 19 in ListX and 24 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 9 in ListX and 13 in ListX and 17 in ListX and 21 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 10 in ListX and 11 in ListX and 12 in ListX and 13 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 11 in ListX and 12 in ListX and 13 in ListX and 14 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 15 in ListX and 16 in ListX and 17 in ListX and 18 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 16 in ListX and 17 in ListX and 18 in ListX and 19 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 20 in ListX and 21 in ListX and 22 in ListX and 23 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 21 in ListX and 22 in ListX and 23 in ListX and 24 in ListX:
            canvas.create_text(500, 97, text="Победа Бот_1!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif len(List) == 25:
            canvas.create_text(500, 97, text="Ничья")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 0 in ListY and 1 in ListY and 2 in ListY and 3 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 0 in ListY and 5 in ListY and 10 in ListY and 15 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 0 in ListY and 6 in ListY and 12 in ListY and 18 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 1 in ListY and 2 in ListY and 3 in ListY and 4 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 1 in ListY and 7 in ListY and 13 in ListY and 19 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 1 in ListY and 6 in ListY and 11 in ListY and 16 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 2 in ListY and 7 in ListY and 12 in ListY and 17 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 3 in ListY and 8 in ListY and 13 in ListY and 18 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 3 in ListY and 7 in ListY and 11 in ListY and 15 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 4 in ListY and 9 in ListY and 14 in ListY and 19 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 4 in ListY and 8 in ListY and 12 in ListY and 16 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 5 in ListY and 6 in ListY and 7 in ListY and 8 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 5 in ListY and 11 in ListY and 17 in ListY and 23 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 5 in ListY and 10 in ListY and 15 in ListY and 20 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 8 in ListY and 12 in ListY and 16 in ListY and 20 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 6 in ListY and 11 in ListY and 16 in ListY and 21 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 6 in ListY and 7 in ListY and 8 in ListY and 9 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 6 in ListY and 12 in ListY and 18 in ListY and 24 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 7 in ListY and 12 in ListY and 17 in ListY and 22 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 8 in ListY and 13 in ListY and 18 in ListY and 23 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 9 in ListY and 14 in ListY and 19 in ListY and 24 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 9 in ListY and 13 in ListY and 17 in ListY and 21 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 10 in ListY and 11 in ListY and 12 in ListY and 13 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 11 in ListY and 12 in ListY and 13 in ListY and 14 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 15 in ListY and 16 in ListY and 17 in ListY and 18 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 16 in ListY and 17 in ListY and 18 in ListY and 19 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 20 in ListY and 21 in ListY and 22 in ListY and 23 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        elif 21 in ListY and 22 in ListY and 23 in ListY and 24 in ListY:
            canvas.create_text(500, 97, text="Победа Бот_2!")
            t = 0
            q = open('List.txt', 'a')
            q.write('    ')
            for o in List:
                q.write(str(o) + '\n')
            List.clear()
            ListX.clear()
            ListY.clear()
        else:
            t = 1



root.mainloop()

