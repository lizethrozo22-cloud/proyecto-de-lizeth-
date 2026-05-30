from datetime import datetime

class Grade:

    def __init__(
            self,
            grade_id,
            student_id,
            subject_id,
            grade
    ):

        self.id = grade_id
        self.student_id = student_id
        self.subject_id = subject_id
        self.grade = grade
        self.created_at = datetime.now().isoformat()

    def is_passing(self):

        return self.grade >= 3.0

    def __str__(self):

        return (
            f"Estudiante:{self.student_id} "
            f"Materia:{self.subject_id} "
            f"Nota:{self.grade}"
        )