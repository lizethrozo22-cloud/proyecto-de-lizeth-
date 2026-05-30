from datetime import datetime

class Teacher:

    def __init__(self, teacher_id, name, specialty, email, salary=None):
        self.id = teacher_id
        self.name = name
        self.specialty = specialty
        self.email = email
        self.salary = salary
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialty": self.specialty,
            "email": self.email,
            "salary": self.salary,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        teacher = cls(
            data["id"],
            data["name"],
            data["specialty"],
            data["email"],
            data.get("salary")
        )

        teacher.created_at = data.get("created_at")
        return teacher

    def __str__(self):
        return f"{self.id} - {self.name} - {self.specialty}"