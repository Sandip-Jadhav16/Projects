from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Student Performance Prediction System")
    root.configure(background="Black")
    
    gender = tk.IntVar()
    Nationlity = tk.IntVar()
    PlaceofBirth = tk.IntVar()
    StageID = tk.IntVar()
    GradeID = tk.IntVar()
    Topic = tk.IntVar()
    Semester = tk.IntVar()
    VisitedResources= tk.IntVar()
    AnnouncementsView= tk.IntVar()
    Discussion = tk.IntVar()
    ParentAnsweringSurvey = tk.DoubleVar()
    ParentsShoolSatisfaction = tk.IntVar()
    StudentAbsenceDays = tk.IntVar()
   
    
    #===================================================================================================================
    def Detect():
        e1= gender.get()
        print(e1)
        e2=Nationlity.get()
        print(e2)
        e3= PlaceofBirth.get()
        print(e3)
        e4=StageID.get()
        print(e4)
        e5=GradeID.get()
        print(e5)
        e6=Topic.get()
        print(e6)
        e7=Semester.get()
        print(e7)
        e8=VisitedResources.get()
        print(e8)
        e9=AnnouncementsView.get()
        print(e9)
        e10=Discussion.get()
        print(e10)
        e11=ParentAnsweringSurvey.get()
        print(e11)
        e12=ParentsShoolSatisfaction.get()
        print(e12)
        e13=StudentAbsenceDays.get()
        print(e13)
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('RF_student_performance.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9,e10, e11, e12, e13]])
        print(v)
        if v[0]==0:
            print("High")
            yes = tk.Label(root,text="Performance is Above 75%",background="red",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=700,y=610)
                     
        elif v[0]==1:
            print("Medium")
            no = tk.Label(root, text="Performance is 50% - 70% ", background="red", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=700, y=610)
            
            
        else:
            print("Low")
            no = tk.Label(root, text="Performance is 10% - 40%", background="green", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=700, y=610)
            


    l1=tk.Label(root,text="Gender",font=('times', 14),width=20)
    l1.place(x=150,y=50)
    ts1=tk.Label(root,text="Male:0 Female:1",background="#969696",font=('times', 12),width=65)
    ts1.place(x=650,y=50)
    gender=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    gender.place(x=450,y=50)
    

    l2=tk.Label(root,text="Nationality",font=('times', 14),width=20)
    l2.place(x=150,y=90)
    Nationlity=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    Nationlity.place(x=450,y=90)
    ts2= tk.Label(root,text="India:0,China:1,America:3,Pakistan:4,Japan:5,Dubai:6,canada:7",background="#969696",font=('times', 12),width=65)
    ts2.place(x=650,y=90)

    l3=tk.Label(root,text="Attendence in %",font=('times', 14),width=20)
    l3.place(x=150,y=130)
    PlaceofBirth=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    PlaceofBirth.place(x=450,y=130)
    ts10= tk.Label(root,text="10%:0,20%:1,30%:2,40%:3,50%:4,60%:5,\70%:6,80%:7,90%:8,100%:9",background="#969696",font=('times', 12),width=65)
    ts10.place(x=650,y=130)

    l4=tk.Label(root,text="StageID",font=('times', 14),width=20)
    l4.place(x=150,y=170)
    ts3=tk.Label(root,text="Lower level:0,Middle level:1,High level:2",background="#969696",font=('times', 12),width=65)
    ts3.place(x=650,y=170)
    StageID=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    StageID.place(x=450,y=170)

    l5=tk.Label(root,text="GradeID",font=('times', 14),width=20)
    l5.place(x=150,y=210)
    ts4 = tk.Label(root,text="Grade:0 to Grade:9",background="#969696",font=('times', 12),width=65)
    ts4.place(x=650,y=210)
    GradeID=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    GradeID.place(x=450,y=210)

    l6=tk.Label(root,text="Field",font=('times', 14),width=20)
    l6.place(x=150,y=250)
    ts5 = tk.Label(root,text="IT:0,Computer:1,Electrical:3,Mechanical:4,Civil:5,Chemical:6,Automobile:7,Aerospace:8",background="#969696",font=('times', 12),width=65)
    ts5.place(x=650,y=250)
    Topic=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    Topic.place(x=450,y=250)

    l7=tk.Label(root,text="Semester",font=('times', 14),width=20)  
    l7.place(x=150,y=290)
    ts6 = tk.Label(root,text="Sem-I:0 SemII:1",background="#969696",font=('times', 12),width=65)
    ts6.place(x=650,y=290)
    Semester=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    Semester.place(x=450,y=290)

    l8=tk.Label(root,text="VisitedResources",font=('times', 14),width=20)
    l8.place(x=150,y=330)
    VisitedResources=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    VisitedResources.place(x=450,y=330) 
    ts7 = tk.Label(root,text="Visited Resources may vary on Student max(100)",background="#969696",font=('times', 12),width=65)
    ts7.place(x=650,y=330)

    l9=tk.Label(root,text="AnnouncementsView",font=('times', 14),width=20)
    l9.place(x=150,y=370)
    AnnouncementsView=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    AnnouncementsView.place(x=450,y=370)
    ts8 = tk.Label(root,text="Resources provided by Teacher max(100)",background="#969696",font=('times', 12),width=65)
    ts8.place(x=650,y=370)

    l10=tk.Label(root,text="Discussion",font=('times', 14),width=20)
    l10.place(x=150,y=410)
    ts = tk.Label(root,text="To be fulfiled by teacher",background="#969696",font=('times', 12),width=65)
    ts.place(x=650,y=410)
    Discussion=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    Discussion.place(x=450,y=410)

    l11=tk.Label(root,text="ParentAnsweringSurvey",font=('times', 14),width=20)
    l11.place(x=150,y=450)
    ts11 = tk.Label(root,text="Yes:0 No:1",background="#969696",font=('times', 12),width=65)
    ts11.place(x=650,y=450)
    ParentAnsweringSurvey=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    ParentAnsweringSurvey.place(x=450,y=450)

   
    l12=tk.Label(root,text="ParentsSchoolSatisfaction",font=('times', 14),width=20)
    l12.place(x=150,y=490)
    ts9 = tk.Label(root,text="Good:0 Bad:1",background="#969696",font=('times', 12),width=65)
    ts9.place(x=650,y=490)
    ParentsShoolSatisfaction=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    ParentsShoolSatisfaction.place(x=450,y=490)

    l13=tk.Label(root,text="StudentAbsenceDays",font=('times', 14),width=20)
    l13.place(x=150,y=530)
    ts10 = tk.Label(root,text="under 7:0 Above 7:1",background="#969696",font=('times', 12),width=65)
    ts10.place(x=650,y=530)
    StudentAbsenceDays=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 14))
    StudentAbsenceDays.place(x=450,y=530)


    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=500,y=610)


    root.mainloop()

Train()