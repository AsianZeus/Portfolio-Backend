from pymongo import MongoClient
from bson.objectid import ObjectId
import wikipedia


class MongoConnect:

    def __init__(self, username, password, db):
        try:
            self.client = MongoClient(
                f"mongodb+srv://{username}:{password}@cluster0.n9g25.mongodb.net/test?retryWrites=true&w=majority")
            self.db = self.client[db]
            self.Personal_Info_c = self.db["Personal_Info"]
            self.Experiences_c = self.db["Experiences"]
            self.Education_c = self.db["Education"]
            self.Certifications_c = self.db["Certifications"]
            self.Projects_c = self.db["Projects"]
            self.Publications_c = self.db["Publications"]
            self.Skills_c = self.db["Skills"]
            print("Connected to MongoDB!")
        except Exception as e:
            print("Unable to connect to the database!", e)

    def verify_id(self, id):
        try:
            ObjectId(id)
            return True
        except Exception:
            return False

    def insert_personal_info(self, payload):
        res = self.Personal_Info_c.insert_one(payload)
        return res

    def insert_skills(self, payload):
        payload['Description'] = wikipedia.summary(
            f"{payload['Name']} {payload['Type']}", sentences=1)
        res = self.Skills_c.insert_one(payload)
        return res

    def insert_experiences(self, payload):
        res = self.Experiences_c.insert_one(payload)
        return res

    def insert_education(self, payload):
        res = self.Education_c.insert_one(payload)
        return res

    def insert_certifications(self, payload):
        res = self.Certifications_c.insert_one(payload)
        return res

    def insert_projects(self, payload):
        res = self.Projects_c.insert_one(payload)
        return res

    def insert_publications(self, payload):
        res = self.Publications_c.insert_one(payload)
        return res

    def get_personal_info(self):
        personal_info = self.Personal_Info_c.find(projection={"_id": 0})
        personal_info = [i for i in personal_info]
        return personal_info

    def get_skills(self):
        skills = self.Skills_c.find(projection={"_id": 0})
        skills = [i for i in skills]
        return skills

    def get_experiences(self):
        experiences = self.Experiences_c.find(projection={"_id": 0})
        experiences = [i for i in experiences]
        return experiences

    def get_education(self):
        education = self.Education_c.find(projection={"_id": 0})
        education = [i for i in education]
        return education

    def get_certifications(self):
        certifications = self.Certifications_c.find(projection={"_id": 0})
        certifications = [i for i in certifications]
        return certifications

    def get_projects(self):
        projects = self.Projects_c.find(projection={"_id": 0})
        projects = [i for i in projects]
        return projects

    def get_publications(self):
        publications = self.Publications_c.find(projection={"_id": 0})
        publications = [i for i in publications]
        return publications

    def get_all(self):
        return {
            "Personal_Info": self.get_personal_info(),
            "Skills": self.get_skills(),
            "Experiences": self.get_experiences(),
            "Education": self.get_education(),
            "Certifications": self.get_certifications(),
            "Projects": self.get_projects(),
            "Publications": self.get_publications()
        }

    def get_personal_info_by_id(self, id):
        if self.verify_id(id):
            personal_info = self.Personal_Info_c.find_one(
                {"_id": ObjectId(id)}, {'_id': 0})
            return personal_info
        else:
            return None

    def get_skills_by_id(self, id):
        if self.verify_id(id):
            skills = self.Skills_c.find_one(
                {"_id": ObjectId(id)}, {'_id': 0})
            return skills
        else:
            return None

    def get_experiences_by_id(self, id):
        if self.verify_id(id):
            experiences = self.Experiences_c.find_one(
                {"_id": ObjectId(id)}, {'_id': 0})
            return experiences

    def get_education_by_id(self, id):
        if self.verify_id(id):
            education = self.Education_c.find_one(
                {"_id": ObjectId(id)}, {'_id': 0})
            return education
        else:
            return None

    def get_certifications_by_id(self, id):
        if self.verify_id(id):
            certifications = self.Certifications_c.find_one(
                {"_id": ObjectId(id)}, {'_id': 0})
            return certifications
        else:
            return None

    def get_projects_by_id(self, id):
        if self.verify_id(id):
            projects = self.Projects_c.find_one(
                {"_id": ObjectId(id)}, {'_id': 0})
            return projects
        else:
            return None

    def get_publications_by_id(self, id):
        if self.verify_id(id):
            publications = self.Publications_c.find_one(
                {"_id": ObjectId(id)}, {'_id': 0})
            return publications
        else:
            return None

    def update_personal_info(self, id, payload):
        if self.verify_id(id):
            res = self.Personal_Info_c.update_one(
                {"_id": ObjectId(id)}, {"$set": payload})
            return res.modified_count
        else:
            return None

    def update_skills(self, id, payload):
        if self.verify_id(id):
            res = self.Skills_c.update_one(
                {"_id": ObjectId(id)}, {"$set": payload})
            return res.modified_count
        else:
            return None

    def update_experiences(self, id, payload):
        if self.verify_id(id):
            res = self.Experiences_c.update_one(
                {"_id": ObjectId(id)}, {"$set": payload})
            return res.modified_count
        else:
            return None

    def update_education(self, id, payload):
        if self.verify_id(id):
            res = self.Education_c.update_one(
                {"_id": ObjectId(id)}, {"$set": payload})
            return res.modified_count
        else:
            return None

    def update_certifications(self, id, payload):
        if self.verify_id(id):
            res = self.Certifications_c.update_one(
                {"_id": ObjectId(id)}, {"$set": payload})
            return res.modified_count
        else:
            return None

    def update_projects(self, id, payload):
        if self.verify_id(id):
            res = self.Projects_c.update_one(
                {"_id": ObjectId(id)}, {"$set": payload})
            return res.modified_count
        else:
            return None

    def update_publications(self, id, payload):
        if self.verify_id(id):
            res = self.Publications_c.update_one(
                {"_id": ObjectId(id)}, {"$set": payload})
            return res.modified_count
        else:
            return None

    def delete_personal_info(self, id):
        if self.verify_id(id):
            res = self.Personal_Info_c.delete_one(
                {"_id": ObjectId(id)})
            return res.deleted_count
        else:
            return None

    def delete_skills(self, id):
        if self.verify_id(id):
            res = self.Skills_c.delete_one(
                {"_id": ObjectId(id)})
            return res.deleted_count
        else:
            return None

    def delete_experiences(self, id):
        if self.verify_id(id):
            res = self.Experiences_c.delete_one({"_id": ObjectId(id)})
            return res.deleted_count
        else:
            return None

    def delete_education(self, id):
        if self.verify_id(id):
            res = self.Education_c.delete_one({"_id": ObjectId(id)})
            return res.deleted_count
        else:
            return None

    def delete_certifications(self, id):
        if self.verify_id(id):
            res = self.Certifications_c.delete_one(
                {"_id": ObjectId(id)})
            return res.deleted_count
        else:
            return None

    def delete_projects(self, id):
        if self.verify_id(id):
            res = self.Projects_c.delete_one({"_id": ObjectId(id)})
            return res.deleted_count
        else:
            return None

    def delete_publications(self, id):
        if self.verify_id(id):
            res = self.Publications_c.delete_one({"_id": ObjectId(id)})
            return res.deleted_count
        else:
            return None

    def close(self):
        self.client.close()
