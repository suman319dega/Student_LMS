import pandas as pd
import os

FILE = "simple_lms.xlsx"

SHEETS = {
    "students": ["student_id", "name"],
    "courses": ["course_id", "course_name"],
    "enrollments": ["student_id", "course_id"],
    "marks": ["student_id", "course_id", "marks"]
}

# ---------------- Create Excel if needed ----------------

def init_excel():
    if not os.path.exists(FILE):
        with pd.ExcelWriter(FILE, engine="openpyxl") as writer:
            for sheet, cols in SHEETS.items():
                pd.DataFrame(columns=cols).to_excel(writer, sheet_name=sheet, index=False)

def read(sheet):
    return pd.read_excel(FILE, sheet_name=sheet)

def write(sheet, df):
    all_data = {s: read(s) for s in SHEETS}
    all_data[sheet] = df
    with pd.ExcelWriter(FILE, engine="openpyxl") as writer:
        for s, d in all_data.items():
            d.to_excel(writer, sheet_name=s, index=False)

# ---------------- Student Functions ----------------

def add_student():
    students = read("students")
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    students.loc[len(students)] = [sid, name]
    write("students", students)
    print("Student added.\n")

def view_students():
    print("\n--- Students ---")
    print(read("students"), "\n")

def update_student():
    df = read("students")
    sid = input("Enter Student ID to update: ")
    if sid not in df["student_id"].astype(str).values:
        print("Student not found.\n")
        return
    new_name = input("Enter new name: ")
    df.loc[df["student_id"].astype(str) == sid, "name"] = new_name
    write("students", df)
    print("Student updated.\n")

def delete_student():
    df = read("students")
    sid = input("Enter Student ID to delete: ")
    df = df[df["student_id"].astype(str) != sid]
    write("students", df)
    print("Student deleted.\n")

# ---------------- Course Functions ----------------

def add_course():
    courses = read("courses")
    cid = input("Enter Course ID: ")
    cname = input("Enter Course Name: ")
    courses.loc[len(courses)] = [cid, cname]
    write("courses", courses)
    print("Course added.\n")

def view_courses():
    print("\n--- Courses ---")
    print(read("courses"), "\n")

def delete_course():
    df = read("courses")
    cid = input("Enter Course ID to delete: ")
    df = df[df["course_id"].astype(str) != cid]
    write("courses", df)
    print("Course deleted.\n")

# ---------------- Enrollment ----------------

def enroll_student():
    en = read("enrollments")
    sid = input("Student ID: ")
    cid = input("Course ID: ")
    en.loc[len(en)] = [sid, cid]
    write("enrollments", en)
    print("Student enrolled.\n")

def view_enrollments():
    print("\n--- Enrollments ---")
    print(read("enrollments"), "\n")

# ---------------- Marks ----------------

def add_marks():
    marks_df = read("marks")
    sid = input("Student ID: ")
    cid = input("Course ID: ")
    marks = input("Enter Marks: ")
    marks_df.loc[len(marks_df)] = [sid, cid, marks]
    write("marks", marks_df)
    print("Marks added.\n")

def update_marks():
    df = read("marks")
    sid = input("Student ID: ")
    cid = input("Course ID: ")

    if not ((df["student_id"].astype(str) == sid) & (df["course_id"].astype(str) == cid)).any():
        print("Marks not found.\n")
        return

    new_marks = input("Enter new marks: ")
    df.loc[(df["student_id"].astype(str) == sid) & (df["course_id"].astype(str) == cid), "marks"] = new_marks
    write("marks", df)
    print("Marks updated.\n")

def view_marks():
    df = read("marks")
    sid = input("Enter Student ID: ")
    result = df[df["student_id"].astype(str) == sid]
    print("\n--- Marks ---")
    print(result, "\n")

# ---------------- Full Report Card ----------------

def report_card():
    sid = input("Enter Student ID: ")

    students = read("students")
    marks = read("marks")
    courses = read("courses")

    s = students[students["student_id"].astype(str) == sid]
    if s.empty:
        print("Student not found.\n")
        return

    print(f"\n===== REPORT CARD FOR {s.iloc[0]['name']} =====")

    student_marks = marks[marks["student_id"].astype(str) == sid]
    if student_marks.empty:
        print("No marks available.\n")
        return

    merged = student_marks.merge(courses, on="course_id", how="left")
    print(merged[["course_name", "marks"]], "\n")

    # Percentage (only if numerical)
    total = 0
    count = 0
    for m in merged["marks"]:
        try:
            total += float(m)
            count += 1
        except:
            pass

    if count > 0:
        print(f"Total: {total}")
        print(f"Percentage: {total / count:.2f}%\n")

# ---------------- Menu ----------------

def main():
    init_excel()
    while True:
        print("===== SIMPLE LMS =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Course")
        print("6. View Courses")
        print("7. Delete Course")
        print("8. Enroll Student")
        print("9. View Enrollments")
        print("10. Add Marks")
        print("11. Update Marks")
        print("12. View Marks")
        print("13. Report Card")
        print("14. Exit")

        choice = input("Enter choice: ")

        if choice == "1": add_student()
        elif choice == "2": view_students()
        elif choice == "3": update_student()
        elif choice == "4": delete_student()
        elif choice == "5": add_course()
        elif choice == "6": view_courses()
        elif choice == "7": delete_course()
        elif choice == "8": enroll_student()
        elif choice == "9": view_enrollments()
        elif choice == "10": add_marks()
        elif choice == "11": update_marks()
        elif choice == "12": view_marks()
        elif choice == "13": report_card()
        elif choice == "14":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()
