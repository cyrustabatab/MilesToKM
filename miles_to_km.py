import tkinter



def calculate_km():
    _input = float(miles_entry.get())
    radio_value = radio_state.get()
    if radio_value == 1:
        if _input == 1.0:
            miles_label['text'] = 'Mile'
        else:
            miles_label['text'] = "Miles"


    if radio_value == 1: 
        result = round(_input * 1.60934,2)
    else:
        result= round(_input * 0.621371,2)

    km_amount['text'] = result


def radio_used():

    radio_value = radio_state.get()
    miles_entry.delete(0,tkinter.END)
    miles_entry.insert(tkinter.END,"0")
    if radio_value == 1:
        miles_label["text"] =  'Miles'
        km_label['text'] = 'KM'
    else:
        miles_label["text"] =  'KM'
        km_label['text'] = 'Miles'




font = ("Arial",24,"bold")
radio_font = ("Arial",12,"bold")

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=500,height=200)




is_equal_to_label = tkinter.Label(text='is equal to',font=font)
is_equal_to_label.grid(row=1,column=0)
is_equal_to_label.config(padx=20)


frame_1 = tkinter.Frame()
frame_1.grid(row=2,column=0)
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(frame_1,text="M to KM",value=1,variable=radio_state,font=radio_font,command=radio_used)
radiobutton2 = tkinter.Radiobutton(frame_1,text="KM to M",value=2,variable=radio_state,font=radio_font,command=radio_used)
radio_state.set(1)
#radiobutton1.grid(row=2,column=0)
#radiobutton2.grid(row=3,column=0)
radiobutton1.grid(row=0,column=0)
radiobutton2.grid(row=0,column=1)

miles_entry = tkinter.Entry(width=15,font=font)
miles_entry.insert(tkinter.END,"0")
miles_entry.focus_set()
miles_entry.grid(row=0,column=1,pady=10,ipady=20)

miles_label = tkinter.Label(text="Miles",font=font)
miles_label.grid(row=0,column=2)
miles_label.config(padx=20)


km_amount = tkinter.Label(text='0',font=font)
km_amount.grid(row=1,column=1)

km_label = tkinter.Label(text="KM",font=font)
km_label.grid(row=1,column=2)



calculate_button = tkinter.Button(text="Calculate",font=font,command=calculate_km)
calculate_button.grid(row=2,column=1,pady=5)
calculate_button.config(padx=20,pady=5)

window.mainloop()

