from ..models.grade import Grade


class GradeService:

    def __init__(self):
        self.grades = []

    def get_next_id(self):

        if not self.grades:
            return 1

        return max(grade.id for grade in self.grades) + 1

    # CREATE
    def add_grade(
            self,
            student_id,
            subject_id,
            grade_value
    ):

        new_grade = Grade(
            self.get_next_id(),
            student_id,
            subject_id,
            grade_value
        )

        self.grades.append(new_grade)

        return new_grade

    # READ
    def get_all_grades(self):
        return self.grades

    def get_grade_by_id(self, grade_id):

        for grade in self.grades:

            if grade.id == grade_id:
                return grade

        return None

    # DELETE
    def delete_grade(self, grade_id):

        grade = self.get_grade_by_id(grade_id)

        if grade:

            self.grades.remove(grade)

            return True

        return False