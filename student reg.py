import tkinter as tk
window = tk.Tk()
window.title("Student Registration Form")
window.geometry("400x450")
tk.Label(window, text="Name").pack()
e1 = tk.Entry(window)
e1.pack()

tk.Label(window, text="Age").pack()
e2 = tk.Entry(window)
e2.pack()

tk.Label(window, text="Date of Birth").pack()
e3 = tk.Entry(window)
e3.pack()

tk.Label(window, text="Phone").pack()
e4 = tk.Entry(window)
e4.pack()

tk.Label(window, text="Qualification").pack()
e5 = tk.Entry(window)
e5.pack()

tk.Label(window, text="Address").pack()
e6 = tk.Entry(window)
e6.pack()
tk.Label(window, text="Gender").pack()
gender_var = tk.StringVar()

tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").pack()
def show_data():
    name = e1.get()
    age = e2.get()
    dob = e3.get()
    phone = e4.get()
    qualification = e5.get()
    address = e6.get()
    gender = gender_var.get()

    print("Student Details")
    print("Name:", name)
    print("Age:", age)
    print("DOB:", dob)
    print("Phone:", phone)
    print("Qualification:", qualification)
    print("Address:", address)
    print("Gender:", gender)
tk.Button(window, text="Submit", command=show_data).pack(pady=10)

window.mainloop()