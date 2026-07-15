import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime
import matplotlib.pyplot as plt

# -------------------- DATABASE --------------------

conn = sqlite3.connect("bmi.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_records(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
weight REAL,
height REAL,
bmi REAL,
category TEXT,
date TEXT
)
""")

conn.commit()

# -------------------- FUNCTIONS --------------------

def calculate_bmi():

    try:
        name = name_entry.get().strip()

        if name == "":
            messagebox.showwarning("Missing Name","Please enter your name.")
            return

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = round(weight / (height ** 2),2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"

        elif bmi < 25:
            category = "Normal"
            color = "green"

        elif bmi < 30:
            category = "Overweight"
            color = "orange"

        else:
            category = "Obese"
            color = "red"

        result.config(
            text=f"BMI : {bmi}\nCategory : {category}",
            fg=color
        )

        today = datetime.datetime.now().strftime("%d-%m-%Y")

        cursor.execute("""
        INSERT INTO bmi_records
        (name,weight,height,bmi,category,date)
        VALUES(?,?,?,?,?,?)
        """,(name,weight,height,bmi,category,today))

        conn.commit()

    except ValueError:
        messagebox.showerror("Invalid Input","Please enter valid weight and height.")

    except Exception as e:
        messagebox.showerror("Error",str(e))


# -------------------- HISTORY --------------------

def show_history():

    history=tk.Toplevel(root)

    history.title("BMI History")

    history.geometry("600x350")

    text=tk.Text(history,font=("Consolas",11))

    text.pack(fill="both",expand=True)

    cursor.execute("""
    SELECT name,bmi,category,date
    FROM bmi_records
    ORDER BY id DESC
    """)

    rows=cursor.fetchall()

    if len(rows)==0:

        text.insert(tk.END,"No Records Found.")

    else:

        for row in rows:

            text.insert(
                tk.END,
                f"{row[0]:15} BMI:{row[1]:5}   {row[2]:12}   {row[3]}\n"
            )


# -------------------- GRAPH --------------------

def show_graph():

    name=name_entry.get().strip()

    if name=="":

        messagebox.showwarning("Name Required","Enter your name first.")
        return

    cursor.execute("""
    SELECT bmi,date
    FROM bmi_records
    WHERE name=?
    """,(name,))

    rows=cursor.fetchall()

    if len(rows)==0:

        messagebox.showinfo("No Data","No BMI history found.")
        return

    bmi=[]
    dates=[]

    for row in rows:

        bmi.append(row[0])
        dates.append(row[1])

    plt.figure(figsize=(7,4))

    plt.plot(
        dates,
        bmi,
        marker="o",
        linewidth=2
    )

    plt.title(name+"'s BMI Progress")

    plt.xlabel("Date")

    plt.ylabel("BMI")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


# -------------------- GUI --------------------

root=tk.Tk()

root.title("Advanced BMI Calculator")

root.geometry("420x470")

root.configure(bg="#f4f4f4")

root.resizable(False,False)

title=tk.Label(
    root,
    text="Advanced BMI Calculator",
    font=("Segoe UI",18,"bold"),
    bg="#f4f4f4"
)

title.pack(pady=15)

tk.Label(root,text="Name",bg="#f4f4f4").pack()

name_entry=tk.Entry(root,width=30)

name_entry.pack(pady=5)

tk.Label(root,text="Weight (kg)",bg="#f4f4f4").pack()

weight_entry=tk.Entry(root,width=30)

weight_entry.pack(pady=5)

tk.Label(root,text="Height (m)",bg="#f4f4f4").pack()

height_entry=tk.Entry(root,width=30)

height_entry.pack(pady=5)

tk.Button(
    root,
    text="Calculate BMI",
    width=20,
    bg="#4CAF50",
    fg="white",
    command=calculate_bmi
).pack(pady=12)

result=tk.Label(
    root,
    text="",
    font=("Segoe UI",14,"bold"),
    bg="#f4f4f4"
)

result.pack()

tk.Button(
    root,
    text="View History",
    width=20,
    command=show_history
).pack(pady=5)

tk.Button(
    root,
    text="Show BMI Graph",
    width=20,
    command=show_graph
).pack(pady=5)

root.mainloop()

conn.close()