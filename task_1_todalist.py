from tkinter import*


window=Tk()
window.geometry('400x650')
window.resizable=False
window.configure(background='#393a3b')


task_list=[]

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f'\n{task}')
        task_list.append(task)
        listbox.insert(END,task)


def deletetask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt','w')as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')
        listbox.delete(ANCHOR)




def openTaskfirl():
    try:
        global task_list
        with open('F:\\os module\\tasklist.txt','r') as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()



Topimage=PhotoImage(file='F:\\os module\\template\\menu.png')
Label(window,image=Topimage).pack()



frame=Frame(window,width=400,height=50,bg='white')
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font='MetaOT-Black',bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text='ADD',font='arial 20 bold',width=6,bg='#001524',fg='#D6CC99',bd=0,command=addTask)
button.place(x=300,y=0)




frame1=Frame(window,bd=3,width=700,height=280,bg='black')
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg='#393a3b',fg='white',cursor='hand2',selectbackground='#5a95ff')
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskfirl()

delete_icon=PhotoImage(file="F:\\os module\\template\\deletee.png")
Button(window,image=delete_icon,bd=0,command=deletetask).pack(side=BOTTOM,pady=13)



window.mainloop()