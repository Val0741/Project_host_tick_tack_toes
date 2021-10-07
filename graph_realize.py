from tkinter import*

root=Tk()

#################################################
root.title('Графическая реализация окна')
root.geometry('700x600')

#################################################
canvas=Canvas(root,height=500,width=500)
canvas.pack()
frame=Frame(root)
frame.place(relx=0.424,rely=0.9,relwidth=0.15,relheight=0.15)

##################################################
canvas.create_rectangle(75,75,425,425)
canvas.create_line(145,75,145,425)
canvas.create_line(215,75,215,425)
canvas.create_line(285,75,285,425)
canvas.create_line(355,75,355,425)
canvas.create_line(75,145,425,145)
canvas.create_line(75,215,425,215)
canvas.create_line(75,285,425,285)
canvas.create_line(75,355,425,355)

########################
btn=Button(frame,text='Перезапуск',bg='blue')
btn.pack()

root.mainloop()#запуск постоянного цикла