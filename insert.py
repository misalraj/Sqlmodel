from create_db import Student
from sqlmodel import Session, create_engine

student_1 = Student(id=1, first_name="Misal", last_name="Gupta", email="misal.gupta@gmail.com")
student_2 = Student(id=2, first_name="Vivek", last_name="Kumar", email="vivek.kumar@gmail.com")
student_3 = Student(id=3, first_name="Himesh", last_name="Mahto", email="himesh.mahto@gmail.com")


sqlite_url = "sqlite:///school.db"
engine = create_engine(sqlite_url, echo=True)
session = Session(engine)

session.add(student_1)
session.add(student_2)
session.add(student_3)

session.commit()
session.close()
