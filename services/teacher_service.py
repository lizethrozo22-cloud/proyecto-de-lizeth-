from ..models.teacher import Teacher

class TeacherService:

    def __init__(self):
        self.teachers = []

    def get_next_id(self):

        if not self.teachers:
            return 1

        return max(t.id for t in self.teachers) + 1

    def add_teacher(self, name, specialty, email, salary=None):

        new_teacher = Teacher(
            self.get_next_id(),
            name,
            specialty,
            email,
            salary
        )

        self.teachers.append(new_teacher)

        print("Profesor agregado")

        return new_teacher

    def get_all_teachers(self):
        return self.teachers

    def get_teacher_by_id(self, teacher_id):

        for teacher in self.teachers:

            if teacher.id == teacher_id:
                return teacher

        return None

    def delete_teacher(self, teacher_id):

        teacher = self.get_teacher_by_id(teacher_id)

        if teacher:
            self.teachers.remove(teacher)
            return True

        return False