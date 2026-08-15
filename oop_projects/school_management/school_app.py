import json
import streamlit as st
from abc import ABC, abstractmethod
from pathlib import Path

DATABASE = "School_data.json"


# ---------------------------------------------------------------------
# Data persistence
# ---------------------------------------------------------------------
def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE, "r") as f:
            content = f.read()
            if content:
                return json.loads(content)
    return {"students": [], "teachers": []}


def save(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)


if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data


# ---------------------------------------------------------------------
# Domain classes (same structure as the original, but no input())
# ---------------------------------------------------------------------
class Person(ABC):
    @abstractmethod
    def register(self, **kwargs):
        pass

    @abstractmethod
    def show_details(self, identifier):
        pass

    @abstractmethod
    def get_role(self):
        pass

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email


class Student(Person):
    def register(self, name, roll_no, email, standard, age):
        if not self.validate_email(email):
            return False, "Invalid email address."

        for i in data["students"]:
            if i["roll_no"] == roll_no:
                return False, "Roll number already exists."

        data["students"].append(
            {
                "name": name,
                "roll_no": roll_no,
                "email": email,
                "standard": standard,
                "age": age,
                "grades": {},
            }
        )
        save(data)
        return True, f"Student '{name}' registered successfully."

    def get_role(self):
        return "student"

    def show_details(self, roll_no):
        for i in data["students"]:
            if i["roll_no"] == roll_no:
                return i
        return None

    def grade(self, roll_no, subject, marks):
        for i in data["students"]:
            if i["roll_no"] == roll_no:
                i["grades"][subject] = marks
                save(data)
                return True, "Grades added successfully."
        return False, "Student not found."


class Teacher(Person):
    def register(self, name, emp_no, email, post, age):
        if not self.validate_email(email):
            return False, "Invalid email address."

        for i in data["teachers"]:
            if i["emp_no"] == emp_no:
                return False, "Employee number already exists."

        data["teachers"].append(
            {
                "name": name,
                "emp_no": emp_no,
                "email": email,
                "post": post,
                "age": age,
            }
        )
        save(data)
        return True, f"Information saved for teacher '{name}'."

    def get_role(self):
        return "teacher"

    def show_details(self, emp_no):
        for i in data["teachers"]:
            if i["emp_no"] == emp_no:
                return i
        return None


stud = Student()
teach = Teacher()

# ---------------------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------------------
st.set_page_config(page_title="School Data Management", page_icon="🏫", layout="centered")
st.title("🏫 School Data Management System")

menu = st.sidebar.radio(
    "Menu",
    [
        "Register Student",
        "Register Teacher",
        "Enter Grades",
        "View Student Details",
        "View Teacher Details",
        "View All Data",
    ],
)

# 1. Register Student
if menu == "Register Student":
    st.header("Register a Student")
    with st.form("register_student", clear_on_submit=True):
        name = st.text_input("Name")
        roll_no = st.number_input("Roll No", min_value=0, step=1, format="%d")
        email = st.text_input("Email")
        standard = st.text_input("Standard")
        age = st.number_input("Age", min_value=1, max_value=100, step=1, format="%d")
        submitted = st.form_submit_button("Register")

        if submitted:
            if not name.strip():
                st.error("Name cannot be empty.")
            else:
                ok, msg = stud.register(name, int(roll_no), email, standard, int(age))
                (st.success if ok else st.error)(msg)

# 2. Register Teacher
elif menu == "Register Teacher":
    st.header("Register a Teacher")
    with st.form("register_teacher", clear_on_submit=True):
        name = st.text_input("Name")
        emp_no = st.number_input("Employee No", min_value=0, step=1, format="%d")
        email = st.text_input("Email")
        post = st.text_input("Post (e.g. PGT/TGT along with subject)")
        age = st.number_input("Age", min_value=1, max_value=100, step=1, format="%d")
        submitted = st.form_submit_button("Register")

        if submitted:
            if not name.strip():
                st.error("Name cannot be empty.")
            else:
                ok, msg = teach.register(name, int(emp_no), email, post, int(age))
                (st.success if ok else st.error)(msg)

# 3. Enter Grades
elif menu == "Enter Grades":
    st.header("Enter Grades for a Student")
    if not data["students"]:
        st.info("No students registered yet.")
    else:
        with st.form("enter_grades", clear_on_submit=True):
            roll_no = st.number_input("Roll No", min_value=0, step=1, format="%d")
            subject = st.text_input("Subject")
            marks = st.number_input("Marks", min_value=0.0, max_value=100.0, step=0.5)
            submitted = st.form_submit_button("Add Grade")

            if submitted:
                if not subject.strip():
                    st.error("Subject cannot be empty.")
                else:
                    ok, msg = stud.grade(int(roll_no), subject, marks)
                    (st.success if ok else st.error)(msg)

# 4. View Student Details
elif menu == "View Student Details":
    st.header("View Student Details")
    roll_no = st.number_input("Roll No", min_value=0, step=1, format="%d", key="view_student")
    if st.button("Search"):
        result = stud.show_details(int(roll_no))
        if result:
            st.json(result)
        else:
            st.warning("Student not found.")

# 5. View Teacher Details
elif menu == "View Teacher Details":
    st.header("View Teacher Details")
    emp_no = st.number_input("Employee No", min_value=0, step=1, format="%d", key="view_teacher")
    if st.button("Search"):
        result = teach.show_details(int(emp_no))
        if result:
            st.json(result)
        else:
            st.warning("Teacher not found.")

# 6. View All Data
elif menu == "View All Data":
    st.header("All School Data")
    tab1, tab2 = st.tabs(["Students", "Teachers"])
    with tab1:
        if data["students"]:
            st.dataframe(data["students"], use_container_width=True)
        else:
            st.info("No student records yet.")
    with tab2:
        if data["teachers"]:
            st.dataframe(data["teachers"], use_container_width=True)
        else:
            st.info("No teacher records yet.")

    with st.expander("Raw JSON"):
        st.json(data)
