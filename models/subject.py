from datetime import datetime

class Subject:

    def __init__(
            self,
            subject_id,
            name,
            teacher_id,
            credits,
            description=""
    ):

        self.id = subject_id
        self.name = name
        self.teacher_id = teacher_id
        self.credits = credits
        self.description = description
        self.created_at = datetime.now().isoformat()

    def __str__(self):

        return (
            f"{self.id} - "
            f"{self.name} - "
            f"Profesor {self.teacher_id}"
        )