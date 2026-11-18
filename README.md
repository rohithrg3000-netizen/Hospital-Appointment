# Hospital Appointment Booking System (Tkinter)

A simple 3-page desktop app made with **Python Tkinter**.
Data is stored in Python lists and dictionaries (no database).

> Course: 21CSC203P – Advanced Programming Practice
> R.K. Krishiv Kumar (RA2511028010156), SRMIST

## Pages
1. **Login / Sign Up**: there are no built-in login details. A new user types a username and password and clicks *Sign Up* to create an account (stored in a dictionary), then clicks *Login*. Empty fields, short passwords (under 4 characters), existing usernames, unknown users and wrong passwords all show an error message.
2. **Book Appointment**: enter patient details, choose department, doctor, day and time. Choosing a department fills the doctor list automatically.
3. **Dashboard**: shows total appointments, the count per department, and a table of all appointments. Select a row and click *Cancel Appointment* to remove it.

## Screenshots
| Login before signing up | After Sign Up |
|---|---|
| ![No account](screenshots/01_login_no_account.png) | ![Sign up](screenshots/02_signup.png) |

| Booking form | After booking |
|---|---|
| ![Booking form](screenshots/03_booking_form.png) | ![Booked](screenshots/04_appointment_booked.png) |

| Dashboard |
|---|
| ![Dashboard](screenshots/05_dashboard.png) |

*(The yellow bar at the bottom of some screenshots shows the text of the popup message.)*

## Validation
- Sign Up: username must be new, password at least 4 characters
- All fields must be filled
- Age must be a number
- Phone number must be 10 digits
- The same doctor can't be booked twice at the same day and time

## Tkinter concepts used
- `Tk`, `Frame`, `Label`, `Entry`, `Button`, `Radiobutton`, `ttk.Combobox`, `ttk.Treeview`
- `pack()` and `grid()` layouts, `StringVar`
- Switching between pages with `tkraise()`
- Event handling: button `command=`, `bind("<Return>", ...)`, `bind("<<ComboboxSelected>>", ...)`
- `messagebox` for errors, confirmations and success messages

## How to run
Needs only Python 3 (Tkinter comes with Python, no packages to install).

```
python main.py
```

First click **Sign Up** with any username and password (at least 4 characters), then click **Login**.
Accounts are kept in memory, so you need to sign up again each time the app restarts.
