from create_db import Student
from sqlmodel import Session, create_engine, select

sqlite_url = "sqlite:///school.db"
engine = create_engine(sqlite_url, echo=True)


# Read database
with Session(engine) as session:
    statement = select(Student)
    results = session.exec(statement)
    for student in results:
        print(student)
        print("-"*100)


# # Read one row
# with Session(engine) as session:
#     statement = select(Student).where(Student.first_name=="Misal")
#     results = session.exec(statement)
#     for student in results:
#         print(student)
