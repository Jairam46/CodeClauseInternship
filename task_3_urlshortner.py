import pyshorteners
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("blue")


root=ctk.CTk()
root.geometry('600x300')
root.title("URL Shortner")


string_variable =ctk.StringVar()

def short():
    url=entry_box.get()
    s=pyshorteners.Shortener()
    gurl=s.tinyurl.short(url)
    string_variable.set(gurl)
    entry_box2.configure(textvariable=string_variable)
    
    print(gurl)


frame=ctk.CTkFrame(master=root)
frame.pack(pady=20,padx=40,fill='both',expand=True) 

label1=ctk.CTkLabel(frame,text="Enter the URL to be shorted",font=('Boulder',20))
label1.pack(padx=10,pady=10)

entry_box=ctk.CTkEntry(frame,width=240)
entry_box.pack(padx=10,pady=10)

submit=ctk.CTkButton(frame,text="GENERATE",command=short)
submit.pack(padx=10,pady=10)

entry_box2=ctk.CTkEntry(frame,textvariable='',font=("Helvetica",11),width=240,state="readonly")
entry_box2.pack(padx=10,pady=10)

root.mainloop()