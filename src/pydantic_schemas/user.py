from pydantic import BaseModel
from src.enums.user_enums import Genders, Status


class User(BaseModel):
    id: int
    name : str
    email : str
    gender : Genders
    status : Status