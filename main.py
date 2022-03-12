from fastapi import FastAPI, status, HTTPException, Header
from utils import *
from connectDatabase import MongoConnect
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = [
    "http://www.akshatsurolia.com",
    "https://www.akshatsurolia.com",
    "http://akshatsurolia.com",
    "https://akshatsurolia.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_PASSWORD')
db = os.getenv('MONGO_DB')
SECRET_KEY = os.getenv('SECRET_KEY')

database = MongoConnect(username=username,
                        password=password, db=db)


@app.get("/")
def root():
    return "Welcome to Akshat's Portfolio"

@app.get("/requests")
def get_requests():
    requests = database.get_requests()
    if not requests:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="requests not found")
    return {"request": requests}

@app.get("/all")
def get_all():
    return database.get_all()

@app.post("/requests", status_code=status.HTTP_201_CREATED)
def request(payload: Request, origin: str = Header(None), key: str = Header(None)):
    res = database.insert_request(payload.dict(exclude_unset=True))
    return {"created_id": res.inserted_id.__str__(), "origin":origin, "key":key}

@app.post("/personal_info", status_code=status.HTTP_201_CREATED)
def personal_info(payload: Personal_Info):
    res = database.insert_personal_info(payload.dict(exclude_unset=True))
    return {"created_id": res.inserted_id.__str__()}


@app.post("/skills", status_code=status.HTTP_201_CREATED)
def skills(payload: Skill):
    res = database.insert_skills(payload.dict(exclude_unset=True))
    return {"created_id": res.inserted_id.__str__()}


@app.post("/experiences", status_code=status.HTTP_201_CREATED)
def experiences(payload: Experience):
    res = database.insert_experiences(payload.dict(exclude_unset=True))
    return {"created_id": res.inserted_id.__str__()}


@app.post("/educations", status_code=status.HTTP_201_CREATED)
def education(payload: Education):
    res = database.insert_education(payload.dict(exclude_unset=True))
    return {"created_id": res.inserted_id.__str__()}


@app.post("/certifications", status_code=status.HTTP_201_CREATED)
def certifications(payload: Certification):
    res = database.insert_certifications(payload.dict(exclude_unset=True))
    return {"created_id": res.inserted_id.__str__()}


@app.post("/projects", status_code=status.HTTP_201_CREATED)
def projects(payload: Project):
    res = database.insert_projects(payload.dict(exclude_unset=True))
    return {"created_id": res.inserted_id.__str__()}


@app.post("/publications", status_code=status.HTTP_201_CREATED)
def publications(payload: Publication):
    res = database.insert_publications(payload.dict(exclude_unset=True))
    return {"created_id": res.inserted_id.__str__()}


@app.get("/personal_info")
def get_personal_info():
    personal_info = database.get_personal_info()
    if not personal_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Personal Info not found")
    return {"personal_info": personal_info}


@app.get("/skills")
def get_skills():
    skills = database.get_skills()
    if not skills:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skills not found")
    return {"skills": skills}


@app.get("/experiences")
def get_experiences():
    experiences = database.get_experiences()
    if not experiences:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experiences not found")
    return {"experiences": experiences}


@app.get("/educations")
def get_education():
    education = database.get_education()
    if not education:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Education not found")
    return {"educations": education}


@app.get("/certifications")
def get_certifications():
    certifications = database.get_certifications()
    if not certifications:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Certifications not found")
    return {"certifications": certifications}


@app.get("/projects")
def get_projects():
    projects = database.get_projects()
    if not projects:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Projects not found")
    return {"projects": projects}


@app.get("/publications")
def get_publications():
    publications = database.get_publications()
    if not publications:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publications not found")
    return {"publications": publications}


@app.get("/personal_info/{id}")
def get_personal_info_by_id(id: str):
    personal_info = database.get_personal_info_by_id(id)
    if not personal_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Personal Info not found")
    return {"personal_info": personal_info}


@app.get("/skills/{id}")
def get_skills_by_id(id: str):
    skills = database.get_skills_by_id(id)
    if not skills:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skills not found")
    return {"skills": skills}


@app.get("/experiences/{id}")
def get_experiences_by_id(id: str):
    experiences = database.get_experiences_by_id(id)
    if not experiences:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experiences not found")
    return {"experiences": experiences}


@app.get("/educations/{id}")
def get_education_by_id(id: str):
    education = database.get_education_by_id(id)
    if not education:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Education not found")
    return {"educations": education}


@app.get("/certifications/{id}")
def get_certifications_by_id(id: str):
    certifications = database.get_certifications_by_id(id)
    if not certifications:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Certifications not found")
    return {"certifications": certifications}


@app.get("/projects/{id}")
def get_projects_by_id(id: str):
    projects = database.get_projects_by_id(id)
    if not projects:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Projects not found")
    return {"projects": projects}


@app.get("/publications/{id}")
def get_publications_by_id(id: str):
    publications = database.get_publications_by_id(id)
    if not publications:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publications not found")
    return {"publications": publications}


@app.delete("/personal_info/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_personal_info(id: str):
    personal_info = database.delete_personal_info(id)
    if personal_info is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Personal Info not found")
    return {"deleted_id": personal_info}


@app.delete("/skills/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_skills(id: str):
    skills = database.delete_skills(id)
    if skills is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skills not found")
    return {"deleted_id": skills}


@app.delete("/experiences/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_experiences_by_id(id: str):
    experiences = database.delete_experiences(id)
    if experiences is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experiences not found")
    return {"delete_count": experiences}


@app.delete("/educations/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_education_by_id(id: str):
    education = database.delete_education(id)
    if education is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Education not found")
    return {"delete_count": education}


@app.delete("/certifications/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_certifications_by_id(id: str):
    certifications = database.delete_certifications(id)
    if certifications is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Certifications not found")
    return {"delete_count": certifications}


@app.delete("/projects/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_projects_by_id(id: str):
    projects = database.delete_projects(id)
    if projects is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Projects not found")
    return {"delete_count": projects}


@app.delete("/publications/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_publications_by_id(id: str):
    publications = database.delete_publications(id)
    if publications is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publications not found")
    return {"delete_count": publications}


@app.put("/personal_info/{id}", status_code=status.HTTP_200_OK)
def update_personal_info(id: str, personal_info: Personal_Info):
    personal_info_update = database.update_personal_info(
        id, personal_info.dict(exclude_unset=True))
    if personal_info_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Personal Info not found")
    return {"modified_count": personal_info_update}


@app.put("/skills/{id}", status_code=status.HTTP_200_OK)
def update_skills(id: str, skills: Skill):
    skills_update = database.update_skills(id, skills.dict(exclude_unset=True))
    if skills_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skills not found")
    return {"modified_count": skills_update}


@app.put("/experiences/{id}", status_code=status.HTTP_200_OK)
def update_experiences_by_id(id: str, experiences: Experience):
    experiences = database.update_experiences(
        id, experiences.dict(exclude_unset=True))
    if experiences is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experiences not found")
    return {"modified_count": experiences}


@app.put("/educations/{id}", status_code=status.HTTP_200_OK)
def update_education_by_id(id: str, education: Education):
    education = database.update_education(
        id, education.dict(exclude_unset=True))
    if education is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Education not found")
    return {"modified_count": education}


@app.put("/certifications/{id}", status_code=status.HTTP_200_OK)
def update_certifications_by_id(id: str, certifications: Certification):
    certifications = database.update_certifications(
        id, certifications.dict(exclude_unset=True))
    if certifications is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Certifications not found")
    return {"modified_count": certifications}


@app.put("/projects/{id}", status_code=status.HTTP_200_OK)
def update_projects_by_id(id: str, projects: Project):
    projects = database.update_projects(
        id, projects.dict(exclude_unset=True))
    if not projects:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Projects not found")
    return {"modified_count": projects}


@app.put("/publications/{id}", status_code=status.HTTP_200_OK)
def update_publications_by_id(id: str, publications: Publication):
    publications = database.update_publications(
        id, publications.dict(exclude_unset=True))
    if publications is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Publications not found")
    return {"modified_count": publications}
