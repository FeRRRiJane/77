from pydantic import BaseModel


class User(BaseModel):

    user_id : int
    email : str
    password : str
 



class Employee(BaseModel):
    employee_id : int
    current_salary : str
    date_rotation : str