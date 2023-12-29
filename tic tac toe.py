from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

#defining restart
def restart():
    global flag
    flag=0
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
    button10["text"]="Restart"
    
    button1.configure(background='white')
    button2.configure(background='white')
    button3.configure(background='white')
    button4.configure(background='white')
    button5.configure(background='white')
    button6.configure(background='white')
    button7.configure(background='white')
    button8.configure(background='white')
    button9.configure(background='white')
    button10.configure(background='white')
    return(btnClick)


#defining button clicks
def btnClick(buttons):
    global bclick,flag,player2_name, player1_name, playerb, pa
    #click prints x
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1

    #click prints o   
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    #print if button is already clicked    
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


#checking wins
def checkForWin():
    #win check for x
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
        button1.configure(background='red')
        button2.configure(background='red')
        button3.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        return(restart)
                          
    elif(button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'):
        button4.configure(background='red')
        button5.configure(background='red')
        button6.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        return(restart)
        
    elif(button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X'):
        button7.configure(background='red')
        button8.configure(background='red')
        button9.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        return(restart)
        
    elif(button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
        button1.configure(background='red')
        button5.configure(background='red')
        button9.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        return(restart)
        
    elif(button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        button3.configure(background='red')
        button5.configure(background='red')
        button7.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        return(restart)
        
    elif(button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
        button1.configure(background='red')
        button4.configure(background='red')
        button7.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        return(restart)

    elif(button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
        button2.configure(background='red')
        button5.configure(background='red')
        button8.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        return(restart)
        
    elif(button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        button3.configure(background='red')
        button6.configure(background='red')
        button9.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        return(restart)
        
    #check for o
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'):
        button1.configure(background='red')
        button2.configure(background='red')
        button3.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        return(restart)
        
    elif(button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'):
        button4.configure(background='red')
        button5.configure(background='red')
        button6.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        return(restart)
        
    elif( button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' ):
        button7.configure(background='red')
        button8.configure(background='red')
        button9.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        return(restart)
        
    elif(button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' ):
        button1.configure(background='red')
        button5.configure(background='red')
        button9.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        return(restart)
        
    elif(button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' ):
        button3.configure(background='red')
        button5.configure(background='red')
        button7.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        return(restart)

    elif(button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'):
        button1.configure(background='red')
        button4.configure(background='red')
        button7.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        return(restart)
        
    elif(button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'):
        button2.configure(background='red')
        button5.configure(background='red')
        button8.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        return(restart)
        
    elif(button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        button3.configure(background='red')
        button6.configure(background='red')
        button9.configure(background='red')
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        return(restart)

    #check for tie
    elif(flag==8) :
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        return(restart)


buttons = StringVar()

#taking player one name
label = Label( tk, text="Player 1 :", font='Times 20 bold', bg='white', fg='black', height=0, width=9)
label.grid(row=1, column=0)

#taking player two name
label = Label( tk, text="Player 2 :", font='Times 20 bold', bg='white', fg='black', height=0, width=9)
label.grid(row=2, column=0)

#setting buttons
button1 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=9, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=9, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='white', fg='black', height=4, width=9, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=9, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=9, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=9, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=9, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=9, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=9, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

button10= Button(tk, text='Reset',font='Times 20 bold', bg='grey', fg='black', height=1, width=9, command=restart)
button10.grid(row=6, column=1)

tk.mainloop()
