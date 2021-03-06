from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help_desk import Help_desk
import os


def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")



        img = Image.open(r"Images\style.jpg")
        img = img.resize((450,100), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=100)

        

        img1 = Image.open(r"Images\style.jpg")
        img1 = img1.resize((450,100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=450, y=0, width=450, height=100)



        img2 = Image.open(r"Images\style.jpg")
        img2 = img2.resize((450,100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=450, height=100)



        #bg img

        img3 = Image.open(r"Images\background.jpg")
        img3 = img3.resize((1250,600), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=50, y=125, width=1250, height=550)

        title_lbl = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE", font = ("arial", 30, "bold"), bg = "white", fg = "black")
        title_lbl.place(x=0, y=0, width=1246, height=45)



        #student button

        img4 = Image.open(r"Images\student.jpg")
        img4 = img4.resize((150,125), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100, width=150, height=125)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font = ("arial narrow", 12, "bold"), bg = "grey", fg = "white")
        b1_1.place(x=100, y=225, width=150, height=30)



        #detect face button

        img5 = Image.open(r"Images\face-detection.png")
        img5 = img5.resize((150,125), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=400, y=100, width=150, height=125)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font = ("arial", 12, "bold"), bg = "grey", fg = "white")
        b1_1.place(x=400, y=225, width=150, height=30)



        #Attendance button

        img6 = Image.open(r"Images\attendance.png")
        img6 = img6.resize((150,125), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=700, y=100, width=150, height=125)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font = ("arial", 12, "bold"), bg = "grey", fg = "white")
        b1_1.place(x=700, y=225, width=150, height=30)



        #Help button

        img7 = Image.open(r"Images\help.png")
        img7 = img7.resize((150,125), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_desk_data)
        b1.place(x=1000, y=100, width=150, height=125)

        b1_1 = Button(bg_img, text="Help", cursor="hand2", command=self.help_desk_data, font = ("arial", 12, "bold"), bg = "grey", fg = "white")
        b1_1.place(x=1000, y=225, width=150, height=30)



        #train face button

        img8 = Image.open(r"Images\train-data.png")
        img8 = img8.resize((150,125), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b1.place(x=100, y=350, width=150, height=125)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font = ("arial", 12, "bold"), bg = "grey", fg = "white")
        b1_1.place(x=100, y=475, width=150, height=30)



        #Photos button

        img9 = Image.open(r"Images\photos.png")
        img9 = img9.resize((150,125), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=400, y=350, width=150, height=125)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font = ("arial", 12, "bold"), bg = "grey", fg = "white")
        b1_1.place(x=400, y=475, width=150, height=30)



        #Developer button

        img10 = Image.open(r"Images\developer.jpg")
        img10 = img10.resize((150,125), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b1.place(x=700, y=350, width=150, height=125)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font = ("arial", 12, "bold"), bg = "grey", fg = "white")
        b1_1.place(x=700, y=475, width=150, height=30)



        #Exit button

        img11 = Image.open(r"Images\exit.png")
        img11 = img11.resize((150,125), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.Exit)
        b1.place(x=1000, y=350, width=150, height=125)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.Exit, font = ("arial", 12, "bold"), bg = "grey", fg = "white")
        b1_1.place(x=1000, y=475, width=150, height=30)


        changeOnHover(b1_1, "#444444", "grey")

    def open_img(self):
        os.startfile("data")

    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("Face Recognition","Are you sure :(", parent = self.root)
        if self.Exit > 0:
            self.root.destroy()
        else:
            return

    # ================ Function Buttons ================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)


    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    
    def help_desk_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help_desk(self.new_window)






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
