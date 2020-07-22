#importing the required libraries


from tkinter import *
import time 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random

root =Tk()

#initializing firebase database
cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL':"https://park-arduino-3451d.firebaseio.com/"
})
trigger = db.reference('sensors/trigger_car_sensor')
n1 = db.reference('sensors/sensor_01/name')
v1 = db.reference('sensors/sensor_01/value')

n2 = db.reference('sensors/sensor_02/name')
v2 = db.reference('sensors/sensor_02/value')

n3 = db.reference('sensors/sensor_03/name')
v3 = db.reference('sensors/sensor_03/value')

n4 = db.reference('sensors/sensor_04/name')
v4 = db.reference('sensors/sensor_04/value')

n5 = db.reference('sensors/sensor_05/name')
v5 = db.reference('sensors/sensor_05/value')

n6 = db.reference('sensors/sensor_06/name')
v6 = db.reference('sensors/sensor_06/value')

n7 = db.reference('sensors/sensor_07/name')
v7 = db.reference('sensors/sensor_07/value')

n8 = db.reference('sensors/sensor_08/name')
v8 = db.reference('sensors/sensor_08/value')

n9 = db.reference('sensors/sensor_09/name')
v9 = db.reference('sensors/sensor_09/value')

n10 = db.reference('sensors/sensor_10/name')
v10 = db.reference('sensors/sensor_10/value')

n11 = db.reference('sensors/sensor_11/name')
v11 = db.reference('sensors/sensor_11/value')

n12 = db.reference('sensors/sensor_12/name')
v12 = db.reference('sensors/sensor_12/value')

n13 = db.reference('sensors/sensor_13/name')
v13 = db.reference('sensors/sensor_13/value')

n14 = db.reference('sensors/sensor_14/name')
v14 = db.reference('sensors/sensor_14/value')

n15 = db.reference('sensors/sensor_15/name')
v15 = db.reference('sensors/sensor_15/value')

n16 = db.reference('sensors/sensor_16/name')
v16 = db.reference('sensors/sensor_16/value')

n17 = db.reference('sensors/sensor_17/name')
v17 = db.reference('sensors/sensor_17/value')
2
n18 = db.reference('sensors/sensor_18/name')
v18 = db.reference('sensors/sensor_18/value')

n19 = db.reference('sensors/sensor_19/name')
v19 = db.reference('sensors/sensor_19/value')

n20 = db.reference('sensors/sensor_20/name')
v20 = db.reference('sensors/sensor_20/value')


n21 = db.reference('sensors/sensor_21/name')
v21 = db.reference('sensors/sensor_21/value')

n22 = db.reference('sensors/sensor_22/name')
v22 = db.reference('sensors/sensor_22/value')

n23 = db.reference('sensors/sensor_23/name')
v23 = db.reference('sensors/sensor_23/value')

n24 = db.reference('sensors/sensor_24/name')
v24 = db.reference('sensors/sensor_24/value')

n25 = db.reference('sensors/sensor_25/name')
v25 = db.reference('sensors/sensor_25/value')

n26 = db.reference('sensors/sensor_26/name')
v26 = db.reference('sensors/sensor_26/value')

n27 = db.reference('sensors/sensor_27/name')
v27 = db.reference('sensors/sensor_27/value')

n28 = db.reference('sensors/sensor_28/name')
v28 = db.reference('sensors/sensor_28/value')

n29 = db.reference('sensors/sensor_29/name')
v29 = db.reference('sensors/sensor_29/value')

n30 = db.reference('sensors/sensor_30/name')
v30 = db.reference('sensors/sensor_30/value')

n31 = db.reference('sensors/sensor_31/name')
v31 = db.reference('sensors/sensor_31/value')

n32 = db.reference('sensors/sensor_32/name')
v32 = db.reference('sensors/sensor_32/value')

n33 = db.reference('sensors/sensor_33/name')
v33 = db.reference('sensors/sensor_33/value')

n34 = db.reference('sensors/sensor_34/name')
v34 = db.reference('sensors/sensor_34/value')

n35 = db.reference('sensors/sensor_35/name')
v35 = db.reference('sensors/sensor_35/value')

n36 = db.reference('sensors/sensor_36/name')
v36 = db.reference('sensors/sensor_36/value')

n37 = db.reference('sensors/sensor_37/name')
v37 = db.reference('sensors/sensor_37/value')

n38 = db.reference('sensors/sensor_38/name')
v38 = db.reference('sensors/sensor_38/value')

n39 = db.reference('sensors/sensor_39/name')
v39 = db.reference('sensors/sensor_39/value')

n40 = db.reference('sensors/sensor_40/name')
v40 = db.reference('sensors/sensor_40/value')
 
#intializing a dictionary with sensor name and data 
car_slots_dict ={n1:v1,n2:v2,n3:v3,n4:v4,n5:v5,n6:v6,n7:v7,n8:v8,n9:v9,n10:v10,
                n11:v11,n12:v12,n13:v13,n14:v14,n15:v15,n16:v16,n17:v17,n18:v18,n19:v19,n20:v20,
                n21:v21,n22:v22,n23:v23,n24:v24,n25:v25,n26:v26,n27:v27,n28:v28,n29:v29,n30:v30,
                n31:v31,n32:v32,n33:v33,n34:v34,n35:v35,n36:v36,n37:v37,n38:v38,n39:v39,n40:v40
}


#creating an array for empty current car slots list 
current_slots=[]

def update_car_slots():
    current_slots.clear()
   
    for x,y in car_slots_dict.items():
        print(x.get(),y.get())
        if int(y.get())>30:
            current_slots.append(x.get())
    print(current_slots)
    root.after(300000,update_car_slots)

#calling that function
update_car_slots()

#creating a function to display data
shifter =  0
def display_current_pos():
    global shifter
    print("debug"+ shifter)
    print("debug"+ trigger.get())
    if ((trigger.get() == "true") and  (shifter==0)):
        print(" debug 1")
        shifter = 1
        if (len(current_slots)==0):
            storage  = 'parking is full'

            label['text'] = storage

        else:
            print("debug 2")
            storage  =  current_slots[0]
            current_slots.remove(storage)
            label['text'] = storage
            print("debug" + current_slots)
    if ((trigger.get() == "false")):
        print("debug 3")
        shifter = 0



# creating function for displaying data as tabs with color

def  display_data(a,b,c):
    display = "{0}\n{1}".format(b,a)
    c['text'] = display
def display_color(a,b):
    if(int(a)<30):
        b.configure(bg="red")
    else:
        b.configure(bg="green")
# final display function
def display():
    display_current_pos()

    display_data(v1.get(),n1.get(),button1)
    display_data(v2.get(),n2.get(),button2)
    display_data(v3.get(),n3.get(),button3)
    display_data(v4.get(),n4.get(),button4)
    display_data(v5.get(),n5.get(),button5)
    display_data(v6.get(),n6.get(),button6)
    display_data(v7.get(),n7.get(),button7)
    display_data(v8.get(),n8.get(),button8)
    display_data(v9.get(),n9.get(),button9)
    display_data(v10.get(),n10.get(),button10)
    display_data(v11.get(),n11.get(),button11)
    display_data(v12.get(),n12.get(),button12)
    display_data(v13.get(),n13.get(),button13)
    display_data(v14.get(),n14.get(),button14)
    display_data(v15.get(),n15.get(),button15)
    display_data(v16.get(),n16.get(),button16)
    display_data(v17.get(),n17.get(),button17)
    display_data(v18.get(),n18.get(),button18)
    display_data(v19.get(),n19.get(),button19)
    display_data(v20.get(),n20.get(),button20)
    display_data(v21.get(),n21.get(),button21)
    display_data(v22.get(),n22.get(),button22)
    display_data(v23.get(),n23.get(),button23)
    display_data(v24.get(),n24.get(),button24)
    display_data(v25.get(),n25.get(),button25)
    display_data(v26.get(),n26.get(),button26)
    display_data(v27.get(),n27.get(),button27)
    display_data(v28.get(),n28.get(),button28)
    display_data(v29.get(),n29.get(),button29)
    display_data(v30.get(),n30.get(),button30)
    display_data(v31.get(),n31.get(),button31)
    display_data(v32.get(),n32.get(),button32)
    display_data(v33.get(),n33.get(),button33)
    display_data(v34.get(),n34.get(),button34)
    display_data(v35.get(),n35.get(),button35)
    display_data(v36.get(),n36.get(),button36)
    display_data(v37.get(),n37.get(),button37)
    display_data(v38.get(),n38.get(),button38)
    display_data(v39.get(),n39.get(),button39)
    display_data(v40.get(),n40.get(),button40)
    
    
    
    display_color(v1.get(),button1)
    display_color(v2.get(),button2)
    display_color(v3.get(),button3)
    display_color(v4.get(),button4)
    display_color(v5.get(),button5)
    display_color(v6.get(),button6)
    display_color(v7.get(),button7)
    display_color(v8.get(),button8)
    display_color(v9.get(),button9)
    display_color(v10.get(),button10)
    display_color(v11.get(),button11)
    display_color(v12.get(),button12)
    display_color(v13.get(),button13)
    display_color(v14.get(),button14)
    display_color(v15.get(),button15)
    display_color(v16.get(),button16)
    display_color(v17.get(),button17)
    display_color(v18.get(),button18)
    display_color(v19.get(),button19)
    display_color(v20.get(),button20)
    display_color(v21.get(),button21)
    display_color(v22.get(),button22)
    display_color(v23.get(),button23)
    display_color(v24.get(),button24)
    display_color(v25.get(),button25)
    display_color(v26.get(),button26)
    display_color(v27.get(),button27)
    display_color(v28.get(),button28)
    display_color(v29.get(),button29)
    display_color(v30.get(),button30)
    display_color(v31.get(),button31)
    display_color(v32.get(),button32)
    display_color(v33.get(),button33)
    display_color(v34.get(),button34)
    display_color(v35.get(),button35)
    display_color(v36.get(),button36)
    display_color(v37.get(),button37)
    display_color(v38.get(),button38)
    display_color(v39.get(),button39)
    display_color(v40.get(),button40)
    
    
    
    root.after(1000,display)
    

  




#creating graphical user interface with Tkinter


label = Label(root,text="hello",height=1,width=30,bg="black",fg="red",font="ariel 40")
label.grid(row=0,column=0,columnspan = 6)

button1 = Button(root,height=3,width=20,bg="white")
button1.grid(row=1,column=0)
button2 = Button(root,height=3,width=20,bg="white")
button2.grid(row=2,column=0)
button3 = Button(root,height=3,width=20,bg="white")
button3.grid(row=3,column=0)
button4 = Button(root,height=3,width=20,bg="white")
button4.grid(row=4,column=0)
button5 = Button(root,height=3,width=20,bg="white")
button5.grid(row=5,column=0)
button6 = Button(root,height=3,width=20,bg="white")
button6.grid(row=6,column=0)
button7 = Button(root,height=3,width=20,bg="white")
button7.grid(row=7,column=0)
button8 = Button(root,height=3,width=20,bg="white")
button8.grid(row=8,column=0)
button9 = Button(root,height=3,width=20,bg="white")
button9.grid(row=9,column=0)
button10 = Button(root,height=3,width=20,bg="white")
button10.grid(row=10,column=0)


button_pass_1=Button(root,text="Passage \n 1",font="ariel",height=35,width=35,)
button_pass_1.grid(row=1,column=1,rowspan=10)


button11 = Button(root,height=3,width=20,bg="white")
button11.grid(row=1,column=2)
button12 = Button(root,height=3,width=20,bg="white")
button12.grid(row=2,column=2)
button13 = Button(root,height=3,width=20,bg="white")
button13.grid(row=3,column=2)
button14 = Button(root,height=3,width=20,bg="white")
button14.grid(row=4,column=2)
button15 = Button(root,height=3,width=20,bg="white")
button15.grid(row=5,column=2)
button16 = Button(root,height=3,width=20,bg="white")
button16.grid(row=6,column=2)
button17 = Button(root,height=3,width=20,bg="white")
button17.grid(row=7,column=2)
button18 = Button(root,height=3,width=20,bg="white")
button18.grid(row=8,column=2)
button19 = Button(root,height=3,width=20,bg="white")
button19.grid(row=9,column=2)
button20 = Button(root,height=3,width=20,bg="white")
button20.grid(row=10,column=2)

button21 = Button(root,height=3,width=20,bg="white")
button21.grid(row=1,column=3)
button22 = Button(root,height=3,width=20,bg="white")
button22.grid(row=2,column=3)
button23 = Button(root,height=3,width=20,bg="white")
button23.grid(row=3,column=3)
button24 = Button(root,height=3,width=20,bg="white")
button24.grid(row=4,column=3)
button25 = Button(root,height=3,width=20,bg="white")
button25.grid(row=5,column=3)
button26 = Button(root,height=3,width=20,bg="white")
button26.grid(row=6,column=3)
button27 = Button(root,height=3,width=20,bg="white")
button27.grid(row=7,column=3)
button28 = Button(root,height=3,width=20,bg="white")
button28.grid(row=8,column=3)
button29 = Button(root,height=3,width=20,bg="white")
button29.grid(row=9,column=3)
button30 = Button(root,height=3,width=20,bg="white")
button30.grid(row=10,column=3)



button_pass_2=Button(root,height=35,width=35,text="Passage \n 2",font="ariel")
button_pass_2.grid(row=1,column=4,rowspan=10)

button31 = Button(root,height=3,width=20,bg="white")
button31.grid(row=1,column=5)
button32 = Button(root,height=3,width=20,bg="white")
button32.grid(row=2,column=5)
button33 = Button(root,height=3,width=20,bg="white")
button33.grid(row=3,column=5)
button34 = Button(root,height=3,width=20,bg="white")
button34.grid(row=4,column=5)
button35 = Button(root,height=3,width=20,bg="white")
button35.grid(row=5,column=5)
button36 = Button(root,height=3,width=20,bg="white")
button36.grid(row=6,column=5)
button37 = Button(root,height=3,width=20,bg="white")
button37.grid(row=7,column=5)
button38 = Button(root,height=3,width=20,bg="white")
button38.grid(row=8,column=5)
button39 = Button(root,height=3,width=20,bg="white")
button39.grid(row=9,column=5)
button40 = Button(root,height=3,width=20,bg="white")
button40.grid(row=10,column=5)
# calling out main display function
display()
# calling out main loop
root.mainloop()

