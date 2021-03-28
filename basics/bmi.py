import tkinter

root = tkinter.Tk()
root.geometry("350x300")
#root.configure(background="Grey")
root.title("BMI Calculator")

# function for command button
def calculate_bmi():
    height = float(entry_height.get())
    weight = float(entry_weight.get())
    bmi = round(weight / (height ** 2),2)
    label_result["text"] = "Your BMI is {}".format(bmi)

# Create GUI
# first label widget
label_height = tkinter.Label(root, text="Enter your Height:")
label_height.pack()
# first entry text widget
entry_height = tkinter.Entry(root)
entry_height.pack()
# second label widget
label_weight = tkinter.Label(root, text = "Enter your Weight:")
label_weight.pack()
# second entry text widget
entry_weight = tkinter.Entry(root)
entry_weight.pack()

# 1 button widget
button_calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.pack()

# third label widget
label_result = tkinter.Label(root, text="Result:")
label_result.pack()

root.mainloop()