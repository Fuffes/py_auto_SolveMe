
from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from src.enums.user_enums import Status
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Network, IPv6Network
from pydantic.color import Color


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4

class Owner(BaseModel):
    name: str
    card: PaymentCardNumber
    email: EmailStr

class Detailes(BaseModel):
    physical : Physical
    owners: List[Owner]

class Computer(BaseModel):
    status: Status
    activated_at: PastDate
    exp_at: FutureDate
    host_v4: IPv4Network
    host_v6: IPv6Network
    details: Detailes





