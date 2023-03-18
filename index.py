from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
class Hospital:
    def __init__(self, root):
        self.root= root
        self.root.title("Hospital Management")
        self.root.geometry('1540x800+0+0')
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM", fg="red",bg="white", font=("times new roman",50,"bold")) 
        lbltitle.pack(side=TOP,fill=X)
        
        #===================Dataframe=========================================
        Dataframe=Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400) 
        
        dataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        dataframeLeft.place(x=0,y=5,width=980,height=350) 
        
        dataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        dataframeRight.place(x=990,y=5,width=450,height=350)
        
        #========================== buttons frame =============================
        
        Buttonframe=Frame(self.root, bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        #========================== Details frame =============================
        Detailsframe=Frame(self.root, bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        #========================== dataframeLeft==============================
        
        lblNameTablet=Label(dataframeLeft,text="Names of Tablet",font=('times new roman',12,'bold'),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        comNametablet=ttk.Combobox(dataframeLeft,font=('times new roman',12,'bold'), width=35)
        comNametablet['values']=('Nice','Corona Vaccine','Acetaminophen','Adderall','Amlodipine','Ativan')
        comNametablet.grid(row=0,column=1)
        
        lblref=Label(dataframeLeft,font=('arial',12,'bold'),text="Reference No:",padx=2,pady=4)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtref.grid(row=1,column=1)
        
        lblDose=Label(dataframeLeft,font=('arial',12,'bold'),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtDose.grid(row=2,column=1)
        
        lblNooftablets=Label(dataframeLeft,font=('arial',12,'bold'),text="No. Of Tablets:",padx=2,pady=4)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtLot=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtLot.grid(row=3,column=1)
        
        lblLot=Label(dataframeLeft,font=('arial',12,'bold'),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtLot.grid(row=4,column=1)
        
        lblissuedate=Label(dataframeLeft,font=('arial',12,'bold'),text="Issue Date:",padx=2,pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtissueDate.grid(row=5,column=1)
        
        lblExpdate=Label(dataframeLeft,font=('arial',12,'bold'),text="Exp Date:",padx=2,pady=4)
        lblExpdate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose=Label(dataframeLeft,font=('arial',12,'bold'),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblsideeffect=Label(dataframeLeft,font=('arial',12,'bold'),text="Side Effect:",padx=2,pady=4)
        lblsideeffect.grid(row=8,column=0,sticky=W)
        txtsideeffect=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtsideeffect.grid(row=8,column=1)
        
        lblFurtherinfo=Label(dataframeLeft,font=('arial',12,'bold'),text="Further Information:",padx=2,pady=4)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        lblBloodPressure=Label(dataframeLeft,font=('arial',12,'bold'),text="Blood Pressure:",padx=2,pady=4)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtBloodPressure.grid(row=1,column=3)
        
        lblStorage=Label(dataframeLeft,font=('arial',12,'bold'),text="Storage Advice:",padx=2,pady=4)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtStorage.grid(row=2,column=3)
        
        lblMedicine=Label(dataframeLeft,font=('arial',12,'bold'),text="Medication",padx=2,pady=4)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)
        
        lblPatientId=Label(dataframeLeft,font=('arial',12,'bold'),text="Patient Id :",padx=2,pady=4)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtPatientId.grid(row=4,column=3)
        
        lblNhsNumber=Label(dataframeLeft,font=('arial',12,'bold'),text="NHS Number",padx=2,pady=4)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtNhsNumber.grid(row=5,column=3)
        
        lblPatientname=Label(dataframeLeft,font=('arial',12,'bold'),text="Patient Name",padx=2,pady=4)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtPatientname.grid(row=6,column=3)
        
        lblDateofBirth=Label(dataframeLeft,font=('arial',12,'bold'),text="Date of Birth:",padx=2,pady=4)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtDateofBirth.grid(row=7,column=3)
        
        lblPatientAddress=Label(dataframeLeft,font=('arial',12,'bold'),text="Patient Address:",padx=2,pady=4)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(dataframeLeft,font=('arial',13,'bold'),width=35)
        txtPatientAddress.grid(row=8,column=3)
        
         #========================== dataframeRight==============================
        self.txtPrescription=Text(dataframeRight, font=("arial", 12,"bold"), width=45, height=16,padx=2, pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
         #===============================Buttons=================================
        btnPrescription=Button(Buttonframe,text="Prescription", bg="green", fg="white", font=("arial",12,"bold"),width=23)
        btnPrescription.grid(row=0,column=0)
         
        btnPrescriptionData=Button(Buttonframe,text="Prescription Data", bg="green", fg="white", font=("arial",12,"bold"),width=23)
        btnPrescriptionData.grid(row=0,column=0)
         
        btnUpdate=Button(Buttonframe,text="Update", bg="green", fg="white", font=("arial",12,"bold"),width=23)
        btnUpdate.grid(row=0,column=0)
         
        btnDelete=Button(Buttonframe,text="Delete", bg="green", fg="white", font=("arial",12,"bold"),width=23)
        btnDelete.grid(row=0,column=0)
         
        btnClear=Button(Buttonframe,text="Clear", bg="green", fg="white", font=("arial",12,"bold"),width=23)
        btnClear.grid(row=0,column=0)
         
        btnExit=Button(Buttonframe,text="Exit", bg="green", fg="white", font=("arial",12,"bold"),width=23)
        btnExit.grid(row=0,column=0)
         
        Detailsframe=Frame(self.root, bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        #===============================Table=====================================
        #===============================ScrollBar=================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        
        self.hospital_table=ttk.Treeview(Detailsframe, column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expate",
                                                               "dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_y.set,
                                         yscrollcommand=scroll_x.set)
        scroll_x.pack= (side :=BOTTOM, fill :=X)
        scroll_y.pack= (side :=RIGHT, fill :=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameofthetable",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pnaame",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("nameofthetable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pnaame",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        
        self.hospital_table.pack(fill=BOTH, expand=1)
        
        
      
        
root=Tk()
ob=Hospital(root)
root.mainloop() 


