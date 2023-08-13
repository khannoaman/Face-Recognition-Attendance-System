from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import sys
import cv2
import threading
import mysql.connector
import pyttsx3
import time
import datetime
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join,split,exists


class faceRecogSystem(Frame):
    
    def check(self):
        pass

    def windowexit(self,key=None):
        sys.exit()
    
    def __init__(self, master=None):
        
        Frame.__init__(self, master)
        self.master = master
        self.master.config(bg="#FFF")
        
        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
        # Menu bar

        # File
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        #file.add_command(label="Save Chat Log", command=self.save_chat)
        file.add_command(label="Home", command=self.home)

        img1=Image.open(r"F:\Python Projects\Major Project Face Recognition Attendence System\Images\Jamia_Hamdard_Logo.png")
        img1=img1.resize((130,140),Image.ANTIALIAS)
        self.logoImg=ImageTk.PhotoImage(img1,master=self.master)
        
        # Hamdard Logo
        logo = Label(self.master,image=self.logoImg,bg="#FFF")
        logo.place(x=50,y=5,height=140,width=130)
        
        # Jamia Hamdard
        JH = Label(self.master, text ="JAMIA HAMDARD",font='TkDefaultFont 45 bold',bg="#FFF",fg="#0065ad")
        JH.place(x=200,y=0)
        
        # Department 
        Dep = Label(self.master, text ="Department of Computer Science",font='TkDefaultFont 18 bold',bg="#FFF",fg="#f0840a")
        Dep.place(x=260,y=65)
        
        # Title 
        title = Label(self.master, text ="FACE RECOGNITION ATTENDANCE SYSTEM",font='TkDefaultFont 15 bold',bg="#FFF",fg="#f0120a")
        title.place(x=235,y=100)
        
        # Student Details
        img2=Image.open(r"F:\Python Projects\Major Project Face Recognition Attendence System\Images\students.jpg")
        img2=img2.resize((122,100),Image.ANTIALIAS)
        self.studentsImg=ImageTk.PhotoImage(img2,master=self.master)
        
        # Student Image Button
        studentImage_button = Button(self.master,  image=self.studentsImg, relief=RIDGE, command=self.studentDetails,cursor="hand2")
        studentImage_button.place(x=109,y=200)
        
        # Student Button
        studentText_button = Button(self.master,  text="Add Student Details", width=17, relief=RIDGE,font='TkDefaultFont 8 bold',
                                  bg='#0065ad',fg="#FFF",
                                  bd=1, command=self.studentDetails, activebackground="#FFFFFF",
                                  activeforeground="#000000",cursor="hand2")
        studentText_button.place(x=110,y=305,height=30)
        
        
        # Train Data
        img3=Image.open(r"F:\Python Projects\Major Project Face Recognition Attendence System\Images\train.jpg")
        img3=img3.resize((122,100),Image.ANTIALIAS)
        self.trainDataImg=ImageTk.PhotoImage(img3,master=self.master)
        
        # Train Image Button
        trainImage_button = Button(self.master,  image=self.trainDataImg, relief=RIDGE, command=self.trainingData,cursor="hand2")
        trainImage_button.place(x=329,y=200)
        
        # Train Button
        trainText_button = Button(self.master,  text="Train Data", width=17, relief=RIDGE,font='TkDefaultFont 8 bold',
                                  bg='#0065ad',fg="#FFF",
                                  bd=1, command=self.trainingData, activebackground="#FFFFFF",
                                  activeforeground="#000000",cursor="hand2")
        trainText_button.place(x=330,y=305,height=30)
        
        
        # Attendance
        img4=Image.open(r"F:\Python Projects\Major Project Face Recognition Attendence System\Images\attendance.png")
        img4=img4.resize((122,100),Image.ANTIALIAS)
        self.attendanceImg=ImageTk.PhotoImage(img4,master=self.master)
        
        # Attendance Image Button
        attendanceImage_button = Button(self.master,  image=self.attendanceImg, relief=RIDGE, command=self.mark_attendance,cursor="hand2")
        attendanceImage_button.place(x=549,y=200)
        
        # Attendance Button
        attendanceText_button = Button(self.master,  text="Attendance", width=17, relief=RIDGE,font='TkDefaultFont 8 bold',
                                  bg='#0065ad',fg="#FFF",
                                  bd=1, command=self.mark_attendance, activebackground="#FFFFFF",
                                  activeforeground="#000000",cursor="hand2")
        attendanceText_button.place(x=550,y=305,height=30)
        
        # Face Recognition
        img5=Image.open(r"F:\Python Projects\Major Project Face Recognition Attendence System\Images\face.jpg")
        img5=img5.resize((122,100),Image.ANTIALIAS)
        self.faceImg=ImageTk.PhotoImage(img5,master=self.master)
        
        # Face Image Button
        faceImage_button = Button(self.master,  image=self.faceImg, relief=RIDGE, command=self.face_recog,cursor="hand2")
        faceImage_button.place(x=224,y=390)
        
        # Face Button
        faceText_button = Button(self.master,  text="Face Recognition", width=17, relief=RIDGE,font='TkDefaultFont 8 bold',
                                  bg='#0065ad',fg="#FFF",
                                  bd=1, command=self.face_recog, activebackground="#FFFFFF",
                                  activeforeground="#000000",cursor="hand2")
        faceText_button.place(x=225,y=495,height=30)
        
        # Exit 
        img6=Image.open(r"F:\Python Projects\Major Project Face Recognition Attendence System\Images\exit.png")
        img6=img6.resize((122,100),Image.ANTIALIAS)
        self.exitImg=ImageTk.PhotoImage(img6,master=self.master)
        
        # Exit Image Button
        ExitImage_button = Button(self.master,  image=self.exitImg, relief=RIDGE, command=self.windowexit,cursor="hand2")
        ExitImage_button.place(x=444,y=390)
        
        # Exit Button
        ExitText_button = Button(self.master,  text="Exit", width=17, relief=RIDGE,font='TkDefaultFont 8 bold',
                                  bg='#0065ad',fg="#FFF",
                                  bd=1, command=self.windowexit, activebackground="#FFFFFF",
                                  activeforeground="#000000",cursor="hand2")
        ExitText_button.place(x=445,y=495,height=30)
        
        
        ################################################################################################
        
        self.enrollNo=""
        self.studName=""
        self.studEmail=""
        self.studCourse=""
        self.studYear=""
        self.attend=False
        self.lock = threading.Lock()
        
        
        ################################################################################################
        
        self.notebook=ttk.Notebook(self.master)
        self.notebook.pack()
        
        # Enrollment number Entry Box
        self.Enroll =""
        self.Enroll_sv = StringVar()
        self.Enroll_sv.trace("w", self.callback1)
        
        # name Entry Box
        self.name =""
        self.name_sv = StringVar()
        self.name_sv.trace("w", self.callback2)
        
        # Email Entry Box
        self.email =""
        self.email_sv = StringVar()
        self.email_sv.trace("w", self.callback3)
        
        # Course Dropdown
        self.course =""
        self.course_sv = StringVar()
        self.course_sv.trace("w", self.callback4)
        
        # Year Dropdown
        self.year =""
        self.year_sv = StringVar()
        self.year_sv.trace("w", self.callback5)
        
        

        
    def callback1(self,name='', index='', mode=''):
        self.enrollNo=self.Enroll_sv.get()
        #print(self.enrollNo)
        
    def callback2(self,name='', index='', mode=''):
        self.studName=self.name_sv.get()
        #print(self.studName)
        
    def callback3(self,name='', index='', mode=''):
        self.studEmail=self.email_sv.get()
        #print(self.studEmail)
        
            
    def callback4(self,name='', index='', mode=''):
        self.studCourse=self.course_sv.get()
        #print(self.studCourse)
        
                
    def callback5(self,name='', index='', mode=''):
        self.studYear=self.year_sv.get()
        #print(self.studYear)
        
    def studentDetails(self):
        
        self.my_frame1 = Frame(self.notebook,width=780,height=600)
        self.my_frame1.pack()
        self.my_frame1.config(bg="#FFF")
        
        # Hamdard Logo
        logo = Label(self.my_frame1,image=self.logoImg,bg="#FFF")
        logo.place(x=50,y=5,height=140,width=130)
        
        # Jamia Hamdard
        JH = Label(self.my_frame1, text ="JAMIA HAMDARD",font='TkDefaultFont 45 bold',bg="#FFF",fg="#0065ad")
        JH.place(x=200,y=0)
        
        # Department 
        Dep = Label(self.my_frame1, text ="Department of Computer Science",font='TkDefaultFont 18 bold',bg="#FFF",fg="#f0840a")
        Dep.place(x=260,y=65)
        
        # Title 
        title = Label(self.my_frame1, text ="FACE RECOGNITION ATTENDANCE SYSTEM",font='TkDefaultFont 15 bold',bg="#FFF",fg="#f0120a")
        title.place(x=235,y=100)
        
        
        # Enroll Label
        label1 = Label(self.my_frame1, text ="Enrollment No.",font='TkDefaultFont 12 bold',bg='#FFF')
        label1.place(x=190,y=165)
        
        # Enroll Entry Box
        self.Enroll= ttk.Entry(self.my_frame1,textvariable=self.Enroll_sv)
        self.Enroll.place(x=190,y=195,width=400,height=30)
        
        # Name Label
        label2 = Label(self.my_frame1, text ="Name",font='TkDefaultFont 12 bold',bg='#FFF')
        label2.place(x=190,y=245)
        
        # Name Entry Box
        self.name= ttk.Entry(self.my_frame1,textvariable=self.name_sv)
        self.name.place(x=190,y=275,width=400,height=30)
        
        # Email Label
        label3 = Label(self.my_frame1, text ="Email",font='TkDefaultFont 12 bold',bg='#FFF')
        label3.place(x=190,y=325)
        
        # Email Entry Box
        self.email= ttk.Entry(self.my_frame1,textvariable=self.email_sv)
        self.email.place(x=190,y=355,width=400,height=30)
        
        # Course Label
        label4 = Label(self.my_frame1, text ="Course Detail",font='TkDefaultFont 12 bold',bg='#FFF')
        label4.place(x=190,y=405)
        
        # Course DropDown
        self.course = ttk.Combobox(self.my_frame1,width = 21, textvariable = self.course_sv, state="readonly")
        self.course['values'] = ('BTECH CSE','BTECH ESE')
        self.course.current(0)
        self.course.place(x=190,y=455,height=25)
        
        # Year DropDown
        self.year = ttk.Combobox(self.my_frame1,width = 21, textvariable = self.year_sv, state="readonly")
        self.year['values'] = ('1st','2nd','3rd','4th')
        self.year.current(0)
        self.year.place(x=440,y=455,height=25)
        
        # ADD PHOTO Button
        photo_button= Button(self.my_frame1,text="Add Photo Sample",width=20, relief=RIDGE,font='TkDefaultFont 8 bold',
                                  bg='#0065ad',fg="#FFF",
                                  bd=1, command=self.addphotosample, activebackground="#FFFFFF",
                                  activeforeground="#000000",cursor="hand2")
        photo_button.place(x=190,y=505,height=30)
        
        # Save Button
        self.save_button= Button(self.my_frame1,text="Save",width=20, relief=RIDGE,font='TkDefaultFont 8 bold',
                                  bg='#0065ad',fg="#FFF",
                                  bd=1, command=self.savedata, activebackground="#FFFFFF",
                                  activeforeground="#000000",cursor="hand2")
        self.save_button.place(x=440,y=505,height=30)
        self.save_button["state"] = "disabled"
    
    def savedata(self):
        
        if self.enrollNo=="" or self.studName=="" or self.studEmail==""  or self.studCourse=="" or self.studYear=="":
            messagebox.showinfo("Details","Fill all details First")
            return
        
        try:
            conn=mysql.connector.connect(host="localhost",user="root",passwd="xxxxxxxxx",database="attendacesystem")
            mycursor=conn.cursor()
        except Exception as e:
            messagebox.showinfo("Error",e)
            sys.exit()
            
        try:
            mycursor.execute("INSERT INTO `students` (`enrollment`, `Name`, `Email`, `Course`, `Year`) VALUES ('{}', '{}', '{}','{}','{}');".format(self.enrollNo,self.studName,self.studEmail,self.studCourse,self.studYear))
        except Exception as e:
            messagebox.showinfo("Error",e)
            sys.exit()
            
        conn.commit()    
        messagebox.showinfo("Details","Details Saved, please train data as well.")
        
    def speak(self,audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 250)
        #engine.setProperty('volume', 100)
        engine.say(audio)
        engine.runAndWait()

    
    def face_extractor(self,img):
        
        face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)

        if faces ==():
            return None

        for(x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face
    
    def collectdata(self):
        
        messagebox.showinfo("Dataset","Ready for Colleting Samples!!!")

        cap = cv2.VideoCapture(0)
        count=0
        while True:
            ret, frame = cap.read()
            if self.face_extractor(frame) is not None:
                count+=1
                face = cv2.resize(self.face_extractor(frame),(200,200))


                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                file_name_path = './Dataset/user.'+self.enrollNo+"."+str(count)+'.jpg'
                cv2.imwrite(file_name_path,face)

                cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                cv2.imshow('SAMPLES',face)
            else:
                cv2.imshow('SAMPLES', frame)
                print("Face not Found")
                pass

            if cv2.waitKey(1)==13 or count==50:
                break

        cap.release()
        cv2.destroyAllWindows()
        
        messagebox.showinfo("Dataset","Colleting Samples Completed!!!")
        self.save_button["state"] = "normal"
        

    
    def addphotosample(self):
        self.save_button["state"] = "disable"
        #print(self.enrollNo,self.studName,self.studEmail,self.studCourse,self.studYear)
        if self.enrollNo=="" or self.studName=="" or self.studEmail==""  or self.studCourse=="" or self.studYear=="":
            messagebox.showinfo("Details","Fill all details First")
            return
        else:
            t1=threading.Thread(target=self.collectdata)
            t1.start()
            
    def trainingData(self):
        messagebox.showinfo("Training","Model Training Started")
        data_path = './Dataset/'
        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]



        Training_Data, Labels = [], []

        for i, files in enumerate(onlyfiles):
            image_path = data_path + onlyfiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype="uint8"))
            Labels.append(split(image_path)[1].split(".")[1])

        Labels = np.asarray(Labels, dtype=np.int32)

        model = cv2.face.LBPHFaceRecognizer_create()

        model.train(np.asarray(Training_Data), np.asarray(Labels))
        
        messagebox.showinfo("Training","Model Training Complete")
    
    def face_recog(self):
        t1=threading.Thread(target=self.recognition)
        t1.start()
        
    def recognition(self):
        #Trainer

        data_path = './Dataset/'
        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

        Training_Data, Labels = [], []

        for i, files in enumerate(onlyfiles):
            image_path = data_path + onlyfiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype="uint8"))
            Labels.append(split(image_path)[1].split(".")[1])

        Labels = np.asarray(Labels, dtype=np.int32)

        model = cv2.face.LBPHFaceRecognizer_create()

        model.train(np.asarray(Training_Data), np.asarray(Labels))

        print("Model Training Complete!!!!!")

        #RECOGNITION

        face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        enroll=0
        display_string=""
        
        if self.attend:
            face_recog={}

        cap = cv2.VideoCapture(0)
        while True:

            ret, frame = cap.read()
            cv2.rectangle(frame, (0, 0), (640, 60), (224, 224, 224), -1)
            cv2.rectangle(frame, (0, 420), (640, 480), (224, 224, 224), -1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray,1.3,5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)


                enroll, result = model.predict(gray[y:y+h, x:x+w])
                #print(enroll,result)
                #MATCHING

                if result<50:
                    try:
                        conn=mysql.connector.connect(host="localhost",user="root",passwd="xxxxxxx",database="attendacesystem")
                        mycursor=conn.cursor()
                    except Exception as e:
                        messagebox.showinfo("Error",e)
                        sys.exit()

                    try:
                        mycursor.execute("select Name from students where enrollment={}".format(enroll))
                        if mycursor.fetchone()!=None:
                            mycursor.execute("select Name from students where enrollment={}".format(enroll))
                            name=mycursor.fetchone()[0]
                            display_string="Name: "+name
                            
                            if self.attend:
                                if face_recog.get(enroll,0)==-1:
                                    t1 = threading.Thread(target=self.alreadymarked, args=("{} your attendance has already been marked.".format(name),))
                                    t1.start()
                                    #self.alreadymarked("{} your attendance has already been marked.".format(name))
                                    continue
                                elif face_recog.get(enroll,0)==20:
                                    mycursor.execute("select * from students where enrollment={}".format(enroll))
                                    t1 = threading.Thread(target=self.marking, args=(list(mycursor.fetchone()),))
                                    t1.start()
                                    #self.marking(list(mycursor.fetchone()))
                                    face_recog[enroll]=-1
                                else:
                                    face_recog[enroll]=face_recog.get(enroll,0)+1
                            
                        else:
                            display_string="Not Found"
                    except Exception as e:
                        messagebox.showinfo("Error",e)
                        sys.exit()
                else:
                    display_string = "Not Found"

                wd,hei=cv2.getTextSize(display_string,cv2.FONT_HERSHEY_COMPLEX, 0.7, 2)[0]
                cv2.rectangle(frame, (x, y - 50), (x +wd+3 , y - 10), (0, 255, 255), -1)
                cv2.putText(frame, display_string, (x+4, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)



            if faces==():
                 cv2.putText(frame, "FACE NOT FOUND", (185, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)



            cv2.imshow('Face Cropper', frame)
            if cv2.waitKey(1)==13 :
                break


        cap.release()
        cv2.destroyAllWindows()
        
        
    def mark_attendance(self):
        self.attend=True
        self.recognition()
        self.attend=False

    def alreadymarked(self,data):
        with self.lock:
            self.attend=False
        self.speak(data)
        with self.lock:
            self.attend=True
                                          
    def marking(self,data):
        with self.lock:
            self.attend=False
        data.append(datetime.datetime.now())
        file="./Attendance/"+data[3]+" "+data[4]+".csv"
        if exists(file):
            df = pd.read_csv(file)
            df.loc[len(df)] = data
            df.to_csv(file,index=False)
        else:
            df=pd.DataFrame([data], columns=["Enrollment","Name","Email","Course","Year","Datetime"])
            df.to_csv(file,index=False)
        self.speak("{} your attendance has been marked.".format(data[1]))
        time.sleep(3)
        with self.lock:
            self.attend=True
            
    def home(self):
        
        self.notebook.destroy()
        self.notebook=ttk.Notebook(self.master)
        self.notebook.pack()



if __name__ == '__main__':
    root=Tk()
    a = faceRecogSystem(root)
    #root.geometry(window_size)
    root.minsize(780,600)
    root.maxsize(780,600)
    root.title("Face Recognition Attendance System")
    root.mainloop()
