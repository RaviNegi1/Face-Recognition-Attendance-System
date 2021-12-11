from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import data
import pymysql
import cv2
import os
import numpy as np

def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")





        title_lbl = Label(self.root, text="TRAIN  DATA  SET", font = ("arial", 30, "bold"), bg = "white", fg = "black")
        title_lbl.place(x=0, y=0, width=1246, height=45)

        #bg img

        img3 = Image.open(r"Images\background.jpg")
        img3 = img3.resize((1250,600), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=50, y=125, width=1250, height=550)

        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font = ("arial narrow", 50, "bold"), bg = "#333333", fg = "white")
        b1_1.place(x=300, y=275, width=650, height=250)

        
        changeOnHover(b1_1, "#444444", "#333333")




    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)


        # =================Train the classifier and save=================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!!")










if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
