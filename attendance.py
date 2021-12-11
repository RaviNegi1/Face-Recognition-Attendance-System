from os import pardir
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")


        # =============variables=============
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


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

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=625, height=475)


        Left_inside_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, bg="white")
        Left_inside_frame.place(x=5, y=5, width=600, height=375)


        # label and entry

        # attendance id

        attendanceID_label = Label(Left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(Left_inside_frame, width=21, textvariable=self.var_atten_id, font=("times new roman", 11))
        attendanceID_entry.grid(row=0, column=1, padx=0, pady=5, sticky=W)

        #roll no.
        rollLabel = Label(Left_inside_frame, text="Roll:", font=("times new roman", 13, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(Left_inside_frame, width=21, textvariable=self.var_atten_roll, font=("times new roman", 11))
        atten_roll.grid(row=0, column=3, pady=8)


        #name
        nameLabel = Label(Left_inside_frame, text="Name:", font=("times new roman", 13, "bold"), bg="white")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(Left_inside_frame, width=21, textvariable=self.var_atten_name, font=("times new roman", 11))
        atten_name.grid(row=1, column=1, pady=8)


        #dep
        depLabel = Label(Left_inside_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        depLabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(Left_inside_frame, width=21, textvariable=self.var_atten_dep, font=("times new roman", 11))
        atten_dep.grid(row=1, column=3, pady=8)


        #time
        timeLabel = Label(Left_inside_frame, text="Time:", font=("times new roman", 13, "bold"), bg="white")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(Left_inside_frame, width=21, textvariable=self.var_atten_time, font=("times new roman", 11))
        atten_time.grid(row=2, column=1, pady=8)


        #date
        dateLabel = Label(Left_inside_frame, text="Date:", font=("times new roman", 13, "bold"), bg="white")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(Left_inside_frame, width=21, textvariable=self.var_atten_date, font=("times new roman", 11))
        atten_date.grid(row=2, column=3, pady=8)


        #attendance
        attendanceLabel = Label(Left_inside_frame, text="Attendance:", font=("times new roman", 13, "bold"), bg="white")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(Left_inside_frame, width=20, textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)




        # bbuttons

        btn_frame = Frame(Left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=2, y=200, width=592, height=55)

        import_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=18, cursor="hand2", font=("times new roman", 13, "bold"), bg="grey", fg="white")
        import_btn.grid(row=0, column=0)


        export_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=18, cursor="hand2", font=("times new roman", 13, "bold"), bg="grey", fg="white")
        export_btn.grid(row=0, column=1)


        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19, cursor="hand2", font=("times new roman", 13, "bold"), bg="grey", fg="white")
        reset_btn.grid(row=0, column=2)


        


        # right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=645, y=10, width=580, height=475)


        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=10, width=555, height=430)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)


        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")        
        self.AttendanceReportTable.heading("attendance", text="Attendance")


        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)



        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)




    # ================fetch data================
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END, values=i)



    def importCsv(self):
        global mydata
        mydata.clear()
        file=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(file) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetch_data(mydata)
    
    #Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found",parent=self.root)
                return False
            file=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(file,"w",newline="") as myfile:
                export=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export.writerow(i)
                    messagebox.showinfo("Success","Data Exported")
        except Exception as es:
                    messagebox.showerror("Error!!",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    #=============Reset===========
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")    




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
