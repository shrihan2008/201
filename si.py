from tkinter import *
from tkinter import ttk
window=Tk()
window.title("BMI CALCULATOR")
window.geometry("400x400")
window.configure(bg="orange")
def calculate():
    principal=int(principal_entry.get()/100)
    rate=int(rate_entry.get())
    time=int(time_entry.get())
   
    name=user_name.get()
    result_label.destroy()



result_frame=LabelFrame(window,text="result",bg="red",font=("Arial",10))
result_frame.place(x=20,y=300)
result_frame.pack()

app_label=Label(window,text="SI Calculator",bg="green",font=("arial",20))
app_label.place(x=50,y=20)

user_label=Label(window,text="Enter name",bg="orange",font=("arial",10))
user_label.place(x=20,y=90)

user_name=Entry(window,text="",bd=2,width=22)
user_name.place(x=150,y=92)

principal_label=Label(window,text="Enter principal(cm)",bg="grey",font=("arial",10))
principal_label.place(x=20,y=140)

principal_entry=Entry(window,text="",bd=2,width=15)
principal_entry.place(x=150,y=142)

rate_label=Label(window,text="Enter rate(kg)",bg="grey",font=("arial",10))
rate_label.place(x=20,y=185)
rate_entry=Entry(window,text="",bd=2,width=15)
rate_entry.place(x=150,y=187)

time_entry_label=Label(window,text="Enter time",bg="grey",font=("arial",10))
time_entry_label.place(x=200,y=185)
time_entry=Entry(window,text="",bd=2,width=15)
time_entry.place(x=170,y=187)


result_label=Label(result_frame,text=" ",bg="green",font=("Arial",10),width=33)
result_label.place(x=20,y=200)

result_label.pack()

calculate_button=Button(window,text="calculate",bg="blue",bd=4,command=calculate)
calculate_button.place(x=20,y=250)

window.mainloop()