from tkinter import *

import tkinter.messagebox
ttt = Tk()
ttt.title("Tic Tac Toe Game")

plyrx = StringVar()
plyry = StringVar()

bclk = True
count = 0


def disableBtn():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def btnClk(btn):
    global bclk, count,  plyrx, plyry
    if btn['text'] == " " and bclk == True:
        btn.configure(text="X")
        bclk = False
        plyrx = " X Wins!"
        plyry = " O Wins!"
        chkWin()
        count += 1

    elif btn['text'] == " " and bclk == False:
        btn.configure(text="O")
        bclk = True
        chkWin()
        count += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Choosed!")


def chkWin():
    if (button1['text'] == button2['text'] and button1['text'] == button3['text'] and button1['text'] == 'X'
        or button4['text'] == button5['text'] and button4['text'] == button6['text'] and button4['text'] == 'X'
        or button7['text'] == button8['text'] and button7['text'] == button9['text'] and button7['text'] == 'X'
        or button1['text'] == button4['text'] and button1['text'] == button7['text'] and button1['text'] == 'X'
        or button2['text'] == button5['text'] and button2['text'] == button8['text'] and button2['text'] == 'X'
        or button3['text'] == button6['text'] and button3['text'] == button9['text'] and button3['text'] == 'X'
        or button1['text'] == button5['text'] and button1['text'] == button9['text'] and button1['text'] == 'X'
        or button7['text'] == button5['text'] and button7['text'] == button3['text'] and button7['text'] == 'X'
    ):
        disableBtn()
        tkinter.messagebox.showinfo("Tic-Tac-Toe Game", plyrx)

    elif (button1['text'] == button2['text'] and button1['text'] == button3['text'] and button1['text'] == 'O'
          or button4['text'] == button5['text'] and button4['text'] == button6['text'] and button4['text'] == 'O'
          or button7['text'] == button8['text'] and button7['text'] == button9['text'] and button7['text'] == 'O'
          or button1['text'] == button4['text'] and button1['text'] == button7['text'] and button1['text'] == 'O'
          or button2['text'] == button5['text'] and button2['text'] == button8['text'] and button2['text'] == 'O'
          or button3['text'] == button6['text'] and button3['text'] == button9['text'] and button3['text'] == 'O'
          or button1['text'] == button5['text'] and button1['text'] == button9['text'] and button1['text'] == 'O'
          or button7['text'] == button5['text'] and button7['text'] == button3['text'] and button7['text'] == 'O'
    ):
        disableBtn()
        tkinter.messagebox.showinfo("Tic-Tac-Toe Game", plyry)

    elif count == 8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe Game", "Tie Game")


buttons = StringVar()

button1 = Button(ttt, text=' ', font='Times 10 bold', bg='white', fg='green', height=4, width=8, command=lambda: btnClk(button1))
button1.grid(row=0, column=0)

button2 = Button(ttt, text=' ', font='Times 10 bold', bg='white', fg='green', height=4, width=8, command=lambda: btnClk(button2))
button2.grid(row=0, column=1)

button3 = Button(ttt, text=' ',font='Times 10 bold', bg='white', fg='green', height=4, width=8, command=lambda: btnClk(button3))
button3.grid(row=0, column=2)

button4 = Button(ttt, text=' ', font='Times 10 bold', bg='white', fg='green', height=4, width=8, command=lambda: btnClk(button4))
button4.grid(row=1, column=0)

button5 = Button(ttt, text=' ', font='Times 10 bold', bg='white', fg='green', height=4, width=8, command=lambda: btnClk(button5))
button5.grid(row=1, column=1)

button6 = Button(ttt, text=' ', font='Times 10 bold', bg='white', fg='green', height=4, width=8, command=lambda: btnClk(button6))
button6.grid(row=1, column=2)

button7 = Button(ttt, text=' ', font='Times 10 bold', bg='white', fg='green', height=4, width=8, command=lambda: btnClk(button7))
button7.grid(row=2, column=0)

button8 = Button(ttt, text=' ', font='Times 10 bold', bg='white', fg='green', height=4, width=8, command=lambda: btnClk(button8))
button8.grid(row=2, column=1)

button9 = Button(ttt, text=' ', font='Times 10 bold', bg='white', fg='green', height=4, width=8, command=lambda: btnClk(button9))
button9.grid(row=2, column=2)

ttt.mainloop()
