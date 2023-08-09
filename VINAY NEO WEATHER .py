from tkinter import *
from tkinter import ttk
#import the request module
import requests
def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])


#window name,size and font

win=Tk()
win.title("NEO WEATHER ")
win.config(bg="blue")
win.geometry("500x500")

name_label=Label(win,text="NEO WEATHER",font=("Time new roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="NEO WEATHER ",values=list_name,font=("Time new roman",30,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


w_label=Label(win,text="weather climate",font=("Time new roman",20))
w_label.place(x=25,y=260, height=50,width=210)



w_label1=Label(win,text="",font=("Time new roman",20))
w_label1.place(x=250,y=260, height=50,width=210)

wb_label=Label(win,text="weather Desription",font=("Time new roman",17))
wb_label.place(x=25,y=330,height=50,width=210)


wb_label1=Label(win,text="",font=("Time new roman",17))
wb_label1.place(x=250,y=330,height=50,width=210)


temp_label=Label(win,text="Temperature",font=("Time new roman",20))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 =Label(win,text="",font=("Time new roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)


per_label=Label(win,text ="Pressure",font=("Time new roman",20))
per_label.place(x=25,y=470,height=50,width=210)


per_label1 =Label(win,text ="",font=("Time new roman",20))
per_label1.place(x=250,y=470,height=50,width=210)


#button to  search


done_button=Button(win,text="Done",font=("Time new roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)



win.mainloop()