from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    tablename = "users"
    table_args = {'extend_existing': True}


    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))



    class Employee(Base):
        employee_id = Column(Integer, primary_key=True, nullable=False)
        current_salary = Column(String,nullable=False)
        date_rotation = Column(String,nullable=False)
