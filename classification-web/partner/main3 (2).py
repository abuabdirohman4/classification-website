from tkinter import *
# Tkinter Library GUI
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
from tkinter import filedialog
import tkinter.messagebox
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from scipy.stats import mode
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from PIL import Image
# from pre import model
import os


class GUI: #Pembuatan GUI

    df = pd.DataFrame({})

    def __init__(diri, master):
        diri.master = master
        master.title("SITIAPNF Risk Ranking")    

        p1 = PhotoImage(file = 'apk.png')   #logo aplikasi
        master.iconphoto(False, p1) 
        headlabel = Label(master, text = 'SITIAPNF Data Risk Ranking', 
                              fg = 'black', bg = "light blue")  
        headlabel1 = Label(master, text = 'Kalkulasi Sistem Usulan', 
                              fg = 'black', bg = "light blue")  
        headlabel2 = Label(master, text = 'Clustering data', 
                              fg = 'black', bg = "light blue")  
        #headlabel3 = Label(master, text = '>>>>', 
        #                      fg = 'black', bg = "light blue")  

        # Data path
        diri.pathLabel = Label(master, fg = 'black', bg = "light green", text="Cari data:")
        vcmd = master.register(diri.validate)  
        diri.pathEntry = Entry(master, validate="key")  # path for data
        diri.browse_button = Button(
            master, text="Browse", bg = "red", 
                     fg = "black",command=lambda: diri.browse())

        # Num of clusters k
        diri.numOfClusLabel = Label(master, 
                              fg = 'black', bg = "light green",text="Masukkan nilai klaster k:")
        vcmd = master.register(diri.validate)  
        diri.numOfClusEntry = Entry(master, validate="key")

        # Num of runs
        diri.numOfRunsLabel = Label(master, fg = 'black', bg = "light green", text="Masukkan nilai random_state:")
        vcmd = master.register(diri.validate)  
        diri.numOfRunsEntry = Entry(master, validate="key") 

        diri.validLabel = Label(master, fg = 'black', bg = "light green", text="Masukkan nilai data valid:")
        vcmd = master.register(diri.validate)  
        diri.validEntry = Entry(master, validate="key") 

        diri.minLabel = Label(master, fg = 'black', bg = "light green", text="Masukkan nilai minimum data:")
        vcmd = master.register(diri.validate)  
        diri.minEntry = Entry(master, validate="key") 

        diri.maxLabel = Label(master, fg = 'black', bg = "light green", text="Masukkan nilai maximum data:")
        vcmd = master.register(diri.validate)  
        diri.maxEntry = Entry(master, validate="key")   

        diri.label4 = Label(master, text = "Hasil ", 
                   fg = 'black', bg = 'dark green') 
        vcmd = master.register(diri.validate)    
        diri.kolomhasil = Entry(master, validate="key")
        
        # diri.prePro_button = Button(master, text="Pre-Process", command=lambda: diri.preProc())

        # cluster
        diri.cluster_button = Button(
            master, text="Selesai", bg = "red", 
                     fg = "black", command=lambda: diri.KMean1())   
        #diri.button2 = Button(master, text = "Reset", bg = "red", 
        #             fg = "black", command =lambda: diri.clearAll())

        #diri.cluster_button1 = Button(
        #    master, text="Percobaan", command=lambda: diri.KMean2())

        diri.button3 = Button(
            master, text="Kalkulasi", command=lambda: diri.Risk())  
        diri.button4 = Button(
            master, text="Read me", command=lambda: diri.Info_Risk())   
        diri.button5 = Button(
            master, text="Read me", command=lambda: diri.Tutorial())

        # Num of Likelihood Risk
        #diri.datavalid1 = Label(master, text="Nilai Data:")
        #vcmd = master.register(diri.validate1)  # we have to wrap the command
        #diri.datavalids1 = Entry(master, validate="key")

        # Num of Impact
        #diri.minimum = Label(master, text="Nilai Kecil:")
        #vcmd = master.register(diri.validate1)  # we have to wrap the command
        #diri.minimum1 = Entry(master, validate="key")   

        # Num of Impact
        #diri.maximum = Label(master, text="Nilai Besar:")
        #vcmd = master.register(diri.validate1)  # we have to wrap the command
        #diri.maximum1 = Entry(master, validate="key")

        # LAYOUT
        headlabel.grid(row = 0, column = 1 )    
        #headlabel3.grid(row = 0, column = 2 )
        diri.pathLabel.grid(row= 2, column= 0)
        diri.pathEntry.grid(row= 2, column= 1, sticky=W+E)
        diri.browse_button.grid(row= 2 , column= 3 )    
        diri.button5.grid(row= 2 , column= 4 )
        # untuk masukkan nilai k cluster
        headlabel2.grid(row = 5, column = 1 )   
        diri.numOfClusLabel.grid(row= 6 , column= 0 )
        diri.numOfClusEntry.grid(row= 6 , column= 1 , padx = 10 )
        # untuk masukkan nilai random_state
        diri.numOfRunsLabel.grid(row= 7 , column= 0 )
        diri.numOfRunsEntry.grid(row= 7 , column= 1 , padx = 10 )

        # diri.prePro_button.grid(row=4, column=1)

        diri.cluster_button.grid(row= 8 , column= 1 ) 

        #diri.button2.grid(row = 6 , column = 1 )  
        # untuk masukkan nilai data
        headlabel1.grid(row = 9, column = 1 )
        diri.validLabel.grid(row= 10 , column= 0 )
        diri.validEntry.grid(row= 10, column=1, padx = 10 )   
        diri.button4.grid(row = 10 , column = 3)   
        # untuk masukkan nilai minimal  
        diri.minLabel.grid(row= 12 , column= 0 )
        diri.minEntry.grid(row= 12 , column= 1 , padx = 10 ) 
         # untuk masukkan nilai maximal
        diri.maxLabel.grid(row= 13 , column= 0 )
        diri.maxEntry.grid(row= 13 , column= 1 , padx = 10 ) 
        diri.button3.grid(row = 14 , column = 1)    
        diri.label4.grid(row = 15, column = 0)   
        diri.kolomhasil.grid(row = 15, column = 1, padx = 10)      

        #diri.cluster_button1.grid(row=6, column=1)
        #entri untuk Likelihood
        #diri.datavalid1.grid(row=7, column=0)
        #diri.datavalids1.grid(row=7, column=1)	
        #entri untuk impact
        #diri.minimum.grid(row=8, column=0)
        #diri.minimum1.grid(row=8, column=1) 
        #entri untuk impact
        #diri.maximum.grid(row=9, column=0)
        #diri.maximum1.grid(row=9, column=1) 

        #diri.cluster_button1.grid(row=11, column=1) 
#menggunakan tipe data int
    def Tutorial(diri):
        tkinter.messagebox.showinfo("Risk Ranking SITIAPNF", "Buka File Excel Yang sudah ada data hasil SQL Injection lalu tekan selesai")

    def Info_Risk(diri):
        tkinter.messagebox.showinfo("Risk Ranking SITIAPNF", "Pada Kalkulasi ini menggunakan metode MinMaxScaler dan mengacu ke CVSS V2")

    def Risk(diri): 
        valids=float(diri.validEntry.get())  
        mins=float(diri.minEntry.get()) 
        maxs=float(diri.maxEntry.get()) 
        batas_min = 0.0 
        batas_max = 10.0    
        normalisasi = (valids-mins)/(maxs-mins) 
        diri.skors = float(normalisasi)    
        diri.skors = normalisasi *(batas_max-batas_min)+batas_min
        diri.kolomhasil.insert(END, diri.skors)  
        if (diri.skors < 3.9):   
            tkinter.messagebox.showinfo("Risk Ranking SITIAPNF", "Hasilnya : Low")   
            return  
        if ((diri.skors > 3.9) or (diri.skors <= 6.0)):    
            tkinter.messagebox.showinfo("Risk Ranking SITIAPNF", "Hasilnya : Medium") 
            return  
        if ((diri.skors => 6.0) or (diri.skors < 10.0)):   
            tkinter.messagebox.showinfo("Risk Ranking SITIAPNF", "Hasilnya : High") 
            return   

          
    def validate(diri, new_text):
        if not new_text:  # the field is being cleared
            diri.entered_number = 0
            return True
        try:
            diri.entered_number = int(new_text)
            return True
        except ValueError:
            return False
    #menggunakan tipe data float
    def validate1(diri, new_text):
        if not new_text:  # the field is being cleared
            diri.entered_number = 0
            return True
        try:
            diri.entered_number = float(new_text)
            return True
        except ValueError:
            return False
    def browse(diri):
        # input data xlsx atau csv
        diri.datapath = filedialog.askopenfilename()
        diri.pathEntry.insert(0, diri.datapath)
        # check valid path and file
        if(not diri.datapath):
            tkinter.messagebox.showinfo(
                "K Means Clustering", "Silahkan pilih data (berupa excel)")
            return
        if (not (diri.datapath[-5:] == ".xlsx" or diri.datapath[-4:] == ".xls" or diri.datapath[-3:] == ".csv")):
            tkinter.messagebox.showinfo(
                "K Means Clustering", "Invalid data gunakan excel file")
            return
        diri.df = pd.read_excel(diri.datapath, engine='openpyxl')	
        if (diri.df.empty):
        	tkinter.messagebox.showerror("K Means Clustering", "Invalid Excel File!")	
        	return
    # pre process + risk ranking Ilham
    def KMean1(diri):
        try:
            clusNum=int(diri.numOfClusEntry.get())
            if(clusNum<=0):
                tkinter.messagebox.showerror("K Means Clustering", "Number of clusters must be positive")
                return

            runsNum=int(diri.numOfRunsEntry.get())
            if (runsNum <= 0):
                tkinter.messagebox.showerror("K Means Clustering", "Number of runs must be positive")
                return
        except Exception:
            tkinter.messagebox.showerror("K Means Clustering", "invalid numbers")
            return
        # variabel air untuk datapath
        print("--Membaca Semua Data--")	
        print(diri.df)	
        print("--Filter regex--") 
        cek1 = diri.df.filter(regex='l$', axis=1)  #regex tidak bisa pakai space atau _ harus digabung kolomnya bagian lufty   
        print(cek1)    
        '''print("--Membaca DataFrame--")	
        diri.df = pd.DataFrame(diri.df, columns= ['No_web', 'Total', 'Skor', 'Level'])	
        print(diri.df)	
        print("--Menghilangkan Kolom dengan Tipe data string--")	
        df1 = diri.df.drop(["No_web", "Level"], axis = 1)	
        df1''' 
        smk_x = cek1.iloc[:, 0:1]	
        smk_x.head()	
        print("--- Mengubah Variabel Data Frame Menjadi Array ---")	
        x_array = np.array(smk_x)	
        print(x_array)		
        print("--- Menstandarkan Ukuran Variabel ---")	
        x_min = 0.0	
        x_max = 10.0	
        minimum = 24	
        maximum = 1336	
        nw = (x_array-minimum)/(maximum-minimum)	
        ss = nw *(x_max-x_min)+x_min 
        print(ss)	
        print("--- Menentukan dan mengkonfigurasi fungsi kmeans ---")	
        kmeans = KMeans(n_clusters = clusNum, random_state=runsNum)	
        kmeans.fit(ss)	
        print("--- Menampilkan pusat dari klaster dapat dilihat dari visualisasinya ---")	
        print(kmeans.cluster_centers_)	
        print("--- Menambahkan Kolom kluster Dalam Data Frame Driver  ---")	
        print(kmeans.labels_)	
        diri.df["kluster"] = kmeans.labels_ 	
        print("--- Memvisualkan hasil kluster  ---")	
        plt.title("hasil kluster")	
        output = plt.scatter(ss[:,0], ss[:,0], s = 100, c = diri.df.Skor, marker = "o", alpha = 1 )	
        print(output)      
        print("--- Memvisualkan hasil kluster beserta titik tengah / kelompok ---")	
        plt.title("Klaster Risiko")	
        plt.xlabel("Risiko X") 
        plt.ylabel("Data Valid Y")  
        plt.legend(["Risk Ranking", "Data Valid"])     
        output1 = plt.scatter(ss[:,0], ss[:,0], s = 100, c = diri.df.Skor, marker = "o", alpha = 1 )	
        centers = kmeans.cluster_centers_	
        plt.scatter(centers[:,0], centers[:,0], c='red', s=200, alpha=1 , marker="s");	
        plt.colorbar (output1)  

		
        # menyimpan hasil menjadi image
        path = diri.datapath
        diri.savepath=os.path.dirname(os.path.abspath(path))
        plt.savefig(diri.savepath+'\\image\\scatterPlt6.png')	
        im = Image.open(diri.savepath+'\\image\\scatterPlt6.png')	
        im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE)	
        im.save(diri.savepath+'\\image\\scatterPlt6.gif')	
        #plt.show() 
        tkinter.messagebox.showinfo("K Means Clustering", "Clustering completed successfully!") 

        plt.title("Klaster Berdasarkan Level")
        plt.scatter(diri.df.Level , diri.df.Skor, s =100, c = "c", marker = "o", alpha = 1)
            

        path = diri.datapath
        diri.savepath=os.path.dirname(os.path.abspath(path))
        plt.savefig(diri.savepath+'\\image\\scatterPlt7.png')   
        im = Image.open(diri.savepath+'\\image\\scatterPlt7.png')   
        im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE) 
        im.save(diri.savepath+'\\image\\scatterPlt7.gif')   
        #plt.show() 


        
    # clustering
    '''def risk(diri):	

        try:
            clusNum1=float(diri.numOfClusEntry1.get())
            if(clusNum1<=0):
                tkinter.messagebox.showerror("K Means Clustering", "Number of clusters must be positive")
                return

            runsNum1=float(diri.numOfRunsEntry1.get())
            if (runsNum1 <= 0):
                tkinter.messagebox.showerror("K Means Clustering", "Number of runs must be positive")
                return
        except Exception:
            tkinter.messagebox.showerror("K Means Clustering", "invalid numbers")
            return
       	
        rumus = clusNum1 + runsNum1	
        total = driver.kluster / rumus	
        print(total)
        tkinter.messagebox.showinfo("K Means Clustering", "Preprocessing completed successfully!")
        pass'''	
    
root = Tk()
my_gui = GUI(root)  
root.geometry("800x800")   
root.config(background =  "light blue") 

def on_closing():
    if tkinter.messagebox.askokcancel("Quit", "Are you sure?"):
        root.destroy()
        os._exit(0) 

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
