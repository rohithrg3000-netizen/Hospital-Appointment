# Hospital Appointment Booking System - Tkinter (3 pages)
# Page 1: Login   Page 2: Book Appointment   Page 3: Dashboard
# Data is stored in Python lists and dictionaries (no database).

import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- Data ----------------
# user accounts: username -> password
# it starts empty; users create their own account with "Sign Up"
users = {}

# department -> list of doctors
doctors = {
    "Cardiology": ["Dr. Ananya Krishnan", "Dr. Rajesh Menon"],
    "Orthopedics": ["Dr. Sanjay Gupta"],
    "Pediatrics": ["Dr. Lakshmi Iyer"],
    "General Medicine": ["Dr. Suresh Babu", "Dr. Kavya Nair"],
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_slots = ["09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "03:00 PM"]

# each appointment is a dictionary
appointments = [
    {"name": "Ramesh Kumar", "age": "58", "gender": "Male", "phone": "9840012345",
     "doctor": "Dr. Ananya Krishnan", "day": "Monday", "time": "10:00 AM"},
    {"name": "Sita Devi", "age": "34", "gender": "Female", "phone": "9876543210",
     "doctor": "Dr. Suresh Babu", "day": "Tuesday", "time": "09:00 AM"},
]


class HospitalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hospital Appointment Booking")
        self.geometry("750x520")

        # all three pages are frames placed in the same spot
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.pages = {}
        for Page in (LoginPage, BookingPage, DashboardPage):
            page = Page(container, self)
            self.pages[Page.__name__] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("LoginPage")

    def show_page(self, name):
        page = self.pages[name]
        page.refresh()          # update the page's data before showing it
        page.tkraise()          # bring the page to the front


# ---------------- Page 1: Login ----------------
class LoginPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        tk.Label(self, text="Hospital Login", font=("Arial", 20, "bold")).pack(pady=40)

        form = tk.Frame(self)
        form.pack()
        tk.Label(form, text="Username:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.user_entry = tk.Entry(form, font=("Arial", 12))
        self.user_entry.grid(row=0, column=1, pady=10)

        tk.Label(form, text="Password:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.pass_entry = tk.Entry(form, font=("Arial", 12), show="*")
        self.pass_entry.grid(row=1, column=1, pady=10)

        buttons = tk.Frame(self)
        buttons.pack(pady=15)
        tk.Button(buttons, text="Login", font=("Arial", 12), width=10, bg="#80CBC4", fg="black", activebackground="#4DB6AC",
                  command=self.login).grid(row=0, column=0, padx=5)
        tk.Button(buttons, text="Sign Up", font=("Arial", 12), width=10,
                  command=self.signup).grid(row=0, column=1, padx=5)
        tk.Label(self, text="New user? Type a username and password, then click Sign Up.", fg="gray").pack()

        # pressing Enter in the password box also logs in
        self.pass_entry.bind("<Return>", lambda event: self.login())

    def refresh(self):
        self.pass_entry.delete(0, tk.END)

    def signup(self):
        username = self.user_entry.get().strip()
        password = self.pass_entry.get()

        if username == "" or password == "":
            messagebox.showwarning("Error", "Please enter a username and password")
        elif username in users:
            messagebox.showerror("Error", "This username already exists. Please login.")
        elif len(password) < 4:
            messagebox.showerror("Error", "Password must be at least 4 characters")
        else:
            users[username] = password          # save the new account
            messagebox.showinfo("Success", "Account created! You can now login.")
            self.pass_entry.delete(0, tk.END)

    def login(self):
        username = self.user_entry.get().strip()
        password = self.pass_entry.get()

        if username == "" or password == "":
            messagebox.showwarning("Error", "Please enter username and password")
        elif username not in users:
            messagebox.showerror("Error", "No account found. Please Sign Up first.")
        elif users[username] != password:
            messagebox.showerror("Error", "Wrong password")
        else:
            self.app.show_page("BookingPage")


# ---------------- Page 2: Book Appointment ----------------
class BookingPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        tk.Label(self, text="Book an Appointment", font=("Arial", 18, "bold")).pack(pady=15)

        form = tk.Frame(self)
        form.pack()

        tk.Label(form, text="Patient Name:", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=6, sticky="e")
        self.name_entry = tk.Entry(form, font=("Arial", 11), width=25)
        self.name_entry.grid(row=0, column=1, pady=6, sticky="w")

        tk.Label(form, text="Age:", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=6, sticky="e")
        self.age_entry = tk.Entry(form, font=("Arial", 11), width=8)
        self.age_entry.grid(row=1, column=1, pady=6, sticky="w")

        tk.Label(form, text="Gender:", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=6, sticky="e")
        self.gender = tk.StringVar(value="Male")
        gender_frame = tk.Frame(form)
        gender_frame.grid(row=2, column=1, sticky="w")
        tk.Radiobutton(gender_frame, text="Male", variable=self.gender, value="Male").pack(side="left")
        tk.Radiobutton(gender_frame, text="Female", variable=self.gender, value="Female").pack(side="left")

        tk.Label(form, text="Phone No:", font=("Arial", 11)).grid(row=3, column=0, padx=10, pady=6, sticky="e")
        self.phone_entry = tk.Entry(form, font=("Arial", 11), width=25)
        self.phone_entry.grid(row=3, column=1, pady=6, sticky="w")

        tk.Label(form, text="Department:", font=("Arial", 11)).grid(row=4, column=0, padx=10, pady=6, sticky="e")
        self.dept_box = ttk.Combobox(form, values=list(doctors.keys()), state="readonly", width=23)
        self.dept_box.grid(row=4, column=1, pady=6, sticky="w")
        # when a department is chosen, fill the doctor list
        self.dept_box.bind("<<ComboboxSelected>>", self.update_doctors)

        tk.Label(form, text="Doctor:", font=("Arial", 11)).grid(row=5, column=0, padx=10, pady=6, sticky="e")
        self.doctor_box = ttk.Combobox(form, state="readonly", width=23)
        self.doctor_box.grid(row=5, column=1, pady=6, sticky="w")

        tk.Label(form, text="Day:", font=("Arial", 11)).grid(row=6, column=0, padx=10, pady=6, sticky="e")
        self.day_box = ttk.Combobox(form, values=days, state="readonly", width=23)
        self.day_box.grid(row=6, column=1, pady=6, sticky="w")

        tk.Label(form, text="Time:", font=("Arial", 11)).grid(row=7, column=0, padx=10, pady=6, sticky="e")
        self.time_box = ttk.Combobox(form, values=time_slots, state="readonly", width=23)
        self.time_box.grid(row=7, column=1, pady=6, sticky="w")

        buttons = tk.Frame(self)
        buttons.pack(pady=15)
        tk.Button(buttons, text="Book Appointment", width=16, bg="#80CBC4", fg="black", activebackground="#4DB6AC",
                  command=self.book).grid(row=0, column=0, padx=5)
        tk.Button(buttons, text="Clear", width=10, command=self.clear_form).grid(row=0, column=1, padx=5)
        tk.Button(buttons, text="Go to Dashboard", width=15,
                  command=lambda: app.show_page("DashboardPage")).grid(row=0, column=2, padx=5)
        tk.Button(buttons, text="Logout", width=10, command=self.logout).grid(row=0, column=3, padx=5)

    def refresh(self):
        pass        # nothing to reload on this page

    def update_doctors(self, event):
        dept = self.dept_box.get()
        self.doctor_box.config(values=doctors[dept])
        self.doctor_box.set("")

    def book(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        phone = self.phone_entry.get().strip()
        doctor = self.doctor_box.get()
        day = self.day_box.get()
        time = self.time_box.get()

        # ---- validation ----
        if name == "" or age == "" or phone == "" or doctor == "" or day == "" or time == "":
            messagebox.showwarning("Error", "Please fill all the fields")
            return
        if not age.isdigit():
            messagebox.showerror("Error", "Age must be a number")
            return
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Phone number must be 10 digits")
            return

        # check if this doctor is already booked at the same day and time
        for a in appointments:
            if a["doctor"] == doctor and a["day"] == day and a["time"] == time:
                messagebox.showerror("Error", f"{doctor} is already booked on {day} at {time}")
                return

        appointments.append({"name": name, "age": age, "gender": self.gender.get(),
                             "phone": phone, "doctor": doctor, "day": day, "time": time})
        messagebox.showinfo("Booked", f"Appointment booked for {name}\nwith {doctor}\non {day} at {time}")
        self.clear_form()

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.gender.set("Male")
        self.dept_box.set("")
        self.doctor_box.set("")
        self.doctor_box.config(values=[])
        self.day_box.set("")
        self.time_box.set("")

    def logout(self):
        if messagebox.askyesno("Logout", "Do you want to logout?"):
            self.app.show_page("LoginPage")


# ---------------- Page 3: Dashboard ----------------
class DashboardPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        tk.Label(self, text="Appointments Dashboard", font=("Arial", 18, "bold")).pack(pady=15)

        self.count_label = tk.Label(self, font=("Arial", 12))
        self.count_label.pack()
        self.dept_label = tk.Label(self, font=("Arial", 11), fg="#00796B")
        self.dept_label.pack(pady=(0, 10))

        # table of appointments
        columns = ("name", "age", "gender", "doctor", "day", "time")
        self.table = ttk.Treeview(self, columns=columns, show="headings", height=10)
        headings = ["Patient", "Age", "Gender", "Doctor", "Day", "Time"]
        widths = [140, 50, 70, 170, 100, 90]
        for col, text, width in zip(columns, headings, widths):
            self.table.heading(col, text=text)
            self.table.column(col, width=width)
        self.table.pack(pady=5)

        buttons = tk.Frame(self)
        buttons.pack(pady=15)
        tk.Button(buttons, text="Cancel Appointment", width=17, bg="#EF9A9A", fg="black", activebackground="#E57373",
                  command=self.cancel).grid(row=0, column=0, padx=5)
        tk.Button(buttons, text="Back", width=12,
                  command=lambda: app.show_page("BookingPage")).grid(row=0, column=1, padx=5)

    def refresh(self):
        self.table.delete(*self.table.get_children())
        for a in appointments:
            self.table.insert("", tk.END, values=(a["name"], a["age"], a["gender"],
                                                   a["doctor"], a["day"], a["time"]))

        self.count_label.config(text=f"Total Appointments: {len(appointments)}")

        # count appointments in each department
        counts = []
        for dept, doctor_list in doctors.items():
            n = 0
            for a in appointments:
                if a["doctor"] in doctor_list:
                    n += 1
            counts.append(f"{dept}: {n}")
        self.dept_label.config(text="   |   ".join(counts))

    def cancel(self):
        selected = self.table.selection()
        if not selected:
            messagebox.showwarning("Error", "Please select an appointment to cancel")
            return
        index = self.table.index(selected[0])
        a = appointments[index]
        if messagebox.askyesno("Cancel", f"Cancel appointment of {a['name']}?"):
            appointments.pop(index)
            self.refresh()


app = HospitalApp()
app.mainloop()
