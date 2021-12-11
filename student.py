from os import pardir
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2

def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")


        # ===========Variables===========
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_rollno=StringVar()
        self.var_fathername=StringVar()
        self.var_sec=StringVar()
        self.var_course=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_email=StringVar()
        self.var_phoneno=StringVar()
        self.var_address=StringVar()
        self.var_dob=StringVar()
        self.var_teachername=StringVar()


        img = Image.open(r"C:\Users\RAVI\Desktop\face-recognition-attendance-system\Images\style.jpg")
        img = img.resize((450,100), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=100)

        

        img1 = Image.open(r"C:\Users\RAVI\Desktop\face-recognition-attendance-system\Images\style.jpg")
        img1 = img1.resize((450,100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=450, y=0, width=450, height=100)



        img2 = Image.open(r"C:\Users\RAVI\Desktop\face-recognition-attendance-system\Images\style.jpg")
        img2 = img2.resize((450,100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=450, height=100)



        #bg img

        img3 = Image.open(r"C:\Users\RAVI\Desktop\face-recognition-attendance-system\Images\background.jpg")
        img3 = img3.resize((1250,600), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=50, y=125, width=1250, height=550)

        title_lbl = Label(bg_img, text="STUDENT  DETAILS", font = ("arial", 30, "bold"), bg = "white", fg = "black")
        title_lbl.place(x=0, y=0, width=1246, height=45)



        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=47, width=1246, height=499)



        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=625, height=475)


        # current course

        Current_Course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Details", font=("times new roman", 12, "bold"))
        Current_Course_frame.place(x=10, y=10, width=600, height=120)



        # course

        course_label = Label(Current_Course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=0, padx=10, sticky=W)

        course_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_course, font=("times new roman", 12), state="readonly", width=20)
        course_combo["values"] = ("Select Course","B.Tech","B.Sc","B.Com","BCA","MBA")
        course_combo.current(0)
        course_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        # department

        dep_label = Label(Current_Course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=2, padx=10, sticky=W)

        dep_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_dep, font=("times new roman", 12), state="readonly", width=20)
        dep_combo["values"] = ("Select Department","Computer Science","Mechanical Engineering","Civil Engineering","IT","Specialization")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)




        # year

        year_label = Label(Current_Course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_year, font=("times new roman", 12), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)



        # semester

        semester_label = Label(Current_Course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_sem, font=("times new roman", 12), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)



        # Class Student Information

        Class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Details", font=("times new roman", 12, "bold"))
        Class_Student_frame.place(x=10, y=140, width=600, height=300)



        # student id

        studentID_label = Label(Class_Student_frame, text="Student's ID:", font=("times new roman", 13, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_id, width=19, font=("times new roman", 11))
        studentID_entry.grid(row=0, column=1, padx=0, pady=5, sticky=W)



        # student's name

        studentName_label = Label(Class_Student_frame, text="Student's Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_name, width=19, font=("times new roman", 11))
        studentName_entry.grid(row=0, column=3, padx=0, pady=5, sticky=W)



        # Roll no

        roll_no_label = Label(Class_Student_frame, text="University Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_rollno, width=19, font=("times new roman", 11))
        roll_no_entry.grid(row=1, column=1, padx=0, pady=5, sticky=W)



        # Section

        sec_label=Label(Class_Student_frame, text="Section:", font=("times new roman", 12, "bold"),bg="white", fg="black")
        sec_label.grid(row=1,column=2,padx=15,sticky=W)

        sec_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_sec, width=19, font=("times new roman", 11))
        sec_entry.grid(row=1, column=3, padx=0, pady=5, sticky=W)



        # Father's Name

        father_label = Label(Class_Student_frame, text="Father's Name:", font=("times new roman", 13, "bold"), bg="white")
        father_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        father_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_fathername, width=19, font=("times new roman", 11))
        father_entry.grid(row=2, column=1, padx=0, pady=5, sticky=W)



        # DOB

        dob_label = Label(Class_Student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_dob, width=19, font=("times new roman", 11))
        dob_entry.grid(row=2, column=3, padx=0, pady=5, sticky=W)
        


        # Email

        email_label = Label(Class_Student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_email, width=19, font=("times new roman", 11))
        email_entry.grid(row=3, column=1, padx=0, pady=5, sticky=W)



        # Phone no

        phone_label = Label(Class_Student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_phoneno, width=19, font=("times new roman", 11))
        phone_entry.grid(row=3, column=3, padx=0, pady=5, sticky=W)
        


        # Address

        address_label = Label(Class_Student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_address, width=19, font=("times new roman", 11))
        address_entry.grid(row=4, column=1, padx=0, pady=5, sticky=W)



        # Teacher Name

        teacher_label = Label(Class_Student_frame, text="Teacher's Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_teachername, width=19, font=("times new roman", 11))
        teacher_entry.grid(row=4, column=3, padx=0, pady=5, sticky=W)



        # radio Buttons

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Class_Student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)


        radiobtn2 = ttk.Radiobutton(Class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # bbuttons

        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=2, y=200, width=592, height=55)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=14, cursor="hand2", font=("times new roman", 13, "bold"), bg="grey", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=14, cursor="hand2", font=("times new roman", 13, "bold"), bg="grey", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=14, cursor="hand2", font=("times new roman", 13, "bold"), bg="grey", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=13, cursor="hand2", font=("times new roman", 13, "bold"), bg="grey", fg="white")
        reset_btn.grid(row=0, column=3)




        btn_frame1 = Frame(Class_Student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=2, y=235, width=592, height=35)


        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", cursor="hand2", width=28, font=("times new roman", 13, "bold"), bg="grey", fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", cursor="hand2", width=29, font=("times new roman", 13, "bold"), bg="grey", fg="white")
        update_photo_btn.grid(row=1, column=1)

        changeOnHover(save_btn, "#444444", "grey")
        changeOnHover(update_btn, "#444444", "grey")
        changeOnHover(delete_btn, "#444444", "grey")
        changeOnHover(reset_btn, "#444444", "grey")
        changeOnHover(take_photo_btn, "#444444", "grey")
        changeOnHover(update_photo_btn, "#444444", "grey")



        # right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=645, y=10, width=580, height=475)


        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=10, width=555, height=430)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("name","id","rollno","father","sec","course","branch","year","sem","email","phone","address","dob","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name",text="Student's Name")
        self.student_table.heading("id",text="Student's ID")
        self.student_table.heading("rollno",text="University RollNo")
        self.student_table.heading("father",text="Father's Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("branch",text="Branch")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("teacher", text="Teacher's Name")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"


        self.student_table.column("name", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("rollno", width=100)
        self.student_table.column("father", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("branch", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("email", width=160)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)



        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    # ============Function Declaration============
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name =="" or self.var_id =="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                                                                                                                self.var_name.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_rollno.get(),
                                                                                                                self.var_fathername.get(),
                                                                                                                self.var_sec.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phoneno.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_teachername.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error!!",f"Due To:{str(es)}",parent=self.root)



    #=================FetchData=============
    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()



    #================GetCursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_name.set(data[0]),
        self.var_id.set(data[1]),
        self.var_rollno.set(data[2]),
        self.var_fathername.set(data[3]),
        self.var_sec.set(data[4]),
        self.var_course.set(data[5]),
        self.var_dep.set(data[6]),
        self.var_year.set(data[7]),
        self.var_sem.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phoneno.set(data[10]),
        self.var_address.set(data[11]),
        self.var_dob.set(data[12]),
        self.var_teachername.set(data[13]),
        self.var_radio1.set(data[14])


    #====================Update Function=============
    def update_data(self):
        if self.var_course.get()=="Select Course" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error!!","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update Student's Information",parent=self.root)
                if Update>0:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set name=%s,rollno=%s,fathername=%s,sec=%s,course=%s,dep=%s,year=%s,sem=%s,email=%s,phoneno=%s,address=%s,dob=%s,teachername=%s,photo=%s where id=%s",(
                                                                                self.var_name.get(),                                                                                                                              
                                                                                self.var_rollno.get(),
                                                                                self.var_fathername.get(),
                                                                                self.var_sec.get(),
                                                                                self.var_course.get(),
                                                                                self.var_dep.get(),
                                                                                self.var_year.get(),
                                                                                self.var_sem.get(),
                                                                                self.var_email.get(),
                                                                                self.var_phoneno.get(),
                                                                                self.var_address.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_teachername.get(),
                                                                                self.var_radio1.get(),
                                                                                self.var_id.get()
                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success!!","Details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)



    #=============Delete Function================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error!","Student ID is required",parent=self.root)  
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete data",parent=self.root) 
                if delete>0:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()    
                conn.close()
                messagebox.showinfo("Delete","Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)




    #=============Reset===========
    def reset_data(self):
        self.var_name.set("")
        self.var_id.set("")
        self.var_rollno.set("")
        self.var_fathername.set("")
        self.var_sec.set("")
        self.var_course.set("Select Course")
        self.var_dep.set("Select Branch")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_email.set("")
        self.var_phoneno.set("")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_teachername.set("")
        self.var_rollno.set("")



    #===============Generate Dataset/Take Photos==============
    def generate_dataset(self):
        if self.var_course.get()=="Select Course" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error!!","All fields are required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set name=%s,rollno=%s,fathername=%s,sec=%s,course=%s,dep=%s,year=%s,sem=%s,email=%s,phoneno=%s,address=%s,dob=%s,teachername=%s,photo=%s where id=%s",(
                                                                                self.var_name.get(),                                                                                                                              
                                                                                self.var_rollno.get(),
                                                                                self.var_fathername.get(),
                                                                                self.var_sec.get(),
                                                                                self.var_course.get(),
                                                                                self.var_dep.get(),
                                                                                self.var_year.get(),
                                                                                self.var_sem.get(),
                                                                                self.var_email.get(),
                                                                                self.var_phoneno.get(),
                                                                                self.var_address.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_teachername.get(),
                                                                                self.var_radio1.get(),
                                                                                self.var_id.get()==id+1
                                                                            ))                                                                                                                                                                                                                                                                            
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=====Load Predefined Data On Face Frontals from Open CV=====
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_crop(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_crop(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Image",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset Completed!!",parent=self.root)    
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root) 







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
