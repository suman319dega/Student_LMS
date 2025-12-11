<p align="center">
<pre>    

     SIMPLE STUDENT LMS (PYTHON + EXCEL)
</pre>
</p>

---

## 🚀 Overview

A clean, simple, and beginner-friendly **console-based Learning Management System (LMS)** built using Python.  
This application helps you manage:

✔ Students  
✔ Courses  
✔ Enrollments  
✔ Marks  
✔ Report Cards  

All data is stored **locally in an Excel file** using `pandas` + `openpyxl`.  
Perfect for beginner Python developers, academic projects, and mini-project submissions.

---

# 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Excel Storage](https://img.shields.io/badge/Storage-Excel-green)
![Platform](https://img.shields.io/badge/Platform-Console--Based-orange)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

---

# 📑 Table of Contents

- [Features](#-features)
- [Data Storage](#%EF%B8%8F-data-storage)
- [Technologies Used](#%EF%B8%8F-technologies-used)
- [How to Run](#%EF%B8%8F-how-to-run)
- [Project Structure](#-project-structure)
- [Sample Output](#-sample-output)
- [Learning Goals](#-learning-goals)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

# 🚀 Features

## 🎓 Student Management
- Add Student  
- View All Students  
- Update Student  
- Delete Student  

## 📚 Course Management
- Add Course  
- View Courses  
- Delete Course  

## 📝 Enrollment
- Enroll Student into Course  
- View All Enrollments  

## 📊 Marks & Report Card
- Add Marks  
- Update Marks  
- View Marks  
- Generate Report Card:
  - Course-wise Marks  
  - Total Marks  
  - Percentage  

---

# 🗂️ Data Storage

All LMS data is stored in an auto-generated Excel file:


with sheets:

✔ students  
✔ courses  
✔ enrollments  
✔ marks  

No SQL database needed!

---

# 🛠️ Technologies Used

- **Python 3**  
- **pandas** – Excel read/write  
- **openpyxl** – Excel engine  

---

# ▶️ How to Run

### 1️⃣ Install Dependencies
```bash
pip install pandas openpyxl


2️⃣ Run the Program
python app.py


The console menu will appear.

📦 Project Structure
Student_LMS/
│── app.py                 # Main Application
│── simple_lms.xlsx        # Auto-generated
└── README.md              # Documentation

📸 Sample Output
===== SIMPLE LMS =====
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Add Course
6. View Courses
7. Delete Course
8. Enroll Student
9. View Enrollments
10. Add Marks
11. Update Marks
12. View Marks
13. Report Card
14. Exit
