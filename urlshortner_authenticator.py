import customtkinter as ctk
import tkinter.messagebox as ms
import pyshorteners
import customtkinter as ctk

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

app = ctk.CTk() 
app.geometry("400x400") 
app.title("Authentication") 

def login():
    if u_button.get()=='jairam' and p_button.get()=='jk@123':
        # app=ctk.CTk()
        newwindwo=ctk.CTkToplevel(app)
        # newwindwo.geometry('400x400')
# ---------------------------------------------------------------------------------------------------
        ctk.set_appearance_mode("black")
        ctk.set_default_color_theme("blue")


        # app=ctk.CTk()
        newwindwo.geometry('600x300')
        newwindwo.title("URL Shortner")


        string_variable =ctk.StringVar()

        def short():
            url=entry_box.get()
            s=pyshorteners.Shortener()
            gurl=s.tinyurl.short(url)
            string_variable.set(gurl)
            entry_box2.configure(textvariable=string_variable)
            
            print(gurl)


        frame=ctk.CTkFrame(master=newwindwo)
        frame.pack(pady=20,padx=40,fill='both',expand=True) 

        label1=ctk.CTkLabel(frame,text="Enter the URL to be shorted",font=('Boulder',20))
        label1.pack(padx=10,pady=10)

        entry_box=ctk.CTkEntry(frame,width=240)
        entry_box.pack(padx=10,pady=10)

        submit=ctk.CTkButton(frame,text="GENERATE",command=short)
        submit.pack(padx=10,pady=10)

        entry_box2=ctk.CTkEntry(frame,textvariable='',font=("Helvetica",11),width=240,state="readonly")
        entry_box2.pack(padx=10,pady=10)
#----------------------------------------------------------------------------------------------------------------   
    else:
        ms.showerror("Error", "wrong username or password")



label= ctk.CTkLabel(app,text="AUTHENTICATION") 
label.pack(pady=20)

frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 
  
label = ctk.CTkLabel(master=frame, text='Log-in to continue') 
label.pack(pady=12,padx=10)

u_button=ctk.CTkEntry(frame,width=200,placeholder_text="Username")
u_button.pack(padx=10,pady=10,)

p_button=ctk.CTkEntry(frame,width=200,show="*",placeholder_text="Password")
p_button.pack(padx=10,pady=10,)

submit=ctk.CTkButton(frame,text="LogIn",command=login)
submit.pack(padx=10,pady=10)


app.mainloop()