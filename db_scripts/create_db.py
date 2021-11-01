from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    # dob: 


sqlite_url = "sqlite:///school.db"
engine = create_engine(sqlite_url)
SQLModel.metadata.create_all(engine)
