from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Developer's Info")


        title_lbl=Label(self.root,text="...DEVELOPER...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=30,width=1350,height=45)
        
        main_frame=Frame(self.root, bd=2)
        main_frame.place(x=20,y=120,width=1300,height=620)        


        #Right LabelFrame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="About Me",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="purple")
        Right_frame.place(x=250,y=0,width=850,height=470)
        
        l1_label=Label(Right_frame,text="Hi guys my name is Ravi Negi, currently pursuing B.Tech in Computer Science from Graphic", font=("Bahnschrift Condensed",20,"bold"),bg="white", fg="black")
        l1_label.place(x=0,y=40)

        l2_label=Label(Right_frame,text="Era Hill University. I'm currently in 3rd year (5th sem).I have worked on Face Recognition", font=("Bahnschrift Condensed",20,"bold"),bg="white", fg="black")
        l2_label.place(x=0,y=100)

        l3_label=Label(Right_frame,text="Attendance System using Python, tkinter", font=("Bahnschrift Condensed",20,"bold"),bg="white", fg="black")
        l3_label.place(x=0,y=160)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
