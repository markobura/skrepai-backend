from pydantic import BaseModel


class Candidate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
