from pydantic import BaseModel, HttpUrl, validator
from typing import Optional, List
from datetime import date, datetime


def date2datetime(date):
    return datetime.combine(date, datetime.min.time())


class Address(BaseModel):
    House_Number: Optional[int]
    Area: Optional[str]
    City: str
    State: str
    Pincode: Optional[str]
    Country: str


class Social(BaseModel):
    Website: Optional[HttpUrl]
    Linkedin: Optional[HttpUrl]
    GitHub: Optional[HttpUrl]
    Twitter: Optional[HttpUrl]
    Spotify: Optional[HttpUrl]
    Instagram: Optional[HttpUrl]


class Skill(BaseModel):
    Name: str
    Type: str
    Expertise: Optional[int]


class Date(BaseModel):
    Start_Date: date
    End_Date: Optional[date]
    _normalize_date = validator(
        "Start_Date", "End_Date", allow_reuse=True)(date2datetime)


class Personal_Info(BaseModel):
    First_Name: str
    Last_Name: str
    Date_of_Birth: date
    Sex: str
    Interests: Optional[List[str]]
    Profile_Picture_URL: str
    Address: Address
    Mobile_Number: str
    Current_Title: str
    Mail_ID: str
    Social: Optional[Social]
    Professional_Summary: str
    _normalize_date = validator(
        "Date_of_Birth", allow_reuse=True)(date2datetime)


class Project(BaseModel):
    Title: str
    Tech_Stacks: List[Skill]
    Summary: List[str]
    Repo_URL: Optional[HttpUrl]
    Hosting_URL: Optional[HttpUrl]
    Date: Date


class Experience(BaseModel):
    Designation: str
    Type: str
    Date: Date
    Company_Name: str
    Company_URL: HttpUrl
    Achievements: Optional[List]
    Technologies_worked_on: List[Skill]
    Summary: List[str]
    Address: Address


class Publication(BaseModel):
    Title: str
    Publishing_Journal: str
    Publishing_URL: HttpUrl
    Abstract: str
    Publishing_Date: date
    Institute_Logo: Optional[str]
    Citation: str
    _normalize_date = validator(
        "Publishing_Date", allow_reuse=True)(date2datetime)


class Education(BaseModel):
    Degree: str
    Degree_Type: str
    University_or_Board: str
    College_or_School: str
    Date: Date
    Address: Address
    Achievements: Optional[List[str]]
    Grades: str
    Institute_URL: Optional[HttpUrl]
    Institute_Logo: Optional[str]


class Certification(BaseModel):
    Title: str
    From: str
    Issuing_organization: str
    Credential_URL: HttpUrl
    Issuing_Date: date
    _normalize_date = validator(
        "Issuing_Date", allow_reuse=True)(date2datetime)

def sort_skills(skillz):
    order = ['Language',
    'Framework',
    'Cloud Services',
    'Database',
    'IDE',
    'Operating System']
    skills = []
    for i in range(len(order)):
        for skill in skillz:
            if skill['Type'] == order[i]:
                skills.append(skill)
    return skills