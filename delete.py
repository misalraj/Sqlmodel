from create_db import Student
from sqlmodel import Session, create_engine, select

sqlite_url = "sqlite:///school.db"
engine = create_engine(sqlite_url, echo=True)


# Update the record

with Session(engine) as session:
    statement = select(Student).where(Student.first_name=="Vijay")
    result = session.exec(statement)
    student = result.one()
    print("fetch result", student)

    session.delete(student)  #Delete data
    session.commit()

