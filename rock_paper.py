import tkinter as tk
from tkinter import messagebox
import random as rand 
scoreuser=0
scorecomp=0
display="                      "
class rock_paper_scissor:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("500x500")
        self.root.configure(bg="black")
        self.test=tk.PhotoImage(file ="Screenshot 2023-12-15 223908.png")
        self.label=tk.Label(text="ROCK PAPER SCISSOR",bg="black",fg="white")
        self.label.pack()
        self.labell=tk.Label(image=self.test,width=500,height=500)
        self.labell.pack()
        self.startbutton=tk.Button(self.root,bg="black", fg="white" ,text="START",font=("jokerman",20),command=self.startgame)
        self.startbutton.place(relx=0.35,rely=0.7)
        self.root.mainloop()
        
    def startgame(self):
        self.labell.destroy()
        self.startbutton.destroy()
        self.messagelabel=tk.Label(bg="black",fg="#FF7A33",text="get ready \n for an insane ride")
        self.messagelabel.pack(pady=100)
        self.check_state1=tk.IntVar()
        self.check_state2=tk.IntVar()
        self.check1=tk.Checkbutton(self.root,variable=self.check_state1,text="do you consent to having your mind blown",bg="black",fg="#FF7A33")
        self.check1.pack()
        self.check2=tk.Checkbutton(self.root,variable=self.check_state2,text="do you consent to giving all your wealth to hriday patney",bg="black",fg="#FF7A33")
        self.check2.pack()
        self.btnplay=tk.Button(self.root,bg="black",text="enter",fg="#FF7A33",font=("jokerman",20),command=self.setgame)
        self.btnplay.pack()
    def setgame(self):
        if self.check_state1.get()==1 and self.check_state2.get()==1:
            self.check1.destroy()
            self.check2.destroy()
            self.messagelabel.destroy()
            self.btnplay.destroy()
            self.makegame()


        else :
            messagebox.showerror("ERROR",message="TICK ALL BOXES")
    def makegame(self):
        global scorecomp
        global scoreuser
        self.buttonframe=tk.Frame(self.root)
        self.buttonframe.columnconfigure(0,weight=1)
        self.buttonframe.columnconfigure(1,weight=1)
        self.buttonframe.columnconfigure(2,weight=1)

        self.btnrock=tk.Button(self.buttonframe,text="rock",command= lambda : self.game(0))
        self.btnpaper=tk.Button(self.buttonframe,text="paper",command =lambda : self.game(1))
        self.btnscissor=tk.Button(self.buttonframe,text="scissor",command=lambda:self.game(2))
        self.btnrock.grid(row=0,column=0,sticky=tk.W+tk.E)
        self.btnpaper.grid(row=0,column=1,sticky=tk.W+tk.E)
        self.btnscissor.grid(row=0,column=2,sticky=tk.W+tk.E)
        self.buttonframe.place(x=190,y=250)
        self.showscore()
    
    def showscore(self):
        global display
        self.displaylabel=tk.Label(text=display)
        self.displaylabel.pack()
        self.scorelabeluser=tk.Label(text="player: "+ str(scoreuser))
        self.scorelabeluser.pack()
        self.scorelabelcomp=tk.Label(text="computer: "+str(scorecomp))
        self.scorelabelcomp.pack()    
    def game(self,n):
        global scorecomp
        global scoreuser
        global display
    
        self.m=rand.randint(0,2)
        if n==self.m:
            display="TIE"
        if n==0 and self.m==1:
            scorecomp+=1#rock and paper
            display="player:"+"rock "+"computer:"+"paper"
        if n==0 and self.m==2:
            scoreuser+=1#rock and scissor 
            display="player:"+"rock "+"computer:"+"scissor"
        if n==1 and self.m==0:
            scoreuser+=1#paper and rock
            display="player:"+"paper "+"computer:"+"rock"
        if n==1 and self.m==2:
            scorecomp+=1#paper and scissor
            display="player:"+"paper "+"computer:"+"scissor"
        if n==2 and self.m==0:
            scorecomp+=1#scissor and rock
            display="player:"+"scissor "+"computer:"+"rock"
        if n==2 and self.m==1:
            scoreuser+=1#scissor and paper
            display="player:"+"scissor "+"computer:"+"paper"
        
        self.scorelabelcomp.destroy()
        self.scorelabeluser.destroy()
        self.displaylabel.destroy()
        self.showscore()

    


        
game=rock_paper_scissor()

