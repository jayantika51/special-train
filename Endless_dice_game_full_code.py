from tkinter import*
from PIL import ImageTk, Image 
root=Tk()

root.title("endless dice game")
root.geometry("600x400")

root.configure(background="royal blue")

img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player1=Label(root, text = "player 1", bg = "pink", fg = "blue")
player1.place(relx = 0.1, rely = 0.3 , anchor = CENTER)

player2=Label(root, text = "player 2", bg = "pink", fg = "blue")
player2.place(relx = 0.9, rely = 0.3 , anchor = CENTER)



player_1_score_label = Label(root, bg = "pink", fg = "blue")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor = CENTER)

player_2_score_label = Label(root, bg = "pink", fg = "blue")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor = CENTER)



random_dice_label = Label(root, bg = "pink", fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5 , anchor = CENTER)


root.mainloop()
