from tkinter import * #here tinkter is use for graphic
from tkinter import ttk #here we import ttk class because we made a combo box 
 
#import weather api ----------------------->
import requests #for run url we use requests module

def data_get(): #store  data
    city=city_name.get() #city name data store
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=REPLACE_WITH_YOUR_OWN_API_KE").json() #we use json() function to convert data in json format / we use get() function to get dta from url

    w_label1.config(text=data["weather"][0]["main"])

    wb_label1.config(text=data["weather"][0]["description"])

    temp_label1.config(text=str((int(data["main"]["temp"]-273)))+u"°C")
    
    pre_label1.config(text=data["main"]["pressure"])



win = Tk()   #Tk() is class / win is veriable
win.title("Tech Guru") # for title
win.config(bg="#ffdf09") #background colour
win.geometry("500x570") #for size of window

name_label=Label(win,text="Weather Forecast",font=("Time New Roman",35,"bold")) #using label function create a lable/box where we write the weather forecaast
name_label.place(x=25,y=50,height=50,width=450) #place of the name_label in the window / size of the name_label box in the window 

city_name=StringVar() #string type data get
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"] # india state name list in python
com=ttk.Combobox(win,text="Weather Forecast",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name) #values parameter use for the list creation / textveriable get city name as string
com.place(x=25,y=120,height=50,width=450)#place of the combo box in the window / size of the combo box in the window 




#weather_climate---------->

w_label=Label(win,text="Weather Climate",font=("Time New Roman",20,))
w_label.place(x=25,y=260,height=50,width=210)

w_label1=Label(win,text="",font=("Time New Roman",20,))
w_label1.place(x=255,y=260,height=50,width=210)

#weather_description----------->

wb_label=Label(win,text="Weather Description",font=("Time New Roman",16,))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1=Label(win,text="",font=("Time New Roman",20,))
wb_label1.place(x=255,y=330,height=50,width=210)


#temperature-------------------->

temp_label=Label(win,text="Temmperature",font=("Time New Roman",20,))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1=Label(win,text="",font=("Time New Roman",20,))
temp_label1.place(x=255,y=400,height=50,width=210)



#pressure----------------------->

pre_label=Label(win,text="Pressure",font=("Time New Roman",20,))
pre_label.place(x=25,y=470,height=50,width=210)

pre_label1=Label(win,text="",font=("Time New Roman",20,))
pre_label1.place(x=255,y=470,height=50,width=210)



#done button--------------->

"""always create button last"""

done_button=Button(win,text="Done",font=("Time New Roman",20,"bold"),command=data_get ) #Using button function we create a button where collect the data / through commmand we call function

done_button.place(y=190,height=50,width=100,x=200)#place of the done button in the window / size of the done button in the window 


win.mainloop() #here mainloop() is for continously run the window
