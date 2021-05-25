import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.geometry("380x500")
root.configure(background="Grey")
root.title("BMI Calculator")

# function for command button
def reset_entries():
    entry_height.delete(0,"end")
    entry_weight.delete(0,"end")
    label_result["text"] = ""
    label_result_2["text"] = ""

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = round(weight / (height ** 2),2)
        label_result["text"] = "Your BMI is {}".format(bmi)
        if bmi == 18.5 or bmi < 18.5:
            label_result_2["text"] = "You are underweight"
        elif bmi > 18.5 and bmi < 25:
            label_result_2["text"] = "You are normalweight"
        elif bmi > 25 and bmi < 29:
            label_result_2["text"] = "You are overweight"
        else:
            label_result_2["text"] = "You are obesity"
    except ValueError:
        tkinter.messagebox.showerror(root, message="Not a valid number!")

# Create GUI
# first label widget
label_header = tkinter.Label(root, text="BMI CALCULATOR", bg="Grey", font=("arial",20,"bold"))
label_header.pack(pady=15)
# second label widget
label_height = tkinter.Label(root, text="Enter your Height in Meter", bg="Grey", font=("arial",12,"bold"))
label_height.pack(pady=10)
# first entry text widget
entry_height = tkinter.Entry(root, justify="center", font=("arial",15,"bold"))
entry_height.pack()
# third label widget
label_weight = tkinter.Label(root, text = "Enter your Weight in KG", bg="Grey", font=("arial",12,"bold"))
label_weight.pack(pady=10)
# second entry text widget
entry_weight = tkinter.Entry(root, justify="center", font=("arial",15,"bold"))
entry_weight.pack()

# 1 button widget
button_calculate = tkinter.Button(root, text="Calculate", font=("arial",12,"bold"), command=calculate_bmi)
button_calculate.pack(pady=15)

# 2 button_widget
button_reset = tkinter.Button(root, text="Clear Entries", font=("arial",12,"bold"), command=reset_entries)
button_reset.pack(pady=15)
 
# 3 button widget
button_close = tkinter.Button(root, text="Close Window", font=("arial",12,"bold"), command=root.destroy)
button_close.pack()

# third label widget
label_result = tkinter.Label(root, text="Result", bg="Grey", font=("arial",15,"bold"))
label_result.pack(pady=10)

label_result_2 =  tkinter.Label(root, bg="Grey", font=("arial",15,"bold"))
label_result_2.pack(pady=10)

root.mainloop()