from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import data
import pymysql
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="FACE  RECOGNITION", font = ("arial", 30, "bold"), bg = "white", fg = "black")
        title_lbl.place(x=0, y=0, width=1246, height=45)

        #bg img

        img3 = Image.open(r"Images\background.jpg")
        img3 = img3.resize((1250,600), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=50, y=125, width=1250, height=550)


        b1_1 = Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2", font = ("arial narrow", 50, "bold"), bg = "#333333", fg = "white")
        b1_1.place(x=300, y=275, width=650, height=250)

        changeOnHover(b1_1, "#444444", "#333333")



    #===========Attendance==============
    def attendance(self,i,r,n,d):
        with open("Ravi.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dt},{d1},Present")





    # =============Face Recognition=============
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)   
            
            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=pymysql.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()


                my_cursor.execute("select id from student where id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select rollno from student where id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select name from student where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select dep from student where id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                

                if confidence>77:
                    cv2.putText(img,f"id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"rollno:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                
                coord=[x,y,w,h]     
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognizer",img)

            if cv2.waitKey(1)==13:
              break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
