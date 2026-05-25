import tkinter as tk
from tkinter import messagebox

students = []
student_labels = []

window = tk.Tk()
window.title ("Student Management System")
window.geometry("700x600")
window.resizable(True, True)
window.configure(bg= "#FFFFFF")

title_label = tk.Label(window,
                       text = "STUDENT MANAGEMENT SYSTEM",
                       font = ("Arial", 24, "bold"),
                       bg = "#FFFFFF",
                       fg = "#00FF00"
                       )
name_label = tk.Label(window,
                      text = "Student Name: ",
                      font = ("Arial", 12),
                      bg = "#FFFFFF",
                      fg = "#00FF00")
name_entry = tk.Entry(window,
                      width = 25,
                      font = ("Arial", 12)
                      )
id_label = tk.Label(window,
                    text = "Student ID: ",
                    font = ("Arial", 12),
                    bg = "#FFFFFF",
                    fg = "#00FF00")
id_entry = tk.Entry(window,
                    width = 25,
                    font = ("Arial", 12))
email_label = tk.Label(window,
                       text = "Email: ",
                       font = ("Arial", 12),
                       bg = "#FFFFFF",
                       fg = "#00FF00")
email_entry = tk.Entry (window,
                        width = 25,
                        font = ("Arial", 12))
phone_label = tk.Label(window, 
                       text = "Phone Number: ",
                       font = ("Arial", 12),
                       bg = "#FFFFFF",
                       fg = "#00FF00")
phone_entry = tk.Entry(window,
                       width = 25,
                       font = ("Arial", 12))
course_label = tk.Label(window,
                        text = "Course: ",
                        font = ("Arial", 12),
                        bg = "#FFFFFF",
                        fg = "#00FF00")
course_entry = tk.Entry(window,
                        width = 25,
                        font = ("Arial", 12))
year_label = tk.Label(window,
                      text = "Year Level:",
                      font = ("Arial", 12),
                      bg = "#FFFFFF", 
                      fg = "#00FF00")
year_entry = tk.Entry(window,
                      width = 25,
                      font = ("Arial", 12))

def addStudents():
    name = name_entry.get()
    student_id = id_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    course = course_entry.get()
    year = year_entry.get()
    gpa = gpa_entry.get()
    status = status_entry.get()

    if name == "" or student_id == "" or email == "" or phone == "" or course == "" or year == ""or gpa == "" or status == "" :
        messagebox.showwarning("Warning" , "Please complete the information.")
        return
    try:
        gpa_value = float(gpa)

        if gpa_value < 0 or gpa_value > 4:
            messagebox.showerror("Error" , "GPA must be between 0.0 - 4.0")
            return
        
    except ValueError:
        messagebox.showerror("Error" , "Invalid GPA")
        return
    
    student = {
        "name": name,
        "id": student_id,
        "email": email,
        "phone": phone, 
        "course": course, 
        "year": year,
        "gpa": gpa,
        "status": status, 
    }

    students.append(student)


    student_text = f"""

Name: {name}
ID: {student_id}
Email: {email}
Phone: {phone}
Course: {course}
Year: {year}
GPA: {gpa}
Status: {status}
- - - - - - - - - - - - - - - - - - -
 """
    
    student_label = tk.Label(list_frame,
                             text = student_text,
                             font = ("Arial" , 10),
                             bg = "#FFFFFF",
                             fg = "#00FF00",
                             justify = "center")
    
    student_label.pack(pady=2, fill="both", expand = True)

    student_labels.append(student_label)

    status_label.config(text = f"Total Students: {len(students)}")

    clearFields()

def clearFields():
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    gpa_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)

def deleteLastStudent():
    if len(students) == 0:
        messagebox.showinfo("Info", "No student record to delete.")
        return
    
    students.pop()

gpa_label = tk.Label(window,
                     text = "GPA: ",
                     font = ("Arial", 12),
                     bg = "#FFFFFF",
                     fg = "#00FF00")
gpa_entry = tk.Entry(window,
                     width = 25,
                     font = ("Arial", 12))
status_label2 = tk.Label(window,
                         text = "Status: ",
                         bg = "#FFFFFF",
                         fg = "#00FF00",
                         width = 30,
                         font = ("Arial", 12))
status_entry = tk.Entry(window,
                        width = 30,
                        font = ("Arial", 12))
status_label = tk.Label(window,
                        text = "Total Students: 0",
                        font = ("Arial", 12, "bold"),
                        bg = "#FFFFFF")

btn_frame = tk.Frame(window, bg="#FFFFFF")
btn_add = tk.Button(window,
                    text = "Add Student",
                    font = ("Arial", 11),
                    bg = "#008080",
                    fg = "#FFFFFF",
                    command= addStudents
                    )
btn_clear = tk.Button(window,
                      text = "Clear Fields",
                      font = ("Arial", 11),
                      bg = "#008080",
                      fg = "#FFFFFF",
                      command = clearFields
                      )
btn_delete = tk.Button(window,
                       text = "Delete Last Record",
                       font = ("Arial", 11),
                       bg = "#008080",
                       fg = "#FFFFFF",
                       command = deleteLastStudent
                       )

list_title = tk.Label(window,
                      text = "Student List: ",
                      font = ("Arial", 12, "bold"),
                      bg = "#FFFFFF",
                      fg = "#00FF00")
list_frame = tk.Frame(window,
                      bg = "#FFFFFF",
                      bd = 2,
                      relief = "groove",
                      width = 750,
                      height = 450)
list_frame.pack_propagate(False)

title_label.pack(pady=15)
name_label.pack()
name_entry.pack(pady=2)
id_label.pack()
id_entry.pack(pady=2)
email_label.pack()
email_entry.pack(pady=2)
phone_label.pack()
phone_entry.pack(pady=2)
course_label.pack()
course_entry.pack(pady=2)
year_label.pack()
year_entry.pack(pady=2)
gpa_label.pack()
gpa_entry.pack(pady=2)
status_label2.pack()
status_entry.pack(pady=2)

btn_frame.pack(pady=15)
btn_add.pack(side=tk.LEFT, padx= 5)
btn_clear.pack(side=tk.LEFT, padx=5)
btn_delete.pack(side=tk.LEFT, padx=5)

status_label.pack(pady=5)
list_title.pack()
list_frame.pack(padx = 20, pady = 5)

window.mainloop()